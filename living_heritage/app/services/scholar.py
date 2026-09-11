"""
Scholar service — queries for researcher profiles.
"""
import sqlite3
import json
from app.services.locale import TextResolver


class ScholarService:
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.text = TextResolver(db)

    def _base(self, r: dict, locale: str) -> dict:
        r = dict(r)
        r["name"] = self.text.resolve(r.get("name_key"), locale)
        r["bio"] = self.text.resolve(r.get("bio_key"), locale)
        r["corridors"] = json.loads(r.get("corridor_slugs") or "[]")
        r["works"] = self._works(r, locale)
        r["traits"] = self._traits(r, locale)
        return r

    def list_scholars(self, locale: str) -> list[dict]:
        """List all scholars with resolved names."""
        rows = self.db.execute("SELECT * FROM scholars ORDER BY name_key").fetchall()
        return [self._base(r, locale) for r in rows]

    def get_scholar(self, scholar_id: int, locale: str) -> dict | None:
        """Get a single scholar by ID."""
        r = self.db.execute("SELECT * FROM scholars WHERE id = ?", (scholar_id,)).fetchone()
        if not r:
            return None
        return self._base(r, locale)

    def _works(self, row: dict, locale: str) -> list[dict]:
        """Resolve the bilingual works list to the requested locale."""
        raw = row.get("works_json")
        if not raw:
            return []
        try:
            works = json.loads(raw)
        except (ValueError, TypeError):
            return []
        resolved = []
        for w in works:
            item = dict(w)
            item["title"] = item.get(f"title_{locale}") or item.get("title_en") or item.get("title_zh") or ""
            item["venue"] = item.get(f"venue_{locale}") or item.get("venue_en") or item.get("venue_zh") or ""
            item.pop("title_en", None)
            item.pop("title_zh", None)
            item.pop("venue_en", None)
            item.pop("venue_zh", None)
            resolved.append(item)
        return resolved

    def _traits(self, row: dict, locale: str) -> dict[str, str]:
        """Resolve the six-dimension trait portrait to the requested locale."""
        raw = row.get("traits_json")
        if not raw:
            return {}
        try:
            traits = json.loads(raw)
        except (ValueError, TypeError):
            return {}
        resolved = {}
        for key, val in traits.items():
            if isinstance(val, dict):
                resolved[key] = val.get(locale) or val.get("en") or val.get("zh") or ""
            else:
                resolved[key] = str(val)
        return resolved