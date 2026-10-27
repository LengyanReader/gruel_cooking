#!/usr/bin/env python3
"""Discovery Atlas · wikidata_qid resolver (verified, never fabricated).

Strategy (entity-resolution, M0.1/M0.4 — no fabrication):
  - Wikipedia-anchored url (en.wikipedia.org/wiki/<Title>): resolve exactly via
    sitelink lookup (sites=enwiki&titles=<Title>).
  - otherwise: wbsearchentities by name, then CONFIRM each candidate by its
    P856 "official website" claim — accept the QID only when the candidate's
    registrable domain matches this entry's url domain. Unconfirmed -> leave blank.

Writes resolved QIDs back in place (ensure_ascii=False, indent=2) and prints a
per-file summary. Requires network; run from the module root.
"""
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://www.wikidata.org/w/api.php"
UA = "discovery-atlas-qid-resolver/0.1 (research registry; contact: local)"


def api(params: dict) -> dict:
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    delay = 3.0
    for attempt in range(8):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                # polite gap between every raw request
                time.sleep(1.0)
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 7:
                retry_after = e.headers.get("Retry-After") if e.headers else None
                try:
                    wait = max(delay, float(retry_after)) if retry_after else delay
                except (TypeError, ValueError):
                    wait = delay
                time.sleep(min(wait, 60.0))
                delay = min(delay * 2, 60.0)
                continue
            raise
    raise RuntimeError("unreachable")


def reg_domain(url: str) -> str:
    m = re.match(r"https?://([^/]+)", url or "")
    if not m:
        return ""
    host = m.group(1).lower().removeprefix("www.")
    parts = host.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def clean_name(name: str) -> str:
    # drop parenthetical glosses (both fullwidth and ascii)
    return re.split(r"[（(]", name)[0].strip() or name.strip()


def qid_from_sitelink(title: str) -> str:
    d = api({"action": "wbgetentities", "sites": "enwiki", "titles": title, "props": "info"})
    for ent in d.get("entities", {}).values():
        if ent.get("missing") == "":
            return ""
        q = ent.get("id", "")
        return q if re.match(r"^Q\d+$", q) else ""
    return ""


def p856_batch(qids: list) -> dict:
    """One call -> {qid: set(registrable domains from P856)}."""
    if not qids:
        return {}
    d = api({"action": "wbgetentities", "ids": "|".join(qids), "props": "claims"})
    out = {q: set() for q in qids}
    for q, ent in d.get("entities", {}).items():
        for cl in ent.get("claims", {}).get("P856", []):
            try:
                val = cl["mainsnak"]["datavalue"]["value"]
            except (KeyError, TypeError):
                continue
            out.setdefault(q, set()).add(reg_domain(val))
    return out


def resolve(entry: dict) -> str:
    url = entry.get("url", "")
    m = re.match(r"https?://en\.wikipedia\.org/wiki/(.+)$", url)
    if m:  # Wikipedia-anchored entry -> exact sitelink
        return qid_from_sitelink(urllib.parse.unquote(m.group(1)))
    host = reg_domain(url)
    if not host:
        return ""
    sr = api({"action": "wbsearchentities", "search": clean_name(entry.get("name", "")),
              "language": "en", "uselang": "en", "limit": "5", "type": "item"})
    cands = [c["id"] for c in sr.get("search", []) if re.match(r"^Q\d+$", c.get("id", ""))]
    batch = p856_batch(cands[:5])
    for q in cands:
        if host in batch.get(q, set()):
            return q
    return ""


def main(argv: list) -> int:
    # optional: pass filenames to restrict scope (resume-friendly)
    only = {a.lower() for a in argv[1:]}
    total = resolved = 0
    unresolved = []
    files = [f for f in sorted((ROOT / "sources").glob("*.json"))
             if not only or f.name.lower() in only]
    for f in files:
        data = json.loads(f.read_text(encoding="utf-8"))
        changed = 0
        for ent in data.get("sources", []):
            total += 1
            if ent.get("wikidata_qid"):
                continue
            try:
                qid = resolve(ent)
            except Exception as e:
                qid = ""
                print(f"  ! {ent.get('id')}: {type(e).__name__}", flush=True)
            if qid:
                ent["wikidata_qid"] = qid
                resolved += 1
                changed += 1
                # checkpoint write so progress survives an interrupt
                f.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")
                print(f"  + {ent.get('id')} -> {qid}", flush=True)
            else:
                unresolved.append(f"{f.name}:{ent.get('id')}")
                print(f"  . {ent.get('id')} (no verified match)", flush=True)
            time.sleep(1.2)
        print(f"{f.name}: +{changed} resolved", flush=True)
    print(f"\nresolved {resolved}/{total}; left blank (needs manual/verified) {len(unresolved)}",
          flush=True)
    if unresolved:
        print("unresolved ids:", ", ".join(unresolved), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
