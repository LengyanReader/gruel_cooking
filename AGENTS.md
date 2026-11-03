# AGENTS.md — 数字人文

> Generated harness for: **reseArch_X 科研机会与学者评估**
> By `harness-factory` v1.5 on 2026-10-29. This file is the operating manual for the task.

## 中文速览

本文件是本次任务所需 harness 的操作说明。**任务特征**：horizon: long · verifiability: high · stakes: medium · grounding: deep · artifact: dataset · tool_surface: research · collaboration: solo。**启用模块**：M0, M1, M3, M4, M6。硬规则以 M0 为准；完成判定见 `.harness/gates.md`。选择理由见 `.harness/manifest.json`（可运行 `harness explain`）。

---

## Task · 任务

reseArch_X 科研机会与学者评估

- **Domain:** digital-humanities (数字人文) — Wiring core modules into machine-readable cultural heritage: encode, canonicalise, publish with provenance.
- **Goal:** 基于 harness-factory 纪律，深入开展 reseArch_X 的科研机会与学者评估工作，确保真相优先与来源可溯。

## Feature vector · 任务特征

| feature | value |
|---|---|
| horizon | long |
| verifiability | high |
| stakes | medium |
| grounding | deep |
| artifact | dataset |
| tool_surface | research |
| collaboration | solo |
| classification source | llm (L0 derivation) |

## Modules · 启用模块

| id | module | rule |
|---|---|---|
| M0 | core/01-meta-principles.md | Truth before throughput; source-grounding; verify before "done". |
| M1 | core/02-context-engineering.md | Minimal high-signal context; route-first, load-on-demand. |
| M3 | core/04-verification-and-gates.md | Define done before work; separate builder from critic. |
| M4 | core/05-provenance-and-integrity.md | Primary sources first; meaning-unit fidelity across languages. |
| M6 | core/07-tools-and-skills.md | Use expert instruments (DH standards: TEI, CIDOC-CRM). |

## Capabilities · 能力（需求→模块）

| capability | module | fired by |
|---|---|---|
| `baseline-discipline` | M0, M1, M3 | Any task at all (the floor) |
| `traceable-sources` | M4 | Claims/citations/Facts must be traceable |
| `ontology-as-contract` | M4 | Building or serving a knowledge base / graph |
| `entity-resolution` | M4 | Records that may (or may not) be the same entity |
| `expression-design` | M4 | Content is right but the form is wrong |

> 推导依据（读了哪些规则、匹配了哪个 capability）见 `.harness/PROVENANCE.md`。

## Evidence instrument · 证据仪器

M3.10 — Primary Source Pointer + Access Date (harness-factory reference/evidence-instruments.md)

> **M3.10 — match the instrument to the claim.** A formal claim is settled by a machine-checked
> derivation, a physical quantity by units + propagated uncertainty, an empirical claim by an effect
> size with an interval and a reliability estimate. Naming the instrument is naming what would refute
> the claim: if no instrument can be named, the claim is unverified. Full map: the harness-factory's
> `reference/evidence-instruments.md` (or `harness skill evidence-instruments`). · 先说清用什么仪器：
> 仪器说不出，就等于没有验证；这份合同在开工前定，不在收尾时补。

## Hard rules (M0) · 硬规则

- **Truth before throughput.** Never let a mechanism that "helps finish" invent content.
- **Source-grounding.** Every factual claim traces to a primary source (+ access date), or is marked `unverified`.
- **Verify before "done".** "Done" is a verified state with observed evidence, not a feeling.
- **Machines observe, humans decide substance.** Automation may observe, record, and rank — never fabricate or silently mutate substantive output.
- **Human gate.** Irreversible acts (delete / push / publish / spend / contact) require explicit human authorization.

> 真相优先；来源可溯；先验证再称完成；机器只观察、实质靠人决断；破坏性动作须人工确认。

## Standing reference · 常驻引用

> The user may open a conversation by pointing the assistant at a `harness_factory` directory (or an
> ancestor). That makes it the harness-capability reference for the **whole conversation**, active until
> the user says to stop. **Reference it, never dump it:** read `SKILL.md`, route via
> `reference/capability-router.md`, load only the matched row's files, and **declare each use** (which
> capability + which file). · 会话一开始提到 `harness_factory` 即成为**常驻能力参考**，除非用户明确说
> 「停止使用」；先路由、再按需加载，绝不整包灌入上下文。

```text
STANDING REFERENCE (until I revoke it) — treat C:\DA_Practice\research_foodie\research_foodie\harness_factory as my harness capability reference
for this whole conversation.
1. Read C:\DA_Practice\research_foodie\research_foodie\harness_factory/SKILL.md first; its load-index is authoritative.
2. Route: read C:\DA_Practice\research_foodie\research_foodie\harness_factory/reference/capability-router.md and load ONLY the files the matching row names.
3. If the ask is vague / under-aimed: run C:\DA_Practice\research_foodie\research_foodie\harness_factory/reference/requirement-refinement.md (R0-R5) and WAIT for my confirmation.
Standing behaviour: before each substantive answer, check whether a capability applies; when you use one, declare which capability + which file. Keep it active until I say "stop using harness_factory".
Never fabricate task substance (M0.4); truth/traceability outrank speed; irreversible acts need my explicit OK.
```

> **Pointer · 指针.** `.harness/pointer.json` records the **resolved** factory path and its **full
> loadable entry set** — `SKILL.md`, the router, refinement/flow, the instrument/methodology/outlet
> maps, cross-language, and the derivation rules (the same set as `harness skill`) — so a later
> session never has to be told the path again, and no capability reference is out of reach.
> Verify it with `harness doctor --project .`; a `null` path means the factory was not reachable when
> this harness was generated — then just ask the user for it. · 该文件记下工厂的**绝对路径**，新会话无需再被告知。

> **Path convention · 路径约定.** References like `SKILL.md`, `reference/*.md`, `core/*.md`, `domains/*`, and
> `harness …` point at the **harness-factory that generated this harness** — not this project. If it is not
> checked out locally, ask for its path; `harness skill <name>` prints the same content. · 本文件里的
> `SKILL.md`、`reference/*.md`、`core/*.md`、`domains/*` 指**生成本 harness 的 harness-factory**，不是本项目自身。

## Requirement refinement · 需求精炼

Before executing, run the six-step protocol in the harness-factory's `reference/requirement-refinement.md`
(or `harness skill requirement-refinement`):
**R0 restate → R1 elevate (propose stretch/moonshot) → R2 classify constraints (hard/soft/assumed) →
R3 offer MVP · Elevated · Exploratory readings → R4 confirm with the human → R5 converge**.
Do not begin work until the reading is explicitly confirmed; treat assumed constraints as open questions,
and assume an expert persona from the domain (persona changes method, never facts).

> 先复述、再拔高、分类约束、给候选版本、**得到确认**后再动手；假定约束要转成待确认问题；人格只改方法不改事实。

## Bidirectional capability flow · 双向能力流

- **Concretize (factory → this task):** maintain `.harness/capabilities.local.md` — record *how each fired
  capability is realised here*, its evidence, gaps, and whether it looks generalisable.
- **Keep the working set leased, not bought:** `.harness/working-set.json` is the set this task is *currently
  holding*. At a phase boundary, move what no longer changes a decision to `evicted` with a `reason` and a
  `reload_when`; never evict an always-on invariant and never drop silently (`harness check --dir` rejects both).
- **Distill (this task → factory):** at session end, propose generalisable patterns back via
  `harness learn` + `harness evolve` (writes only to `updates/`, gitignored). **Never edit the factory
  catalogue from here**; a human approves. See the harness-factory's `reference/capability-flow.md`
  (or `harness skill capability-flow`).

> 具体化的留在本任务（`.harness/capabilities.local.md`）；通用化的只以**提案**回流，人类把关，绝不自动合并。
> 工作集是租的不是买的：换阶段就把不再影响决策的能力退回索引（`.harness/working-set.json` 记理由与重载条件），硬不变式不退、不许静默丢弃。

## Workflow · 工作流

1.  Requirement Refinement (R0-R5)
2.  Harness Initialization
3.  Research Audit (scholars & opportunities)
4.  MVP Dialogue Generation
5.  Verification & Gates

## Gates · 完成门禁

See `.harness/gates.md`. Gate strictness: **strict**. Do not claim "done" without observed evidence.

## Governance · 变更治理

- Single source of truth; reviewable diffs; Conventional Commits (short subject).
- Commit locally is routine; **never push/publish without an explicit human request**.

## Session protocol · 会话协议

- Plan first: update `tasks/PLAN.md`; log results in `tasks/PROGRESS.md`.
- End every session with a handoff: goal · done · blocked · next · sources.

## Files in this harness · 生成的文件

- AGENTS.md
- tasks/PLAN.md
- tasks/PROGRESS.md
- .harness/pointer.json
- .harness/capabilities.local.md
- .harness/PROVENANCE.md

## Self-check · 自检

```
PYTHONPATH=C:\DA_Practice\research_foodie\research_foodie\harness_factory/src python -m harness_factory check --dir .
```
