# -*- coding: utf-8 -*-
"""engine/ingest.py — RKF Layer-0/1 registry-driven ingest front.

Thin on purpose: it contains NO domain logic. It reads
``knowledge/adapters.manifest.json`` to choose an adapter for an input
(file path or URL), resolves that adapter's ``emitter`` symbol, emits a
Corpus IR, validates it against ``knowledge/corpus_ir.schema.json``, and
writes ``web/data/corpus/<book_id>.json`` (gitignored raw text).

Adding a format or a source = edit the manifest, not this file.
"""
from __future__ import annotations

import argparse
import importlib
import importlib.util
import json
import os
import sys
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE = os.path.normpath(os.path.join(HERE, "..", "knowledge"))
EXTRACTION = os.path.normpath(os.path.join(HERE, "..", "readings", "extraction"))
CORPUS_DIR = os.path.normpath(os.path.join(HERE, "..", "web", "data", "corpus"))

ADAPTERS = os.path.join(KNOWLEDGE, "adapters.manifest.json")
IR_SCHEMA = os.path.join(KNOWLEDGE, "corpus_ir.schema.json")


def _load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _load_extract_corpus():
    """Import the sibling extract_corpus backbone without packaging gymnastics."""
    spec = importlib.util.spec_from_file_location(
        "extract_corpus", os.path.join(EXTRACTION, "extract_corpus.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _resolve_emitter(symbol: str, ec):
    """'module:function' -> callable. 'extract_corpus:*' resolves against the
    loaded backbone; any dotted module path otherwise."""
    mod_name, _, fn = symbol.partition(":")
    if mod_name == "extract_corpus":
        return getattr(ec, fn)
    return getattr(importlib.import_module(mod_name), fn)


def _ext_of(source: str) -> str:
    return os.path.splitext(urlparse(source).path if "://" in source else source)[1].lower()


def _scheme_of(source: str) -> str:
    return urlparse(source).scheme.lower() if "://" in source else ""


def pick_adapter(manifest: dict, source: str):
    ext, scheme = _ext_of(source), _scheme_of(source)
    for a in manifest.get("adapters", []):
        det = a.get("detect", {})
        if scheme and scheme in [s.lower() for s in det.get("scheme", [])]:
            return a
        if not scheme and ext and ext in [e.lower() for e in det.get("ext", [])]:
            return a
    # routing default when nothing matched but the file is real
    default_id = (manifest.get("routing") or {}).get("default_when_unmatched")
    if default_id and os.path.exists(source):
        return next((a for a in manifest["adapters"] if a["id"] == default_id), None)
    return None


_TYPE_MAP = {"str": str, "int": int, "float": float, "dict": dict, "list": list}


def validate_ir(data: dict, schema: dict) -> list:
    """Structural validation driven entirely by the schema file (no hard-coded
    field lists). Returns a list of human-readable problems ([] == valid)."""
    problems = []
    for k in schema.get("required_top", []):
        if k not in data:
            problems.append(f"missing top-level key: {k}")
    for k, tname in (schema.get("top_types") or {}).items():
        if k in data and not isinstance(data[k], _TYPE_MAP.get(tname, object)):
            problems.append(f"top-level {k} should be {tname}, got {type(data[k]).__name__}")
    ch = data.get("chapters") or []
    cons = schema.get("constraints") or {}
    if len(ch) < cons.get("min_chapters", 1):
        problems.append(f"too few chapters: {len(ch)}")
    fmt = data.get("format")
    enum = cons.get("format_enum")
    if enum and fmt not in enum:
        problems.append(f"format '{fmt}' not in {enum}")
    ctypes = schema.get("chapter_types") or {}
    creq = schema.get("chapter_required", [])
    for i, c in enumerate(ch):
        for k in creq:
            if k not in c:
                problems.append(f"chapter[{i}] missing {k}")
        for k, tname in ctypes.items():
            if k in c and c[k] is not None and not isinstance(c[k], _TYPE_MAP.get(tname, object)):
                problems.append(f"chapter[{i}].{k} should be {tname}")
    if ch:
        nonempty = sum(1 for c in ch if (c.get("char_count") or 0) > 0)
        ratio = nonempty / len(ch)
        if ratio < cons.get("nonempty_text_ratio_min", 0):
            problems.append(f"nonempty-text ratio {ratio:.2f} below minimum")
    return problems


def ingest_one(source: str, book_id: str, manifest: dict, schema: dict, ec,
               out_dir: str = CORPUS_DIR) -> dict:
    adapter = pick_adapter(manifest, source)
    if adapter is None:
        raise RuntimeError(f"no adapter matched for: {source}")
    if adapter.get("status") != "wired":
        raise RuntimeError(f"adapter '{adapter['id']}' is '{adapter.get('status')}', not wired yet "
                           f"(see TOOLING.md / roadmap phase)")
    emitter = _resolve_emitter(adapter["emitter"], ec)
    data = emitter(source)
    data["book_id"] = book_id
    data["adapter"] = adapter["id"]
    data["fidelity"] = adapter.get("fidelity")
    data["summary"] = ec.summarize(data)

    problems = validate_ir(data, schema)
    if problems:
        raise RuntimeError("Corpus IR failed schema validation:\n  - " + "\n  - ".join(problems))

    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, f"{book_id}.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    return {"dest": dest, "adapter": adapter["id"], "summary": data["summary"]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="RKF L0/L1 ingest: source -> validated Corpus IR -> corpus/<id>.json")
    ap.add_argument("--source", help="file path or URL to ingest")
    ap.add_argument("--id", dest="book_id", help="book id (else auto-mapped / derived)")
    ap.add_argument("--penguin-dir", help="batch: ingest a dir of volumes, auto-map ids")
    ap.add_argument("--check", action="store_true", help="dry-run: route+emit+validate, do not write")
    args = ap.parse_args(argv)

    manifest = _load_json(ADAPTERS)
    schema = _load_json(IR_SCHEMA)
    ec = _load_extract_corpus()

    jobs = []
    if args.source:
        bid = args.book_id or ec.match_penguin_id(os.path.basename(args.source)) or \
            ec._norm(os.path.splitext(os.path.basename(args.source))[0])[:48]
        jobs.append((args.source, bid))
    if args.penguin_dir:
        for fn in sorted(os.listdir(args.penguin_dir)):
            if not fn.lower().endswith((".epub", ".pdf")):
                continue
            full = os.path.join(args.penguin_dir, fn)
            bid = ec.match_penguin_id(fn)
            if bid:
                jobs.append((full, bid))
            else:
                print(f"skip (unmapped): {fn}")
    if not jobs:
        ap.error("pass --source ... [--id ...] or --penguin-dir ...")

    ok = 0
    for src, bid in jobs:
        try:
            res = ingest_one(src, bid, manifest, schema, ec)
            s = res["summary"]
            tag = "check" if args.check else "wrote"
            print(f"OK   [{res['adapter']:<15}] {bid:<34} docs={s['n_chapters']:>3} chars={s['total_chars']:>10,}")
            ok += 1
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL {bid}: {exc}", file=sys.stderr)
    print(f"\ningested {ok}/{len(jobs)} -> {CORPUS_DIR}  (raw text; gitignored)")
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
