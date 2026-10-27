#!/usr/bin/env python3
"""Discovery Atlas · data export.

Consolidates sources/*.json (the verified registry) into machine-readable
downloads placed beside the static web view so third parties can consume the
atlas without parsing four JSON files. Pure transform — adds no data, so it can
be re-run after any batch. Emits:
  docs/discovery_atlas/atlas.csv     (flat; langs/regions ;-joined; quoted)
  docs/discovery_atlas/atlas.ndjson  (one full entry per line)
  docs/discovery_atlas/atlas.json    (single consolidated object, indent=2)

Usage (from module root):  python scripts/export_data.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTDIR = ROOT.parent / "docs" / "discovery_atlas"

FIELDS = ["id", "wikidata_qid", "domain", "layer", "circle", "name", "url",
          "langs", "regions", "kind", "why", "not_for", "verified",
          "access_date", "status", "note"]


def load():
    ents = []
    for f in sorted((ROOT / "sources").glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        ents.extend(data.get("sources", []))
    ents.sort(key=lambda e: (e.get("domain", ""), e.get("layer", ""), e.get("id", "")))
    return ents


def main():
    ents = load()
    OUTDIR.mkdir(parents=True, exist_ok=True)

    # CSV (flatten list fields)
    with (OUTDIR / "atlas.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_ALL)
        w.writerow(FIELDS)
        for e in ents:
            row = []
            for k in FIELDS:
                v = e.get(k, "")
                if isinstance(v, list):
                    v = ";".join(str(x) for x in v)
                row.append(v)
            w.writerow(row)

    # NDJSON (full entries, one per line)
    with (OUTDIR / "atlas.ndjson").open("w", encoding="utf-8") as fh:
        for e in ents:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")

    # Consolidated JSON
    out = {"generated": "2026-10-27", "total": len(ents),
           "sources": ents}
    (OUTDIR / "atlas.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    qid = sum(1 for e in ents if e.get("wikidata_qid"))
    live = sum(1 for e in ents if str(e.get("verified", "")).startswith("\u2714"))
    print(f"exported {len(ents)} entries ({qid} QID, {live} live) -> {OUTDIR}\\atlas.csv|ndjson|json")


if __name__ == "__main__":
    main()
