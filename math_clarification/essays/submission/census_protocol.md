# Census protocol — *Machine-graded mathematics 2024–2026: enumeration and dispute coding*

> **Status 状态**: Design document for the study that Section 11.5 of [`../ai_and_math.md`](../ai_and_math.md) calls for. **AI-drafted, unreviewed** (harness §I.6). Contains no results — only the protocol by which results would be gathered. Nothing here was executed; hit-counts marked `⟨pilot⟩` must be measured before the protocol is frozen.
> **Prerequisite 前置**: register this document (timestamped, public) **before** any leaderboard snapshot after the registration date is coded — the parent paper's own rule (its §11.8, prediction P-series). Suggested venues: OSF registration, or an arXiv-annex methods note, or a public repo commit whose date is independently attestable.
> **Harness mapping 家规对应**: 来源可信度仪式 (harness §I.2) applies to every coded cell; 本域 R-B/R-C (`math_clarification/docs/workflows.md`) apply to every source row; MC-W2 applies to the arithmetic in §6.

---

## 1 · Objective and primary endpoint

**Objective.** Replace the publicity-selected corpus of eleven events (parent paper §11.4) with a census of *attempted certifications* in mathematics by AI systems, 2024-01-01 through the registration-plus-collection window, and re-test the regime–dispute association on it.

**Primary endpoint (exactly one).** The difference in *recorded-public-dispute rate* between:
- stratum **M** — events whose certification verdict is executed by a mechanical procedure (machine-graded, per §11.2 of the parent paper, decision rule applied unchanged); and
- stratum **C** — events whose acceptance depends on an unfixed body of people (community-graded).

Hybrid-graded events are a pre-declared third stratum, never pooled post hoc with either. Test: Fisher exact (M vs C only), one-sided, α = 0.025, plus the pre-declared trend test over M < H < C. No other endpoint can falsify the paper's ordering.

**Predictions inherited from §11.5, restated in census terms.**
- **P1** dispute rate in stratum M = 0; any single documented false positive from a machine grader falsifies the parent paper's mechanism claim. Falsification condition fixed now, not after counting.
- **P2** disputes arise in stratum C only where the producer disclosed before independent grading.
- **P3** in stratum C events where the grader was designated by a body the producer did not select, dispute rate = 0.

## 2 · Unit of enumeration and inclusion rule

**Unit**: one *attempted certification event* = a public claim that a mathematical result holds, attached to an identifiable producer, at an identifiable date, which either (i) was submitted to, or (ii) publicly declared itself subject to, a gradeable verdict (formal check, official grading, benchmark run, or community admissibility claim).

**Inclusion**: every event found in any source of §3 that passes the unit definition, **regardless of whether it attracted attention**. This is the point of the census: the current corpus is selected by publicity, and publicity is manufactured by dispute — the circularity the parent paper concedes at its §3.5 and §11.5.

**Exclusions (recorded with counts, PRISMA-style, never silently)**: non-mathematical claims by the same producers; restatements and press echoes of an already-included event (the event stays once, the echo is logged as a duplicate); events whose producer is unidentifiable; pre-2024 events (out of window).

## 3 · Sources and exact queries

Three sampling frames, run in parallel; every run logged as §7 requires.

### 3.1 Frame A — arXiv (formalized-mathematics output)

API base: `http://export.arxiv.org/api/query` (respect its rate policy: 3 s between requests, `max_results` ≤ 2000 with paging).

Query families (submit-term window 2024-01-01 → collection date):

| # | Query (arXiv API syntax) | Captures |
|---|---|---|
| A1 | `(cat:cs.LO OR cat:math.LO) AND (abs:"Lean" OR abs:"mathlib")` | Lean-formalized results |
| A2 | `(cat:cs.LO OR cat:math.LO) AND (abs:"Coq" OR abs:"Isabelle" OR abs:"rocq")` | other proof assistants |
| A3 | `abs:"formalized proof" OR abs:"machine-checked proof" OR abs:"verified conjecture"` (cross-list) | phrasing variants |
| A4 | `abs:"counterexample" AND (abs:"computer search" OR abs:"sat solver" OR abs:"SMT")` | mechanically-disproved claims without assistants |

Pilot each query, record total hits `⟨pilot⟩`, then manually screen titles/abstracts against the unit definition. Benchmarked-model papers that *report* scores (no new mathematical result) are excluded as not attempted certifications — but the excluded count is logged.

### 3.2 Frame B — mathlib merge records (verdicts executed at the kernel)

- Repo: `leanprover-community/mathlib4`. GitHub REST: `search/issues?q=repo:leanprover-community/mathlib4+is:pr+is:merged+merged:2024-01-01..YYYY-MM-DD&per_page=100` (page until exhausted; note the search API caps at 1000 results — if hit, switch to date-bisected queries, which is exact).
- **Bulk alternative (preferred, cheaper)**: clone the repo and enumerate merge commits locally (`git log --merges --since=2024-01-01 --pretty=...`); every merge is a kernel-graded event by construction.
- **Denominator correction**: a merge certifies a *formalization*, most of which re-expresses known mathematics. The census stratum M must count only merges that formalize a **new** mathematical result. Screening rule: from the PR title/body, does it name a result not previously in the literature (new bound, new example, disproof)? If unclear, code `novelty=unresolved` and keep out of the primary analysis; the count of unresolved is reported. This screen is the protocol's weakest link and gets its own §8 reliability check.
- Companion frames, same treatment: `leanprover-community/batteries`, coq-community, Isabelle/AFP (`isabelle/afp` merge/HOL-entry records).

### 3.3 Frame C — published leaderboards and challenge results

Snapshot **weekly**, whatever is publicly posted, with the snapshot date in every cell (leaderboards are revised; an undated scrape is not evidence — parent paper §11.6):

| Board | URL family | Event definition |
|---|---|---|
| FrontierMath (incl. Erdős set) | epoch.ai/frontiermath* | each published model-run table row |
| miniF2F / ProofNet / Putnam-AXIOM leaderboards | respective project pages | each listed system–date score |
| IMO shortlist results of AI systems | IMO official pages + organizing-body reports | each officially graded system-year |
| First Proof / similar expert challenges | host pages as archived | each published outcome |
| Terence Tao's blog / wiki of AI-and-mathematics results (if enumerated) | as it exists | each listed item, verified to its own primary |

An event enters the census when a *result claim* is graded on such a board; a bare model score on a benchmark of textbook exercises is stratum M data for P1 (disputes about it), not a new certification event, unless the board itself declares a mathematical novelty.

### 3.4 Supplementary sweep (negative cases and disputes, PRISMA-auditable)

Frame C2 — dispute search, run **independent of** frames A–C so that silence is sought, not assumed: for each included event, query `"retraction OR disputed OR criticized OR controversy" AND <event keywords>` across news archives and mathoverflow/math.stackexchange; record *every* query with its date and result count, including the queries that return nothing (§11.6 of the parent paper — "not found" is only evidence if the search is on the record).

## 4 · Record schema (one row per event; CSV as single source)

```
event_id, date, producer, result_one_line, math_area, novelty(new/known/unresolved),
frame(A/B/C + query id), regime(M/H/C + rule clause 11.2a/b/c + tiebreaker a/b/c if used),
grader_identity, grader_selected_by(producer/third-party/n.a.),
q1..q5(+/-/±/n.r. per coding cards 11.3), dispute(0/1), dispute_type(framing/subset/attribution/admissibility/none),
dispute_evidence(url + access date), citation_tier(一手/权威/共识解读/存疑 per R-B),
marker(✓/◐/○/✗ per harness §I.2), coder1, coder2, divergence_note
```

## 5 · Coding procedure

1. Regime and Q1–Q5 are coded with the parent paper's instruments **unchanged**: ordered decision rule §11.2 (clauses fire in order; tie-breakers (a)(b)(c) as written), coding cards §11.3. Any proposed amendment to a card is registered **before** use and applied to the whole corpus, never event by event.
2. Dispute = 1 iff a public, attributable objection concerning framing, subset, attribution, or admissibility is documented against the event's own record; technical limitations stated by the producer are not disputes.
3. Two coders code **all** rows independently (not a subsample — the corpus is bounded). Resolve by discussion; record every changed cell in `divergence_note`.

## 6 · Analysis plan and power

- Primary: one-sided Fisher exact, stratum M vs stratum C, dispute as outcome. α = 0.025. Report exact CI for both rates.
- Trend: Cochran–Armitage over M < H < C, secondary and pre-declared; it cannot rescue a failed primary.
- Descriptive companions (no inferential status): Q1–Q5 satisfaction profiles by stratum; dispute-type distribution; Frame-B unresolved-novelty count.

Power (computed 2026-09-25 by exact enumeration, not by normal approximation: the two strata's dispute counts are taken as independent binomials of size n, each table's one-sided Fisher p-value from the hypergeometric conditional distribution, and n raised until the rejection probability reaches 0.80 at α = 0.025 one-sided. The generating script is kept beside this protocol as [`checks/power_fisher.py`](checks/power_fisher.py) — `python checks/power_fisher.py` reproduces the table below and the table is its verbatim output; re-run at registration, since MC-W2/R-D requires that arithmetic a machine can check be machine-checked).

| dispute rate in C | dispute rate in M | n per stratum | achieved power |
|---|---|---|---|
| 0.60 | 0.05 | 13 | 0.84 |
| 0.60 | 0.00 | 10 | 0.83 |
| 0.40 | 0.05 | 24 | 0.82 |
| 0.40 | 0.00 | 16 | 0.83 |
| 0.30 | 0.05 | 39 | 0.81 |
| 0.30 | 0.00 | 21 | 0.80 |
| 0.20 | 0.05 | 82 | 0.81 |
| 0.20 | 0.00 | 39 | 0.82 |
| 0.15 | 0.00 | 52 | 0.81 |
| 0.10 | 0.00 | 78 | 0.80 |

Reading. The design is generous to the study because P1 predicts a rate of *zero* in stratum M, and a zero-rate comparison needs few events: if community-graded dispute runs near the publicity-corpus rate (~0.6), a dozen events per stratum already carry 80% power. The requirement hardens steeply as the community rate falls — 0.20 with a machine rate of 0.05 needs 82 per stratum, and 0.10 needs 78 even if the machine rate is exactly zero. Two consequences are fixed now, before collection: the Frame A/B volume pilots `⟨pilot⟩` must be run first, and if their projected event counts fall below the row matching the plausible community rate, the protocol is amended **before** registration (widening the window, or dropping to a trend test with the primary as secondary), never after. Note also that a normal-approximation formula gives noticeably smaller n at these rates and was discarded in favour of the exact enumeration; any reviewer recomputing sample size with `pwr.2p2n` or `zt_ind_solve_power` will get a different, slightly optimistic number.

## 7 · Traceability requirements (what makes this a census rather than an anecdote)

- Every query: syntax, date, time, total hits, screened-in, screened-out with reason codes → machine-readable log (`queries.csv`).
- Every included event: primary-source URL + access date; secondary reporting only when labeled as such (R-C: no stable link → full bibliographic citation and an explicit statement of the fact).
- A PRISMA-style flow count: identified → screened → included, per frame; excluded-with-reason lists published in full.
- All snapshots archived (web.archive.org submission per URL on entry) before analysis.

## 8 · Reliability and preregistration gates

- Cohen's κ per column (regime, each Q, dispute) on the doubly-coded full corpus; κ ≥ 0.6 required for any column to enter the primary analysis; columns below threshold are reported descriptively with the divergence list. The novelty screen (§3.2) gets its own κ.
- Registration package = this protocol + §11.2–11.3 of the parent paper as appendix + analysis code stub (data-generating plan included), deposited with timestamp before Frame C's first post-registration snapshot is inspected.
- Falsification report obligation: if P1 fails (a machine-graded dispute is found), the finding is published with the same prominence as confirmation — stated here so it cannot become a postscript.

## 9 · Deliverables of the census study

1. `census.csv` (schema §4) + `queries.csv` (§7) in this folder, single source.
2. Flow diagram + Fig. 2 of the parent paper redrawn from the census (staircase × dispute density, one point per event, §11 placement rule).
3. Results section drafted as an increment to parent §11.5 — the eleven-event table is **superseded, not amended**, and retains its rows marked as the pilot corpus.
