"""
Living Cultural Corridors — entry point.
Run: python -m app.main
"""
import sys
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import AVAILABLE_LOCALES, DEFAULT_LOCALE, TRAIT_KEYS, GRAPH_ENGINE
from app.db.sqlite import get_db
from app.services.content import ContentService
from app.services.heritage import HeritageService
from app.services.scholar import ScholarService
from app.services.graph import get_graph_service
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

class AppContext:
    """Services bound to one request/db connection."""

    def __init__(self, req: Request):
        self.req = req
        self.locale = get_locale(req)
        self.db = get_db()
        self.content = ContentService(self.db)
        self.heritage = HeritageService(self.db)
        self.scholars = ScholarService(self.db)
        self.graph = get_graph_service(self.db)


def base_context(ctx: AppContext) -> dict:
    """Common template context for all pages."""
    locale = ctx.locale
    content_svc = ctx.content

    # Resolve nav items from pages table (data-driven, not hardcoded)
    pages = content_svc.list_pages(locale)
    nav_items = []
    for p in pages:
        if not p.get("nav_key"):
            continue
        href = "/" if p["slug"] == "home" else f"/{p['slug']}"
        nav_items.append({
            "slug": p["slug"],
            "href": href,
            "label": content_svc.resolve_text(p["nav_key"], locale),
            "is_home": p["slug"] == "home",
        })

    trait_label_keys = [f"label.trait_{k}" for k in TRAIT_KEYS]
    label_keys = [
        "label.sites", "label.observations", "label.latest_observations",
        "label.corridors", "label.scholars", "label.institution",
        "label.specialization", "label.website", "label.region",
        "label.unesco", "label.type", "label.established", "label.coordinates",
        "label.works",
    ] + trait_label_keys
    label_texts = content_svc.resolve_texts_batch(label_keys, locale)

    trait_labels = {k: label_texts.get(f"label.trait_{k}", k) for k in TRAIT_KEYS}

    return {
        "locale": locale,
        "locales": AVAILABLE_LOCALES,
        "nav_items": nav_items,
        "current_slug": getattr(ctx.req, "page_slug", None),
        "nav": {p["slug"]: p["label"] for p in nav_items},
        "labels": label_texts,
        "trait_labels": trait_labels,
        "trait_keys": TRAIT_KEYS,
        "works_label": label_texts.get("label.works", "Selected works"),
        "label_sites": label_texts.get("label.sites", "Heritage Sites"),
        "label_latest_observations": label_texts.get("label.latest_observations", "Latest Field Observations"),
        "nav_texts": {p["slug"]: p["label"] for p in nav_items},
        "site_title": content_svc.resolve_text("site.title", locale),
        "site_subtitle": content_svc.resolve_text("site.subtitle", locale),
        "footer_tagline": content_svc.resolve_text("footer.tagline", locale),
        "graph_engine": GRAPH_ENGINE,
    }


# ── Routes ──

@get("/")
def home(req: Request):
    ctx = AppContext(req)
    ctx.req.page_slug = "home"
    base = base_context(ctx)
    base["page"] = ctx.content.get_page("home", ctx.locale)

    corridors = ctx.graph.list_corridors(ctx.locale)
    base["corridors"] = corridors

    base["observations"] = ctx.heritage.list_observations(locale=ctx.locale)[:5]
    html = render("pages/home.html", base)
    ctx.db.close()
    return html


@get("/corridors")
def corridor_list(req: Request):
    ctx = AppContext(req)
    ctx.req.page_slug = "corridors"
    base = base_context(ctx)
    base["page"] = ctx.content.get_page("corridors", ctx.locale)

    corridors = ctx.graph.list_corridors(ctx.locale)
    for c in corridors:
        c["sites"] = ctx.heritage.list_sites(c["slug"], ctx.locale)
        c["site_count"] = len(c["sites"])
    base["corridors"] = corridors
    html = render("pages/corridors.html", base)
    ctx.db.close()
    return html


@get("/scholars")
def scholar_list(req: Request):
    ctx = AppContext(req)
    ctx.req.page_slug = "scholars"
    base = base_context(ctx)
    base["page"] = ctx.content.get_page("scholars", ctx.locale)
    base["scholars"] = ctx.scholars.list_scholars(ctx.locale)
    html = render("pages/scholars.html", base)
    ctx.db.close()
    return html


@get("/literature")
def literature(req: Request):
    ctx = AppContext(req)
    ctx.req.page_slug = "literature"
    base = base_context(ctx)
    base["page"] = ctx.content.get_page("literature", ctx.locale)
    base["scholars"] = ctx.scholars.list_scholars(ctx.locale)
    html = render("pages/literature.html", base)
    ctx.db.close()
    return html


@get("/graph")
def graph_view(req: Request):
    ctx = AppContext(req)
    ctx.req.page_slug = "graph"
    base = base_context(ctx)
    base["page"] = ctx.content.get_page("graph", ctx.locale)
    base["corridors"] = ctx.graph.corridor_profiles(ctx.locale)
    base["relations"] = ctx.graph.list_relations(ctx.locale)[:200]
    html = render("pages/graph.html", base)
    ctx.db.close()
    return html


@get("/methodology")
def methodology(req: Request):
    ctx = AppContext(req)
    ctx.req.page_slug = "methodology"
    base = base_context(ctx)
    base["page"] = ctx.content.get_page("methodology", ctx.locale)
    html = render("pages/methodology.html", base)
    ctx.db.close()
    return html


@get("/fieldwork")
def fieldwork(req: Request):
    ctx = AppContext(req)
    ctx.req.page_slug = "fieldwork"
    base = base_context(ctx)
    base["page"] = ctx.content.get_page("fieldwork", ctx.locale)
    base["observations"] = ctx.heritage.list_observations(locale=ctx.locale)
    html = render("pages/fieldwork.html", base)
    ctx.db.close()
    return html


@post("/locale/<lang>")
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
    from app.boot import boot
    boot()