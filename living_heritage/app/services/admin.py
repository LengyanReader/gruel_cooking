"""
Admin service — content intake & maintenance for the research console.

All writes go through here. Token-protected at the route layer.
"""
import json
import sqlite3
from datetime import datetime

from app.services.locale import TextResolver


class SourceLevelError(ValueError):
    pass


class AdminService:
    def __init__(self, db: sqlite3.Connection, allowed_levels: list[str] | None = None):
        self.db = db
        self.text = TextResolver(db)
        self.allowed_levels = allowed_levels or ["A", "B", "C", "D"]

    # ── Dash ──

    def dashboard_counts(self) -> dict:
        rows = {
            "bilingual_text": "bilingual_text",
            "pages": "pages",
            "heritage_sites": "heritage_sites",
            "scholars": "scholars",
            "corridors": "corridors",
            "field_observations": "field_observations",
            "publications": "publications",
            "relations": "relations",
        }
        return {name: self.db.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
                for name, tbl in rows.items()}

    def recent_observations(self, limit: int = 12) -> list[dict]:
        rows = self.db.execute(
            """SELECT fo.*, h.name_key AS site_name_key
               FROM field_observations fo
               LEFT JOIN heritage_sites h ON fo.site_id = h.id
               ORDER BY fo.date_observed DESC, fo.id DESC LIMIT ?""",
            (limit,)
        ).fetchall()
        for r in rows:
            r = dict(r)
            r["title"] = self.text.resolve(r.get("title_key"), locale="en")
            r["site_name"] = self.text.resolve(r.get("site_name_key"), locale="en")
        return [dict(r) for r in rows]

    def recent_publications(self, limit: int = 12) -> list[dict]:
        rows = self.db.execute(
            "SELECT * FROM publications ORDER BY id DESC LIMIT ?", (limit,)
        ).fetchall()
        for r in rows:
            r = dict(r)
            r["title"] = self.text.resolve(r.get("title_key"), locale="en")
        return [dict(r) for r in rows]

    def list_sites(self, locale: str = "en") -> list[dict]:
        rows = self.db.execute(
            "SELECT id, name_key FROM heritage_sites ORDER BY corridor_slug, name_key"
        ).fetchall()
        return [{"id": r["id"], "name": self.text.resolve(r["name_key"], locale)} for r in rows]

    # ── Writes ──

    def _check_level(self, level: str | None) -> str | None:
        if not level:
            return None
        level = level.strip().upper()
        if level not in self.allowed_levels:
            raise SourceLevelError(f"Unknown source level: {level}")
        return level

    def add_observation(self, *, title_en: str, title_zh: str, notes_en: str, notes_zh: str,
                        site_id: int | None, date_observed: str, observation_type: str,
                        source_level: str | None, tags: str, scholar_id: int | None = None) -> int:
        """Create a bilingual observation + its bilingual_text rows."""
        stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        title_key = f"observation.{stamp}.title"
        notes_key = f"observation.{stamp}.notes"
        self.db.execute(
            "INSERT INTO bilingual_text (key, en, zh, updated_at) VALUES (?, ?, ?, datetime('now'))",
            (title_key, title_en or "", title_zh or "")
        )
        self.db.execute(
            "INSERT INTO bilingual_text (key, en, zh, updated_at) VALUES (?, ?, ?, datetime('now'))",
            (notes_key, notes_en or "", notes_zh or "")
        )
        cur = self.db.execute(
            """INSERT INTO field_observations
               (site_id, scholar_id, date_observed, title_key, notes_key,
                observation_type, source_level, tags)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (site_id, scholar_id, date_observed or "", title_key, notes_key,
             observation_type or "", self._check_level(source_level), tags or "")
        )
        self.db.commit()
        return cur.lastrowid

    def delete_observation(self, obs_id: int) -> bool:
        cur = self.db.execute("DELETE FROM field_observations WHERE id = ?", (obs_id,))
        self.db.commit()
        return cur.rowcount > 0

    def add_publication(self, *, title_en: str, title_zh: str, abstract_en: str, abstract_zh: str,
                        authors: str, publication_type: str, year: int | None,
                        doi: str, url: str, tags: str, source_level: str | None,
                        corridor_slugs: str) -> int:
        stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        title_key = f"publication.{stamp}.title"
        abstract_key = f"publication.{stamp}.abstract"
        self.db.execute(
            "INSERT INTO bilingual_text (key, en, zh, updated_at) VALUES (?, ?, ?, datetime('now'))",
            (title_key, title_en or "", title_zh or "")
        )
        self.db.execute(
            "INSERT INTO bilingual_text (key, en, zh, updated_at) VALUES (?, ?, ?, datetime('now'))",
            (abstract_key, abstract_en or "", abstract_zh or "")
        )
        cur = self.db.execute(
            """INSERT INTO publications
               (title_key, abstract_key, authors, publication_type, year, doi, url,
                tags, source_level, corridor_slugs)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (title_key, abstract_key, authors or "", publication_type or "", year,
             doi or "", url or "", tags or "", self._check_level(source_level), corridor_slugs or "")
        )
        self.db.commit()
        return cur.lastrowid

    def delete_publication(self, pub_id: int) -> bool:
        cur = self.db.execute("DELETE FROM publications WHERE id = ?", (pub_id,))
        self.db.commit()
        return cur.rowcount > 0

    def set_text(self, key: str, en: str, zh: str) -> bool:
        """Insert or update a single bilingual_text row."""
        key = key.strip()
        if not key:
            raise ValueError("text key required")
        self.db.execute(
            """INSERT INTO bilingual_text (key, en, zh, created_at, updated_at)
               VALUES (?, ?, ?, datetime('now'), datetime('now'))
               ON CONFLICT(key) DO UPDATE SET
                 en = excluded.en,
                 zh = excluded.zh,
                 updated_at = datetime('now')""",
            (key, en, zh)
        )
        self.db.commit()
        return True

    def search_text(self, term: str, limit: int = 40) -> list[dict]:
        like = f"%{term}%"
        rows = self.db.execute(
            """SELECT key, en, zh FROM bilingual_text
               WHERE key LIKE ? OR en LIKE ? OR zh LIKE ?
               ORDER BY key LIMIT ?""",
            (like, like, like, limit)
        ).fetchall()
        return [dict(r) for r in rows]