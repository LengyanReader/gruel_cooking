# -*- coding: utf-8 -*-
"""engine/graph_export_neo4j.py — RKF L3 → Neo4j projection (optional).

File authority stays with knowledge/graph/{nodes,edges}.jsonl; Neo4j is a
*derived projection* (locked assumption A1 — no DB needed to develop/maintain).
This tool reads the graph store + graph/schema.json and emits idempotent Cypher
(``CALL { } IN TRANSACTIONS;`` MERGE+SET), matching the Language-Stacking
convention in ``web/export_neo4j.py``. It never connects to a DB by itself; pipe
the .cypher into cypher-shell, or run with --exec when a driver + URI exist.

Schema-driven: node labels come from schema.node_types, relationship types are
the upper-cased schema.edge_types keys. Only scalar properties are projected
(labels + the reader's own short relation notes) — never any book text.

Usage:
    python -X utf8 engine/graph_export_neo4j.py            # write neo4j_load.cypher
    python -X utf8 engine/graph_export_neo4j.py --summary   # counts only
"""
from __future__ import annotations

import argparse
import json
import os
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.normpath(os.path.join(HERE, "..", "knowledge", "graph"))
SCHEMA = os.path.join(GRAPH, "schema.json")
NODES = os.path.join(GRAPH, "nodes.jsonl")
EDGES = os.path.join(GRAPH, "edges.jsonl")
OUT = os.path.join(GRAPH, "neo4j_load.cypher")


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _esc(s) -> str:
    return str(s).replace("\\", "\\\\").replace('"', '\\"')


def _cstmt(body: str) -> str:
    return "CALL { %s } IN TRANSACTIONS;" % " ".join(body.split())


def _scalar_props(d: dict) -> dict:
    return {k: v for k, v in (d or {}).items() if isinstance(v, (str, int, float, bool)) and str(v) != ""}


def _edge_key(e: dict) -> str:
    seed = json.dumps([e["from"], e["to"], e["type"], e.get("props", {})],
                      ensure_ascii=False, sort_keys=True)
    return "%08x" % (zlib.crc32(seed.encode("utf-8")) & 0xFFFFFFFF)


def export(schema: dict, nodes: list, edges: list) -> str:
    node_types = schema.get("node_types", {})
    L = ["// Reading Knowledge Fabric → Neo4j (derived projection of graph/*.jsonl)",
         "// idempotent: MERGE + SET; regenerate via engine/graph_export_neo4j.py",
         f"// nodes={len(nodes)} edges={len(edges)}", ""]

    for n in nodes:
        label = node_types.get(n["type"], {}).get("id_prefix", n["type"]).capitalize()
        # use a stable type name (Author/Book/Character/Person/Concept)
        label = n["type"]
        props = {"gid": n["id"], "rkf_label": n.get("label", "")}
        props.update(_scalar_props(n.get("props")))
        set_clause = ", ".join(f"n.{k} = \"{_esc(v)}\"" for k, v in props.items())
        L.append(_cstmt(f"MERGE (n:{label} {{gid: \"{_esc(n['id'])}\"}}) SET {set_clause}"))

    L.append("")
    for e in edges:
        rel = e["type"].upper()
        eprops = _scalar_props(e.get("props"))
        eprops["rk_key"] = _edge_key(e)
        set_clause = ", ".join(f"rel.{k} = \"{_esc(v)}\"" for k, v in eprops.items())
        L.append(_cstmt(
            f"MATCH (a {{gid: \"{_esc(e['from'])}\"}}), (b {{gid: \"{_esc(e['to'])}\"}}) "
            f"MERGE (a)-[rel:{rel} {{rk_key: \"{eprops['rk_key']}\"}}]->(b) SET {set_clause}"))

    L += ["", "// index suggestions:",
          "//   CREATE INDEX node_gid IF NOT EXISTS FOR (n:Author) ON (n.gid);",
          "//   (repeat for :Book :Character :Person :Concept)", ""]
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Project RKF graph to Neo4j Cypher")
    ap.add_argument("--summary", action="store_true", help="print counts, do not write")
    ap.add_argument("--out", default=OUT)
    args = ap.parse_args(argv)

    if not (os.path.exists(NODES) and os.path.exists(EDGES)):
        print("[graph_export_neo4j] no graph store yet — run engine/graph_build.py first")
        return 1
    schema = _load(SCHEMA)
    nodes = _jsonl(NODES)
    edges = _jsonl(EDGES)
    text = export(schema, nodes, edges)
    labels = {}
    for n in nodes:
        labels[n["type"]] = labels.get(n["type"], 0) + 1
    rels = {}
    for e in edges:
        rels[e["type"]] = rels.get(e["type"], 0) + 1
    if args.summary:
        print(f"[graph_export_neo4j] would write {len(text.splitlines())} statements"
              f"  nodes={len(nodes)} edges={len(edges)}")
        print("  labels:", labels)
        print("  rels:", rels)
        return 0
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"[graph_export_neo4j] wrote {len(text.splitlines())} lines -> {os.path.relpath(args.out, HERE)}")
    print("  load: cypher-shell -u neo4j -p <pass> -f knowledge/graph/neo4j_load.cypher")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
