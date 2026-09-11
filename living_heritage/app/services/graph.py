"""
Graph service — corridor/site/scholar knowledge graph over SQLite.

Source of truth is SQLite (corridors + relations tables). Neo4j is an
OPTIONAL analysis layer behind the same interface (see neo4j_graph.py);
the site never depends on an external service being online.
"""
import sqlite3
from app.services.locale import TextResolver

# Relation predicates used across seeds/services (single source of truth)
R_BELONGS_TO = "belongs_to"     # site → corridor
R_STUDIES = "studies"           # scholar → corridor / scholar → site
R_INVOLVES = "involves"         # publication → corridor / observation → site


class GraphService:
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.text = TextResolver(db)

    # ── Corridors ──

    def list_corridors(self, locale: str) -> list[dict]:
        """All corridors with resolved names/descriptions and node counts."""
        rows = self.db.execute(
            "SELECT * FROM corridors ORDER BY sort_order, id"
        ).fetchall()
        result = []
        for r in rows:
            r = dict(r)
            texts = self.text.resolve_many(
                [k for k in (r.get("title_key"), r.get("intro_key"), r.get("detail_key")) if k],
                locale,
            )
            r["name"] = texts.get(r.get("title_key"), "") or r["slug"]
            r["description"] = texts.get(r.get("intro_key"), "")
            r["detail"] = texts.get(r.get("detail_key"), "")
            r["region"] = r.get("region") or ""
            r["node_count"] = self._corridor_node_count(r["id"])
            result.append(r)
        return result

    def get_corridor_by_slug(self, slug: str, locale: str) -> dict | None:
        for c in self.list_corridors(locale):
            if c["slug"] == slug:
                return c
        return None

    def _corridor_node_count(self, corridor_id: int) -> int:
        """Count linked nodes: sites (belongs_to) + scholars (studies)."""
        return self.db.execute(
            """SELECT (SELECT COUNT(*) FROM relations
                     WHERE relation = ? AND target_type = 'corridor' AND target_id = ?)
                  + (SELECT COUNT(*) FROM relations
                     WHERE relation = ? AND target_type = 'corridor' AND target_id = ?)""",
            (R_BELONGS_TO, corridor_id, R_STUDIES, corridor_id),
        ).fetchone()[0]

    # ── Relations ──

    def list_relations(self, locale: str, limit: int = 500) -> list[dict]:
        """All relations with resolved entity names (for the graph view)."""
        rows = self.db.execute(
            "SELECT * FROM relations ORDER BY source_type, source_id, target_type, target_id LIMIT ?",
            (limit,),
        ).fetchall()
        rels = [dict(r) for r in rows]

        # Collect name keys for all involved entities, resolve in bulk
        key_by_ref = {}
        for rel in rels:
            for side in ("source", "target"):
                ref = (rel[f"{side}_type"], rel[f"{side}_id"])
                if ref not in key_by_ref:
                    key_by_ref[ref] = self._entity_name_key(*ref)
        resolved = self.text.resolve_many([k for k in key_by_ref.values() if k], locale)

        for rel in rels:
            for side in ("source", "target"):
                ref = (rel[f"{side}_type"], rel[f"{side}_id"])
                rel[f"{side}_name"] = resolved.get(key_by_ref[ref], "") or str(rel[f"{side}_id"])
        return rels

    def _entity_name_key(self, entity_type: str, entity_id: int) -> str | None:
        """Return the bilingual_text key used to name an entity (or None if N/A)."""
        if entity_type == "corridor":
            row = self.db.execute("SELECT title_key FROM corridors WHERE id = ?", (entity_id,)).fetchone()
        elif entity_type == "site":
            row = self.db.execute("SELECT name_key FROM heritage_sites WHERE id = ?", (entity_id,)).fetchone()
        elif entity_type == "scholar":
            row = self.db.execute("SELECT name_key FROM scholars WHERE id = ?", (entity_id,)).fetchone()
        elif entity_type == "publication":
            row = self.db.execute("SELECT title_key FROM publications WHERE id = ?", (entity_id,)).fetchone()
        elif entity_type == "observation":
            row = self.db.execute("SELECT title_key FROM field_observations WHERE id = ?", (entity_id,)).fetchone()
        else:
            return None
        return dict(row).get("title_key" if entity_type in ("corridor", "publication", "observation") else "name_key") if row else None

    # ── Corridor profiles (sites + scholars linked to each corridor) ──

    def corridor_profiles(self, locale: str) -> list[dict]:
        """Each corridor with its sites and scholars attached."""
        profiles = self.list_corridors(locale)
        for c in profiles:
            c["sites"] = self.linked_entities(c["id"], "corridor", "site", R_BELONGS_TO, locale, inverse=True)
            c["scholars"] = self.linked_entities(c["id"], "corridor", "scholar", R_STUDIES, locale, inverse=True)
            c["site_count"] = len(c["sites"])
            c["scholar_count"] = len(c["scholars"])
        return profiles

    def linked_entities(self, entity_id: int, entity_type: str, link_type: str,
                        relation: str, locale: str, inverse: bool = False) -> list[dict]:
        """Entities of a given link_type related to an entity via a relation predicate.

        inverse=True  → this entity is the target; returns matching sources.
        inverse=False → this entity is the source; returns matching targets.
        """
        if inverse:
            rows = self.db.execute(
                "SELECT * FROM relations WHERE relation = ? AND target_type = ? AND target_id = ?",
                (relation, entity_type, entity_id),
            ).fetchall()
            refs = [(r["source_type"], r["source_id"]) for r in rows]
        else:
            rows = self.db.execute(
                "SELECT * FROM relations WHERE relation = ? AND source_type = ? AND source_id = ?",
                (relation, entity_type, entity_id),
            ).fetchall()
            refs = [(r["target_type"], r["target_id"]) for r in rows]

        refs = list(dict.fromkeys(refs))  # de-duplicate, preserve order
        keys = [self._entity_name_key(*ref) for ref in refs]
        resolved = self.text.resolve_many([k for k in keys if k], locale)
        out = []
        for ref, key in zip(refs, keys):
            out.append({
                "entity_type": ref[0],
                "id": ref[1],
                "name": resolved.get(key, "") or str(ref[1]),
            })
        return out

    # ── Scholar profiles ──

    def scholar_profiles(self, locale: str) -> list[dict]:
        """Each scholar with linked corridors and sites."""
        rows = self.db.execute("SELECT * FROM scholars ORDER BY name_key").fetchall()
        out = []
        for r in rows:
            r = dict(r)
            name = self.text.resolve(r.get("name_key"), locale)
            corridors = self.linked_entities(r["id"], "scholar", "corridor", R_STUDIES, locale)
            sites = self.linked_entities(r["id"], "scholar", "site", R_STUDIES, locale)
            out.append({
                "id": r["id"],
                "name": name,
                "institution": r.get("institution") or "",
                "corridors": corridors,
                "sites": sites,
            })
        return out


def get_graph_service(db) -> GraphService:
    """Resolve the configured graph engine. SQLite is the default and canonical."""
    from app.config import GRAPH_ENGINE, NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
    if GRAPH_ENGINE == "neo4j":
        try:
            from app.services.neo4j_graph import get_neo4j_service
            return get_neo4j_service(db, NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
        except Exception as e:  # pragma: no cover - depends on external service
            print(f"Neo4j unavailable, falling back to SQLite graph: {e}")
    return GraphService(db)