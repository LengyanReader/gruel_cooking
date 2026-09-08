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

    for line in lines:
        # Extract title from first # heading
        if not title and line.startswith("# "):
            title = line[2:].strip()
            buffer.append(line)
            continue

        # Check for level markers: <!-- L0 -->, <!-- L1 -->, etc.
        level_match = re.match(r"<!--\s*(L[0-5])\s*-->", line.strip())
        if level_match:
            if buffer:
                sections.append((current_level, current_lang, "\n".join(buffer)))
                buffer = []
            current_level = level_match.group(1)
            continue

        # Check for language markers: <!-- zh -->, <!-- en -->, <!-- dual -->
        lang_match = re.match(r"<!--\s*(zh|en|dual)\s*-->", line.strip())
        if lang_match:
            if buffer:
                sections.append((current_level, current_lang, "\n".join(buffer)))
                buffer = []
            current_lang = lang_match.group(1)
            continue

        # Check for end markers: <!-- zh-end -->, <!-- en-end -->
        if re.match(r"<!--\s*(zh|en|dual)-end\s*-->", line.strip()):
            if buffer:
                sections.append((current_level, current_lang, "\n".join(buffer)))
                buffer = []
            current_lang = "en"  # reset to default
            continue

        buffer.append(line)

    # Flush remaining buffer
    if buffer:
        sections.append((current_level, current_lang, "\n".join(buffer)))

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
        html = md_converter.convert(content)
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


def list_entries(base_dir: Path) -> list[dict]:
    """List all available entries across basics/, famous_problems/ and proof_narratives/."""
    entries = []
    for subdir in ["basics", "famous_problems", "proof_narratives"]:
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
