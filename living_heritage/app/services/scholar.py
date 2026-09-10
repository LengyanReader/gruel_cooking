"""
Scholar service — queries for researcher profiles.
"""
import sqlite3
import json
from app.services.locale import resolve_text


class ScholarService:
    def __init__(self, db: sqlite3.Connection):
        self.db = db

    def list_scholars(self, locale: str) -> list[dict]:
        """List all scholars with resolved names."""
        rows = self.db.execute("SELECT * FROM scholars ORDER BY name_key").fetchall()
        result = []
        for r in rows:
            r = dict(r)
            r["name"] = self._resolve(r, "name_key", locale)
            r["bio"] = self._resolve(r, "bio_key", locale)
            r["corridors"] = json.loads(r.get("corridor_slugs") or "[]")
            result.append(r)
        return result

    def get_scholar(self, scholar_id: int, locale: str) -> dict | None:
        """Get a single scholar by ID."""
        r = self.db.execute("SELECT * FROM scholars WHERE id = ?", (scholar_id,)).fetchone()
        if not r:
            return None
        r = dict(r)
        r["name"] = self._resolve(r, "name_key", locale)
        r["bio"] = self._resolve(r, "bio_key", locale)
        r["corridors"] = json.loads(r.get("corridor_slugs") or "[]")
        return r

    def _resolve(self, row: dict, field: str, locale: str) -> str:
        key = row.get(field)
        if not key:
            return ""
        r = self.db.execute(
            "SELECT key, en, zh FROM bilingual_text WHERE key = ?", (key,)
        ).fetchone()
        if not r:
            return key
        r = dict(r)
        return r.get(locale) or r.get("en") or key
