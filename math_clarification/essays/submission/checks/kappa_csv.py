#!/usr/bin/env python3
"""Per-column Cohen's kappa from a paired-coding CSV — the census reliability gate.

Companion to ../census_protocol.md §8 and ../census_coder2_packet.md. kappa.py in
this folder holds the hand-checked arithmetic; this file only turns two coders'
independent sheets into the per-column verdicts the protocol demands:

    regime, each of Q1..Q5, dispute, and the novelty screen each need kappa >= 0.6
    to enter the primary analysis; a column below threshold is reported descriptively.

Input CSV — two accepted layouts, auto-detected:
  * WIDE : each coded column appears twice, once per coder, as `NAME_a`/`NAME_b`
           (also accepts `_coder1`/`_coder2`, `_c1`/`_c2`). One row per event.
           e.g.  event_id,regime_a,regime_b,dispute_a,dispute_b,...
  * LONG : columns `column,coder_a,coder_b` (or `...,coder1,coder2`). One row per
           (event, column) pair. Use this when melting two sheets is easier.

Only categorical labels are compared; blank cells are dropped (a column a coder
left empty is not scored, and the packet says why). Unweighted kappa only, per §8.

Run:  python checks/kappa_csv.py ../paired_codings.csv   (or a path you choose)
      python checks/kappa_csv.py                         (no arg -> self-test)
Exit: 0 if every non-degenerate column passes >= 0.6 (or the self-test holds), else 1.

Adds no facts; it only computes the reliability statistic the protocol fixes.
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kappa import kappa_from_pairs, verdict  # noqa: E402

GATE = 0.6
SUFFIX_PAIRS = [("_a", "_b"), ("_coder1", "_coder2"), ("_c1", "_c2")]


def _clean(v):
    return (v or "").strip()


def columns_from_wide(header):
    """Map base column name -> (coder_a_field, coder_b_field) from a wide header."""
    pairs = {}
    hset = set(header)
    for col in header:
        for suf_a, suf_b in SUFFIX_PAIRS:
            if col.endswith(suf_a):
                base = col[: -len(suf_a)]
                mate = base + suf_b
                if mate in hset:
                    pairs[base] = (col, mate)
                break
    return pairs


def pairs_from_rows(rows, header):
    """Return {column: [(coder_a_label, coder_b_label), ...]} from a parsed sheet."""
    out = defaultdict(list)
    if "column" in header and any(h in header for h in ("coder_a", "coder_b", "coder1", "coder2")):
        ca = "coder_a" if "coder_a" in header else "coder1"
        cb = "coder_b" if "coder_b" in header else "coder2"
        for r in rows:
            col, a, b = _clean(r.get("column")), _clean(r.get(ca)), _clean(r.get(cb))
            if col and a and b:
                out[col].append((a, b))
        return out
    for base, (fa, fb) in columns_from_wide(header).items():
        for r in rows:
            a, b = _clean(r.get(fa)), _clean(r.get(fb))
            if a and b:
                out[base].append((a, b))
    return out


def report(pairs_by_column, gate=GATE):
    all_pass = True
    for col in sorted(pairs_by_column):
        k = kappa_from_pairs(pairs_by_column[col])
        line = verdict(k, gate)
        if k is None or k < gate:
            all_pass = False
        print(f"{col:28s} n={len(pairs_by_column[col]):3d}  {line}")
    return all_pass


def _self_test():
    """Reproduce kappa.py's hand-checked 2x2 example through this file's parsing,
    proving the grouping/reading layer matches the verified arithmetic."""
    header = ["event_id", "regime_a", "regime_b", "dispute_a", "dispute_b"]
    rows = []
    # dispute column = the worked matrix: 55 yes/yes, 15 yes/no, 10 no/yes, 20 no/no
    plan = [("yes", "yes", 55), ("yes", "no", 15), ("no", "yes", 10), ("no", "no", 20)]
    # regime column = perfect agreement across two categories (both coders always
    # concur, alternating M/C) so kappa is 1.0, not the degenerate None of a
    # single-category column (see kappa.py: a one-category column is undefined).
    i = 0
    for a, b, n in plan:
        for _ in range(n):
            i += 1
            reg = "M" if i % 2 else "C"
            rows.append({"event_id": str(i), "regime_a": reg, "regime_b": reg,
                         "dispute_a": a, "dispute_b": b})
    pairs = pairs_from_rows(rows, header)
    assert "dispute" in pairs and "regime" in pairs, "wide parser found no columns"
    k_disp = kappa_from_pairs(pairs["dispute"])
    exp = 0.19 / 0.44
    assert abs(k_disp - exp) < 1e-9, f"dispute kappa {k_disp} != hand-checked {exp}"
    assert kappa_from_pairs(pairs["regime"]) == 1.0, "perfect regime should be 1.0"
    print("self-test: wide-parse reproduces kappa.py's hand-checked example")
    print(f"  dispute kappa = {k_disp:.6f} (expected {exp:.6f}) -> FAILS gate, as designed")
    print("  regime   kappa = 1.000000 -> PASSES gate")
    print("  report() run:")
    report(pairs)
    print("ALL SELF-CHECKS PASSED (exit 0 does not require gate pass in self-test)")


def main(argv):
    if len(argv) < 2:
        _self_test()
        return 0
    path = Path(argv[1])
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        header = reader.fieldnames or []
        rows = list(reader)
    pairs = pairs_from_rows(rows, header)
    if not pairs:
        print(f"no paired coding columns found in {path.name}; header was {header}", file=sys.stderr)
        return 1
    print(f"reliability gate (kappa >= {GATE}) for {path.name}:")
    return 0 if report(pairs) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
