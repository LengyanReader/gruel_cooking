"""
build_static_site.py — render the whole public site to static HTML for GitHub Pages.

The app is server-rendered (stdlib http.server, no client-side data fetches), so we
can snapshot every public page per locale and get a fully static mirror: the result
keeps all text, photos, graph, plan and KaTeX blocks, minus the admin editing backend.

Usage:
    python scripts/build_static_site.py

Environment:
    LH_SQLITE_PATH  DB to seed (defaults to the repo's normal data DB)
    LH_BASE_URL     absolute site root (public Pages URL, drives canonical/og/<base>)
    LH_SITE_OUT     output dir (defaults to ../docs beside the repo root)

Design notes:
  * Portability first: every page gets a depth-relative <base href="../…/"> so the
    mirror works from the live Pages URL, a local HTTP server AND plain file://
    double-clicks. canonical/og tags keep the absolute LH_BASE_URL (template-side),
    independent of the <base> tag.
  * Internal /-rooted hrefs/srcs are made base-relative; https/data/#/mailto untouched.
  * Directory-style page links (corridors, scholars/, zh/plan/, even the bare
    href="" home link) are rewritten to explicit <dir>/index.html targets — the
    only form that opens under file://. Asset paths (they contain a dot: .css/.js/
    .jpg) and pure #fragments are left alone.
  * /literature?view=… becomes /literature/<view>/ folders; the two tab links are
    rewritten accordingly.
  * The POST /locale/<lang> forms (cookie switch) are replaced by static links to the
    parallel page in the other language (en at root, zh under /zh/).
"""
import os
import re
import shutil
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from app.db.sqlite import init_db, get_db  # noqa: E402
from app.seed import seed_all  # noqa: E402
from app.config import STATIC_DIR, DEFAULT_LOCALE, AVAILABLE_LOCALES  # noqa: E402
from app.services.scholar import slug_from_name_key  # noqa: E402
import app.main  # noqa: E402,F401  (registers the public route table)

LOCALES = [l for l in ("en", "zh") if l in AVAILABLE_LOCALES] or [DEFAULT_LOCALE]

# out_key -> (path, query)
PAGES = [
    ("index", "/", {}),
    ("corridors/index", "/corridors", {}),
    ("scholars/index", "/scholars", {}),
    ("literature/index", "/literature", {}),
    ("literature/scholars/index", "/literature", {"view": ["scholars"]}),
    ("literature/dimensions/index", "/literature", {"view": ["dimensions"]}),
    ("graph/index", "/graph", {}),
    ("methodology/index", "/methodology", {}),
    ("fieldwork/index", "/fieldwork", {}),
    ("map/index", "/map", {}),
    ("publications/index", "/publications", {}),
    ("plan/index", "/plan", {}),
]

LANG_TOGGLE_RE = re.compile(
    r'<div class="lang-toggle">.*?</div>', re.DOTALL
)
INTERNAL_ATTR_RE = re.compile(r'\s(href|src)="/')
HREF_RE = re.compile(r'href="([^"#]*?)([?#][^"]*)?"')


def relative_base(out_key: str, locale: str) -> str:
    """Depth-relative <base> href: '../' per folder level below the mirror root."""
    head = "" if out_key == "index" else out_key.rsplit("/index", 1)[0]  # '' | 'scholars' | 'literature/dimensions'
    depth = (1 if locale != "en" else 0) + (1 if head else 0) + head.count("/")
    return "./" if depth == 0 else "../" * depth


def page_link(match: re.Match) -> str:
    """Rewrite one href to an explicit <dir>/index.html target (file://-friendly).

    Skips: absolute URLs (https:/data:, rewritten away already), assets (any path
    containing a dot, e.g. css/main.css), and the <base> tag itself ('../').
    """
    target, suffix = match.group(1), match.group(2) or ""
    if ":" in target or "." in target:
        return match.group(0)
    dir_ = "index" if target in ("", "index") else target.strip("/").removesuffix("/index")
    # 'index' was the old (broken) home link; '' and 'index' both mean the root page.
    if dir_ == "index":
        dir_ = ""
    return f'href="{dir_ + "/" if dir_ else ""}index.html{suffix}"'


def scholar_pages() -> list[tuple[str, str, dict]]:
    """One snapshot per scholar detail route /scholars/<slug>."""
    rows = get_db().execute("SELECT name_key FROM scholars ORDER BY name_key").fetchall()
    slugs = sorted(filter(None, (slug_from_name_key(r["name_key"]) for r in rows)))
    return [(f"scholars/{s}/index", f"/scholars/{s}", {}) for s in slugs]


def fetch(path: str, query: dict, locale: str) -> str:
    """Call the route handler in-process (no socket needed)."""
    from app.router import Request, routes
    req = Request("GET", path, dict(query), {}, b"", {"locale": locale}, {})
    for info in routes["GET"].values():
        m = info["regex"].match(path)
        if m:
            req.params = dict(zip(info["params"], m.groups()))
            out = info["handler"](req)
            if isinstance(out, str):
                return out
    raise RuntimeError(f"no GET route for {path}")


def parallel_href(out_key: str, target_locale: str) -> str:
    """Base-relative href to the same page in another language."""
    key = out_key if target_locale == "en" else f"zh/{out_key}"
    return key.rsplit("/index", 1)[0] + "/"


def rewrite(html: str, *, out_key: str, locale: str, base_href: str) -> str:
    """Make a rendered page work on a static host and under file://."""
    html = html.replace("<head>", f'<head>\n<base href="{base_href}">', 1)

    # Internal /-rooted URLs become base-relative; https:/data:/# untouched.
    html = INTERNAL_ATTR_RE.sub(' \\1="', html)

    # Query-string literature tabs -> folder paths.
    html = html.replace('href="literature?view=dimensions"', 'href="literature/dimensions/"')
    html = html.replace('href="literature?view=scholars"', 'href="literature/scholars/"')

    # Static language switch (replaces the POST forms). Directory-style targets
    # are normalised to index.html by the final pass below.
    en_href = parallel_href(out_key, "en")
    zh_href = parallel_href(out_key, "zh")
    en_active = ' active' if locale == "en" else ''
    zh_active = ' active' if locale == "zh" else ''
    block = (
        f'<div class="lang-toggle">'
        f'<a href="{en_href}"{en_active}>EN</a>'
        f'<a href="{zh_href}"{zh_active}>中文</a>'
        f'</div>'
    )
    html = LANG_TOGGLE_RE.sub(block, html, count=1)

    # Every page-directory href -> explicit <dir>/index.html (file:// needs the
    # real file; Pages/HTTP keep working identically).
    html = HREF_RE.sub(page_link, html)
    return html


def main() -> int:
    init_db()
    seed_all()
    pages = PAGES + scholar_pages()

    out_root = Path(os.getenv("LH_SITE_OUT", str(BASE_DIR / "dist"))).resolve()
    # LH_BASE_URL still drives canonical/og absolute URLs (read by app.config at
    # render time); the <base> tag itself is now depth-relative per page.
    if out_root.exists():
        shutil.rmtree(out_root)

    written = 0
    for locale in LOCALES:
        prefix = "" if locale == "en" else "zh"
        for out_key, path, query in pages:
            html = rewrite(fetch(path, query, locale), out_key=out_key, locale=locale,
                           base_href=relative_base(out_key, locale))
            rel = (Path(prefix) / out_key).with_suffix(".html")
            dest = out_root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(html, encoding="utf-8")
            written += 1

    # Static assets (css/js/img/vendor incl. KaTeX).
    shutil.copytree(STATIC_DIR, out_root, dirs_exist_ok=True)

    print(f"static site written: {out_root} ({written} pages, {len(LOCALES)} locales)")
    return 0


if __name__ == "__main__":
    sys.exit(main())