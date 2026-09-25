# Preregistration draft — Machine-graded mathematics 2024–2026 (census)

> **Status 状态**: Fill-in-and-paste registration text. **AI-drafted, unreviewed** (harness §I.6). This is a *submission-ready wrapper* around [`census_protocol.md`](census_protocol.md); it adds no design, only the fields a registry (OSF / asPredicted / arXiv-annex) asks for. Angle-bracket items `⟨author⟩` must be completed by a human before deposit. **Do not deposit after inspecting any post-registration leaderboard snapshot** — the whole value of the registration is that its timestamp precedes coding (parent §11.8; census_protocol §8).

---

## 1 · Study title
Machine-graded mathematics 2024–2026: a census of attempted AI certifications and their dispute outcomes.

## 2 · Registration type
Confirmatory analysis plan on a to-be-collected census; observational, no intervention, no human-subjects data. ⟨author: choose OSF / asPredicted / dated public repo commit⟩.

## 3 · Research question
Does the location of public controversy over AI-produced mathematics track the **certification regime** (machine-graded / hybrid-graded / community-graded) rather than the difficulty or prestige of the result?

## 4 · Hypotheses (pre-declared, from census_protocol §1)
- **P1** — Dispute rate in the machine-graded stratum (M) is 0. A single documented false positive from a machine grader **falsifies** the mechanism claim. ⟨fixed now, not after counting⟩.
- **P2** — In the community-graded stratum (C), disputes arise only where the producer disclosed before independent grading.
- **P3** — In C events where the grader was designated by a body the producer did **not** select, dispute rate is 0.

## 5 · Primary endpoint (exactly one)
Difference in recorded-public-dispute rate between stratum M and stratum C. Hybrid (H) is a third stratum, never pooled post hoc. Test: one-sided Fisher exact, M vs C, α = 0.025. Pre-declared secondary trend test: Cochran–Armitage over M < H < C (cannot rescue a failed primary).

## 6 · Unit, inclusion, exclusion
One *attempted certification event* = a public claim that a mathematical result holds, attached to an identifiable producer and date, submitted to or declaring itself subject to a gradeable verdict. Include every event passing the definition **regardless of attention received**. Exclusions logged PRISMA-style with counts (non-mathematical claims; duplicate echoes; unidentifiable producer; out-of-window). Full rule: census_protocol §2.

## 7 · Sampling frames and stopping
Frame A arXiv (queries A1–A4), Frame B mathlib/Coq/Isabelle merge records, Frame C weekly leaderboard snapshots, plus Frame C2 independent dispute sweep. Collection window 2024-01-01 → ⟨author: planned collection end date⟩. Exact query syntax, rate policy, and paging: census_protocol §3.

## 8 · Sample size / power (pre-committed)
Design powered at 80%, α = 0.025 one-sided by **exact enumeration** (not normal approximation): 13/stratum if C-rate ≈ 0.60 & M-rate ≈ 0.05, hardening to 82/stratum if C-rate ≈ 0.20 & M-rate ≈ 0.05. Reproducible via `python checks/power_fisher.py`. ⟨author: record the frame-volume pilot counts ⟨pilot⟩ BEFORE freezing; if projected counts fall under the row matching the plausible community rate, amend the protocol here, not after collection⟩.

## 9 · Coding procedure
Regime and Q1–Q5 coded with the parent paper's instruments **unchanged** (decision rule §11.2, coding cards §11.3); any card amendment is registered before use and applied corpus-wide. Dispute = 1 iff a public, attributable objection on framing/subset/attribution/admissibility is documented against the event's own record; producer-stated limitations are not disputes. Full rule: census_protocol §5.

## 10 · Inter-coder reliability gate
Two coders code **all** rows independently. Per-column unweighted Cohen's κ (regime, Q1–Q5, dispute, and the §3.2 novelty screen); κ ≥ 0.6 required to enter the primary analysis, below-threshold columns reported descriptively with the divergence list. Reproducible via `python checks/kappa_csv.py <paired_codings.csv>` (see `census_coder2_packet.md`).

## 11 · Analysis plan
Primary one-sided Fisher exact (M vs C) with exact CIs on both rates; pre-declared Cochran–Armitage trend; descriptive-only Q1–Q5 profiles, dispute-type distribution, Frame-B unresolved-novelty count. No other endpoint can falsify the ordering. Full rule: census_protocol §6.

## 12 · Data & code availability on publication
`census.csv` + `queries.csv` as single source; every query logged with date/hits/screen counts; every event with primary-source URL + access date + archive snapshot; PRISMA flow published. Excluded-with-reason lists in full. Full rule: census_protocol §7.

## 13 · Falsification reporting obligation
If P1 fails, the finding is published with the same prominence as a confirmation. Stated here so it cannot become a postscript (census_protocol §8).

## 14 · Deviation log (post-registration)
| Date | Field | Change | Why it was pre-registration-safe |
|---|---|---|---|
| ⟨author⟩ | | | amendments only with a justified, timestamped entry; never after seeing the coded outcome |

---

*Fields to complete before deposit: registry venue (§2), collection end date (§7), pilot counts (§8), author names/ORCID, funder, conflicts. The design text itself is fixed by `census_protocol.md`; this wrapper only exposes it to a registry form.*
