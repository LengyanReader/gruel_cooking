#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_all — run every repo gate in one pass (REVIEW-2026-11 P1-7).

Each module ships its own gate(s); this script lines them up so any session
(or CI) can prove repo health with one command:

    python scripts/check_all.py [--audio] [--living]

Default set = the four content/tool gates + the task-harness self-check.
--audio adds culture_review's verify_audio (needs ffmpeg + beautifulsoup4).
--living adds living_heritage's pytest (needs its requirements installed).

Exit 0 = all enabled gates PASS (SKIP does not fail); exit 1 = any FAIL.
Gates are listed, never invented: each maps 1:1 to a script that already
exists in the repo (M0.4 — observe/report only).
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PY = sys.executable
UTF8 = ["-X", "utf8"]


def factory_path():
    """Resolve the harness-factory path from the task harness pointer, if any."""
    ptr = REPO / ".harness" / "pointer.json"
    try:
        return json.loads(ptr.read_text(encoding="utf-8")).get("harness_factory")
    except (OSError, ValueError):
        return None


def gates(audio: bool, living: bool):
    essays = REPO / "math_clarification" / "essays"
    out = [
        ("discovery_atlas gate.py", REPO / "discovery_atlas",
         [PY, *UTF8, "gate.py"], None, None),
        ("reseArch_X dashboard --check", REPO,
         [PY, *UTF8, "reseArch_X/web/build_reseArch_X.py", "--check"], None, None),
        ("math build_reader --check", essays,
         [PY, *UTF8, "submission/build_reader.py", "--check"], None, None),
        ("math refcheck", essays,
         [PY, *UTF8, "submission/checks/refcheck.py"], None, None),
        ("math review_scope", essays,
         [PY, *UTF8, "submission/checks/review_scope.py"], None, None),
    ]
    hf = factory_path()
    if hf and (Path(hf) / "SKILL.md").is_file():
        out.append(("harness check (.harness)", REPO,
                    [PY, "-m", "harness_factory", "check", "--dir", "."],
                    {"PYTHONPATH": f"{hf}/src"}, None))
    else:
        out.append(("harness check (.harness)", None, None, None,
                    "SKIP: factory not reachable"))
    if audio:
        out.append(("culture_review verify_audio", REPO / "docs" / "culture_review",
                    [PY, *UTF8, "verify_audio.py"], None, None))
    if living:
        out.append(("living_heritage pytest", REPO / "living_heritage",
                    [PY, "-m", "pytest", "-q"], None, None))
    return out


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    audio = "--audio" in sys.argv
    living = "--living" in sys.argv
    rows, failed = [], 0
    for name, cwd, cmd, extra_env, skip in gates(audio, living):
        if cmd is None:
            rows.append((name, "SKIP", skip or "", 0.0))
            continue
        t0 = time.time()
        env = dict(os.environ)
        if extra_env:
            env.update(extra_env)
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env)
        dt = time.time() - t0
        tail = (r.stdout or r.stderr or "").strip().splitlines()
        detail = tail[-1][:110] if tail else ""
        if r.returncode == 0:
            rows.append((name, "PASS", detail, dt))
        else:
            failed += 1
            rows.append((name, "FAIL", detail, dt))
    w = max(len(n) for n, *_ in rows) + 2
    print(f"{'GATE'.ljust(w)}RESULT  TIME     DETAIL")
    for name, verdict, detail, dt in rows:
        mark = {"PASS": "✅", "FAIL": "❌", "SKIP": "⏭️ "}.get(verdict, "  ")
        print(f"{name.ljust(w)}{mark} {verdict.ljust(6)} {dt:5.1f}s  {detail}")
    print(f"\n{len(rows)} gates · {failed} failed · {'ALL OK' if not failed else 'NOT OK'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
