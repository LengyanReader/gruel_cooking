"""
Graph service — Cypher queries against Neo4j for corridor network analysis.
Falls back gracefully if Neo4j is not running.
"""
from typing import Optional
from app.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

_driver = None
_available = False


def get_driver():
    global _driver, _available
    if _driver is not None:
        return _driver
    try:
        from neo4j import AsyncGraphDatabase
        _driver = AsyncGraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        _available = True
        return _driver
    except Exception as e:
        print(f"Neo4j unavailable: {e}")
        _available = False
        return None


def is_available() -> bool:
    return _available


async def close_driver():
    global _driver
    if _driver:
        await _driver.close()
        _driver = None


class GraphService:
    async def get_corridor_summary(self) -> list[dict]:
        """Get all corridors with node counts."""
        driver = get_driver()
        if not driver:
            return _fallback_corridors()
        async with driver.session() as session:
            result = await session.run(
                """MATCH (c:Corridor)
                   OPTIONAL MATCH (c)-[:CONTAINS]->(n)
                   RETURN c.id AS id, c.name_en AS name_en, c.name_zh AS name_zh,
                          c.slug AS slug, c.region AS region,
                          COUNT(n) AS node_count
                   ORDER BY c.slug"""
            )
            return [dict(record) for record in result]

    async def get_corridor_graph(self, slug: str) -> dict:
        """Get nodes and edges for a corridor's neighborhood."""
        driver = get_driver()
        if not driver:
            return {"nodes": [], "edges": []}
        async with driver.session() as session:
            # Get nodes within 2 hops of the corridor
            result = await session.run(
                """MATCH (c:Corridor {slug: $slug})-[*1..2]-(n)
                   WITH DISTINCT n
                   RETURN labels(n)[0] AS label, n.id AS id,
                          COALESCE(n.name_en, n.name) AS name_en,
                          COALESCE(n.name_zh, n.name) AS name_zh,
                          n AS properties""",
                slug=slug
            )
            nodes = []
            async for record in result:
                props = dict(record["properties"])
                props.pop("id", None)
                props.pop("name_en", None)
                props.pop("name_zh", None)
                nodes.append({
                    "id": record["id"],
                    "label": record["label"],
                    "name_en": record["name_en"],
                    "name_zh": record["name_zh"],
                    "properties": props,
                })

            # Get edges between these nodes
            node_ids = [n["id"] for n in nodes]
            if not node_ids:
                return {"nodes": nodes, "edges": []}

            result = await session.run(
                """MATCH (a)-[r]->(b)
                   WHERE a.id IN $ids AND b.id IN $ids
                   RETURN a.id AS source, b.id AS target,
                          type(r) AS type,
                          r AS properties""",
                ids=node_ids
            )
            edges = []
            async for record in result:
                props = dict(record["properties"])
                props.pop(None, None)
                edges.append({
                    "source": record["source"],
                    "target": record["target"],
                    "type": record["type"],
                })

            return {"nodes": nodes, "edges": edges}

    async def get_interfaces(self, corridor_slug: str) -> list[dict]:
        """Get cultural interfaces touching a corridor."""
        driver = get_driver()
        if not driver:
            return []
        async with driver.session() as session:
            result = await session.run(
                """MATCH (i:Interface)-[:LINKS]-(c:Corridor {slug: $slug})
                   RETURN i.id AS id, i.name_en AS name_en, i.name_zh AS name_zh,
                          i.interface_type AS type,
                          i.description_en AS desc_en, i.description_zh AS desc_zh
                   ORDER BY i.name_en""",
                slug=corridor_slug
            )
            return [dict(record) for record in result]

    async def find_shortest_path(self, slug_a: str, slug_b: str) -> dict:
        """Find shortest path between two corridors."""
        driver = get_driver()
        if not driver:
            return {"path": [], "length": -1}
        async with driver.session() as session:
            result = await session.run(
                """MATCH path = shortestPath(
                     (a:Corridor {slug: $a})-[*]-(b:Corridor {slug: $b})
                   )
                   RETURN [n IN nodes(path) | n.id] AS node_ids,
                          [r IN relationships(path) | type(r)] AS rel_types,
                          length(path) AS dist""",
                a=slug_a, b=slug_b
            )
            record = await result.single()
            if not record:
                return {"path": [], "length": -1}
            return {
                "node_ids": record["node_ids"],
                "rel_types": record["rel_types"],
                "length": record["dist"],
            }


def _fallback_corridors() -> list[dict]:
    """Return hardcoded corridor list when Neo4j is offline."""
    return [
        {"id": "grand_canal", "name_en": "Grand Canal Beijing", "name_zh": "北京大运河",
         "slug": "grand_canal", "region": "Beijing", "node_count": 0},
        {"id": "gotland", "name_en": "Gotland", "name_zh": "哥特兰",
         "slug": "gotland", "region": "Sweden", "node_count": 0},
        {"id": "southern_oland", "name_en": "Southern Öland", "name_zh": "南厄兰岛",
         "slug": "southern_oland", "region": "Sweden", "node_count": 0},
        {"id": "linkoping", "name_en": "Linköping / Kinda Canal", "name_zh": "林雪平/金达运河",
         "slug": "linkoping", "region": "Sweden", "node_count": 0},
    ]
