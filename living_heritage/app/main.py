"""
Living Cultural Corridors — entry point.
Run: python -m app.main
"""
import sys
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import AVAILABLE_LOCALES, DEFAULT_LOCALE, TRAIT_KEYS, GRAPH_ENGINE, ADMIN_TOKEN, SOURCE_LEVELS
from app.db.sqlite import get_db
from app.services.content import ContentService
from app.services.heritage import HeritageService
from app.services.scholar import ScholarService
from app.services.graph import get_graph_service
from app.services.admin import AdminService
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
        self.admin = AdminService(self.db, allowed_levels=SOURCE_LEVELS)


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

    brand = content_svc.resolve_texts_batch(
        ["brand.identity", "brand.nav_sub", "brand.kicker", "brand.zhou_line"], locale
    )

    return {
        "locale": locale,
        "locales": AVAILABLE_LOCALES,
        "brand": brand,
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
    corridor_objs = ctx.graph.list_corridors(ctx.locale)
    observations = ctx.heritage.list_observations_by_corridor(
        [c["slug"] for c in corridor_objs], ctx.locale
    )
    groups = []
    for c in corridor_objs:
        items = [o for o in observations if o.get("corridor_slug") == c["slug"]]
        if items:
            groups.append({"slug": c["slug"], "name": c["name"], "observations": items})
    base["observations"] = observations
    base["corridor_groups"] = groups
    html = render("pages/fieldwork.html", base)
    ctx.db.close()
    return html


@get("/publications")
def publications(req: Request):
    ctx = AppContext(req)
    ctx.req.page_slug = "publications"
    base = base_context(ctx)
    base["page"] = ctx.content.get_page("publications", ctx.locale)
    corridor = (req.query.get("corridor") or [""])[0]
    level = (req.query.get("level") or [""])[0]
    base["active_corridor"] = corridor
    base["active_level"] = level
    base["filter_corridors"] = ctx.graph.list_corridors(ctx.locale)
    base["filter_levels"] = SOURCE_LEVELS
    base["publications"] = ctx.heritage.list_publications(
        locale=ctx.locale, corridor=corridor or None, level=level or None
    )
    html = render("pages/publications.html", base)
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


# ── Admin console (protected content intake) ──

def _admin_authed(req: Request) -> bool:
    """Authorize via HMAC session cookie or X-Admin-Token header.
    Admin stays closed unless LH_ADMIN_TOKEN is set."""
    import hashlib
    import hmac
    if not ADMIN_TOKEN:
        return False
    # Cookie: "lcc_admin=<hexdigest>" where digest is SHA256(ADMIN_TOKEN)
    cookie = req.cookies.get("lcc_admin", "")
    if cookie and hmac.compare_digest(cookie, hashlib.sha256(ADMIN_TOKEN.encode()).hexdigest()):
        return True
    supplied = req.headers.get("X-Admin-Token", "").strip()
    return hmac.compare_digest(supplied, ADMIN_TOKEN)


def _unauthorized() -> Response:
    return Response.json({"error": "unauthorized"}, status=401)


@post("/admin/session")
def admin_session(req: Request):
    """Exchange a valid token for an HMAC session cookie."""
    import hashlib
    import hmac
    digest = hashlib.sha256(ADMIN_TOKEN.encode()).hexdigest() if ADMIN_TOKEN else ""
    if not ADMIN_TOKEN or not hmac.compare_digest(req.headers.get("X-Admin-Token", "").strip(), ADMIN_TOKEN):
        return _unauthorized()
    resp = Response.json({"ok": True})
    resp.headers["Set-Cookie"] = f"lcc_admin={digest}; Path=/; HttpOnly; Max-Age=86400; SameSite=Lax"
    return resp


@post("/admin/logout")
def admin_logout(req: Request):
    resp = Response.json({"ok": True})
    resp.headers["Set-Cookie"] = "lcc_admin=; Path=/; HttpOnly; Max-Age=0; SameSite=Lax"
    return resp


@get("/admin")
def admin_dash(req: Request):
    if not _admin_authed(req):
        ctx = AppContext(req)
        html = render("admin/login.html", {"locale": ctx.locale})
        ctx.db.close()
        return html
    ctx = AppContext(req)
    base = base_context(ctx)
    base["counts"] = ctx.admin.dashboard_counts()
    base["source_levels"] = SOURCE_LEVELS
    base["observations"] = ctx.admin.recent_observations(12)
    base["publications"] = ctx.admin.recent_publications(12)
    base["sites"] = ctx.admin.list_sites(ctx.locale)
    base["page"] = None
    html = render("admin/dashboard.html", base)
    ctx.db.close()
    return html


@post("/admin/observation/add")
def admin_observation_add(req: Request):
    if not _admin_authed(req):
        return _unauthorized()
    ctx = AppContext(req)
    q = req.query
    try:
        site_id = q.get("site_id", [None])[0]
        site_id = int(site_id) if site_id else None
        obs_id = ctx.admin.add_observation(
            title_en=q.get("title_en", [""])[0],
            title_zh=q.get("title_zh", [""])[0],
            notes_en=q.get("notes_en", [""])[0],
            notes_zh=q.get("notes_zh", [""])[0],
            site_id=site_id,
            date_observed=q.get("date", [""])[0] or "",
            observation_type=q.get("observation_type", [""])[0],
            source_level=(q.get("source_level", [None])[0] or None),
            tags=q.get("tags", [""])[0],
        )
    except Exception as e:  # noqa: BLE001
        ctx.db.close()
        return Response.json({"error": str(e)}, status=400)
    ctx.db.close()
    return Response.json({"ok": True, "id": obs_id})


@post("/admin/observation/<obs_id>/delete")
def admin_observation_delete(req: Request):
    if not _admin_authed(req):
        return _unauthorized()
    ctx = AppContext(req)
    ok = ctx.admin.delete_observation(int(req.params["obs_id"]))
    ctx.db.close()
    return Response.json({"ok": ok})


@post("/admin/publication/add")
def admin_publication_add(req: Request):
    if not _admin_authed(req):
        return _unauthorized()
    ctx = AppContext(req)
    q = req.query
    try:
        year = q.get("year", [None])[0]
        year = int(year) if year else None
        pub_id = ctx.admin.add_publication(
            title_en=q.get("title_en", [""])[0],
            title_zh=q.get("title_zh", [""])[0],
            abstract_en=q.get("abstract_en", [""])[0],
            abstract_zh=q.get("abstract_zh", [""])[0],
            authors=q.get("authors", [""])[0],
            publication_type=q.get("publication_type", [""])[0],
            year=year,
            doi=q.get("doi", [""])[0],
            url=q.get("url", [""])[0],
            tags=q.get("tags", [""])[0],
            source_level=(q.get("source_level", [None])[0] or None),
            corridor_slugs=q.get("corridor_slugs", [""])[0],
        )
    except Exception as e:  # noqa: BLE001
        ctx.db.close()
        return Response.json({"error": str(e)}, status=400)
    ctx.db.close()
    return Response.json({"ok": True, "id": pub_id})


@post("/admin/publication/<pub_id>/delete")
def admin_publication_delete(req: Request):
    if not _admin_authed(req):
        return _unauthorized()
    ctx = AppContext(req)
    ok = ctx.admin.delete_publication(int(req.params["pub_id"]))
    ctx.db.close()
    return Response.json({"ok": ok})


@post("/admin/text/update")
def admin_text_update(req: Request):
    if not _admin_authed(req):
        return _unauthorized()
    ctx = AppContext(req)
    q = req.query
    try:
        ctx.admin.set_text(q.get("key", [""])[0], q.get("en", [""])[0], q.get("zh", [""])[0])
    except Exception as e:  # noqa: BLE001
        ctx.db.close()
        return Response.json({"error": str(e)}, status=400)
    ctx.db.close()
    return Response.json({"ok": True})


@post("/admin/text/search")
def admin_text_search(req: Request):
    if not _admin_authed(req):
        return _unauthorized()
    ctx = AppContext(req)
    terms = ctx.admin.search_text(req.query.get("q", [""])[0], limit=40)
    ctx.db.close()
    return Response.json({"results": terms})


# ── Run ──

if __name__ == "__main__":
    from app.boot import boot
    boot()