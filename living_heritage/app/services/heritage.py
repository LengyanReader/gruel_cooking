"""
Heritage site service — queries for corridor sites and field observations.
"""
import sqlite3
import json
from app.services.locale import resolve_text


class HeritageService:
    def __init__(self, db: sqlite3.Connection):
        self.db = db

    def list_corridors(self) -> list[dict]:
        """List distinct corridors with site counts."""
        rows = self.db.execute(
            "SELECT corridor_slug, COUNT(*) as site_count FROM heritage_sites GROUP BY corridor_slug ORDER BY corridor_slug"
        ).fetchall()
        return [dict(r) for r in rows]

    def list_sites(self, corridor_slug: str | None = None, locale: str = "en") -> list[dict]:
        """List heritage sites, optionally filtered by corridor."""
        if corridor_slug:
            rows = self.db.execute(
                "SELECT * FROM heritage_sites WHERE corridor_slug = ? ORDER BY name_key",
                (corridor_slug,)
            ).fetchall()
        else:
            rows = self.db.execute(
                "SELECT * FROM heritage_sites ORDER BY corridor_slug, name_key"
            ).fetchall()
        result = []
        for r in rows:
            r = dict(r)
            r["name"] = self._resolve(r, "name_key", locale)
            r["description"] = self._resolve(r, "description_key", locale)
            result.append(r)
        return result

    def get_site(self, site_id: int, locale: str) -> dict | None:
        r = self.db.execute("SELECT * FROM heritage_sites WHERE id = ?", (site_id,)).fetchone()
        if not r:
            return None
        r = dict(r)
        r["name"] = self._resolve(r, "name_key", locale)
        r["description"] = self._resolve(r, "description_key", locale)
        return r

    def list_observations(self, corridor_slug: str | None = None, locale: str = "en") -> list[dict]:
        """List field observations with resolved text."""
        if corridor_slug:
            rows = self.db.execute(
                """SELECT fo.*, hs.corridor_slug FROM field_observations fo
                   LEFT JOIN heritage_sites hs ON fo.site_id = hs.id
                   WHERE hs.corridor_slug = ?
                   ORDER BY fo.date_observed DESC""",
                (corridor_slug,)
            ).fetchall()
        else:
            rows = self.db.execute(
                """SELECT fo.*, hs.corridor_slug FROM field_observations fo
                   LEFT JOIN heritage_sites hs ON fo.site_id = hs.id
                   ORDER BY fo.date_observed DESC"""
            ).fetchall()
        result = []
        for r in rows:
            r = dict(r)
            r["title"] = self._resolve(r, "title_key", locale)
            r["notes"] = self._resolve(r, "notes_key", locale)
            result.append(r)
        return result

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
