#!/usr/bin/env python3
"""Reproduce the WITHDRAWN pilot tallies as history, not as a manuscript claim.

Scope change from the previous version of this script
-----------------------------------------------------
The old script validated a prose sentence in ai_and_math.md ("1 dispute among 6
machine-/hybrid-graded events, 3 among 5 community-graded-or-non-result
events"). That sentence is gone. The Review now makes no tally, presents no
figure and reports no statistical test, so there is nothing for this script to
validate.

What it does now
----------------
It re-derives the historical arithmetic from census_pilot_11events.csv and
prints it as an archive fact, alongside the honest stratum split. It fails only
if the arithmetic no longer reproduces *as history*, i.e. if someone edits the
pilot CSV and breaks the record of what was coded.

It is a check on the archive, not a validation of any claim in the Review.
Do not quote its output in the manuscript.

Run:  python checks/table1_tally.py      (exit 0 iff the archive reproduces)
"""

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE.parent / "census_pilot_11events.csv"

# the withdrawn headline, kept only to show that it reproduces
WITHDRAWN_HEADLINE = {"machine_or_hybrid": (1, 6), "community_or_nonresult": (3, 5)}


def bin_of(regime):
    """Machine/hybrid stratum vs the community-graded-or-non-result stratum.

    Note the second arm: an empty regime is treated as 'non-result' and lands
    with the community. That was the original error, and it is preserved here
    only so the withdrawn figure can be reproduced exactly.
    """
    return "machine_or_hybrid" if regime in ("M", "H") else "community_or_nonresult"


def tally(path=CSV):
    counts = {k: [0, 0] for k in WITHDRAWN_HEADLINE}
    strata = {"M": [0, 0], "H": [0, 0], "C": [0, 0], "": [0, 0]}
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            regime = (row.get("regime") or "").strip().upper()
            dispute = (row.get("dispute") or "").strip()
            if dispute == "":
                continue  # no verdict recorded -> not in the 2x2
            counts[bin_of(regime)][1] += 1
            strata.setdefault(regime, [0, 0])[1] += 1
            if dispute == "1":
                counts[bin_of(regime)][0] += 1
                strata[regime][0] += 1
    return {k: tuple(v) for k, v in counts.items()}, {k: tuple(v) for k, v in strata.items()}


def main():
    if not CSV.exists():
        print(f"FAIL: {CSV} not found (the archive data was deleted)", file=sys.stderr)
        return 1
    got, strata = tally()

    print("ARCHIVE ONLY. Nothing below is a claim of the Nature Review.")
    print(f"withdrawn headline, re-derived from {CSV.name}:")
    ok = True
    for key, (d, n) in WITHDRAWN_HEADLINE.items():
        g = got.get(key, (0, 0))
        mark = "OK" if g == (d, n) else "MISMATCH"
        if g != (d, n):
            ok = False
        print(f"  {key:26s} withdrawn {d}/{n}   archive {g[0]}/{g[1]}   [{mark}]")

    print("honest stratum split (the n-a row kept as its own category):")
    for regime, (d, n) in strata.items():
        name = {"M": "machine", "H": "hybrid", "C": "community", "": "not applicable"}[regime]
        print(f"  {name:26s} {d}/{n}")

    print("why the headline was withdrawn: the not-applicable row is not community-graded; "
          "the pilot contradicts its own P1 prediction that machine-graded events never "
          "produce a dispute; and n = 11 selected through publicity supports no rate.")
    print("PASS: the archive reproduces" if ok else "FAIL: the archive no longer reproduces")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
