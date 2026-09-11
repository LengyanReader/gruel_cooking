"""
Heritage site service — queries for corridor sites and field observations.
"""
import json
import sqlite3
from app.services.locale import TextResolver


class HeritageService:
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.text = TextResolver(db)

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
            r["name"] = self.text.resolve(r.get("name_key"), locale)
            r["description"] = self.text.resolve(r.get("description_key"), locale)
            result.append(r)
        return result

    def get_site(self, site_id: int, locale: str) -> dict | None:
        r = self.db.execute("SELECT * FROM heritage_sites WHERE id = ?", (site_id,)).fetchone()
        if not r:
            return None
        r = dict(r)
        r["name"] = self.text.resolve(r.get("name_key"), locale)
        r["description"] = self.text.resolve(r.get("description_key"), locale)
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
            r["title"] = self.text.resolve(r.get("title_key"), locale)
            r["notes"] = self.text.resolve(r.get("notes_key"), locale)
            result.append(r)
        return result

    def list_observations_by_corridor(self, corridors: list[str], locale: str = "en") -> list[dict]:
        """Observations grouped per corridor, for the fieldwork page."""
        if not corridors:
            return self.list_observations(None, locale)
        placeholders = ",".join("?" for _ in corridors)
        rows = self.db.execute(
            f"""SELECT fo.*, h.corridor_slug FROM field_observations fo
                LEFT JOIN heritage_sites h ON fo.site_id = h.id
                WHERE h.corridor_slug IN ({placeholders})
                ORDER BY fo.date_observed DESC""",
            list(corridors)
        ).fetchall()
        result = []
        for r in rows:
            r = dict(r)
            r["title"] = self.text.resolve(r.get("title_key"), locale)
            r["notes"] = self.text.resolve(r.get("notes_key"), locale)
            result.append(r)
        return result

    def list_publications(self, locale: str = "en", limit: int = 200,
                          corridor: str | None = None, level: str | None = None) -> list[dict]:
        """List research sources/publications with resolved bilingual text.
        corridor filters on the stored corridor_slugs JSON; level on source_level."""
        rows = self.db.execute(
            "SELECT * FROM publications ORDER BY year DESC, id DESC LIMIT ?", (limit,)
        ).fetchall()
        result = []
        for r in rows:
            r = dict(r)
            r["title"] = self.text.resolve(r.get("title_key"), locale)
            r["abstract"] = self.text.resolve(r.get("abstract_key"), locale)
            raw = r.get("tags") or ""
            r["tag_list"] = [x.strip() for x in raw.split(",") if x.strip()]
            if corridor:
                try:
                    slugs = json.loads(r.get("corridor_slugs") or "[]")
                except (ValueError, TypeError):
                    slugs = []
                if corridor not in slugs:
                    continue
            if level and r.get("source_level") != level:
                continue
            result.append(r)
        return result