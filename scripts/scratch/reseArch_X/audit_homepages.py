#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Audit every `homepage:` field under reseArch_X/scholars/.

Three checks, in order of how often they bite:

1. **Non-URL / placeholder fields** — values that are prose ("(UNC)",
   "无个人主页 ◇") never became links; they render as a "no stable homepage"
   span, but they still need a human pass now and then.
2. **URL with trailing CJK / parenthetical** — the real defect: a note glued
   straight onto the URL ("https://x.org（个人页）") keeps the anchor but
   poisons the href. This is what broke 5 dossiers across v16-v17.
3. **Reachability** — GET each URL and report anything that is not 200.
   403 usually means bot-gating (browser still opens it); 000 usually means
   the host is unreachable from this network, not that the page is gone.
   Re-probe 000s by hand with a delay before concluding anything: the local
   network throttles after ~40 requests and starts returning 000 in bulk.

Usage:
    python scripts/scratch/reseArch_X/audit_homepages.py            # list only
    python scripts/scratch/reseArch_X/audit_homepages.py --probe    # + HTTP codes
    python scripts/scratch/reseArch_X/audit_homepages.py --probe --delay 3

Exit code is 1 when check 2 finds anything (a broken href is a real defect);
403/000 do not fail the run, they are printed for triage.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SCHOLARS = REPO / "reseArch_X" / "scholars"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
URL_RE = re.compile(r"^https?://\S+$")


def parse_field(text: str, key: str) -> str:
    """Pull `key: value` from the yaml-in-fence block, dropping `# comments`."""
    for line in text.splitlines():
        if line.startswith(key + ":"):
            value = line[len(key) + 1:].strip()
            return re.sub(r"\s+#.*$", "", value).strip()
    return ""


def read_records():
    for path in sorted(SCHOLARS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        name = parse_field(text, "name")
        if not name:
            continue
        yield path, name, parse_field(text, "homepage")


def probe(url: str, timeout: int) -> str:
    result = subprocess.run(
        ["curl.exe", "-s", "-L", "-m", str(timeout), "-o", "NUL",
         "-w", "%{http_code}", "-A", UA, url],
        capture_output=True,
    )
    return result.stdout.decode("utf-8", "replace").strip() or "???"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", action="store_true", help="GET every URL")
    ap.add_argument("--delay", type=float, default=1.5,
                    help="seconds between requests (default 1.5)")
    ap.add_argument("--timeout", type=int, default=25)
    args = ap.parse_args()

    placeholders, clean_urls, glued = [], [], []
    for path, name, home in read_records():
        if not home:
            placeholders.append((path.name, name, "(empty)"))
        elif not home.startswith(("http://", "https://")):
            placeholders.append((path.name, name, home))
        elif not URL_RE.match(home):
            glued.append((path.name, name, home))
        else:
            clean_urls.append((path.name, name, home))

    print(f"scholars with homepage: {len(placeholders) + len(clean_urls) + len(glued)}"
          f" · clean URL {len(clean_urls)} · placeholder {len(placeholders)}"
          f" · URL+note glued {len(glued)}")

    if placeholders:
        print("\n## placeholder (no link rendered — confirm it still deserves one)")
        for f, n, h in placeholders:
            print(f"   {n:32s} {h[:110]}")

    if glued:
        print("\n## URL with trailing note — BROKEN href, move the note into a comment")
        for f, n, h in glued:
            print(f"   {f:34s} {h[:110]}")

    if args.probe:
        print(f"\n## reachability ({len(clean_urls)} URLs, {args.delay}s apart)")
        for i, (_f, n, url) in enumerate(clean_urls):
            if i:
                time.sleep(args.delay)
            code = probe(url, args.timeout)
            if code != "200":
                print(f"   {code:>3}  {n:32s} {url}")

    return 1 if glued else 0


if __name__ == "__main__":
    sys.exit(main())
