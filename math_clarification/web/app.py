"""FastAPI app for Math Clarification web viewer.

Routes:
  /                           - Home page (entry list)
  /entry/{category}/{slug}    - View a single entry
  /api/entry/{category}/{slug} - JSON API for entry data

Query params:
  level  - max display level: L0..L5 (default: L5)
  lang   - language mode: zh, en, dual (default: dual)
"""

from pathlib import Path
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from parser import (
    parse_entry,
    filter_by_level,
    filter_by_lang,
    render_entry_html,
    build_toc,
    extract_notes,
    list_entries,
    LEVEL_ORDER,
)

BASE_DIR = Path(__file__).resolve().parent.parent  # math_clarification/

app = FastAPI(title="Math Clarification", version="0.1.0")

app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

CATEGORY_LABELS = {
    "basics": ("Basics", "基础"),
    "famous_problems": ("Famous Problems", "名题"),
    "proof_narratives": ("Proof Narratives", "证明的叙事"),
    "articles": ("Articles", "文章"),
}


def _entry_counts():
    """{category: n} for the nav badges."""
    counts = {}
    for e in list_entries(BASE_DIR):
        counts[e["category"]] = counts.get(e["category"], 0) + 1
    return counts


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, cat: str = Query("", description="Filter by category")):
    entries = list_entries(BASE_DIR)
    if cat:
        entries = [e for e in entries if e["category"] == cat]
    groups = []
    for key in ("basics", "famous_problems", "proof_narratives", "articles"):
        items = [e for e in entries if e["category"] == key]
        if items:
            en, zh = CATEGORY_LABELS.get(key, (key, key))
            groups.append({"key": key, "en": en, "zh": zh, "items": items})
    static_dir = Path(__file__).parent / "static" / "articles"
    static_slugs = {p.stem for p in static_dir.glob("*.html")} - {"index"} if static_dir.exists() else set()
    return templates.TemplateResponse(request, "home.html", {
        "entries": entries,
        "groups": groups,
        "counts": _entry_counts(),
        "labels": CATEGORY_LABELS,
        "current_cat": cat,
        "static_slugs": static_slugs,
        "hide_draft": True,
        "lang": "dual",
    })


@app.get("/entry/{category}/{slug}", response_class=HTMLResponse)
async def view_entry(
    request: Request,
    category: str,
    slug: str,
    level: str = Query("L5", description="Max level: L0-L5"),
    lang: str = Query("dual", description="Language: zh, en, dual"),
):
    # Validate
    if level not in LEVEL_ORDER:
        level = "L5"
    if lang not in ("zh", "en", "dual"):
        lang = "dual"

    # Locate file
    filepath = BASE_DIR / category / f"{slug}.md"
    if not filepath.exists():
        return HTMLResponse(f"Entry not found: {category}/{slug}", status_code=404)

    # Parse and filter
    entry = parse_entry(filepath)
    entry = filter_by_level(entry, level)
    entry = filter_by_lang(entry, lang)
    toc_items, sections = build_toc(entry.sections)
    entry_html = render_entry_html(
        type(entry)(title=entry.title, sections=sections, toc=entry.toc, raw_md=entry.raw_md,
                    note=entry.note)
    )

    en_label, zh_label = CATEGORY_LABELS.get(category, (category, category))
    static_page = Path(__file__).parent / "static" / "articles" / f"{slug}.html"

    # Article titles are stored as "中文 / English"; show only the half that
    # matches the requested language, and both when reading bilingually.
    if " / " in entry.title:
        title_zh, title_en = entry.title.split(" / ", 1)
    else:
        title_zh = title_en = entry.title
    title_zh, title_en = title_zh.strip(), title_en.strip()
    doc_title = {"en": title_en, "zh": title_zh}.get(lang, f"{title_zh} / {title_en}")
    note_zh, note_en = extract_notes(entry.raw_md)

    return templates.TemplateResponse(request, "entry.html", {
        "title": entry.title,
        "doc_title": doc_title,
        "title_zh": title_zh,
        "title_en": title_en,
        "entry_html": entry_html,
        "toc_items": toc_items,
        "category": category,
        "cat_en": en_label,
        "cat_zh": zh_label,
        "slug": slug,
        "current_level": level,
        "current_lang": lang,
        "lang": lang,
        "levels": LEVEL_ORDER,
        "note_zh": note_zh,
        "note_en": note_en,
        "has_static": static_page.exists(),
    })


@app.get("/api/entry/{category}/{slug}")
async def api_entry(
    category: str,
    slug: str,
    level: str = Query("L5"),
    lang: str = Query("dual"),
):
    filepath = BASE_DIR / category / f"{slug}.md"
    if not filepath.exists():
        return {"error": f"Entry not found: {category}/{slug}"}

    entry = parse_entry(filepath)
    entry = filter_by_level(entry, level)
    entry = filter_by_lang(entry, lang)

    return {
        "title": entry.title,
        "sections": [
            {"level": l, "lang": la, "html": h}
            for l, la, h in entry.sections
        ],
    }
