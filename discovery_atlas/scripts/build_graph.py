#!/usr/bin/env python3
"""Discovery Atlas · graph builder.

Derives an entity constellation purely from Wikidata claims (no fabrication):
  1. direct edges  — a registered entity's corporate/organisational claim
                     (P127 owned by / P176 publisher / P355 subsidiary /
                     P361 part of / P527 has part) whose target is ANOTHER
                     registered QID;
  2. class hubs    — P31 (instance of) / P279 (subclass of) values shared by
                     >= MIN shared entities become intermediate nodes.
Writes docs/discovery_atlas/graph.json (nodes + links) consumed by the web
view's "星图/Graph" panel. Re-run after any batch. Polite: batched wbgetentities.
"""
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
OUT = REPO / "docs" / "discovery_atlas" / "graph.json"
UA = {"User-Agent": "DiscoveryAtlasRegistry/1.0 (research; contact via repo)"}

DIRECT_PROPS = {"P127": "owned by", "P176": "published by",
                "P355": "subsidiary", "P361": "part of", "P527": "has part"}
CLASS_PROPS = ["P31", "P279"]
MIN_HUB = 3           # class must connect >= this many registered entities to show
MAX_HUBS = 30         # cap hubs by degree to avoid a hairball


def api(url):
    delay = 3.0
    for attempt in range(8):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                time.sleep(0.6)
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 7:
                ra = e.headers.get("Retry-After")
                time.sleep(min(max(delay, float(ra) if ra and ra.isdigit() else delay), 60))
                delay = min(delay * 2, 60)
                continue
            raise
        except Exception:
            if attempt < 7:
                time.sleep(delay); delay = min(delay * 2, 60); continue
            raise


def fetch_claims(qids):
    out = {}
    for i in range(0, len(qids), 50):
        chunk = qids[i:i + 50]
        js = api("https://www.wikidata.org/w/api.php?action=wbgetentities"
                 "&props=claims&format=json&ids=" + "|".join(chunk))
        out.update(js.get("entities", {}))
        time.sleep(1.0)
    return out


def fetch_labels(qids):
    out = {}
    for i in range(0, len(qids), 50):
        chunk = [q for q in qids[i:i + 50] if q]
        if not chunk:
            continue
        js = api("https://www.wikidata.org/w/api.php?action=wbgetentities"
                 "&props=labels&languages=en&format=json&ids=" + "|".join(chunk))
        for q, ent in js.get("entities", {}).items():
            out[q] = (ent.get("labels", {}).get("en", {}) or {}).get("value", q)
        time.sleep(1.0)
    return out


def item_targets(claims, prop):
    res = []
    for sn in (claims or {}).get(prop, []):
        dv = ((sn.get("mainsnak") or {}).get("datavalue") or {})
        if dv.get("type") == "wikibase-entityid":
            q = dv["value"].get("id")
            if q:
                res.append(q)
    return res


def main():
    ents = []
    for f in sorted((ROOT / "sources").glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        for e in data.get("sources", []):
            if e.get("wikidata_qid"):
                ents.append(e)
    by_qid = {e["wikidata_qid"]: e for e in ents}
    qids = list(by_qid)
    print(f"registered entities with QID: {len(qids)}")

    claims = fetch_claims(qids)

    nodes = {}
    for q, e in by_qid.items():
        nodes[q] = {"id": q, "kind": "entity", "domain": e["domain"],
                    "circle": e["circle"], "name": e["name"], "url": e["url"],
                    "why": e.get("why", "")}
    links = []
    seen_link = set()

    # 1. direct entity<->entity edges
    for q, e in by_qid.items():
        for prop, label in DIRECT_PROPS.items():
            for tgt in item_targets(claims.get(q, {}).get("claims"), prop):
                if tgt in by_qid and tgt != q:
                    key = tuple(sorted((q, tgt))) + (prop,)
                    if key in seen_link:
                        continue
                    seen_link.add(key)
                    links.append({"source": q, "target": tgt, "type": "direct",
                                  "rel": label})

    # 2. class hubs
    member = {}   # classQid -> set(entityQid)
    for q in by_qid:
        for cp in CLASS_PROPS:
            for c in item_targets(claims.get(q, {}).get("claims"), cp):
                member.setdefault(c, set()).add(q)
    hubs = [(c, ms) for c, ms in member.items() if len(ms) >= MIN_HUB]
    hubs.sort(key=lambda x: -len(x[1]))
    hubs = hubs[:MAX_HUBS]
    hub_labels = fetch_labels([c for c, _ in hubs])
    for c, ms in hubs:
        nodes[c] = {"id": c, "kind": "class", "name": hub_labels.get(c, c)}
        for q in ms:
            links.append({"source": q, "target": c, "type": "class", "rel": "instance"})

    graph = {"generated": "2026-10-27",
             "counts": {"entities": len(qids), "hubs": len(hubs), "links": len(links)},
             "nodes": list(nodes.values()), "links": links}
    OUT.write_text(json.dumps(graph, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT} · entities {len(qids)} · hubs {len(hubs)} · links {len(links)}")


if __name__ == "__main__":
    main()
