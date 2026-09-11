"""
Neo4j graph repository — OPTIONAL analysis layer behind the same interface.

The website serves from SQLite (graph.py) and never requires Neo4j.
Enable it explicitly with LH_GRAPH_ENGINE=neo4j; load data first via
`python scripts/sync_neo4j.py`. All methods mirror GraphService's public API.
"""
import sqlite3


class Neo4jGraphService:
    """Read-only view over Neo4j mirroring GraphService's interface."""

    def __init__(self, db: sqlite3.Connection, uri: str, user: str, password: str):
        from neo4j import GraphDatabase
        self._db = db
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        self._driver.verify_connectivity()

    def _names(self, ids):
        from app.services.locale import TextResolver
        resolver = TextResolver(self._db)
        keys = {}
        for entity_type, entity_id in ids:
            if entity_type == "corridor":
                row = self._db.execute("SELECT title_key FROM corridors WHERE id = ?", (entity_id,)).fetchone()
                k = dict(row).get("title_key") if row else None
            elif entity_type == "site":
                row = self._db.execute("SELECT name_key FROM heritage_sites WHERE id = ?", (entity_id,)).fetchone()
                k = dict(row).get("name_key") if row else None
            elif entity_type == "scholar":
                row = self._db.execute("SELECT name_key FROM scholars WHERE id = ?", (entity_id,)).fetchone()
                k = dict(row).get("name_key") if row else None
            else:
                k = None
            keys[(entity_type, entity_id)] = k
        # locale is resolved on the Neo4j side for name_en/name_zh stored properties
        return keys

    def _load(self, cypher, **params):
        with self._driver.session() as session:
            return [dict(r) for r in session.run(cypher, **params)]

    def list_corridors(self, locale: str) -> list[dict]:
        rows = self._load(
            """MATCH (c:Corridor)
               OPTIONAL MATCH (s:Site)-[:BELONGS_TO]->(c)
               WITH c, COUNT(s) AS sites
               OPTIONAL MATCH (h:Scholar)-[:STUDIES]->(c)
               RETURN c.slug AS slug, c.region AS region,
                      c.name_en AS name_en, c.name_zh AS name_zh,
                      c.intro_en AS intro_en, c.intro_zh AS intro_zh,
                      sites + COUNT(h) AS node_count
               ORDER BY c.sort_order"""
        )
        out = []
        for r in rows:
            out.append({
                "id": None, "slug": r["slug"], "region": r["region"] or "",
                "name": (r.get("name_en") if locale == "en" else r.get("name_zh")) or r["slug"],
                "description": (r.get("intro_en") if locale == "en" else r.get("intro_zh")) or "",
                "node_count": r["node_count"],
            })
        return out

    def list_relations(self, locale: str, limit: int = 500) -> list[dict]:
        rows = self._load(
            """MATCH (s)-[r]->(t)
               WITH s, r, t LIMIT $limit
               RETURN head(labels(s)) AS source_type, s.id AS source_id,
                      type(r) AS relation,
                      head(labels(t)) AS target_type, t.id AS target_id,
                      COALESCE(s.name_en, s.name) AS source_name,
                      COALESCE(t.name_en, t.name) AS target_name""",
            limit=limit,
        )
        out = []
        for r in rows:
            out.append({
                "source_type": r["source_type"], "source_id": r["source_id"],
                "relation": r["relation"],
                "target_type": r["target_type"], "target_id": r["target_id"],
                "source_name": r["source_name"] or "", "target_name": r["target_name"] or "",
            })
        return out

    def corridor_profiles(self, locale: str) -> list[dict]:
        corridors = self.list_corridors(locale)
        for c in corridors:
            if c["id"] is None:
                c["id"] = -1  # corridor id not stored on node in this view
            c["sites"] = []
            c["scholars"] = []
            c["site_count"] = 0
            c["scholar_count"] = 0
        return corridors

    def scholar_profiles(self, locale: str) -> list[dict]:
        return []

    def close(self):
        if self._driver:
            self._driver.close()


def get_neo4j_service(db, uri: str, user: str, password: str) -> Neo4jGraphService:
    return Neo4jGraphService(db, uri, user, password)