# Red-team panel — an adversarial reviewer test of *"Mathematics is not in crisis: its consensus is"*

> **Status 状态**: Working derivative of [`../ai_and_math.md`](../ai_and_math.md) and companion to [`comment_draft.md`](comment_draft.md). **AI-drafted, unreviewed** (harness §I.6). This is a red-team of the *argument*, not a submission artifact: its output is meant to feed §A revision, never the reference list.
>
> **Guardrail (harness §E; the "trap" rule)**: each lens below is a *documented position reconstructed in the parent paper*, used only as an adversarial test. **Nothing here may be quoted as a named scholar's actual stance on AI-and-mathematics in 2024–2026.** Every lens states what that work, as the parent reads it, logically puts under pressure — not what its author "would say." All factual claims remain the parent's; no new external facts are introduced in this file.
>
> **Parent-reference key**: [7] Lean kernel ("the kernel checks proof terms; meaning is a separate task") · [9] Appel & Haken four-colour · [10] Tymoczko fallibilism · [11] DeMillo, Lipton & Perlis symmetry thesis · [14] Gowers two cultures · [15][16] Avigad on understanding/method · [17] Hales/Flyspeck · [27] Merton Matthew effect · [28] Kuhn normal/revolutionary · [32] Tao on the implicit value framework · parent §3 enumerates five rival explanations (capability gradient, announcement incentive, certification regime, institutional latency, resource concentration).

---

## How to read a verdict

| Verdict | Meaning |
|---|---|
| **survives** | the draft already answers the objection on the page |
| **nick** | answered in substance but a careful referee can press once; a clause closes it |
| **exposed** | a rejection-grade paragraph could be written from this objection today; needs a real edit |

---

## Lens 1 — The Matthew-effect sociologist (parent [27]; §2, §10)

**Position (as the parent reads it).** Recognition in science attaches to prestige-bearers and their sites, not to propositional content alone — which is exactly why a 2026 authorship quarrel is a *normal-sociology* event, not an anomaly.

**Strongest objection.** The draft's independent variable, *certification regime*, is confounded with *prestige of the grader*. The unit-distance disproof drew no scandal not because it was cleanly community-graded but because nine named mathematicians *including a Fields medallist* absorbed it. The draft cites Merton itself, so it cannot plead ignorance of the confound. Is "regime" doing explanatory work, or is it a redecription of "the famous signed off"?

**Where the draft parries.** It concedes publicity-selection and that the Fisher test is descriptive only (*P* ≈ 0.24).

**Residual exposure.** In the eleven-event table, regime and grader-prestige are collinear — high-prestige verifiers cluster in the community-graded rows that *did not* scandal, and the scandal rows are precisely those graded by a *self*-selected laboratory. The mechanism the paper loves (prestige) is silently load-bearing in the very evidence for the regime claim.

**Cheapest fix.** One clause acknowledging that regime and prestige are not separable in a publicity-selected corpus, and that the census ( [`census_protocol.md`](census_protocol.md) §6) is where they come apart — a new bounded result graded by unknown-but-independent verifiers is the discriminating case. → **exposed** (this is the paragraph Reviewer 2 writes).

## Lens 2 — The symmetry-breaker (DeMillo–Lipton–Perlis [11]; Tymoczko [10])

**Position (as the parent reads it).** Mathematics has always certified theorems *and* programs by the same social machinery; a machine-checked proof is therefore not the scandal people took it to be.

**Strongest objection.** The draft's machine-graded stratum breaks the 1979 symmetry by declaring a kernel verdict non-social. The Edinburgh-school answer: trusting the kernel, the compiler, and — decisively — *the formalized statement* is itself social knowledge. The draft's own citation [7] concedes "meaning is a separate task." So the mechanical/communal line is drawn at the *derivation*, while the scandals all live in the *statement*, which is always community-graded.

**Where the draft parries.** Q5 (found/made), the signifier/signified §, and the Navier–Stokes row already place the dispute on admissibility, not derivation.

**Residual exposure.** The §A definition says a machine-graded verdict is one "no human score can alter" — the symmetry-breaker's single best line is that a mis-stated spec *is* a human score that alters everything.

**Cheapest fix.** Qualify the machine-graded definition with "given agreement on what sentence is being checked," turning the objection into a distinction the draft already owns. → **nick**.

## Lens 3 — The fallibilist about the kernel (parent [7]; Tymoczko [10]; Avigad [15][16])

**Position.** Formalization does not merely confirm a theorem; it displaces what "understanding" and "method" denote, and neither is exhausted by the check.

**Strongest objection.** "Where grading is mechanical, the record contains no scandals" reads as an incorruptibility claim about the kernel. Fallibilism says the *certainty* is located in the grammar and dissolves at the moment you ask whether the grammar says the thing you meant. The draft's P1 ("machine-graded dispute rate = 0") is therefore not an empirical prediction about graders but a *tautology* about where disputes are permitted to be registered: a formal-check dispute is filed against the *statement*, and statements were community-graded all along.

**Where the draft parries.** It says verification "certifies grammar, never the object," and that the crisis is about authority, not truth — i.e. it agrees with the objection.

**Residual exposure.** If L3 is right, the MG/CG axis is a distinction with no difference at the level of *what the profession must decide*. The draft must show the axis predicts something the tautology does not.

**Cheapest fix.** Reframe P1 from "no disputes" to "disputes, when they occur about a machine-graded event, are re-filed against the statement and thereby move the event into the community-graded stratum" — which makes the taxonomy dynamic rather than a classification artifact, and converts L3 from a refutation into a feature. → **exposed** (needs the reframe, not just a clause).

## Lens 4 — The cost-of-formalization practitioner (Hales / Flyspeck [17])

**Position (as the parent reads it).** A refereeing of the Kepler proof *stopped at partial acceptance because no referee team could finish checking it*; only re-verification in HOL Light and Isabelle, published as a formally-verified result, certified community-scale proof — *and showed its cost*.

**Strongest objection.** From the opposite direction: the draft is too tender to community grading ("how mathematics has always decided its hardest cases, and still decides the ones that matter most"). Hales's record says community grading *failed* and had to be replaced, at enormous labor. The draft's remedy — three *cheap* institutional changes — is insultingly modest against a problem whose known solution consumed years of the strongest formalizers alive.

**Where the draft parries.** The staircase itself, and the parent's line that verification is the lowest-paid, most-critical rung.

**Residual exposure.** Calling the changes "cheap" invites L4 to answer that cheapness is the bug: the profession will not pay for the meaning-layer, so a disclosure norm will not move the equilibrium.

**Cheapest fix.** One sentence conceding that the three changes are necessary-not-sufficient and that Flyspeck prices the labor they presuppose, tying to the parent's call to fund the verification rung. → **nick**.

## Lens 5 — The capability-gradient sceptic (Gowers [14]; Kuhn [28]; parent §3)

**Position.** Mathematics splits into theory-builders and problem-solvers; and science separates normal problem-solving from revolutionary re-framing. The parent lists "capability gradient" as one of five *rival* explanations of the dispute pattern.

**Strongest objection.** The MG/HG/CG staircase may just be the two-cultures / difficulty divide in disguise: Olympiad and finite-combinatorics results are *easy to formalize* and land in machine-graded rows precisely because they are tractable, while deep structural claims resist formalization and stay community-graded. If so, "regime," not "difficulty," is the thing that failed to vary independently — the reverse of the paper's claim.

**Where the draft parries.** The explicit rejection of the syllogism's minor premise ("mathematics is a game" true only of the formalized fragment), and the border-vs-frontier criterion.

**Residual exposure.** Neither is decisive *within the eleven events*; the draft argues the point at the level of the sample it admits is publicity-selected.

**Cheapest fix.** Name capability-gradient as the specific rival the census is built to exclude (Frame B's novelty screen, the trend test over M<H<C), and say plainly that the Comment cannot exclude it and the study can. → **nick** (already nearly handled; a clause seals it).

---

## Synthesis — what actually bites a Nature referee

1. **Lens 1 (prestige confound)** and **Lens 3 (kernel-tautology)** are rejection-grade: each can carry a full referee paragraph, and each strikes the *independent variable* the Comment stands on. They share a root — regime and prestige/tautology are not separable in an eleven-event, publicity-selected table.
2. **Lens 5 (capability gradient)** is what a careful referee raises *because the parent itself named it a rival* — the draft should not be surprised by its own §3.
3. **Lens 2 and 4** are nicks, not breaks; the draft's existing signifier/signified and lowest-paid-rung material already parry most of them.
4. Net: the argument survives its own red-team **only if** it (i) stops treating "machine-graded ⇒ no dispute" as flat and re-frames it as a *statement-vs-derivation* rule (L3), and (ii) concedes the prestige/selection confound is real *here* and is what the census exists to break (L1, L5). Both are wording-level, both trace to the parent.

## Concrete §A edits — status (author approved the pass on 2026-09-25)

| # | Lens | Proposed edit to §A | Type | Status |
|---|---|---|---|---|
| e1 | L3 | In the machine-graded definition and the "no scandals" line: qualify with "given agreement on the statement," and add the move that a dispute about a machine-graded event re-files against its statement, relocating it to the community stratum. | accuracy / pre-empt | **APPLIED** (definition qualified + re-filing move added) |
| e2 | L1 | One sentence conceding regime and grader-prestige are collinear in a publicity-selected corpus, and pointing to the census trend test as the discriminator. | honesty / pre-empt | **APPLIED** (candidacy paragraph) |
| e3 | L5 | Name capability-gradient as the rival the census is designed to exclude; state the Comment cannot, the study can. | scope control | **APPLIED** (candidacy paragraph) |
| e4 | L2/L4 | "No human score can alter the outcome" → "no human score can *overrule* the derivation" (keeps the claim, drops the incorruptibility reading); "cheap" → "necessary but not sufficient." | calibration | **APPLIED** (both) |

e1–e4 were applied on the author's instruction; each is wording only and still backed by the parent, adding no facts (e1 changes P1's shape from a flat "no disputes" to a statement-vs-derivation rule, so the taxonomy is dynamic rather than a classification artifact). A separate citation-integrity check (now `checks/refcheck.py`) found reference 23 uncited in the body and it was fixed by citing the Harvard First Proof case; a live-web re-verification then corrected that case's count (the setters confirmed two, not the parent's "≥6" from OpenAI's claim). The pass took the body from ~1,510 to ~1,670 words (recounted after the live-web correction), still inside the Comment band.

## Boundaries

- Inherits every parent limitation: single-coder coding, publicity-selected corpus, no inter-coder statistic.
- The five lenses are **not** a literature review and add no sources; where they cite a number or event it is the parent's ([7],[9],[10],[11],[14],[15],[16],[17],[27],[28],[32] and §3/§10).
- A lens that "exposes" the draft is a signal the *full* paper (Research Article path) must address in its §7/§8, not that the Comment is wrong — the Comment can pre-empt in three sentences what the Article must prove in a section.
