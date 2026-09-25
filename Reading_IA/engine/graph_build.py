# -*- coding: utf-8 -*-
"""engine/graph_build.py — RKF L3 graph hub assembler (registry-driven).

Projects the existing file sources into a single property-graph store:

    web/data/authors.json     -> Author nodes
    web/data/books.json       -> Book + Character nodes, authored_by / charedge edges
    web/data/relations.json   -> Author<->Author / Author->Person / Author->Concept edges

writes  knowledge/graph/nodes.jsonl + edges.jsonl.

It reads node/edge *types* (and their colors / dash / cardinality) only from
knowledge/graph/schema.json — no domain constants are duplicated here. The
rendering pages (build_reading.py / render.py) and the --graph audit gate both
consume the same schema, so this file and the hub stay the single source and the
old JSON become views of it.

Re-runnable, deterministic (sorted output), prose-free (only labels + short
relation notes already present in the data). Commit-safe.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE = os.path.normpath(os.path.join(HERE, "..", "knowledge"))
GRAPH = os.path.join(KNOWLEDGE, "graph")
WEB_DATA = os.path.normpath(os.path.join(HERE, "..", "web", "data"))

SCHEMA = os.path.join(GRAPH, "schema.json")
NODES_OUT = os.path.join(GRAPH, "nodes.jsonl")
EDGES_OUT = os.path.join(GRAPH, "edges.jsonl")


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _slug(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").strip().lower()
    s = re.sub(r"[（(].*?[)）]", "", s)          # drop parenthetical glosses
    s = re.sub(r"[^\w\u4e00-\u9fff]+", "-", s, flags=re.UNICODE)
    return s.strip("-")[:64] or "x"


class Hub:
    """Accumulates nodes/edges; node ids are globally unique."""

    def __init__(self, schema):
        self.schema = schema
        self.node_types = schema["node_types"]
        self.edge_types = schema["edge_types"]
        self._nodes = {}   # id -> node
        self._edges = {}   # key -> edge (dedup)

    def add_node(self, ntype, key, label, props=None):
        prefix = self.node_types[ntype]["id_prefix"]
        nid = f"{prefix}:{key}"
        if nid not in self._nodes:
            self._nodes[nid] = {"id": nid, "type": ntype, "label": label, "props": props or {}}
        return nid

    def has_node(self, nid):
        return nid in self._nodes

    def node_by_prefix_key(self, prefix, key):
        return f"{prefix}:{key}"

    def add_edge(self, frm, to, etype, props=None):
        key = (frm, to, etype, json.dumps(props or {}, ensure_ascii=False, sort_keys=True))
        self._edges[key] = {"from": frm, "to": to, "type": etype, "props": props or {}}

    def dump(self, nodes_path, edges_path):
        with open(nodes_path, "w", encoding="utf-8") as fh:
            for n in sorted(self._nodes.values(), key=lambda x: x["id"]):
                fh.write(json.dumps(n, ensure_ascii=False) + "\n")
        with open(edges_path, "w", encoding="utf-8") as fh:
            for e in sorted(self._edges.values(), key=lambda x: (x["type"], x["from"], x["to"])):
                fh.write(json.dumps(e, ensure_ascii=False) + "\n")
        return len(self._nodes), len(self._edges)


def build(schema, authors, books, relations):
    hub = Hub(schema)
    aprefix = schema["node_types"]["Author"]["id_prefix"]
    cprefix = schema["node_types"]["Concept"]["id_prefix"]
    pprefix = schema["node_types"]["Person"]["id_prefix"]

    # ---- Author nodes ----
    author_list = authors.get("authors", authors) if isinstance(authors, dict) else authors
    author_ids = set()
    for a in author_list:
        aid = a.get("id")
        if not aid:
            continue
        author_ids.add(aid)
        hub.add_node("Author", aid, a.get("name_en") or a.get("name_zh") or aid,
                     {"name_zh": a.get("name_zh"), "school_zh": a.get("school_zh"),
                      "domain_zh": a.get("domain_zh")})

    # ---- Book nodes + authored_by + characters/charedges ----
    for b in books:
        bid = b.get("id")
        if not bid:
            continue
        hub.add_node("Book", bid, b.get("title_zh") or b.get("title_orig") or bid,
                     {"kind": b.get("kind"), "author": b.get("author"), "year": b.get("year")})
        aslug = b.get("author_slug")
        if aslug:
            book_nid = hub.node_by_prefix_key(schema["node_types"]["Book"]["id_prefix"], bid)
            hub.add_edge(book_nid, f"{aprefix}:{aslug}", "authored_by", {"book": bid})
        # characters -> Character nodes (names only; no prose)
        chars = b.get("characters") or []
        for c in chars:
            cid = c.get("id")
            if not cid:
                continue
            key = f"{bid}:{cid}"
            hub.add_node("Character", key, c.get("name") or cid,
                         {"group": c.get("group"), "conf": c.get("conf"),
                          "book": bid})
        # charedges -> typed edges when the kind is registered in schema
        for ce in (b.get("charedges") or []):
            if len(ce) < 3:
                continue
            a_id, b_id, kind = ce[0], ce[1], ce[2]
            note = ce[3] if len(ce) > 3 else ""
            if kind not in hub.edge_types:
                continue  # audit gate reports unregistered kinds
            frm = hub.node_by_prefix_key(schema["node_types"]["Character"]["id_prefix"], f"{bid}:{a_id}")
            to = hub.node_by_prefix_key(schema["node_types"]["Character"]["id_prefix"], f"{bid}:{b_id}")
            hub.add_edge(frm, to, kind, {"book": bid, "note": note})

    # ---- author relations (relations.json) ----
    def author_or_person(tok):
        if tok in author_ids:
            return f"{aprefix}:{tok}"
        label = re.sub(r"[（(].*?[)）]", "", tok).strip() or tok
        return hub.add_node("Person", _slug(tok), label, {"raw": tok})

    for r in relations.get("influences", []):
        hub.add_edge(author_or_person(r["from"]), author_or_person(r["to"]), "influence",
                     {"conf": r.get("conf"), "why_zh": r.get("why_zh"), "why_en": r.get("why_en")})
    for r in relations.get("circle", []):
        hub.add_edge(author_or_person(r["from"]), author_or_person(r["to"]), "in_circle",
                     {"conf": r.get("conf"), "why_zh": r.get("why_zh"), "why_en": r.get("why_en")})
    for r in relations.get("cowrites", []):
        hub.add_edge(author_or_person(r["from"]), author_or_person(r["to"]), "cowrite",
                     {"conf": r.get("conf"), "book": r.get("book"), "year": r.get("year")})
    for r in relations.get("schools", []):
        skey = _slug(r.get("school_en") or r.get("school_zh") or "school")
        cnode = hub.add_node("Concept", skey, r.get("school_en") or r.get("school_zh"),
                             {"school_zh": r.get("school_zh"), "school_en": r.get("school_en")})
        hub.add_edge(f"{aprefix}:{r['author']}", cnode, "school_of", {"conf": r.get("conf")})

    return hub


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Assemble RKF L3 graph (nodes.jsonl + edges.jsonl) from data files")
    ap.add_argument("--check", action="store_true", help="build + report counts, do not write")
    args = ap.parse_args(argv)

    schema = _load(SCHEMA)
    authors = _load(os.path.join(WEB_DATA, "authors.json"))
    books = _load(os.path.join(WEB_DATA, "books.json"))["books"]
    relations = _load(os.path.join(WEB_DATA, "relations.json"))

    hub = build(schema, authors, books, relations)
    if args.check:
        n, e = len(hub._nodes), len(hub._edges)
        print(f"[graph_build] check: {n} nodes, {e} edges (would write)")
        return 0
    os.makedirs(GRAPH, exist_ok=True)
    n, e = hub.dump(NODES_OUT, EDGES_OUT)
    print(f"[graph_build] wrote {n} nodes -> {os.path.relpath(NODES_OUT, HERE)}")
    print(f"[graph_build] wrote {e} edges -> {os.path.relpath(EDGES_OUT, HERE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
