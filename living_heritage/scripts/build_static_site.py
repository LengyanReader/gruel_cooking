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
  * A <base href="{LH_BASE_URL}/"> tag is injected so every rewritten root-relative
    href/src resolves against the deployed site root (works on project Pages URLs).
  * Internal /-rooted hrefs/srcs are made base-relative; https/data/#/mailto untouched.
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

from app.db.sqlite import init_db  # noqa: E402
from app.seed import seed_all  # noqa: E402
from app.config import STATIC_DIR, DEFAULT_LOCALE, AVAILABLE_LOCALES  # noqa: E402
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
    ("publications/index", "/publications", {}),
    ("plan/index", "/plan", {}),
]

LANG_TOGGLE_RE = re.compile(
    r'<div class="lang-toggle">.*?</div>', re.DOTALL
)
INTERNAL_ATTR_RE = re.compile(r'\s(href|src)="/')


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
    """Make a rendered page work on a static host."""
    html = html.replace("<head>", f'<head>\n<base href="{base_href}">', 1)

    # Internal /-rooted URLs become base-relative; https:/data:/# untouched.
    html = INTERNAL_ATTR_RE.sub(' \\1="', html)

    # Query-string literature tabs -> folder paths.
    html = html.replace('href="literature?view=dimensions"', 'href="literature/dimensions/"')
    html = html.replace('href="literature?view=scholars"', 'href="literature/scholars/"')

    # Static language switch (replaces the POST forms).
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
    return html


def main() -> int:
    init_db()
    seed_all()

    out_root = Path(os.getenv("LH_SITE_OUT", str(BASE_DIR / "dist"))).resolve()
    base_url = os.getenv("LH_BASE_URL", "").rstrip("/")
    base_href = base_url + "/" if base_url else "./"
    if out_root.exists():
        shutil.rmtree(out_root)

    written = 0
    for locale in LOCALES:
        prefix = "" if locale == "en" else "zh"
        for out_key, path, query in PAGES:
            html = rewrite(fetch(path, query, locale), out_key=out_key, locale=locale, base_href=base_href)
            rel = (Path(prefix) / out_key).with_suffix(".html")
            dest = out_root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(html, encoding="utf-8")
            written += 1

    # Static assets (css/js/img/vendor incl. KaTeX).
    shutil.copytree(STATIC_DIR, out_root, dirs_exist_ok=True)

    print(f"static site written: {out_root} ({written} pages, {len(LOCALES)} locales)")
    print(f"base href: {base_href}")
    return 0


if __name__ == "__main__":
    sys.exit(main())