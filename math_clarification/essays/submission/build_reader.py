#!/usr/bin/env python3
"""Build the bilingual Nature Review, its Synopses, and the reader's edition.

Sources of record
-----------------
  ../../articles/ai_and_math.md  bilingual Review body + references (L1/L5 blocks)
  comment_draft.md           English Synopsis (BODY-EN-BEGIN/END)
  comment_draft_zh.md        Chinese Synopsis (BODY-ZH-BEGIN/END)

Generated views
---------------
  reader_edition.md          Synopsis (EN/ZH) + full Review (verbatim bilingual)
  manuscripts/review_EN.md   Synopsis (EN) + Review (EN, incl. references)
  manuscripts/review_ZH.md   Synopsis (ZH) + Review (ZH, incl. references)
  manuscripts/synopsis_EN.md Synopsis (EN)
  manuscripts/synopsis_ZH.md Synopsis (ZH)

Run:  python build_reader.py            # regenerate
      python build_reader.py --check    # exit 1 if stale or orphaned
Deps: none (stdlib).
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ESSAYS = HERE.parent
SYNOPSIS_EN = HERE / "comment_draft.md"
SYNOPSIS_ZH = HERE / "comment_draft_zh.md"
PAPER = ESSAYS.parent / "articles" / "ai_and_math.md"
OUT = HERE / "reader_edition.md"
VIEW_DIR = HERE / "manuscripts"

EN_BEGIN = "<!-- BODY-EN-BEGIN -->"
EN_END = "<!-- BODY-EN-END -->"
ZH_BEGIN = "<!-- BODY-ZH-BEGIN -->"
ZH_END = "<!-- BODY-ZH-END -->"

BLOCK_RE = re.compile(
    r"<!--\s*(?:L1|L5)\s*-->\s*<!--\s*en\s*-->"
    r"(?P<en>.*?)<!--\s*zh\s*-->(?P<zh>.*?)<!--\s*(?:L1|L5)-end\s*-->",
    re.DOTALL,
)
OPEN_RE = re.compile(r"<!--\s*(?:L1|L5)\s*-->")


def _slice(text, begin, end):
    start = text.index(begin) + len(begin)
    stop = text.index(end, start)
    return text[start:stop].strip()


def english_synopsis():
    return _slice(SYNOPSIS_EN.read_text(encoding="utf-8"), EN_BEGIN, EN_END)


def chinese_synopsis():
    return _slice(SYNOPSIS_ZH.read_text(encoding="utf-8"), ZH_BEGIN, ZH_END)


def full_paper():
    return PAPER.read_text(encoding="utf-8").strip()


def _title_for(title, lang):
    """The source H1 is bilingual ('中文 / English'); a single-language view wants its half."""
    parts = [p.strip() for p in title.split(" / ")]
    if len(parts) == 2:
        cjk = re.compile(r"[\u4e00-\u9fff]")
        want = [p for p in parts if bool(cjk.search(p)) == (lang == "zh")]
        if want:
            return want[0]
    return title


def paper_views():
    """Split the bilingual Review into all-English and all-Chinese views.

    The source declares its own block count with opening markers, so adding or
    removing a section does not require editing this script. Every block must
    carry non-empty text in both languages, and anything outside the blocks may
    be only the title, rules, comments or blank lines. The split therefore fails
    loudly rather than silently dropping content.
    """
    text = PAPER.read_text(encoding="utf-8")
    matches = list(BLOCK_RE.finditer(text))
    expected = len(OPEN_RE.findall(text))
    if len(matches) != expected:
        raise AssertionError(
            f"paper_views: {expected} opening markers but {len(matches)} complete "
            "en/zh blocks — check the L1/L5 markers in ai_and_math.md"
        )
    if not matches:
        raise AssertionError("paper_views: no bilingual blocks found in ai_and_math.md")

    head = text[: matches[0].start()]
    title_lines = [
        ln for ln in head.splitlines()
        if ln.strip() and not ln.strip().startswith("<!--") and ln.strip() != "---"
    ]
    if not title_lines or not title_lines[0].startswith("# "):
        raise AssertionError("paper_views: first content line of ai_and_math.md must be its H1 title")
    title = title_lines[0].strip()[2:].strip()

    en_spans = [m.group("en").strip() for m in matches]
    zh_spans = [m.group("zh").strip() for m in matches]
    if any(not s for s in en_spans + zh_spans):
        raise AssertionError("paper_views: an L1/L5 block has an empty language side")

    remainder = BLOCK_RE.sub("", text)
    for ln in remainder.splitlines():
        s = ln.strip()
        if not s or s == "---" or s.startswith("<!--") or s == title_lines[0].strip():
            continue
        raise AssertionError(
            "paper_views: line would be lost by the language split: " + repr(ln)
        )

    en_doc = "## " + _title_for(title, "en") + "\n\n" + "\n\n---\n\n".join(en_spans) + "\n"
    zh_doc = "## " + _title_for(title, "zh") + "\n\n" + "\n\n---\n\n".join(zh_spans) + "\n"
    return en_doc, zh_doc


def view_front(label_zh, label_en, source_hint):
    return (
        f"> **状态 Status**: 由 [`build_reader.py`](../build_reader.py) **生成，请勿手改** "
        f"· *generated, do not edit by hand.* 真源：{source_hint}；运行 "
        f"`python build_reader.py` 刷新。\n>\n"
        f"> **{label_zh} · {label_en}**\n\n"
    )


def manuscript_outputs():
    paper_en, paper_zh = paper_views()
    syn_en = english_synopsis()
    syn_zh = chinese_synopsis()
    return [
        (VIEW_DIR / "synopsis_EN.md",
         "# Synopsis (English) · Mathematical truth is not a matter of consensus\n\n"
         + view_front("提要·英文", "Synopsis (EN)", "`comment_draft.md` BODY-EN")
         + syn_en + "\n"),
        (VIEW_DIR / "synopsis_ZH.md",
         "# 提要（中文）·《数学真理不由共识决定》\n\n"
         + view_front("提要·中文", "Synopsis (ZH)", "`comment_draft_zh.md` BODY-ZH")
         + syn_zh + "\n"),
        (VIEW_DIR / "review_EN.md",
         "# Nature Review (English) · Mathematical truth is not a matter of consensus\n\n"
         + view_front("综述·英文", "The Review (EN)", "`articles/ai_and_math.md` + `comment_draft.md`")
         + syn_en + "\n\n---\n\n" + paper_en),
        (VIEW_DIR / "review_ZH.md",
         "# Nature Review（中文）·《数学真理不由共识决定》\n\n"
         + view_front("综述·中文", "The Review (ZH)", "`articles/ai_and_math.md` + `comment_draft_zh.md`")
         + syn_zh + "\n\n---\n\n" + paper_zh),
    ]


def front_matter():
    return """# 导读与全编 · 数学真理不由共识决定
# Reader's Edition · Mathematical Truth Is Not a Matter of Consensus

> **Status 状态**: A generated single-document reading edition. **AI-drafted, unreviewed.** Built by [`build_reader.py`](build_reader.py) from [`comment_draft.md`](comment_draft.md), [`comment_draft_zh.md`](comment_draft_zh.md) and [`../../articles/ai_and_math.md`](../../articles/ai_and_math.md). Do not edit this file by hand; rebuild after editing any source.
>
> **How to read 阅读法**: Part I is the 300–500-word Synopsis in English and Chinese. Part II is the full bilingual Nature Review, reproduced verbatim from its source of record. The earlier eleven-event coding table and Figure 1 have been withdrawn from the manuscript; the census kit under this folder is retained as a separate, currently **withdrawn** research design.

---

# Part I · 提要 / Synopsis

<!-- en -->"""


def assemble():
    parts = [
        front_matter(),
        english_synopsis(),
        "\n<!-- zh -->\n\n" + chinese_synopsis(),
        "\n\n---\n\n# Part II · 完整综述 / The Full Review\n\n"
        "Verbatim from [`../../articles/ai_and_math.md`](../../articles/ai_and_math.md), bilingual throughout.\n\n---\n\n"
        + full_paper(),
    ]
    return "\n\n".join(p.strip("\n") for p in parts) + "\n"


def all_outputs():
    VIEW_DIR.mkdir(exist_ok=True)
    return [(OUT, assemble())] + manuscript_outputs()


def main(argv):
    outputs = all_outputs()
    expected = {path.name for path, _ in outputs if path.parent == VIEW_DIR}
    if "--check" in argv:
        stale = [
            path.name for path, content in outputs
            if not path.exists() or path.read_text(encoding="utf-8") != content
        ]
        orphans = sorted(p.name for p in VIEW_DIR.glob("*.md") if p.name not in expected)
        if stale or orphans:
            if stale:
                print("FAIL: stale generated file(s): " + ", ".join(stale)
                      + " — run `python build_reader.py`", file=sys.stderr)
            if orphans:
                print("FAIL: unexpected file(s) in manuscripts/: " + ", ".join(orphans)
                      + " — remove or restore them", file=sys.stderr)
            return 1
        print(f"PASS: {len(outputs)} generated file(s) current; manuscripts/ has no orphans")
        return 0

    for path, content in outputs:
        path.write_text(content, encoding="utf-8")
    en_words = len(english_synopsis().split())
    print(f"wrote {OUT.name}")
    print(f"English Synopsis: {en_words} whitespace-delimited words")
    for path, content in manuscript_outputs():
        print(f"wrote manuscripts/{path.name}: {content.count(chr(10)) + 1} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
