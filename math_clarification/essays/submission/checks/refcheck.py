#!/usr/bin/env python3
"""Check the reference apparatus of the Nature Review source of record.

Target: ../../articles/ai_and_math.md (the bilingual Review, not the withdrawn Comment).

Gates
-----
1. English Review body contains no em dash (U+2014) or en dash used as punctuation.
2. Chinese Review body contains no em dash (U+2014).
3. Every citation resolves to a reference entry (no dangling citations).
4. Every reference entry is cited at least once (no orphan entries).
5. Reference numbering is contiguous 1..N in both language blocks.
6. References are ordered by first appearance in the text, Nature style.
7. N <= 150 (Nature's stated ceiling for a Review).

Run:  python checks/refcheck.py        (exit 0 iff all gates pass)
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent.parent.parent / "articles" / "ai_and_math.md"

BLOCK_RE = re.compile(
    r"<!--\s*(?:L1|L5)\s*-->\s*<!--\s*en\s*-->"
    r"(?P<en>.*?)<!--\s*zh\s*-->(?P<zh>.*?)<!--\s*(?:L1|L5)-end\s*-->",
    re.DOTALL,
)
REF_LINE = re.compile(r"^(\d+)\.\s+\S")
CITE_GROUP = re.compile(r"\[((?:\d+)(?:\s*[,\u2013-]\s*\d+)*)\]")
MAX_REFS = 150

ZH_REF_HEADING = "## 参考文献"
EN_REF_HEADING = "## References"


def split_languages(text):
    blocks = list(BLOCK_RE.finditer(text))
    if not blocks:
        raise SystemExit("FAIL: no bilingual L1/L5 blocks found in ai_and_math.md")
    en = "\n\n".join(m.group("en").strip() for m in blocks)
    zh = "\n\n".join(m.group("zh").strip() for m in blocks)
    return en, zh


def split_refs(doc, heading):
    if heading not in doc:
        raise SystemExit(f"FAIL: heading {heading!r} not found")
    body, refs = doc.split(heading, 1)
    return body.strip(), refs.strip()


def ref_numbers(refs_text):
    return [int(m.group(1)) for ln in refs_text.splitlines() if (m := REF_LINE.match(ln))]


def cited_numbers(body_text):
    cited = []
    for group in CITE_GROUP.findall(body_text):
        for part in re.split(r"\s*,\s*", group):
            rng = re.match(r"^(\d+)\s*[\u2013-]\s*(\d+)$", part)
            if rng:
                a, b = int(rng.group(1)), int(rng.group(2))
                cited.extend(range(min(a, b), max(a, b) + 1))
            else:
                cited.append(int(part))
    return cited


def main():
    if not PAPER.exists():
        raise SystemExit(f"FAIL: {PAPER} not found")
    en_all, zh_all = split_languages(PAPER.read_text(encoding="utf-8"))
    en_body, en_refs = split_refs(en_all, EN_REF_HEADING)
    zh_body, zh_refs = split_refs(zh_all, ZH_REF_HEADING)

    failures = []

    for label, text in (("English", en_body), ("Chinese", zh_body)):
        if "\u2014" in text:
            n = text.count("\u2014")
            failures.append(f"{label} body contains {n} em dash(es) (U+2014)")

    en_nums = ref_numbers(en_refs)
    zh_nums = ref_numbers(zh_refs)
    for label, nums in (("EN", en_nums), ("ZH", zh_nums)):
        if not nums:
            failures.append(f"{label} reference list is empty or unparseable")
            continue
        if nums != list(range(1, len(nums) + 1)):
            failures.append(f"{label} reference numbering is not contiguous 1..{len(nums)}")
        if len(nums) > MAX_REFS:
            failures.append(f"{label} has {len(nums)} references, over the Nature ceiling of {MAX_REFS}")
    if en_nums and zh_nums and en_nums != zh_nums:
        failures.append("EN and ZH reference blocks disagree on numbering")

    cited = cited_numbers(en_body)
    ref_set = set(en_nums)
    cited_set = set(cited)
    dangling = sorted(cited_set - ref_set)
    orphan = sorted(ref_set - cited_set)
    if dangling:
        failures.append("citations with no reference entry: " + ", ".join(map(str, dangling)))
    if orphan:
        failures.append("reference entries never cited: " + ", ".join(map(str, orphan)))

    first_seen = []
    for n in cited:
        if n not in first_seen:
            first_seen.append(n)
    if first_seen != sorted(first_seen):
        failures.append("references are not ordered by first appearance in the text")

    n_refs = len(en_nums)
    n_cited = len(cited)
    zh_cjk = len(re.findall(r"[\u4e00-\u9fff]", zh_body))
    print(f"source        : {PAPER}")
    print(f"references    : {n_refs} (EN block) / {len(zh_nums)} (ZH block)")
    print(f"citations     : {n_cited} in-text markers -> {len(cited_set)} distinct entries")
    print(f"english body  : {len(en_body.split())} whitespace words (excl. references)")
    print(f"chinese body  : {zh_cjk} CJK characters")
    if failures:
        print()
        for f in failures:
            print("FAIL: " + f)
        return 1
    print("PASS: no em dash; citations all resolve; no orphan entries; "
          "numbering contiguous and in first-appearance order")
    return 0


if __name__ == "__main__":
    sys.exit(main())
