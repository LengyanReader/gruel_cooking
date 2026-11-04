# 舟洲粥 Zhōu Zhōu Zhōu

**[中文 README](README.zh-CN.md) | English**

> **一叶小舟，渡万洲之远；一碗清粥，暖天地之心。**
>
> *A small boat, sailing across distant continents; a warm bowl of porridge, soothing heaven and earth.*

---

## Project Overview

Cooking porridge from the simplest ingredients — using **first principles** to interpret phenomena across heaven, earth, and society. Beyond application, we ask: why do these "basic" principles hold at all? Where are their boundaries?

Porridge is the simplest food, made from the most fundamental ingredients. This project seeks the minimal kernels that explain complex observed phenomena.

---

## Repository Reality · 仓库现状（2026-11）

> Honest layering, per [tasks/REVIEW-2026-11.md](tasks/REVIEW-2026-11.md): three active lines, a shared tool belt, and the founding skeleton zones — each marked with its real status. The table below is the module manifest of record (the Pages landing page aligns to it incrementally).

### Three Active Lines · 三条活跃线

**1. Culture Monthly · 文化月旦（[`docs/culture_review/`](docs/culture_review/)）**
A bilingual monthly review of cultural currents — 2026-10 issue live: eleven sections, four-voice pre-generated neural audio (44 tracks, `verify_audio` gate), inline glossary, selection read-aloud, an append-only corrections register, and every claim traced to sources (✔/◐/◇ + asof).

**2. Math Clarification · 数学释疑（[`math_clarification/`](math_clarification/)）**
Radical-simplicity math: one entry per concept/problem, visuals first (`basics/`, `famous_problems/`, Lean 4 machine-checked `lean/`, story-proof `proof_narratives/`), rendered by audience level (L0–L5) and language (en/zh/dual). Plus the flagship bilingual essays with a three-gate submission package (`essays/`: `build_reader --check`, `refcheck`, `review_scope` — all enforced in CI).

**3. Research Reconnaissance · 科研侦察（[`academic_research/`](academic_research/) → [`reseArch_X/`](reseArch_X/)）**
A direction × momentum × accessibility map of frontier research, with its opportunity layer [`reseArch_X/`](reseArch_X/): **26 open-minded scholar dossiers** (evidence-of-behaviour, source-marked), 9 PhD opportunity files, 5 auditable scan ledgers, and a read-only dashboard ([`docs/reseArch_X/index.html`](docs/reseArch_X/index.html)). Dialogue-first: each scholar carries a small real MVP hook; applications are secondary. No outreach without explicit human authorization.

### Tool Belt · 工具带（cross-cutting）

| Tool | What it does | Status |
|---|---|---|
| [`discovery_atlas/`](discovery_atlas/) | 237 discovery sources, 5 domains × 5 layers × civilizational circles; schema gate (CI); offline site + constellation graph; feeds the machine-visibility study (MVP-001) | active |
| [`Reading_IA/`](Reading_IA/) | Reading corpus & knowledge engine (graph build/audit/export, CI gates); hand-curated book cards growing alongside | forming |
| [`living_heritage/`](living_heritage/) | Full-stack canal app (Docker, pytest CI, PythonAnywhere deploy guide); field lab: Beijing Grand Canal × Gotland | **paused** since 2026-09 — reactivation bound to reseArch_X MVP-002 or explicit downgrade |
| [`Language Stacking-Linguistic Weaving/`](Language%20Stacking-Linguistic%20Weaving/) | Cross-lingual vocab/corpus facets; build-test CI | low-frequency |
| [`harness/`](harness/) | Repo-wide operating manual: methods, skills, tools, rules, workflows (W-GEN/W-ENV/W-PRE/W-EVO/W-CAP), audit.py | maintained |
| `tasks/` | Session protocol (PLAN/PROGRESS), the 2026-11 full-repo review | maintained |

### Skeleton Zone · 骨架区（founding intentions — promise deferred, marked honestly）

| Zone | Path | Status |
|---|---|---|
| First Principles & Metathinking | [`core/`](core/) | skeleton — README + working method only |
| Heaven & Climate | [`heaven_climate/`](heaven_climate/) | skeleton |
| Cross-Culture Economics | [`economics_cross_culture/`](economics_cross_culture/) | **feeding started 2026-11-04** — first sourced case in [`cases/001-salt-and-iron-debate.md`](economics_cross_culture/cases/001-salt-and-iron-debate.md); corpus for reseArch_X MVPs (technodiversity × taste-hierarchy hooks) |
| Contemplative Science | `contemplative science/` | near-empty; the scholarship lives in [`reseArch_X/scholars/`](reseArch_X/scholars/) (Davidson / Singer / Britton) |
| Direction Refs | `direction_refs/` | local-only by design (`.gitignore`) |

### Module Status Manifest · 模块状态总表

| Module | Layer | Gates | CI (2026-11) | Last commit |
|---|---|---|---|---|
| docs/culture_review | content | verify_audio | ✅ culture-review-ci | 2026-11-03 |
| math_clarification | content | build_reader --check · refcheck · review_scope | ✅ math-ci | 2026-11-03 |
| reseArch_X | content | build_reseArch_X --check | ✅ research-ci | 2026-11-04 |
| discovery_atlas | tool | gate.py | ✅ discovery-ci | 2026-11-04 |
| Reading_IA | tool | graph/corpus audits (fabric) | ✅ reading-ci | 2026-09-27 |
| living_heritage | tool | pytest + verify_seed | ✅ ci | 2026-09-26 |
| Language Stacking | tool | build-test | ✅ learning-ci | 2026-09-17 |
| core / heaven_climate / economics | content | — | — | 2026-09-08 |

---

## Directory Structure

```
gruel_cooking/
├── README.md / README.zh-CN.md  # bilingual readme (this file)
├── docs/                        # GitHub Pages: landing + all module sites
│   ├── index.html               #   landing page
│   ├── culture_review/          #   文化月旦 (issue HTML + assets/audio)
│   ├── reseArch_X/              #   scholar/opportunity dashboard
│   ├── math_clarification/      #   entry viewer
│   ├── reading_ia/ · living_heritage/ · language_stacking/ · discovery_atlas/
├── math_clarification/          # entries + essays + submission machinery + web
├── reseArch_X/                  # scholars/ · opportunities/ · mvp/ · indexes/ · scan_log/ · web/
├── academic_research/           # direction recon map (feeds reseArch_X)
├── discovery_atlas/             # sources/*.json (SSOT) · gate.py · scripts/
├── Reading_IA/                  # readings/ · moment/ · knowledge/ · engine/ · web/
├── living_heritage/             # app/ · data/ · scripts/ (Docker; CI)
├── Language Stacking-Linguistic Weaving/  # languages/ · web/
├── core/ · heaven_climate/ · economics_cross_culture/   # skeleton zones
├── harness/                     # repo-wide manual + audit.py
├── scripts/                     # repo-level utilities (scratch/ for one-offs)
└── tasks/                       # PLAN · PROGRESS · REVIEW-2026-11
```

---

## Operating Principles

1. **Start from the observable** — every inquiry begins with a concrete phenomenon or question.
2. **Reduce to the minimal** — find the smallest model that explains using first principles.
3. **Question the explanation** — why does it hold? What does it assume? Where does it fail?
4. **Trace the genealogy** — every idea has an origin; record the chain of influence.
5. **Cross-pollinate** — economics nourishes climate, climate nourishes astronomy; keep the connections alive.
6. **The simplest ingredients** — complexity emerges from the interaction of simple rules. Trust the porridge.
7. **Sources before narrative** — cite primary sources, verify origins, mark reliability (✔ verified / ◐ partial / ◇ unverified, with an access date).

---

## How to Contribute

- Add to the three active lines: a culture-monthly entry, a math entry, a scholar dossier (schema + source marks are enforced by gates).
- Improve the tool belt: every generator has a `--check`-style gate; run [`scripts/check_all.py`](scripts/check_all.py) before committing.
- Revive a skeleton zone by feeding it one real, sourced case — or propose freezing it in an issue.

Always ask: **"What is the simplest version of this that still explains what we observe?"**
