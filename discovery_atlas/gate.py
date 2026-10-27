#!/usr/bin/env python3
"""Discovery Atlas structural gate.

Checks sources/*.json against the schema declared in README.md:
  - valid JSON, entry fields complete (13 required)
  - enum membership (domain/layer/status), types (langs/regions lists)
  - uniqueness of id, normalized host, wikidata_qid
  - a ✔ verification mark must carry an access_date; a bare ○ must not
Exit code 0 = PASS, 1 = FAIL. Machine-checkable structure only —
quality judgment remains human (harness M0.4/M0.8).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LAYERS = {"discovery", "criticism", "publishing", "infrastructure", "access"}
DOMAINS = {"books", "music", "film", "art"}
STATUSES = {"active", "bot-gated", "moved", "contested", "pending"}
REQUIRED = [
    "id", "domain", "layer", "circle", "name", "url", "langs", "regions",
    "kind", "why", "not_for", "verified", "access_date", "status", "note",
]
QID_RE = re.compile(r"^Q\d+$")
# Anchor hosts carry one entry per distinct entity (different articles),
# so host-uniqueness does not apply there — identity is guarded by id/qid.
ANCHOR_HOSTS = {"en.wikipedia.org"}


def host_of(url: str) -> str:
    m = re.match(r"https?://([^/]+)", url)
    return m.group(1).lower().removeprefix("www.") if m else url.lower()


def main() -> int:
    errors = []
    files = sorted((ROOT / "sources").glob("*.json"))
    if not files:
        print("FAIL: no sources/*.json found")
        return 1
    seen = {}
    total = 0
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{f.name}: invalid JSON: {e}")
            continue
        entries = data.get("sources", [])
        if not entries:
            errors.append(f"{f.name}: empty sources list")
        for ent in entries:
            total += 1
            eid = ent.get("id", "<no-id>")
            for k in REQUIRED:
                if k not in ent:
                    errors.append(f"{f.name}:{eid}: missing field '{k}'")
            if ent.get("layer") not in LAYERS:
                errors.append(f"{f.name}:{eid}: bad layer {ent.get('layer')!r}")
            if ent.get("domain") not in DOMAINS:
                errors.append(f"{f.name}:{eid}: bad domain {ent.get('domain')!r}")
            if ent.get("status") not in STATUSES:
                errors.append(f"{f.name}:{eid}: bad status {ent.get('status')!r}")
            for k in ("langs", "regions"):
                v = ent.get(k)
                if not isinstance(v, list) or not v:
                    errors.append(f"{f.name}:{eid}: {k} must be a non-empty list")
            ver = str(ent.get("verified", ""))
            if ver.startswith("✔") and not ent.get("access_date"):
                errors.append(f"{f.name}:{eid}: ✔ without access_date")
            if ver == "○" and not ent.get("access_date") and ent.get("status") != "pending":
                errors.append(f"{f.name}:{eid}: ○ with no date must be status=pending")
            if ent.get("wikidata_qid") and not QID_RE.match(ent["wikidata_qid"]):
                errors.append(f"{f.name}:{eid}: bad wikidata_qid")
            for key, val in (("id", eid), ("host", host_of(ent.get("url", ""))),
                             ("qid", ent.get("wikidata_qid") or None)):
                if val and not (key == "host" and val in ANCHOR_HOSTS):
                    if val in seen.get(key, {}):
                        errors.append(f"dup {key} '{val}': {f.name}:{eid} vs {seen[key][val]}")
                    seen.setdefault(key, {})[val] = f"{f.name}:{eid}"

    print(f"entries checked: {total} across {len(files)} file(s)")
    if errors:
        print(f"FAIL ({len(errors)} problem(s)):")
        for e in errors:
            print("  -", e)
        return 1
    print("PASS: schema complete · enums valid · ids/hosts/qids unique · marks dated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
