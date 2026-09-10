"""
Living Cultural Corridors — entry point.
Run: python -m app.main
"""
import sys
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import AVAILABLE_LOCALES, DEFAULT_LOCALE
from app.db.sqlite import get_db, init_db
from app.services.content import ContentService
from app.services.heritage import HeritageService
from app.services.scholar import ScholarService
from app.services import graph as graph_service
from app.router import get, post, run_server, Request, Response
from jinja2 import Environment, FileSystemLoader
from app.config import TEMPLATE_DIR

# Jinja2 environment
jinja_env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=True,
)


def render(template_name: str, context: dict) -> str:
    """Render a Jinja2 template."""
    tmpl = jinja_env.get_template(template_name)
    return tmpl.render(**context)


def get_locale(req: Request) -> str:
    locale = req.cookies.get("locale", DEFAULT_LOCALE)
    if locale not in AVAILABLE_LOCALES:
        locale = DEFAULT_LOCALE
    return locale


# ── Template context helper ──

def base_context(req: Request) -> dict:
    """Common template context for all pages."""
    locale = get_locale(req)
    db = get_db()
    content_svc = ContentService(db)

    # Resolve nav items
    nav_keys = ["nav.home", "nav.corridors", "nav.scholars", "nav.methodology", "nav.fieldwork"]
    nav_texts = content_svc.resolve_texts_batch(nav_keys, locale)

    return {
        "locale": locale,
        "locales": AVAILABLE_LOCALES,
        "nav": {
            "home": nav_texts.get("nav.home", "Home"),
            "corridors": nav_texts.get("nav.corridors", "Corridors"),
            "scholars": nav_texts.get("nav.scholars", "Scholars"),
            "methodology": nav_texts.get("nav.methodology", "Methodology"),
            "fieldwork": nav_texts.get("nav.fieldwork", "Fieldwork"),
        },
        "nav_keys": nav_keys,
        "nav_texts": nav_texts,
        "site_title": content_svc.resolve_text("site.title", locale),
        "site_subtitle": content_svc.resolve_text("site.subtitle", locale),
    }


# ── Routes ──

@get("/")
def home(req: Request):
    ctx = base_context(req)
    locale = ctx["locale"]
    db = get_db()
    content_svc = ContentService(db)
    heritage_svc = HeritageService(db)

    # Page content
    page = content_svc.get_page("home", locale)
    ctx["page"] = page

    # Corridor cards
    corridors = graph_service._fallback_corridors()
    # Enrich with bilingual names from DB
    for c in corridors:
        c["name"] = content_svc.resolve_text(f"corridor.{c['slug']}.title", locale)
        c["description"] = content_svc.resolve_text(f"corridor.{c['slug']}.intro", locale)
    ctx["corridors"] = corridors

    # Recent observations
    ctx["observations"] = heritage_svc.list_observations(locale=locale)[:5]

    db.close()
    return render("pages/home.html", ctx)


@get("/corridors")
def corridor_list(req: Request):
    ctx = base_context(req)
    locale = ctx["locale"]
    db = get_db()
    content_svc = ContentService(db)
    heritage_svc = HeritageService(db)

    corridors = graph_service._fallback_corridors()
    for c in corridors:
        c["name"] = content_svc.resolve_text(f"corridor.{c['slug']}.title", locale)
        c["description"] = content_svc.resolve_text(f"corridor.{c['slug']}.intro", locale)
        sites = heritage_svc.list_sites(c["slug"], locale)
        c["sites"] = sites
        c["site_count"] = len(sites)

    ctx["corridors"] = corridors
    db.close()
    return render("pages/corridors.html", ctx)


@get("/scholars")
def scholar_list(req: Request):
    ctx = base_context(req)
    locale = ctx["locale"]
    db = get_db()
    scholar_svc = ScholarService(db)
    ctx["scholars"] = scholar_svc.list_scholars(locale)
    db.close()
    return render("pages/scholars.html", ctx)


@get("/methodology")
def methodology(req: Request):
    ctx = base_context(req)
    locale = ctx["locale"]
    db = get_db()
    content_svc = ContentService(db)
    ctx["page"] = content_svc.get_page("methodology", locale)
    db.close()
    return render("pages/methodology.html", ctx)


@get("/fieldwork")
def fieldwork(req: Request):
    ctx = base_context(req)
    locale = ctx["locale"]
    db = get_db()
    heritage_svc = HeritageService(db)
    ctx["observations"] = heritage_svc.list_observations(locale=locale)
    db.close()
    return render("pages/fieldwork.html", ctx)


@post("/locale/{lang}")
def set_locale(req: Request):
    lang = req.params.get("lang", DEFAULT_LOCALE)
    if lang not in AVAILABLE_LOCALES:
        lang = DEFAULT_LOCALE
    referer = req.headers.get("Referer", "/")
    resp = Response.redirect(referer)
    resp.cookies["locale"] = lang
    return resp


# ── Run ──

if __name__ == "__main__":
    init_db()
    # Seed if DB is empty
    from scripts.seed_content import seed_if_empty
    seed_if_empty()
    run_server()
