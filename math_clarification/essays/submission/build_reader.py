#!/usr/bin/env python3
"""Build the combined reader's edition AND a clean, language-split manuscript set.

Why a build script instead of hand-assembled files: ai_and_math.md is the *source
of record* for the full paper, and comment_draft.md §A is the source of record for the
English Comment (comment_draft_zh.md for its Chinese). Copying them by hand into other
documents would create a second truth that silently drifts. So this script *assembles*
`reader_edition.md` (bilingual, single document) and the four views under `manuscripts/`
from those three files at build time, and `--check` re-assembles and compares, failing
if any generated file no longer matches its sources (harness MC-W2/R-D: what a machine
can keep consistent, keep consistent by machine; 信息无损: nothing is edited in the merge,
only concatenated with generated front matter, and the language split carries a hard
coverage guard so it cannot drop a line).

Layout of the reader's edition (reader_edition.md):
  front matter (provenance + 导读 foreword + Comment->paper section map)
  Part I  简版·导读 / The Comment (reader's guide):  <!-- en --> English, <!-- zh --> Chinese
  Part II 完整版 / The full paper (verbatim from ai_and_math.md)

Clean manuscript set (manuscripts/), one file per language per work, for viewing and
adjusting. These are *generated views*; edit the three source files, then rebuild:
  comment_EN.md   简版·英文 = Comment §A body + §D references
  comment_ZH.md   简版·中文 = Chinese Comment body
  paper_EN.md     完整版·英文 = every <!-- en --> span of ai_and_math.md (incl. refs)
  paper_ZH.md     完整版·中文 = every <!-- zh --> span of ai_and_math.md (incl. refs)

Run:  python build_reader.py            # (re)generate reader_edition.md + manuscripts/
      python build_reader.py --check    # exit 1 if any generated file is stale
Deps: none (stdlib).
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent            # .../essays/submission
ESSAYS = HERE.parent                                # .../essays
COMMENT_EN = HERE / "comment_draft.md"
COMMENT_ZH = HERE / "comment_draft_zh.md"
PAPER = ESSAYS / "ai_and_math.md"
OUT = HERE / "reader_edition.md"
VIEW_DIR = HERE / "manuscripts"

ZH_BEGIN = "<!-- BODY-ZH-BEGIN -->"
ZH_END = "<!-- BODY-ZH-END -->"

# One bilingual block = "<!-- L1|L5 --> <!-- en --> <English> <!-- zh --> <Chinese>
# <!-- L1|L5-end -->". 12 section blocks + 1 reference block (L5) = 13.
BLOCK_RE = re.compile(
    r"<!--\s*(?:L1|L5)\s*-->\s*<!--\s*en\s*-->"
    r"(?P<en>.*?)<!--\s*zh\s*-->(?P<zh>.*?)<!--\s*(?:L1|L5)-end\s*-->",
    re.DOTALL,
)


def english_comment():
    """Slice the §A manuscript body out of comment_draft.md (title line to the rule
    before '## B'), trimmed of the trailing horizontal rule."""
    c = COMMENT_EN.read_text(encoding="utf-8")
    start = c.index("### Mathematics is not in crisis")
    end = c.index("\n## B ", start)
    seg = c[start:end].rstrip()
    while seg.endswith("---"):
        seg = seg[:-3].rstrip()
    return seg


def chinese_comment():
    z = COMMENT_ZH.read_text(encoding="utf-8")
    start = z.index(ZH_BEGIN) + len(ZH_BEGIN)
    end = z.index(ZH_END)
    return z[start:end].strip()


def comment_reference_block():
    """The Nature-format reference list (§D) from comment_draft.md, with the internal
    '## D ·' navigational label normalised to a plain '## References' for the clean view.
    Only the heading text changes; every entry is carried verbatim."""
    c = COMMENT_EN.read_text(encoding="utf-8")
    start = c.index("## D · References")
    end = c.index("\n## E ", start)
    seg = c[start:end].strip()
    return seg.replace("## D · References (Nature format)", "## References (Nature format)", 1)


def full_paper():
    return PAPER.read_text(encoding="utf-8").strip()


def paper_views():
    """Split ai_and_math.md into an all-English and an all-Chinese reading document.

    信息无损 guard: after removing every matched bilingual block, whatever remains in
    the source must be only the (bilingual) title line, horizontal rules, block markers
    or blank lines. If any other line survived, the split would be dropping real content
    and we fail loudly instead of producing a lossy view."""
    text = PAPER.read_text(encoding="utf-8")
    matches = list(BLOCK_RE.finditer(text))
    if len(matches) != 13:
        raise AssertionError(
            f"paper_views: expected 13 bilingual blocks (12 sections + references), "
            f"found {len(matches)} — check the en/zh/L1/L5 markers in ai_and_math.md")
    head = text[:matches[0].start()]
    title_lines = [ln for ln in head.splitlines()
                   if ln.strip() and not ln.strip().startswith("<!--") and ln.strip() != "---"]
    title = title_lines[0].strip() if title_lines else ""
    en_spans = [m.group("en").strip() for m in matches]
    zh_spans = [m.group("zh").strip() for m in matches]
    remainder = BLOCK_RE.sub("", text)
    for ln in remainder.splitlines():
        s = ln.strip()
        if not s or s == "---" or s.startswith("<!--") or s == title:
            continue
        raise AssertionError(
            f"paper_views: line would be lost by the language split (not title/separator/"
            f"marker): {ln!r}")
    en_doc = title + "\n\n" + "\n\n---\n\n".join(en_spans) + "\n"
    zh_doc = title + "\n\n" + "\n\n---\n\n".join(zh_spans) + "\n"
    return en_doc, zh_doc


def view_front(title_zh, title_en, source_hint):
    """A short provenance header for each generated manuscript view."""
    return (
        f"> **状态 Status**: 由 [`build_reader.py`](../build_reader.py) **生成，请勿手改** "
        f"· *generated, do not edit by hand.* 编辑请回到唯一真源 "
        f"({source_hint})，再运行 `python build_reader.py` 刷新本文件。"
        f"To adjust: edit the source of record above, then rebuild.\n"
        f">\n"
        f"> **{title_zh} · {title_en}**\n\n"
    )


def manuscript_outputs():
    """The four clean language-split views as (path, content)."""
    paper_en, paper_zh = paper_views()
    comment_en_doc = english_comment() + "\n\n---\n\n" + comment_reference_block() + "\n"
    comment_zh_doc = chinese_comment() + "\n"
    return [
        (VIEW_DIR / "comment_EN.md",
         "# Comment (English) · Mathematics is not in crisis: its consensus is\n\n"
         + view_front("简版·英文", "The Comment (EN)", "`comment_draft.md` §A + §D")
         + comment_en_doc),
        (VIEW_DIR / "comment_ZH.md",
         "# 中文简版 · 《数学并未陷入危机：陷入危机的是它的共识》\n\n"
         + view_front("简版·中文", "The Comment (ZH)", "`comment_draft_zh.md`")
         + comment_zh_doc),
        (VIEW_DIR / "paper_EN.md",
         "# Full Paper (English)\n\n"
         + view_front("完整版·英文", "The Full Paper (EN)", "`ai_and_math.md`")
         + paper_en),
        (VIEW_DIR / "paper_ZH.md",
         "# 完整版 · 中文\n\n"
         + view_front("完整版·中文", "The Full Paper (ZH)", "`ai_and_math.md`")
         + paper_zh),
    ]


def front_matter():
    """Generated 导读: framing + the Comment->paper map. Authored here (not in the
    source files) so the two source-of-record documents stay untouched."""
    return """# 导读与全编 · 数学的危机，还是数学家的危机？
# Reader's Edition · A Crisis of Mathematics, or of the Mathematicians?

> **Status 状态**: A single-document reading edition. **AI-drafted, unreviewed** (harness §I.6). **Generated by [`build_reader.py`](build_reader.py); do not edit by hand.** The Comment text here is copied from [`comment_draft.md`](comment_draft.md) §A (English) and [`comment_draft_zh.md`](comment_draft_zh.md) (Chinese); the full paper is copied verbatim from [`../ai_and_math.md`](../ai_and_math.md), which **remains the source of record**. To refresh after editing any source: `python build_reader.py`; to verify this file is current: `python build_reader.py --check`. A clean, single-language manuscript set is generated alongside this file under [`manuscripts/`](manuscripts/).
>
> **How to read 阅读法**: Part I is the *Comment* — a ~1,670-word argument written for a general scientific readership. It is also the **导读 (reading guide)** for Part II: every claim it makes is a compressed version of a claim the full paper argues at length. Read Part I for the shape of the case; go to Part II (and the section map below) for the evidence, the rival explanations, the audit apparatus, and the philosophy.

## 前沿 · 导读 · Foreword

The short piece and the long piece are one argument at two resolutions. The Comment stakes a single predictive claim — that where controversy lands in AI mathematics is a function of the **certification regime**, not of difficulty — and hands off, in its own last paragraph, to a census that must test what eleven publicity-selected events cannot. The paper supplies everything the Comment has to compress: the literature reconstruction (1954–2026), the five rival explanations and the four observations that would refute them, the eleven-event coding with its two audit tables, the signifier/signified framework and its limits, the sociology of the ladder, and the demarcation criterion. Where the Comment says "meaning, adjudicated by people," §6 says why in one line: the kernel checks proof terms; what a statement *means* is a separate task.

### Comment → paper, section by section

| The Comment's move | Its home in the full paper |
|---|---|
| The three certification regimes (machine / hybrid / community) | §3.1 (five categories) · §11.2 (the ordered decision rule) |
| "Regime, not difficulty" and the rival it cannot exclude | §3.3 (H1–H5) · §4 (the ordering) |
| The eleven events, 1/6 vs 3/5, Fisher P ≈ 0.24 | §4 (evidential base) · §11.4–11.5 (Table 1; what the coding yields and does not) |
| Navier–Stokes: a dispute about which sentence was proved | §4.9 (the top rung) · §6.5 (a proof of the wrong sentence) |
| 1977 four-colour, Tymoczko, DeMillo–Lipton–Perlis, Merton | §2.2 · §2.4 · §2.5 (the three literature streams) |
| The shared syllogism and its false minor premise | §3.2 (the core argument, reconstructed) |
| Disclose / designate the certifier / register admissibility | §10.2–10.3 (the correct naming) · §11.8 (statements) |
| "Faithful only to itself" (left implicit in the Comment) | §6 (signifier and signified, the limits of formal exactness) |

---

# Part I · 简版 · 导读 / The Comment as Reader's Guide

A *Nature*-format Comment: English body, then its Chinese rendering. Figures, the coding CSV, the reliability appendix, and the reference list live in [`comment_draft.md`](comment_draft.md) §§B–D and are not repeated here.

<!-- en -->"""


def assemble():
    parts = [
        front_matter(),
        english_comment(),
        "\n<!-- zh -->\n\n" + chinese_comment(),
        "\n\n---\n\n# Part II · 完整版 / The Full Paper\n\n"
        "Verbatim from [`../ai_and_math.md`](../ai_and_math.md) (source of record), bilingual throughout.\n\n---\n\n"
        + full_paper(),
    ]
    return "\n\n".join(p.strip("\n") for p in parts) + "\n"


def all_outputs():
    """Every generated file this build owns: (path, content)."""
    VIEW_DIR.mkdir(exist_ok=True)
    return [(OUT, assemble())] + manuscript_outputs()


def main(argv):
    outputs = all_outputs()
    if "--check" in argv:
        stale = []
        for path, content in outputs:
            current = path.read_text(encoding="utf-8") if path.exists() else ""
            if current != content:
                stale.append(path.name)
        if stale:
            print("FAIL: stale generated file(s): " + ", ".join(stale)
                  + " — run `python build_reader.py`", file=sys.stderr)
            return 1
        print(f"PASS: {len(outputs)} generated file(s) current with their sources "
              f"(reader_edition.md + manuscripts/)")
        return 0
    for path, content in outputs:
        path.write_text(content, encoding="utf-8")
    n_lines = assemble().count("\n") + 1
    print(f"wrote {OUT.name}: {n_lines} lines, "
          f"{len(english_comment().split())} EN comment words, "
          f"full paper embedded from {PAPER.name}")
    for path, content in manuscript_outputs():
        print(f"wrote manuscripts/{path.name}: {content.count(chr(10)) + 1} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
