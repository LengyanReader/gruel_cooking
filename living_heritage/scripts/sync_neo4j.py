"""
Sync the SQLite knowledge graph into Neo4j (OPTIONAL analysis layer).

The website always serves from SQLite; this script only loads a mirror into
Neo4j for graph algorithms / visualisations. Requires Neo4j running and
LH_GRAPH_ENGINE=neo4j (or passing --uri/--user/--password).

Run:
    python scripts/sync_neo4j.py
    python scripts/sync_neo4j.py --uri bolt://localhost:7687 --user neo4j --password secret
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
from app.db.sqlite import get_db
from app.services.graph import R_BELONGS_TO, R_STUDIES


def load_counts(db):
    sites = {r["id"]: r for r in db.execute("SELECT id, name_key, corridor_slug FROM heritage_sites").fetchall()}
    corridors = {r["id"]: r for r in db.execute("SELECT id, slug, title_key, intro_key, region, sort_order FROM corridors").fetchall()}
    scholars = {r["id"]: r for r in db.execute("SELECT id, name_key, institution, corridor_slugs FROM scholars").fetchall()}
    texts = {r["key"]: r for r in db.execute("SELECT key, en, zh FROM bilingual_text").fetchall()}

    def t(key, en_fallback="", zh_fallback=""):
        row = texts.get(key)
        if not row:
            return en_fallback, zh_fallback
        return row["en"] or en_fallback, row["zh"] or zh_fallback

    nodes = []
    for c in corridors.values():
        en, zh = t(c["title_key"], c["slug"])
        nodes.append(("Corridor", {
            "id": c["id"], "slug": c["slug"], "region": c["region"] or "",
            "name_en": en, "name_zh": zh,
            "sort_order": c["sort_order"],
        }))
    for s in sites.values():
        en, zh = t(s["name_key"], s["corridor_slug"])
        nodes.append(("Site", {"id": s["id"], "name_en": en, "name_zh": zh}))
    for h in scholars.values():
        en, zh = t(h["name_key"])
        nodes.append(("Scholar", {"id": h["id"], "name_en": en, "name_zh": zh,
                                  "institution": h["institution"] or ""}))

    edges = []
    # site -[BELONGS_TO]-> corridor
    corridors_by_slug = {c["slug"]: c["id"] for c in corridors.values()}
    for s in sites.values():
        cid = corridors_by_slug.get(s["corridor_slug"])
        if cid is not None:
            edges.append((s["id"], R_BELONGS_TO.upper(), cid))
    # scholar -[STUDIES]-> corridor
    for h in scholars.values():
        for slug in json.loads(h["corridor_slugs"] or "[]"):
            cid = corridors_by_slug.get(slug)
            if cid is not None:
                edges.append((h["id"], R_STUDIES.upper(), cid))
    return nodes, edges


def main():
    ap = argparse.ArgumentParser(description="Load SQLite knowledge graph into Neo4j")
    ap.add_argument("--uri", default=NEO4J_URI)
    ap.add_argument("--user", default=NEO4J_USER)
    ap.add_argument("--password", default=NEO4J_PASSWORD)
    ap.add_argument("--wipe", action="store_true", help="Delete all mirrored nodes before loading")
    args = ap.parse_args()

    from neo4j import GraphDatabase
    driver = GraphDatabase.driver(args.uri, auth=(args.user, args.password))
    try:
        driver.verify_connectivity()
    except Exception as e:
        print(f"Cannot reach Neo4j at {args.uri}: {e}")
        print("Start it or leave GRAPH_ENGINE=sqlite (the site works without Neo4j).")
        sys.exit(1)

    db = get_db()
    nodes, edges = load_counts(db)

    with driver.session() as session:
        if args.wipe:
            session.run("MATCH (n) DETACH DELETE n")
        for label, props in nodes:
            session.run(
                f"MERGE (n:{label} {{id: $id}}) SET n += $props",
                id=props["id"], props=props,
            )
        for src, rel, tgt in edges:
            session.run(
                f"""MATCH (a) WHERE a.id = $src
                    MATCH (b) WHERE b.id = $tgt
                    MERGE (a)-[r:{rel}]->(b)""",
                src=src, tgt=tgt,
            )
    db.close()
    driver.close()
    print(f"Synced {len(nodes)} nodes, {len(edges)} edges into Neo4j.")


if __name__ == "__main__":
    main()