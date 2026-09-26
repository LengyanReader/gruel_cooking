"""Markdown parser with level cropping and language filtering.

Levels (audience layers):
  L0 - One-line idea (everyone)
  L1 - Intuition / analogy (general readers)
  L2 - Precise statement + premises (students)
  L3 - Math notation + directions (specialists)
  L4 - Lean machine-checked (researchers)
  L5 - Sources + history (deep readers)

Language modes:
  dual - side-by-side or interleaved
  zh   - Chinese only
  en   - English only
"""

import re
from pathlib import Path
from dataclasses import dataclass
import markdown
from markdown.extensions.toc import TocExtension


LEVEL_ORDER = ["L0", "L1", "L2", "L3", "L4", "L5"]


@dataclass
class ParsedEntry:
    title: str
    sections: list  # list of (level, lang, content_html)
    toc: str
    raw_md: str
    note: str = ""  # provenance comment that sat above the first level marker


COMMENT_RE = re.compile(r"<!--(.*?)-->", re.S)
EN_PREFIX_RE = re.compile(r"^(?:en|EN)\s*[:：]\s*")


def extract_notes(raw: str) -> tuple:
    """Return (zh_note, en_note) from the comment(s) above the first level marker.

    Articles carry an HTML comment (drafting disclosure, sourcing scheme) between
    the H1 and the first `<!-- L0 -->`. Markdown keeps it as a raw HTML block, so
    without this it would surface as a stray, contentless section in the body.

    One comment is taken as the source language. An optional second comment
    prefixed with `en:` supplies the English counterpart, so the viewer can switch
    the note along with the article. A lone comment with no CJK counts as English.
    """
    preamble = re.split(r"<!--\s*L[0-5]\s*-->", raw, maxsplit=1)[0]
    texts = [" ".join(c.split()) for c in COMMENT_RE.findall(preamble)]
    texts = [t for t in texts if t]
    if not texts:
        return "", ""

    zh, en = "", ""
    for t in texts:
        m = EN_PREFIX_RE.match(t)
        if m:
            en = en or t[m.end():].strip()
        else:
            zh = zh or t
    if not en and zh and not re.search(r"[\u4e00-\u9fff]", zh):
        zh, en = "", zh
    return zh, en


def extract_note(raw: str, lang: str = "zh") -> str:
    """The note for one language mode, falling back to whichever side exists."""
    zh, en = extract_notes(raw)
    if lang == "en" and en:
        return en
    return zh or en


def parse_entry(filepath: Path) -> ParsedEntry:
    """Parse a Markdown file into structured sections with level/lang tags."""
    raw = filepath.read_text(encoding="utf-8")
    return parse_markdown(raw)


def parse_markdown(raw: str) -> ParsedEntry:
    """Parse raw Markdown content."""
    lines = raw.split("\n")
    title = ""
    sections = []
    current_level = "L0"
    current_lang = "en"
    buffer = []

    def flush():
        """Emit the buffered lines as a section, skipping whitespace-only buffers."""
        if any(line.strip() for line in buffer):
            sections.append((current_level, current_lang, "\n".join(buffer)))
        buffer.clear()

    for line in lines:
        # Extract title from first # heading. The template already renders it in
        # the entry header, so it is not repeated in the body.
        if not title and line.startswith("# "):
            title = line[2:].strip()
            continue

        # Check for level markers: <!-- L0 -->, <!-- L1 -->, etc., and their
        # <!-- L1-end --> closing form.
        level_match = re.match(r"<!--\s*(L[0-5])(-end)?\s*-->", line.strip())
        if level_match:
            flush()
            if level_match.group(2):
                # Closing marker: resets language per the documented format,
                # and the next opening marker sets the level again.
                current_lang = "en"
            else:
                current_level = level_match.group(1)
            continue

        # Check for language markers: <!-- zh -->, <!-- en -->, <!-- dual -->
        lang_match = re.match(r"<!--\s*(zh|en|dual)\s*-->", line.strip())
        if lang_match:
            flush()
            current_lang = lang_match.group(1)
            continue

        # Check for end markers: <!-- zh-end -->, <!-- en-end -->
        if re.match(r"<!--\s*(zh|en|dual)-end\s*-->", line.strip()):
            flush()
            current_lang = "en"  # reset to default
            continue

        buffer.append(line)

    # Flush remaining buffer
    flush()

    # Convert each section to HTML
    md_converter = markdown.Markdown(extensions=[
        "extra",
        "codehilite",
        "fenced_code",
        TocExtension(permalink=False),
    ])

    html_sections = []
    for level, lang, content in sections:
        md_converter.reset()
        html = nest_sections(md_converter.convert(content))
        # A comment-only chunk carries no readable content; extract_note() has
        # already surfaced the preamble one as a visible note.
        if not COMMENT_RE.sub("", html).strip():
            continue
        html_sections.append((level, lang, html))

    # Build TOC
    md_converter.reset()
    md_converter.convert(raw)
    toc = md_converter.toc

    return ParsedEntry(
        title=title,
        sections=html_sections,
        toc=toc,
        raw_md=raw,
        note=extract_note(raw),
    )


def filter_by_level(entry: ParsedEntry, max_level: str) -> ParsedEntry:
    """Keep only sections up to max_level."""
    max_idx = LEVEL_ORDER.index(max_level)
    filtered = [
        (level, lang, html)
        for level, lang, html in entry.sections
        if LEVEL_ORDER.index(level) <= max_idx
    ]
    return ParsedEntry(
        title=entry.title,
        sections=filtered,
        toc=entry.toc,
        raw_md=entry.raw_md,
        note=entry.note,
    )


def filter_by_lang(entry: ParsedEntry, lang_mode: str) -> ParsedEntry:
    """Filter sections by language mode.

    - 'en': keep only lang='en' sections
    - 'zh': keep only lang='zh' sections (fallback to en if no zh exists)
    - 'dual': keep all sections
    """
    if lang_mode == "dual":
        return entry

    filtered = [
        (level, lang, html)
        for level, lang, html in entry.sections
        if lang == lang_mode or lang == "dual"
    ]

    # Fallback: if no sections for requested lang, return all (unilingual file)
    if not filtered:
        return entry

    return ParsedEntry(
        title=entry.title,
        sections=filtered,
        toc=entry.toc,
        raw_md=entry.raw_md,
        note=entry.note,
    )


def render_entry_html(entry: ParsedEntry) -> str:
    """Render filtered sections into a single HTML string."""
    parts = []
    for level, lang, html in entry.sections:
        lang_tag = f'<span class="lang-tag">{lang.upper()}</span>' if lang != "en" else ""
        level_tag = f'<span class="level-tag">{level}</span>'
        parts.append(
            f'<section class="entry-section" data-level="{level}" data-lang="{lang}">'
            f'{level_tag}{lang_tag}'
            f'<div class="section-content">{html}</div>'
            f'</section>'
        )
    return "\n".join(parts)


HEADING_RE = re.compile(r'<h([2-4])(?:\s+id="[^"]*")?\s*>(.*?)</h\1>', re.S)


NEST_HEAD_RE = re.compile(r"<h([2-4])(?:\s+id=\"[^\"]*\")?\s*>", re.I)


def nest_sections(fragment: str) -> str:
    """Wrap each heading and the content beneath it in a depth-classed <section>.

    Long chapters are flat sequences of `## 1 - ...` then `### 1.1 ...`, `### 1.2 ...`.
    CSS alone cannot scope "indent until the next heading of the same or higher
    rank" — there is no such selector — so the grouping is built here instead.
    Content before the first heading is left at the top level.
    """
    marks = list(NEST_HEAD_RE.finditer(fragment))
    if not marks:
        return fragment
    out = [fragment[: marks[0].start()]]
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(fragment)
        out.append('<section class="sub d%d">%s</section>'
                   % (int(m.group(1)) - 2, fragment[m.start():end]))
    return "\n".join(out)


def build_toc(sections):
    """Assign unique heading ids to the displayed sections and return a TOC.

    TocExtension derives ids from the heading text, so in a bilingual file every
    Chinese heading collapses onto the same slug and the anchors collide. This
    walks the sections that are actually being shown, after level and language
    filtering, and hands out unique ids in document order.

    Returns (toc_items, sections); toc_items is a list of dicts with
    tag, text, id and lang.
    """
    items = []
    seen = {}
    rebuilt = []
    for level, lang, html in sections:
        def repl(m):
            tag, inner = m.group(1), m.group(2)
            text = re.sub(r"<[^>]+>", "", inner).strip()
            base = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", text).strip("-").lower()[:48]
            base = base or "sec"
            n = seen.get(base, 0)
            seen[base] = n + 1
            anchor = base if n == 0 else f"{base}-{n}"
            items.append({"tag": tag, "text": text, "id": anchor, "lang": lang})
            return f'<h{tag} id="{anchor}">{inner}</h{tag}>'
        rebuilt.append((level, lang, HEADING_RE.sub(repl, html)))
    return items, rebuilt


def list_entries(base_dir: Path) -> list[dict]:
    """List all available entries across basics/, famous_problems/, proof_narratives/ and articles/."""
    entries = []
    for subdir in ["basics", "famous_problems", "proof_narratives", "articles"]:
        dir_path = base_dir / subdir
        if not dir_path.exists():
            continue
        for f in sorted(dir_path.glob("*.md")):
            if f.name == "README.md":
                continue
            slug = f.stem
            # Quick title extract
            title = f.stem.replace("_", " ").title()
            for line in f.read_text(encoding="utf-8").split("\n")[:5]:
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
            entries.append({
                "slug": slug,
                "title": title,
                "path": str(f),
                "category": subdir,
            })
    return entries
