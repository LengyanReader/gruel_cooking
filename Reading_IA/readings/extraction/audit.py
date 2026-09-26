# -*- coding: utf-8 -*-
"""Lossless-ledger audit for Reading & IA intake cards.

Checks every library/*.md card for an `extract_ledger:` YAML-ish block and verifies
each kind's thresholds (framework.md §4).

Semantics:
- A card with NO ledger            -> warn ("尚未验账"), never blocks.
- read_status != done (reading…)   -> below-threshold fields are warn (gaps expected
                                      until read is finished), run stays clean.
- read_status == done              -> below-threshold = INCOMPLETE, exit 1.
  The fix is more real content, never loosening a gate.

Usage:
    py -X utf8 Reading_IA/readings/extraction/audit.py         # audit all cards
    py -X utf8 Reading_IA/readings/extraction/audit.py 2026-.. # by slug substring
    py -X utf8 Reading_IA/readings/extraction/audit.py --corpus # gate books.json briefs vs Layer-1 corpus
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
LIBRARY = os.path.normpath(os.path.join(HERE, "..", "library"))
WEB_DATA = os.path.normpath(os.path.join(HERE, "..", "..", "web", "data"))
BOOKS_JSON = os.path.join(WEB_DATA, "books.json")
CORPUS_DIR = os.path.join(WEB_DATA, "corpus")
GRAPH_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "knowledge", "graph"))
GRAPH_SCHEMA = os.path.join(GRAPH_DIR, "schema.json")
GRAPH_NODES = os.path.join(GRAPH_DIR, "nodes.jsonl")
GRAPH_EDGES = os.path.join(GRAPH_DIR, "edges.jsonl")
LENSES_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "knowledge", "lenses"))

# The five lossless sub-fields every chapter brief must carry (framework.md §1).
BRIEF_FIELDS = ("main", "flow", "names", "sources", "link")

DONE_STATUS = {"done", "re-reading"}


def _load_thresholds() -> dict:
    """RKF L2: the card ledger thresholds are DATA, read from
    ``knowledge/lenses/<kind>.json`` each lens's ``ledger`` map. This retires the
    former hard-coded THRESHOLDS dict; a new kind = a new lens file, not a code
    edit. Falls back to {} per-kind if a lens is absent (warns downstream)."""
    table: dict[str, dict[str, int]] = {}
    if not os.path.isdir(LENSES_DIR):
        return table
    for fn in sorted(os.listdir(LENSES_DIR)):
        if not fn.endswith(".json"):
            continue
        try:
            lens = json.load(io.open(os.path.join(LENSES_DIR, fn), encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        ledger = lens.get("ledger")
        kind = lens.get("kind") or fn[:-5]
        if isinstance(ledger, dict) and ledger:
            table[kind] = {k: int(v) for k, v in ledger.items()}
    return table


# kind -> {ledger field: min}. A finished card under any of these is INCOMPLETE.
# Loaded from lenses/*.json (see _load_thresholds); empty only if registries absent.
THRESHOLDS: dict[str, dict[str, int]] = _load_thresholds()

# optional informational fields shown when present (never gated)
INFO_FIELDS = ("characters", "unverified_items", "intent_quotes", "craft_items",
               "quotes_original", "related_edges", "skeleton_parts", "reads",
               "echoes")


def _extract_ledger(text: str) -> tuple[str | None, str, dict[str, int]]:
    m = re.search(r"extract_ledger:\s*\n((?:[ \t]*\S.*\n)+)", text, re.M)
    kind = None
    status = ""
    values: dict[str, int] = {}
    if not m:
        return None, status, values
    for line in m.group(1).splitlines():
        line = line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, _, val = line.strip().partition(":")
        key = key.strip().strip('"\'')
        val = val.strip().strip('"\'')
        if key == "kind":
            kind = val
        elif key == "read_status":
            status = val
            values[key] = val
        elif val.lstrip("-").isdigit():
            values[key] = int(val)
    return kind, status, values


def audit_card(md_path: str) -> dict:
    text = io.open(md_path, encoding="utf-8").read()
    kind, status, values = _extract_ledger(text)

    if kind is None:
        return {"file": md_path, "kind": "?", "status": "?",
                "warns": ["extract_ledger 缺（尚未按 extraction 框架验账）"], "gaps": [], "info": values}

    keys = THRESHOLDS.get(kind)
    if keys is None:
        return {"file": md_path, "kind": kind, "status": status,
                "warns": [f"kind '{kind}' 无阈值表（framework.md §4 注册）"], "gaps": [], "info": values}

    finished = status in DONE_STATUS
    gaps, warns = [], []
    for field, minv in keys.items():
        got = values.get(field, 0)
        if got < minv:
            msg = f"{field}={got}<{minv}"
            (gaps if finished else warns).append(msg)

    info = {k: v for k, v in values.items()
            if k in INFO_FIELDS and isinstance(v, int)}
    status_label = status or "?"
    return {"file": md_path, "kind": kind, "status": status_label,
            "gaps": gaps, "warns": warns, "info": info}


def _load_books() -> list:
    if not os.path.exists(BOOKS_JSON):
        return []
    data = json.load(io.open(BOOKS_JSON, encoding="utf-8"))
    return data.get("books", data) if isinstance(data, dict) else data


def audit_corpus() -> int:
    """Grounding gate: every history-kind chapter must carry a complete
    five-field lossless brief, and (when available) the book must be backed by
    a Layer-1 corpus file. Checks structure only — never reads/compares source
    prose. Exit 1 on any brief gap; missing corpus is a warn (not fatal)."""
    books = _load_books()
    hist = [r for r in books if r.get("kind") == "history" and (r.get("plot_acts") or [])]
    print(f"repo root       : {os.path.dirname(os.path.dirname(WEB_DATA))}")
    print(f"corpus dir      : {CORPUS_DIR} ({'present' if os.path.isdir(CORPUS_DIR) else 'ABSENT — run extract_corpus.py'})")
    print(f"history books   : {len(hist)} (kind=history with >=1 plot_act)")

    bad = 0
    for rec in hist:
        bid = rec.get("id", "?")
        acts = rec.get("plot_acts") or []
        corpus_path = os.path.join(CORPUS_DIR, f"{bid}.json")
        n_corpus = 0
        if os.path.exists(corpus_path):
            cd = json.load(io.open(corpus_path, encoding="utf-8"))
            n_corpus = (cd.get("summary") or {}).get("n_chapters") or len(cd.get("chapters") or [])
        gaps, complete = [], 0
        for a in acts:
            br = a.get("brief") or {}
            missing = [f for f in BRIEF_FIELDS if not str(br.get(f, "")).strip()]
            if missing:
                gaps.append(f"act {a.get('n')} missing:{'/'.join(missing)}")
            else:
                complete += 1
        status = "ok" if not gaps else "INCOMPLETE"
        cov = f"corpus={n_corpus}" if n_corpus else "corpus=NONE"
        print(f"  {status:<11} {bid:<34} briefs {complete}/{len(acts)}  {cov}")
        for g in gaps[:8]:
            print(f"      gap: {g}")
        if len(gaps) > 8:
            print(f"      … {len(gaps) - 8} more brief gaps")
        if gaps:
            bad += 1

    if bad:
        print(f"\nINCOMPLETE: {bad} history book(s) — 每章补齐五维 brief（main/flow/names/sources/link），勿放宽 gate。")
        return 1
    print("\ncorpus audit clean")
    return 0


def _read_jsonl(path):
    rows = []
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def audit_graph() -> int:
    """L3 integrity gate. Reads only knowledge/graph/{schema.json, nodes.jsonl,
    edges.jsonl} and checks, entirely schema-driven: (1) every node type and
    every edge type is registered in schema.json; (2) no dangling edge (both
    endpoints resolve to a node id); (3) no disallowed orphan node (a node with
    no incident edges whose type is not in integrity.allow_orphan_types).
    Exit 1 on any violation. Never reads source prose."""
    for p in (GRAPH_SCHEMA, GRAPH_NODES, GRAPH_EDGES):
        if not os.path.exists(p):
            print(f"MISSING graph artifact: {p}  (run engine/graph_build.py)")
            return 1
    schema = json.load(io.open(GRAPH_SCHEMA, encoding="utf-8"))
    node_types = set(schema.get("node_types", {}))
    edge_types = set(schema.get("edge_types", {}))
    integ = schema.get("integrity", {})
    allow_orphan = set(integ.get("allow_orphan_types", []))

    nodes = _read_jsonl(GRAPH_NODES)
    edges = _read_jsonl(GRAPH_EDGES)
    ids = {n["id"] for n in nodes}

    problems = []
    # (1) registered types
    for n in nodes:
        if n.get("type") not in node_types:
            problems.append(f"node {n.get('id')} has unregistered type '{n.get('type')}'")
    for e in edges:
        if e.get("type") not in edge_types and integ.get("edge_type_must_be_registered", True):
            problems.append(f"edge {e.get('from')} -[{e.get('type')}]-> {e.get('to')} uses unregistered type")
    # (2) dangling edges
    degree = {nid: 0 for nid in ids}
    for e in edges:
        for endp in (e["from"], e["to"]):
            if integ.get("require_nodes_for_edges", True) and endp not in ids:
                problems.append(f"dangling edge endpoint: {endp} (in {e.get('from')} -[{e.get('type')}]-> {e.get('to')})")
            if endp in degree:
                degree[endp] += 1
    # (3) disallowed orphans
    for n in nodes:
        if degree.get(n["id"], 0) == 0 and n["type"] not in allow_orphan:
            problems.append(f"orphan node {n['id']} (type {n['type']} not in allow_orphan_types)")

    by_ntype, by_etype = {}, {}
    for n in nodes:
        by_ntype[n["type"]] = by_ntype.get(n["type"], 0) + 1
    for e in edges:
        by_etype[e["type"]] = by_etype.get(e["type"], 0) + 1
    print(f"graph dir       : {GRAPH_DIR}")
    print(f"nodes           : {len(nodes)}  ({', '.join(f'{k}:{v}' for k, v in sorted(by_ntype.items()))})")
    print(f"edges           : {len(edges)}  ({', '.join(f'{k}:{v}' for k, v in sorted(by_etype.items()))})")
    print(f"registered kinds: {len(node_types)} node / {len(edge_types)} edge types")

    if problems:
        print(f"\nGRAPH INTEGRITY: {len(problems)} problem(s) — 修数据/注册类型，勿放宽 gate。")
        for pr in problems[:40]:
            print(f"  - {pr}")
        if len(problems) > 40:
            print(f"  \u2026 {len(problems) - 40} more")
        return 1
    print("\ngraph integrity clean")
    return 0


def main(argv: list[str]) -> int:
    if "--corpus" in argv:
        return audit_corpus()
    if "--graph" in argv:
        return audit_graph()

    cards = sorted(f for f in os.listdir(LIBRARY)
                   if f.startswith("20") and f.endswith(".md"))
    filter_ = argv[1] if len(argv) > 1 else None
    if filter_:
        cards = [f for f in cards if filter_ in f]

    results = [audit_card(os.path.join(LIBRARY, f)) for f in cards]
    bad = [r for r in results if r["gaps"]]

    print(f"repo root       : {os.path.dirname(os.path.dirname(LIBRARY))}")
    print(f"cards audited   : {len(results)}  ({', '.join(cards) or '(none)'})")
    for r in results:
        flags = []
        if r["gaps"]:
            flags.append("INCOMPLETE")
        if r["warns"]:
            flags.append("warn:" + "; ".join(r["warns"]))
        flags.append("|".join(f"{k}={v}" for k, v in r["info"].items()))
        status = "  ".join(f for f in flags if f) or "ok"
        print(f"  {r['kind']:<8} {r['status']:<9} {os.path.basename(r['file']):<42} {status}")
        for g in r["gaps"]:
            print(f"      gap: {g}")

    if bad:
        print(f"\nINCOMPLETE: {len(bad)} finished card(s) — 缺口补真实内容，勿放宽阈值。")
        return 1
    print("\naudit clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))