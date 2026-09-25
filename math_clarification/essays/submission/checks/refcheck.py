#!/usr/bin/env python3
"""Submission-integrity gate for the Comment draft (harness MC-W2 / R-D).

Two things that a Nature editor's first automated pass will flag, checked here
rather than asserted:

1. Citation integrity. Every bracketed citation in the §A body must resolve to a
   numbered item in §D, and every §D reference must be cited in the body (Nature
   does not print uncited references). Ranges like [10-12] are expanded.
2. House style. No em dash (U+2014) in the §A body prose (the `nature-writing`
   flagship rule); en dashes in ranges and compound names (2024-2026, Navier-
   Stokes) are legal and are not counted.

Run:  python checks/refcheck.py     (from anywhere; paths are resolved)
Exit: 0 on PASS, 1 on any violation.

This adds no facts; it only checks that the draft's own apparatus is consistent.
"""

import re
import sys
from pathlib import Path

DRAFT = Path(__file__).resolve().parent.parent / "comment_draft.md"
EM_DASH = "\u2014"
EN_DASH = "\u2013"


def body_and_refs(text):
    start = text.index("In May 2026")
    body = text[start:text.index("## B ", start)].split("---")[0]
    refs_block = text.split("## D ", 1)[1].split("## E", 1)[0]
    return body, refs_block


def cited_numbers(body):
    cited = set()
    for grp in re.findall(r"\[([0-9," + EN_DASH + r"\s]+)\]", body):
        for part in grp.split(","):
            part = part.strip()
            if not part:
                continue
            if EN_DASH in part:
                a, b = part.split(EN_DASH)
                cited.update(range(int(a), int(b) + 1))
            else:
                cited.add(int(part))
    return cited


def main():
    text = DRAFT.read_text(encoding="utf-8")
    body, refs_block = body_and_refs(text)
    ref_nums = {int(m) for m in re.findall(r"(?m)^(\d+)\.\s", refs_block)}
    cited = cited_numbers(body)

    uncited = sorted(ref_nums - cited)      # in list, never cited in body
    dangling = sorted(cited - ref_nums)     # cited in body, not in list
    em = body.count(EM_DASH)

    print(f"references in list : {len(ref_nums)}")
    print(f"cited in body      : {len(cited)}")
    ok = True
    if uncited:
        ok = False
        print(f"FAIL: references never cited in body: {uncited}")
    if dangling:
        ok = False
        print(f"FAIL: body citations with no reference: {dangling}")
    if em:
        ok = False
        print(f"FAIL: {em} em dash(es) in body prose (Nature house style)")
    if ok:
        print("PASS: every reference is cited, every citation resolves, no em dashes")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
