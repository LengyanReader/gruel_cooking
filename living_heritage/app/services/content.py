"""
Content service — reads pages, sections, and bilingual text from SQLite.
"""
import sqlite3
from app.services.locale import resolve_text, build_text_map


class ContentService:
    def __init__(self, db: sqlite3.Connection):
        self.db = db

    def get_page(self, slug: str, locale: str) -> dict | None:
        """Get a page with all its sections, texts resolved to locale."""
        page = self.db.execute(
            "SELECT * FROM pages WHERE slug = ? AND is_published = 1", (slug,)
        ).fetchone()
        if not page:
            return None
        page = dict(page)

        # Get sections
        sections = self.db.execute(
            "SELECT * FROM page_sections WHERE page_id = ? ORDER BY sort_order",
            (page["id"],)
        ).fetchall()

        # Collect all bilingual text keys
        text_keys = [page["title_key"]]
        for s in sections:
            if s["title_key"]:
                text_keys.append(s["title_key"])
            if s["body_key"]:
                text_keys.append(s["body_key"])

        # Resolve texts
        rows = self.db.execute(
            "SELECT key, en, zh FROM bilingual_text WHERE key IN ({})".format(
                ",".join("?" * len(text_keys))
            ),
            text_keys
        ).fetchall()
        text_map = build_text_map(text_keys, [dict(r) for r in rows], locale)

        # Apply resolved texts
        page["title"] = text_map.get(page["title_key"], page["title_key"])
        page["sections"] = []
        for s in sections:
            s = dict(s)
            s["title"] = text_map.get(s.get("title_key", ""), s.get("title_key", ""))
            s["body"] = text_map.get(s.get("body_key", ""), s.get("body_key", ""))
            page["sections"].append(s)

        return page

    def resolve_text(self, key: str, locale: str) -> str:
        """Resolve a single bilingual text key."""
        row = self.db.execute(
            "SELECT key, en, zh FROM bilingual_text WHERE key = ?", (key,)
        ).fetchone()
        return resolve_text(dict(row) if row else None, locale)

    def resolve_texts_batch(self, keys: list[str], locale: str) -> dict[str, str]:
        """Resolve multiple keys in one query."""
        if not keys:
            return {}
        rows = self.db.execute(
            "SELECT key, en, zh FROM bilingual_text WHERE key IN ({})".format(
                ",".join("?" * len(keys))
            ),
            keys
        ).fetchall()
        return build_text_map(keys, [dict(r) for r in rows], locale)

    def list_pages(self, locale: str) -> list[dict]:
        """List all published pages."""
        pages = self.db.execute(
            "SELECT * FROM pages WHERE is_published = 1 ORDER BY sort_order"
        ).fetchall()
        result = []
        for p in pages:
            p = dict(p)
            p["title"] = self.resolve_text(p["title_key"], locale)
            result.append(p)
        return result
