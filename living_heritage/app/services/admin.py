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

    # ── Graph consistency ──

    def rebuild_edges(self):
        """Rebuild the knowledge-graph edges from current table columns.

        Keeps graph consistent after admin writes; preserves the seeded
        scholar→publication authored edges via the en publications seed.
        """
        from app.seed import scholar_map_from_seed, seed_relations
        seed_relations(self.db, scholar_map_from_seed() or None)

    @staticmethod
    def _json_slugs(raw: str) -> str:
        """Normalize a comma-separated corridor slug string to a JSON list."""
        slugs = [s.strip() for s in (raw or "").split(",") if s.strip()]
        return json.dumps(slugs, ensure_ascii=False)

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
        self.rebuild_edges()
        return cur.lastrowid

    def delete_observation(self, obs_id: int) -> bool:
        row = self.db.execute("SELECT title_key, notes_key FROM field_observations WHERE id = ?",
                              (obs_id,)).fetchone()
        cur = self.db.execute("DELETE FROM field_observations WHERE id = ?", (obs_id,))
        if not cur.rowcount:
            return False
        if row:
            keys = [k for k in (row["title_key"], row["notes_key"]) if k]
            if keys:
                self.db.execute(f"DELETE FROM bilingual_text WHERE key IN ({','.join('?' for _ in keys)})", keys)
        self.db.execute("DELETE FROM relations WHERE (source_type='observation' AND source_id=?) "
                        "OR (target_type='observation' AND target_id=?)", (obs_id, obs_id))
        self.db.commit()
        self.rebuild_edges()
        return True

    def get_observation(self, obs_id: int) -> dict | None:
        row = self.db.execute("SELECT * FROM field_observations WHERE id = ?", (obs_id,)).fetchone()
        if not row:
            return None
        d = dict(row)
        d["title_en"], d["title_zh"] = self._resolve_pair(d.get("title_key"))
        d["notes_en"], d["notes_zh"] = self._resolve_pair(d.get("notes_key"))
        return d

    def update_observation(self, obs_id: int, *, title_en: str, title_zh: str, notes_en: str,
                           notes_zh: str, site_id: int | None, date_observed: str,
                           observation_type: str, source_level: str | None, tags: str) -> bool:
        row = self.db.execute("SELECT title_key, notes_key FROM field_observations WHERE id = ?",
                              (obs_id,)).fetchone()
        if not row:
            return False
        self.set_text(row["title_key"] or "", title_en or "", title_zh or "")
        self.set_text(row["notes_key"] or "", notes_en or "", notes_zh or "")
        self.db.execute(
            """UPDATE field_observations
               SET site_id = ?, date_observed = ?, observation_type = ?, source_level = ?, tags = ?
               WHERE id = ?""",
            (site_id, date_observed or "", observation_type or "",
             self._check_level(source_level), tags or "", obs_id)
        )
        self.db.commit()
        self.rebuild_edges()
        return True

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
             doi or "", url or "", tags or "", self._check_level(source_level),
             self._json_slugs(corridor_slugs))
        )
        self.db.commit()
        self.rebuild_edges()
        return cur.lastrowid

    def delete_publication(self, pub_id: int) -> bool:
        row = self.db.execute("SELECT title_key, abstract_key FROM publications WHERE id = ?",
                              (pub_id,)).fetchone()
        cur = self.db.execute("DELETE FROM publications WHERE id = ?", (pub_id,))
        if not cur.rowcount:
            return False
        if row:
            keys = [k for k in (row["title_key"], row["abstract_key"]) if k]
            if keys:
                self.db.execute(f"DELETE FROM bilingual_text WHERE key IN ({','.join('?' for _ in keys)})", keys)
        self.db.execute("DELETE FROM relations WHERE (source_type='publication' AND source_id=?) "
                        "OR (target_type='publication' AND target_id=?)", (pub_id, pub_id))
        self.db.commit()
        self.rebuild_edges()
        return True

    def get_publication(self, pub_id: int) -> dict | None:
        row = self.db.execute("SELECT * FROM publications WHERE id = ?", (pub_id,)).fetchone()
        if not row:
            return None
        d = dict(row)
        d["title_en"], d["title_zh"] = self._resolve_pair(d.get("title_key"))
        d["abstract_en"], d["abstract_zh"] = self._resolve_pair(d.get("abstract_key"))
        return d

    def update_publication(self, pub_id: int, *, title_en: str, title_zh: str, abstract_en: str,
                           abstract_zh: str, authors: str, publication_type: str, year: int | None,
                           doi: str, url: str, tags: str, source_level: str | None,
                           corridor_slugs: str) -> bool:
        row = self.db.execute("SELECT title_key, abstract_key FROM publications WHERE id = ?",
                              (pub_id,)).fetchone()
        if not row:
            return False
        self.set_text(row["title_key"] or "", title_en or "", title_zh or "")
        self.set_text(row["abstract_key"] or "", abstract_en or "", abstract_zh or "")
        self.db.execute(
            """UPDATE publications
               SET authors = ?, publication_type = ?, year = ?, doi = ?, url = ?,
                   tags = ?, source_level = ?, corridor_slugs = ?
               WHERE id = ?""",
            (authors or "", publication_type or "", year, doi or "", url or "",
             tags or "", self._check_level(source_level), self._json_slugs(corridor_slugs), pub_id)
        )
        self.db.commit()
        self.rebuild_edges()
        return True

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

    def _resolve_pair(self, key: str | None) -> tuple[str, str]:
        if not key:
            return "", ""
        row = self.db.execute(
            "SELECT en, zh FROM bilingual_text WHERE key = ?", (key,)
        ).fetchone()
        return (row["en"], row["zh"]) if row else ("", "")

    def search_text(self, term: str, limit: int = 40) -> list[dict]:
        like = f"%{term}%"
        rows = self.db.execute(
            """SELECT key, en, zh FROM bilingual_text
               WHERE key LIKE ? OR en LIKE ? OR zh LIKE ?
               ORDER BY key LIMIT ?""",
            (like, like, like, limit)
        ).fetchall()
        return [dict(r) for r in rows]