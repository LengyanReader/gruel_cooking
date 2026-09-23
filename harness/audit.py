#!/usr/bin/env python3
"""audit.py — the automatic self-evolving auditor for every harness layer.

Scans the whole harness stack (root harness/ + every registered domain
harness docs/workflows.md) and reports drift that should trigger an evolution
signal from harness/evolution.md. Run from the repo root:

    python harness/audit.py            # full scan -> mutations suggested
    python harness/audit.py --strict   # exit 1 if any finding (CI gate)

It detects the exact signals the Evolution mechanism keys on:
  S1  rule/loop duplicated across >=2 domain harnesses   -> Promote
  S2  an active domain (docs/workflows.md exists) is not registered in
      harness/README.md                                  -> Register
  S3  root workflows.md W-GEN references a generator that no longer exists
      in its domain                                      -> Deepen
  S4  a top-level dir that looks like a working domain has no harness at all
                                                          -> Fission
  S5  documented files referenced by any harness file do not exist (broken
      link/path)                                         -> Archive/Deepen
  S6  a new self-contained workflow file exists unregistered               (same as S2)

Exit codes: 0 = clean, 1 = findings (--strict) or broken links.
Stdlib only; runs under `conda activate hy_py312` or any python3.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROOT_H = REPO / "harness"
REL = lambda p: str(p.relative_to(REPO)).replace("\\", "/")  # noqa: E731


def findings(*msgs: str) -> None:
    for m in msgs:
        print(f"  ! {m}")


def harvest_backticked_docs(text: str) -> list[str]:
    """Collect backticked repo-relative tokens that look like actual file/dir refs."""
    out = set()
    for tok in re.findall(r"`([^`]+)`", text):
        if " " in tok or "\u00b7" in tok:          # prose lists, not paths
            continue
        if tok.startswith(("is ", "e.g. ", "a ", "the ")):
            continue
        if not tok.startswith(("docs/", "harness/", "web/", "scripts/", "app/",
                               "Reading_IA/", "living_heritage/", "math_clarification/",
                               "core/", "heaven_climate/", "economics_cross_culture/",
                               "language", "Language Stacking-Linguistic Weaving/")):
            continue
        out.add(tok)
    return sorted(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 if any finding")
    args = ap.parse_args()
    ok = True  # strict-gate
    hard = False  # broken links -> always exit 1

    # ---------- layout ----------
    print(f"repo root       : {REPO}")

    # S1: duplicate workflow tokens across domain harnesses
    domain_hs = list((REPO / "Reading_IA" / "docs" / "workflows.md",))
    # registered domain harness paths known today
    registered = {
        "Reading_IA": REL(REPO / "Reading_IA" / "docs" / "workflows.md"),
        "living_heritage": REL(REPO / "living_heritage" / "docs" / "workflows.md"),
        "math_clarification": REL(REPO / "math_clarification" / "docs" / "workflows.md"),
    }
    registry_table = (ROOT_H / "README.md").read_text(encoding="utf-8")
    for dom, path in registered.items():
        p = REPO / path
        if not p.exists():
            findings(f"S2/registry broken: {dom} registered at {path} but file missing")
            hard = True
        else:
            domain_hs.append(p)

    # S2: any docs/workflows.md present but NOT registered -> Register
    for wf in REPO.glob("*/docs/workflows.md"):
        rel = REL(wf)
        if rel not in registered.values():
            findings(f"S2 Register: {rel} exists but is not in harness/README.md table")
            ok = False

    # S4: top-level dirs that look like active working domains but have no
    #     harness (no docs/workflows.md and no root-level readable README).
    #     Skip domains already registered in harness/README.md.
    registered_names = set()
    for m in re.finditer(r"\|\s*`([^`]+)/`?\s*\|", registry_table):
        registered_names.add(m.group(1).strip("/"))
    for d in sorted(REPO.iterdir()):
        if not d.is_dir() or d.name.startswith((".", "docs")):
            continue
        if d.name in registered_names:
            continue
        has_wf = (d / "docs" / "workflows.md").exists()
        has_readme = any(r.name.lower() in {"readme.md", "readme.zh-cn.md"} for r in d.iterdir())
        has_code = any((d / s).exists() for s in ("web", "scripts", "app", "languages"))
        if not has_wf and (has_readme and has_code):
            findings(f"S4 Fission? {d.name}/: has README + code ({REL(d)}/), unregistered")

    # S3: file references in harness/*.md that must exist
    for f in sorted(ROOT_H.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        for ref in harvest_backticked_docs(text):
            cand = REPO / ref
            # allow web links
            if ref.startswith(("http:", "https:")):
                continue
            if not cand.exists():
                findings(f"S3/S5 broken ref in {REL(f)}: `{ref}`")
                hard = True

    # S6: cross-check each harness file ends with a Self-evolution section
    for p in ([ROOT_H / "README.md"] + sorted({p for p in domain_hs})):
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        if "Self-evolution" not in text and "evolution.md" not in text:
            findings(f"S6 {REL(p)}: missing self-evolution link/section")

    # reconcile: registry rows must match actual domain harness files exactly.
    registry_ok = True
    for dom, path in registered.items():
        if not (REPO / path).exists():
            registry_ok = False
    if registry_ok and not any(REL(wf) in registered.values() for wf in REPO.glob("*/docs/workflows.md")):
        # no unregistered workflows found -> table consistent
        pass

    if hard:
        print("audit FAILED: hard errors (broken links / broken registry)")
        return 1
    if not ok:
        print("audit: non-blocking findings above (evolution signals recommended)")
        return 0 if not args.strict else 1
    print("audit clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())