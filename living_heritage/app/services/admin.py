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
            "plan_phases": "plan_phases",
            "plan_items": "plan_items",
            "research_notes": "research_notes",
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

    # ── Roadmap phases & items ──

    def list_plan_phases(self, locale: str = "en") -> list[dict]:
        rows = self.db.execute(
            "SELECT id, slug, title_key, sort_order FROM plan_phases ORDER BY sort_order, id"
        ).fetchall()
        return [{"id": r["id"], "slug": r["slug"], "title": self.text.resolve(r["title_key"], locale)}
                for r in rows]

    def list_plan_items(self, locale: str = "en", limit: int = 200) -> list[dict]:
        rows = self.db.execute(
            """SELECT pi.*, pp.slug AS phase_slug FROM plan_items pi
               JOIN plan_phases pp ON pi.phase_id = pp.id
               ORDER BY pp.sort_order, pi.sort_order, pi.id LIMIT ?""",
            (limit,)
        ).fetchall()
        out = []
        for r in rows:
            d = dict(r)
            d["title"] = self.text.resolve(d.get("title_key"), locale)
            d["note"] = self.text.resolve(d.get("note_key") or "", locale)
            out.append(d)
        return out

    @staticmethod
    def _plan_item_keys() -> tuple[str, str, str]:
        stamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        item_key = f"plan.admin.{stamp}"
        return item_key, f"{item_key}.title", f"{item_key}.note"

    def add_plan_item(self, *, phase_slug: str, sort_order: int, status: int,
                      title_en: str, title_zh: str, note_en: str, note_zh: str) -> int:
        pid = self.db.execute("SELECT id FROM plan_phases WHERE slug = ?", (phase_slug,)).fetchone()
        if not pid:
            raise ValueError(f"Unknown phase: {phase_slug}")
        item_key, title_key, note_key = self._plan_item_keys()
        self.db.execute(
            "INSERT INTO bilingual_text (key, en, zh, updated_at) VALUES (?, ?, ?, datetime('now'))",
            (title_key, title_en or "", title_zh or "")
        )
        self.db.execute(
            "INSERT INTO bilingual_text (key, en, zh, updated_at) VALUES (?, ?, ?, datetime('now'))",
            (note_key, note_en or "", note_zh or "")
        )
        cur = self.db.execute(
            """INSERT INTO plan_items (item_key, phase_id, sort_order, status, title_key, note_key)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (item_key, pid["id"], int(sort_order or 0), int(status or 0), title_key, note_key)
        )
        self.db.commit()
        return cur.lastrowid

    def delete_plan_item(self, item_id: int) -> bool:
        row = self.db.execute("SELECT title_key, note_key FROM plan_items WHERE id = ?",
                              (item_id,)).fetchone()
        cur = self.db.execute("DELETE FROM plan_items WHERE id = ?", (item_id,))
        if not cur.rowcount:
            return False
        keys = [k for k in (row["title_key"], row["note_key"]) if k]
        if keys:
            self.db.execute(f"DELETE FROM bilingual_text WHERE key IN ({','.join('?' for _ in keys)})", keys)
        self.db.commit()
        return True

    def get_plan_item(self, item_id: int) -> dict | None:
        row = self.db.execute(
            "SELECT pi.*, pp.slug AS phase_slug FROM plan_items pi "
            "JOIN plan_phases pp ON pi.phase_id = pp.id WHERE pi.id = ?",
            (item_id,)
        ).fetchone()
        if not row:
            return None
        d = dict(row)
        d["title_en"], d["title_zh"] = self._resolve_pair(d.get("title_key"))
        d["note_en"], d["note_zh"] = self._resolve_pair(d.get("note_key"))
        return d

    def update_plan_item(self, item_id: int, *, phase_slug: str, sort_order: int, status: int,
                         title_en: str, title_zh: str, note_en: str, note_zh: str) -> bool:
        row = self.db.execute("SELECT title_key, note_key FROM plan_items WHERE id = ?",
                              (item_id,)).fetchone()
        pid = self.db.execute("SELECT id FROM plan_phases WHERE slug = ?", (phase_slug,)).fetchone()
        if not pid:
            raise ValueError(f"Unknown phase: {phase_slug}")
        if not row:
            return False
        self.set_text(row["title_key"] or "", title_en or "", title_zh or "")
        self.set_text(row["note_key"] or "", note_en or "", note_zh or "")
        self.db.execute(
            "UPDATE plan_items SET phase_id = ?, sort_order = ?, status = ? WHERE id = ?",
            (pid["id"], int(sort_order or 0), int(status or 0), item_id)
        )
        self.db.commit()
        return True

    # ── Research notebook ──

    NOTE_CATEGORIES = ["brainstorm", "question", "decision", "critique", "source"]

    def list_notes(self, limit: int = 200) -> list[dict]:
        rows = self.db.execute(
            "SELECT * FROM research_notes ORDER BY updated_at DESC, id DESC LIMIT ?", (limit,)
        ).fetchall()
        out = []
        for r in rows:
            d = dict(r)
            d["title_en"], d["title_zh"] = self._resolve_pair(d.get("title_key"))
            d["body_en"], d["body_zh"] = self._resolve_pair(d.get("body_key"))
            out.append(d)
        return out

    def search_notes(self, term: str, category: str | None = None,
                     status: int | None = None, limit: int = 60) -> list[dict]:
        sql = ("SELECT id, note_key, category, status, tags, ref_key, updated_at "
               "FROM research_notes WHERE 1=1")
        args = []
        if term:
            sql += """ AND (note_key LIKE ? OR tags LIKE ? OR ref_key LIKE ? OR id IN (
                SELECT rn.id FROM research_notes rn JOIN bilingual_text bt ON bt.key = rn.title_key
                WHERE bt.en LIKE ? OR bt.zh LIKE ? OR rn.id IN (
                    SELECT rn2.id FROM research_notes rn2 JOIN bilingual_text bt2
                    ON bt2.key = rn2.body_key WHERE bt2.en LIKE ? OR bt2.zh LIKE ?)))"""
            like = f"%{term}%"
            args += [like, like, like, like, like, like, like]
        if category:
            sql += " AND category = ?"
            args.append(category)
        if status is not None:
            sql += " AND status = ?"
            args.append(status)
        sql += " ORDER BY updated_at DESC, id DESC LIMIT ?"
        args.append(limit)
        return [dict(r) for r in self.db.execute(sql, args).fetchall()]

    @staticmethod
    def _note_keys() -> tuple[str, str, str]:
        stamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        note_key = f"note.{stamp}"
        return note_key, f"{note_key}.title", f"{note_key}.body"

    def add_note(self, *, title_en: str, title_zh: str, body_en: str, body_zh: str,
                 category: str, status: int, tags: str, ref_key: str) -> int:
        if category not in self.NOTE_CATEGORIES:
            raise ValueError(f"Unknown category: {category}")
        if int(status) not in (0, 1, 2):
            raise ValueError(f"Unknown status: {status}")
        note_key, title_key, body_key = self._note_keys()
        self.db.execute(
            "INSERT INTO bilingual_text (key, en, zh, updated_at) VALUES (?, ?, ?, datetime('now'))",
            (title_key, title_en or "", title_zh or "")
        )
        self.db.execute(
            "INSERT INTO bilingual_text (key, en, zh, updated_at) VALUES (?, ?, ?, datetime('now'))",
            (body_key, body_en or "", body_zh or "")
        )
        cur = self.db.execute(
            """INSERT INTO research_notes
               (note_key, title_key, body_key, category, status, tags, ref_key)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (note_key, title_key, body_key, category, int(status), tags or "", ref_key or "")
        )
        self.db.commit()
        return cur.lastrowid

    def delete_note(self, note_id: int) -> bool:
        row = self.db.execute("SELECT title_key, body_key FROM research_notes WHERE id = ?",
                              (note_id,)).fetchone()
        cur = self.db.execute("DELETE FROM research_notes WHERE id = ?", (note_id,))
        if not cur.rowcount:
            return False
        keys = [k for k in (row["title_key"], row["body_key"]) if k]
        if keys:
            self.db.execute(f"DELETE FROM bilingual_text WHERE key IN ({','.join('?' for _ in keys)})", keys)
        self.db.commit()
        return True

    def get_note(self, note_id: int) -> dict | None:
        row = self.db.execute("SELECT * FROM research_notes WHERE id = ?", (note_id,)).fetchone()
        if not row:
            return None
        d = dict(row)
        d["title_en"], d["title_zh"] = self._resolve_pair(d.get("title_key"))
        d["body_en"], d["body_zh"] = self._resolve_pair(d.get("body_key"))
        return d

    def update_note(self, note_id: int, *, title_en: str, title_zh: str, body_en: str, body_zh: str,
                    category: str, status: int, tags: str, ref_key: str) -> bool:
        row = self.db.execute("SELECT title_key, body_key FROM research_notes WHERE id = ?",
                              (note_id,)).fetchone()
        if not row:
            return False
        if category not in self.NOTE_CATEGORIES:
            raise ValueError(f"Unknown category: {category}")
        if int(status) not in (0, 1, 2):
            raise ValueError(f"Unknown status: {status}")
        self.set_text(row["title_key"] or "", title_en or "", title_zh or "")
        self.set_text(row["body_key"] or "", body_en or "", body_zh or "")
        self.db.execute(
            """UPDATE research_notes
               SET category = ?, status = ?, tags = ?, ref_key = ?, updated_at = datetime('now')
               WHERE id = ?""",
            (category, int(status), tags or "", ref_key or "", note_id)
        )
        self.db.commit()
        return True