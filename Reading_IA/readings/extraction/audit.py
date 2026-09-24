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
"""
from __future__ import annotations

import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
LIBRARY = os.path.normpath(os.path.join(HERE, "..", "library"))

DONE_STATUS = {"done", "re-reading"}

# kind -> {ledger field: min}. A finished card under any of these is INCOMPLETE.
THRESHOLDS: dict[str, dict[str, int]] = {
    "novel": {
        "skeleton_parts": 3,
        "plot_nodes": 8,
        "characters": 1,   # counts must be honest (all named chars listed)
        "charedges": 5,
        "motif_clusters": 2,
        "craft_items": 5,
        "intent_quotes": 2,
        "excerpts": 3,
        "disagreements": 1,
        "related_edges": 3,
    },
    "memoir": {
        "events": 5,
        "turning_points": 3,
        "plot_nodes": 5,
        "excerpts": 2,
        "disagreements": 1,
    },
    "essay": {
        "claims": 5,
        "excerpts": 2,
        "concepts": 4,
        "disagreements": 1,
        "related_edges": 2,
    },
    "generic": {
        "skeleton_parts": 3,
        "concepts": 4,
        "claims": 3,
        "excerpts": 2,
        "related_edges": 2,
        "disagreements": 1,
    },
}

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


def main(argv: list[str]) -> int:
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