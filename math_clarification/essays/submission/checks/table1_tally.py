#!/usr/bin/env python3
"""Reproduce the essay's Section 11.5 tallies from the pilot coding CSV.

This is the parent paper's own MC-W2/R-D discipline applied to the source of
record: the two numbers stated in Section 11.5 (1 dispute among 6 machine-/
hybrid-graded events, 3 among 5 community-graded-or-non-result events) are
re-derived from census_pilot_11events.csv (a faithful transcription of Table 1,
coder 1), and the check fails if they do not reproduce. It adds no facts; it
only verifies that the prose tally matches the coded table, including the
binning of the row-11 attribution episode (regime blank / n-a) with the
community-graded stratum, exactly as Section 11.5 and the Comment's Fig. 1
"CG+na" legend state it.

Run:  python checks/table1_tally.py      (exit 0 iff both tallies reproduce)
"""

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE.parent / "census_pilot_11events.csv"

# expected from ai_and_math.md Section 11.5
EXPECTED = {"machine_or_hybrid": (1, 6), "community_or_nonresult": (3, 5)}


def bin_of(regime):
    """Machine/hybrid stratum vs the community-graded-or-non-result stratum."""
    return "machine_or_hybrid" if regime in ("M", "H") else "community_or_nonresult"


def tally(path=CSV):
    counts = {k: [0, 0] for k in EXPECTED}  # [disputes, events]
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            regime = (row.get("regime") or "").strip().upper()
            dispute = (row.get("dispute") or "").strip()
            if dispute == "":
                continue  # no verdict recorded -> not in the 2x2
            b = bin_of(regime)
            counts[b][1] += 1
            if dispute == "1":
                counts[b][0] += 1
    return {k: (v[0], v[1]) for k, v in counts.items()}


def main():
    got = tally()
    ok = True
    print(f"Section 11.5 tallies, re-derived from {CSV.name}:")
    for key, (d, n) in EXPECTED.items():
        g = got.get(key, (0, 0))
        mark = "OK" if g == (d, n) else "MISMATCH"
        if g != (d, n):
            ok = False
        print(f"  {key:26s} expected {d}/{n}   got {g[0]}/{g[1]}   [{mark}]")
    print("PASS: prose tallies reproduce from the coded table" if ok
          else "FAIL: tallies drift from Table 1 — reconcile Section 11.5 or the pilot")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
