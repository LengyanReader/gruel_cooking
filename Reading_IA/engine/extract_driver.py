# -*- coding: utf-8 -*-
"""engine/extract_driver.py — RKF Layer-2 slot diagnostic (config-driven).

Given a book id, it reads:
  - knowledge/kinds.json           -> which lens governs the book's kind
  - knowledge/lenses/<kind>.json   -> the declarative slot thresholds
  - web/data/books.json            -> the book's CURRENT record (if any)
  - web/data/corpus/<id>.json      -> the extracted Corpus IR (grounding)

and prints, per lens layer, whether the slot is met / thin / missing, plus a
per-chapter extraction-capacity line. This is the "what to enrich next" view:
it turns re-enrichment from guesswork into a data-driven worklist.

Backend choice (see TOOLING.md): 'slot' (this human/agent pass) is default; a
'langextract' backend can be added later behind the same lens config without
changing callers.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE = os.path.normpath(os.path.join(HERE, "..", "knowledge"))
WEB_DATA = os.path.normpath(os.path.join(HERE, "..", "web", "data"))
BOOKS = os.path.join(WEB_DATA, "books.json")
CORPUS = os.path.join(WEB_DATA, "corpus")


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _walk(obj, dotted: str):
    """Resolve 'a.b.c' through dicts. Missing -> None."""
    cur = obj
    for part in dotted.split("."):
        if isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
    return cur


def _resolve_target(record: dict, target: str):
    """Return (kind, value).
    kind='list-of-item-values' for 'plot_acts[].brief.main'
    kind='value' for 'background.zh' / 'characters'.
    """
    if "[]." in target:
        prefix, suffix = target.split("[].", 1)
        items = _walk(record, prefix) or []
        vals = [_walk(it, suffix) for it in items if isinstance(it, dict)]
        return ("items", vals)
    return ("value", _walk(record, target))


def _eval_layer(record: dict, layer: dict) -> tuple[str, str]:
    """Return (status, detail). status in {ok, thin, missing, no-record}."""
    if record is None:
        return ("no-record", "")
    kind, val = _resolve_target(record, layer["target"])
    if kind == "items":
        need = layer.get("per_item_min_chars")
        present = [v for v in val if v]
        if not val:
            return ("missing", "0 items")
        if need:
            good = sum(1 for v in present if isinstance(v, str) and len(v.strip()) >= need)
            status = "ok" if good == len(val) else ("thin" if good else "missing")
            return (status, f"{good}/{len(val)} >= {need}ch")
        return ("ok", f"{len(present)}/{len(val)}")
    # scalar / list value
    if isinstance(val, list):
        n = len(val)
        minv = layer.get("min_items", 1)
        return (("ok" if n >= minv else ("thin" if n else "missing")), f"{n}/{minv} items")
    if isinstance(val, str):
        n = len(val.strip())
        minv = layer.get("min_chars", 1)
        return (("ok" if n >= minv else ("thin" if n else "missing")), f"{n}/{minv} ch")
    return ("missing", "absent") if val is None else ("ok", "present")


def _corpus_info(book_id: str):
    p = os.path.join(CORPUS, f"{book_id}.json")
    if not os.path.exists(p):
        return None
    cd = _load(p)
    return cd


def _chapter_capacity(cd: dict):
    """Summarize corpus chapter readiness (metrics only; never prints body)."""
    if not cd:
        return []
    rows = []
    for c in cd.get("chapters", []):
        rows.append({
            "index": c.get("index"),
            "toc": c.get("toc_title") or "",
            "chars": c.get("char_count", 0),
            "headings": len(c.get("headings") or []),
        })
    return rows


def report(book_id: str) -> int:
    kinds = _load(os.path.join(KNOWLEDGE, "kinds.json"))
    books = _load(BOOKS).get("books", [])
    rec = next((r for r in books if r.get("id") == book_id), None)
    kind = (rec or {}).get("kind") or kinds.get("detect", {}).get("fallback", "generic")
    kspec = (kinds.get("kinds") or {}).get(kind)
    if not kspec:
        print(f"kind '{kind}' has no entry in kinds.json")
        return 1
    lens = _load(os.path.join(KNOWLEDGE, kspec["lens_ref"]))
    cd = _corpus_info(book_id)
    rows = _chapter_capacity(cd)
    corpus_docs = len(rows)

    print(f"== {book_id}  kind={kind}  lens={kspec['lens_ref']}")
    print(f"   corpus: {'present, ' + str(corpus_docs) + ' docs' if cd else 'ABSENT (run engine/ingest.py)'}")
    if cd:
        print(f"   total extracted: {cd['summary']['total_chars']:,} chars / {cd['summary']['total_words']:,} words")
    print(f"   record: {'in books.json' if rec else 'NOT YET (new book — slots start empty)'}")
    print("   ---- slot status (per lenses/" + kind + ".json) ----")

    n_ok = n_bad = 0
    for layer in lens.get("layers", []):
        status, detail = _eval_layer(rec, layer)
        mark = {"ok": "OK ", "thin": "THIN", "missing": "MISS", "no-record": "NEW "}[status]
        if status == "ok":
            n_ok += 1
        elif status != "no-record":
            n_bad += 1
        print(f"     [{mark:>4}] {layer['slot']:<18} ({layer.get('guarantee',''):<9}) {detail}")

    # chapter-level readiness vs skeleton present
    if rec and rows:
        acts = rec.get("plot_acts") or []
        print(f"   ---- grounding: {len(acts)} plot_acts vs {corpus_docs} corpus docs ----")
        if len(acts) > corpus_docs:
            print(f"     WARN more acts than extracted docs — align chapters to corpus spine")
        else:
            print(f"     OK every act has >= 1 backing extracted doc")

    if rec:
        verdict = "COMPLETE" if n_bad == 0 else f"{n_bad} slot(s) short"
        print(f"   => {verdict}")
        return 0 if n_bad == 0 else 1
    print("   => not audited (no record); ready to enrich from corpus")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="RKF L2 slot diagnostic for one book")
    ap.add_argument("book_id", nargs="?", help="id as in books.json / corpus filename")
    ap.add_argument("--list", action="store_true", help="list ids in books.json + corpus")
    args = ap.parse_args(argv)

    if args.list:
        books = _load(BOOKS).get("books", [])
        cfiles = {f[:-5] for f in os.listdir(CORPUS)} if os.path.isdir(CORPUS) else set()
        for r in books:
            print(f"  {r.get('id'):<34} kind={str(r.get('kind')):<8} corpus={'y' if r.get('id') in cfiles else '-'}")
        return 0
    if not args.book_id:
        ap.error("book_id required (or --list)")
    return report(args.book_id)


if __name__ == "__main__":
    raise SystemExit(main())
