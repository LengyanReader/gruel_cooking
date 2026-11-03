#!/usr/bin/env python3
"""Scope and claim guards for the Nature Review package.

This is the gate that keeps the withdrawn material out and keeps the audited
numbers honest. It reads the two sources of record and the generated views.

Gates
-----
A. Synopsis length. Nature asks for 300-500 words. The English gate is
   300-500 whitespace words. Chinese has no whitespace word boundary, so the
   gate is on CJK characters; a faithful rendering of a ~430-word English
   Synopsis runs 380-800 characters, and that band is the documented
   equivalent rather than a literal 1:1 character count.
B. No withdrawn empirical apparatus anywhere in the Review or the Synopses:
   the 1/6 and 3/5 tallies, the Fisher test and its P value, Figure 1, the
   eleven-event census, or links to the census kit.
C. The 75.7% score may appear only next to ARC-AGI. It is o3's ARC-AGI
   result, not a FrontierMath number; the known failure mode of the old
   draft was exactly this conflation, so it is checked mechanically.
D. The four generated views exist and are non-empty, and the four withdrawn
   filenames are gone.

Run:  python checks/review_scope.py     (exit 0 iff all gates pass)
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUB = HERE.parent
ESSAYS = SUB.parent

REVIEW = ESSAYS.parent / "articles" / "ai_and_math.md"
SYN_EN = SUB / "comment_draft.md"
SYN_ZH = SUB / "comment_draft_zh.md"

VIEWS = ["review_EN.md", "review_ZH.md", "synopsis_EN.md", "synopsis_ZH.md"]
WITHDRAWN_VIEWS = ["comment_EN.md", "comment_ZH.md", "paper_EN.md", "paper_ZH.md"]

EN_MIN, EN_MAX = 300, 500
ZH_MIN, ZH_MAX = 380, 800

# (label, regex) -- must not appear in the Review or the Synopses.
# The withdrawn *apparatus* is banned. The plain word "census" is allowed,
# because section 7 legitimately proposes a census of attempted certifications
# as future work; what is banned is the old table, its tallies and the links to
# the kit that held it.
FORBIDDEN = [
    ("the 1/6 tally", r"1\s*/\s*6"),
    ("the 3/5 tally", r"3\s*/\s*5"),
    ("a Fisher test", r"[Ff]isher"),
    ("the P ~= 0.24 value", r"0\.24"),
    ("Figure 1", r"[Ff]igure\s*1\b|figure1"),
    ("the eleven-event census", r"eleven[- ]event|11\s*[场个]\s*事件"),
    ("a table reference", r"\bTable\s*1\b|表\s*1\b"),
    ("links to the census kit",
     r"census_pilot|census_protocol|census_prereg|census_runbook|checks/figure1"),
]

# words that must not survive from the old draft into the new one
STALE = [("old Comment framing", r"\bNature Comment\b|\bComment draft\b|评论稿"),
         ("parent-paper cross reference", r"parent paper|父稿|§\s*11")]


def slice_between(text, begin, end):
    start = text.index(begin) + len(begin)
    return text[start:text.index(end, start)].strip()


def main():
    failures = []
    review = REVIEW.read_text(encoding="utf-8")
    syn_en = slice_between(SYN_EN.read_text(encoding="utf-8"),
                           "<!-- BODY-EN-BEGIN -->", "<!-- BODY-EN-END -->")
    syn_zh = slice_between(SYN_ZH.read_text(encoding="utf-8"),
                           "<!-- BODY-ZH-BEGIN -->", "<!-- BODY-ZH-END -->")

    en_words = len(syn_en.split())
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", syn_zh))
    if not (EN_MIN <= en_words <= EN_MAX):
        failures.append(f"English Synopsis is {en_words} words, outside {EN_MIN}-{EN_MAX}")
    if not (ZH_MIN <= zh_chars <= ZH_MAX):
        failures.append(f"Chinese Synopsis is {zh_chars} CJK characters, outside {ZH_MIN}-{ZH_MAX}")

    scope_text = review + "\n" + syn_en + "\n" + syn_zh
    for label, pattern in FORBIDDEN:
        hits = [m.group(0) for m in re.finditer(pattern, scope_text)]
        if hits:
            uniq = sorted(set(hits))
            failures.append(f"withdrawn material present: {label} -> {uniq[:4]}")
    for label, pattern in STALE:
        hits = [m.group(0) for m in re.finditer(pattern, scope_text)]
        if hits:
            failures.append(f"stale wording present: {label} -> {sorted(set(hits))[:4]}")

    for m in re.finditer(r"75\.7", scope_text):
        window = scope_text[max(0, m.start() - 300): m.end() + 300]
        if "ARC-AGI" not in window and "ARC" not in window:
            snippet = scope_text[max(0, m.start() - 80): m.end() + 80].replace("\n", " ")
            failures.append("75.7% appears without ARC-AGI nearby: ..." + snippet)
            break

    manu = SUB / "manuscripts"
    for name in VIEWS:
        p = manu / name
        if not p.exists() or len(p.read_text(encoding="utf-8").strip()) < 500:
            failures.append(f"generated view missing or too short: manuscripts/{name}")
    for name in WITHDRAWN_VIEWS:
        if (manu / name).exists():
            failures.append(f"withdrawn view still present: manuscripts/{name}")
    if not (SUB / "reader_edition.md").exists():
        failures.append("reader_edition.md is missing")

    print(f"English Synopsis : {en_words} words   (gate {EN_MIN}-{EN_MAX})")
    print(f"Chinese Synopsis : {zh_chars} CJK chars (gate {ZH_MIN}-{ZH_MAX})")
    print(f"scope scan       : {len(scope_text)} chars across Review + both Synopses")
    if failures:
        print()
        for f in failures:
            print("FAIL: " + f)
        return 1
    print("PASS: Synopsis lengths in band; no withdrawn apparatus, tally, Fisher test, "
          "Figure 1 or census link; 75.7% bound to ARC-AGI; generated views present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
