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
    list_entries,
    LEVEL_ORDER,
)

BASE_DIR = Path(__file__).resolve().parent.parent  # math_clarification/

app = FastAPI(title="Math Clarification", version="0.1.0")

app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    entries = list_entries(BASE_DIR)
    return templates.TemplateResponse(request, "home.html", {
        "entries": entries,
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
    entry_html = render_entry_html(entry)

    return templates.TemplateResponse(request, "entry.html", {
        "title": entry.title,
        "entry_html": entry_html,
        "toc": entry.toc,
        "category": category,
        "slug": slug,
        "current_level": level,
        "current_lang": lang,
        "levels": LEVEL_ORDER,
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
