"""
Scholar service — queries for researcher profiles.
"""
import re
import sqlite3
import json
from app.services.locale import TextResolver

# name_key doubles as the stable identity of a scholar: 'scholar.<slug>.name'
# (the same key publications.json uses in scholar_keys / authored edges).
SLUG_RE = re.compile(r"^scholar\.([a-z0-9_]+)\.name$")


def slug_from_name_key(name_key: str | None) -> str | None:
    m = SLUG_RE.match(name_key or "")
    return m.group(1) if m else None


class ScholarService:
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.text = TextResolver(db)

    def _base(self, r: dict, locale: str) -> dict:
        r = dict(r)
        r["name"] = self.text.resolve(r.get("name_key"), locale)
        r["bio"] = self.text.resolve(r.get("bio_key"), locale)
        r["slug"] = slug_from_name_key(r.get("name_key"))
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

    def get_scholar_by_slug(self, slug: str, locale: str) -> dict | None:
        """Get a single scholar by URL slug (from the name_key convention)."""
        if not slug or not re.fullmatch(r"[a-z0-9_]+", slug):
            return None
        r = self.db.execute(
            "SELECT * FROM scholars WHERE name_key = ?", (f"scholar.{slug}.name",)
        ).fetchone()
        return self._base(r, locale) if r else None

    def related_publications(self, scholar_id: int, locale: str) -> list[dict]:
        """Publications linked to this scholar via the authored relation edges."""
        rows = self.db.execute(
            """SELECT p.* FROM publications p
               JOIN relations r
                 ON r.relation = 'authored' AND r.target_type = 'publication' AND r.target_id = p.id
               WHERE r.source_type = 'scholar' AND r.source_id = ?
               ORDER BY p.year DESC, p.id DESC""",
            (scholar_id,),
        ).fetchall()
        out = []
        for row in rows:
            d = dict(row)
            d["title"] = self.text.resolve(d.get("title_key"), locale)
            d["abstract"] = self.text.resolve(d.get("abstract_key"), locale)
            doi = (d.get("doi") or "").strip()
            d["link"] = d.get("url") or (f"https://doi.org/{doi}" if doi else "")
            out.append(d)
        return out

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