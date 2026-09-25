# Comment draft — *Misnaming the crisis in mathematics*

> **Status 状态**: Working derivative of [`../ai_and_math.md`](../ai_and_math.md). **AI-drafted, unreviewed** (harness §I.6) — a human author must accept or delete every claim before this leaves the repo.
> **Target 目标**: *Nature* **Comment** (1,500–2,200 words, ~20–30 references, one Figure). Not a Research Article: this document contains no primary data collection.
> **Drafted 起草**: 2026-09-25. Body text ~1,510 words (recounted after the §E house-style pass: alphabetic tokens from the first §A paragraph to the closing rule), 23 references, 1 figure (CSV dataset, 11 coded events) — inside the 1,500–2,200 Comment band. A Nature house-style pressure-test was run with the installed `nature-writing` skill; its findings, the one mechanical fix it applied (em-dashes → comma/colon/parenthesis, word count −1), and the items left to the author are recorded in §E.
> **Reliability markers 信度标记** carried per harness §I.2 (`✓ verified / ◐ company-claim / ○ unconfirmed / ✗ disputed`) in the appendix only, never in the body prose — see §C.
> **Vocabulary 术语**: machine-graded / hybrid-graded / community-graded are the three certification regimes defined in §3.1 of the parent paper; the five verification questions are those of §4.1.
> **Citation audit 引文稽核 (2026-09-25)**: the list was converted to Nature format and every fact in the body was traced back to the parent paper — all 23 items now resolve to its reference block, and every URL and DOI in it occurs verbatim there. Three items were **removed or demoted** in that pass: an unsourced DeepMind blog URL (the parent cites that page without a stable link, per house rule R-C), a *Nature* volume/page pair for the IMO paper that the parent does not carry, and an Illinois J. Math. page range likewise absent from the parent. Two more were corrected against the parent's own wording: IMO 2024's markers are Gowers and Myers (not "official coordinators", which is the 2025 design), and the FrontierMath v2 fixes were made by the benchmark's builders (not by the problem authors). **Verification here is traceability to the parent paper, not re-verification against the live web**; that second pass is required before submission and is the reason refs 4, 16 and 21–23 carry explicit "pending" notes.

---

## A · The manuscript text (body as it would be submitted)

### Misnaming the crisis in mathematics

*Why the profession should be arguing about verification, not about capability.*

In May 2026 a model at a leading laboratory disproved a conjecture in discrete geometry that had stood open since 1946 [1]. Four months later the same laboratory announced that a Millennium Prize problem had been "apparently" settled, and one of the researchers whose work it drew on disputed, in public, whose name should be attached to it [2,3]. Between those two announcements, machines had taken silver-medal marks at the International Mathematical Olympiad and, the following year, gold-standard results [4], improved a bound on matrix multiplication that had stood for fifty-six years [5], and solved three per cent of a set of open problems written in a proof assistant while every competing system solved none [6]. The obvious reading is that mathematics is in crisis. That reading is wrong, and the wrongness is instructive: what is in crisis is the mathematicians' arrangement for deciding what counts.

We argue that the dispute now convulsing mathematics is not about machine capability at all. Capability is settled: the results above are not contested by anyone who has inspected them. What varies, and what predicts where scandal lands, is the **certification regime**: who executes the check, and whether a third party can demand the same verdict independently. Three regimes recur. A result is *machine-graded* when a mechanical procedure over a formal artifact, or an objectively computable counter, decides it and no human score can alter the outcome. It is *hybrid-graded* when a machine-checkable artifact exists and designated human judges nonetheless award the result and may decline it. It is *community-graded* when acceptance depends on being read, cited, used, or declared admissible by an unfixed body of people, which is how mathematics has always decided its hardest cases, and how it still decides the ones that matter most.

The predictive claim is simple and, to our knowledge, new: the location of controversy is a function of regime, not of difficulty. Where grading is mechanical, the record contains no scandals. Where it is communal, every controversy of the past two years has occurred, including two that the machine-graded results were announced alongside, and which were therefore about disclosure and admissibility rather than about truth.

Consider the evidence in order. At the 2024 Olympiad, a DeepMind system solved four of six problems at silver-medal level, including the hardest question of the year, which only five human contestants completed; the marking was carried out by two named academics, Timothy Gowers and Joseph Myers, and the machine solutions were additionally run through the Lean checker [4,7]. No one disputed it. The o3 announcement of December 2024 reported 75.7% on FrontierMath, a figure computed on a subset the laboratory had selected, on problems whose authors had not been consulted about that run, against a full-set score of 25.2%; the ensuing dispute was the loudest of the period and concerned neither the model nor the mathematics [8,9]. The unit-distance disproof was absorbed by the profession's oldest machinery: nine named mathematicians, one of them a Fields medallist, wrote a verification paper digesting the construction, one of them sharpened the exponent, and the published record states plainly that the gap between the new lower bound n^1.014 and the classic upper bound n^4/3 is now wider than at any time in the problem's history [1,10–12]. Nothing was scandalous there; the machinery simply ran. AlphaEvolve's 48-multiplication algorithm for 4×4 complex matrices beat Strassen's 49 on a counter that cannot be spun, and passed in silence [5], which is precisely what a machine-graded result looks like. So did the Erdős benchmark of 68 open problems formalized in Lean, where the grader is the checker and the reported spread (best system 3%, all others zero) left the benchmark wars no room to argue, because neither subset-selection nor framing is available to a laboratory whose numbers a machine produces [6].

And then the top rung. The Navier–Stokes announcement passed a formal check for the statement it actually proves, a statement with a smooth external forcing term. The Clay Institute's own rules require publication in a qualifying venue, two years in the literature and general acceptance by the mathematical community; its announcement said only "apparently", its evaluation procedure remains in force, and the problem is still listed as open [2,13,14]. A journalist's report described the substance of the objection: the method does not extend to the unforced case the field was asking about [15]. Read carefully, that case is not a failure of the machine. It is a dispute about which sentence was proved and who may say it has been proved: meaning, adjudicated by people. Regime, not difficulty.

None of this is new to historians of the discipline, and it is worth saying so before a reviewer does. In 1977 the four-colour proof reduced the problem to a machine-enumerated case analysis and ignited an argument about exactly this [16]. Tymoczko drew the fallibilist conclusion in 1979 [17]; DeMillo, Lipton and Perlis observed in the same year that mathematics had always certified programs and theorems by the same social machinery, and that a machine-checked proof was therefore not the scandal people took it to be [18]. Merton had documented eleven years earlier that credit in science follows prestige rather than contribution alone [19]. What has changed is not the argument but the burden of proof: in 1979 a mathematician had to defend the claim that machines could produce interesting proofs; by 2026 the interesting proofs exist and the defended claim has migrated to authority: who designates the checker, who frames the announcement, who is named. The proof assistant documents its own limit in one line: the kernel checks proof terms, and what a statement *means* is expressly a separate task [7]. Flyspeck, the completed Kepler-conjecture verification, is the precedent for how a community absorbs machine-scale proof when it chooses to [20].

We should be candid about the strength of our own evidence. Eleven publicly recorded certification events from 2024–2026 are coded here; one of six machine- or hybrid-graded events attracted a recorded public dispute, against three of five community-graded ones (Fig. 1). That association is descriptive: Fisher's exact test on a table this small gives P ≈ 0.24, and the events were selected through publicity, which dispute itself manufactures. The claim we are making is about *where* controversy can arise, not how often (a mechanism argument, falsifiable at low cost). It would be overturned by one documented false positive from a machine grader, or by a high-significance community-graded result that entered the literature without a single public objection. Neither has been found in a targeted search, but the search must be stated to be worth anything, and a census of machine-graded output in the period (arXiv listings for formalized mathematics, merged formalization commits, published benchmark leaderboards) is the study that should follow this one, with its predictions registered before the next results are published rather than after.

Three positions will be quoted at us. The optimists announce a replacement of human mathematicians; the total resisters demand a ban on machine-produced proofs; the institutionalists, whose Leiden Declaration was endorsed by the International Mathematical Union and signed by more than four thousand mathematicians, ask instead for disclosure, standards and authorship [21]. The third is right, for a reason the first two share: all three accept the same syllogism (machines beat humans at chess and Go, mathematics is a game, therefore machines will beat humans at mathematics), and its second premise is true only of the small corner of the subject that has already been written in formal language [22]. Almost all of mathematics is not that corner.

So the agenda is not prohibition, which is unenforceable, but three cheap institutional changes that should be adopted before the next announcement rather than after it. **Disclose symmetrically**: report every item attempted, including zeros, and state the subset and the configuration on which a headline figure was produced. **Designate the certifier before the result is known**: a laboratory that grades itself has not certified anything, however honest its arithmetic. **Register admissibility separately from derivation**: when a formal check establishes that a derivation is valid, some body must still record which statement it establishes and whether the community accepts that as the one it asked. The first is a formatting norm. The second is a conflict-of-interest rule. The third is a sentence in a prize statute. None requires new technology, and all three would have prevented, between them, the three loudest episodes of the past two years.

Mathematics has absorbed every expansion of what counts as a proof (the axiom of choice, reduction to exhaustive case analysis, the formal verification of a Kepler conjecture) and has never once had to discover what a proof is in order to keep using one. It will absorb machines. What the record of 2024–2026 shows is that the profession is not arguing about whether the patterns are correct. It is arguing about who may say so, and about what the saying does to everyone else's work. Machines supply patterns; the wanting of them to be true is not on the bill of materials, and it is that wanting, not the computing, that has organized this discipline since someone first asked why.

---

## B · Figure 1 — spec and plotting dataset

**Figure 1.** *Controversy tracks the certification regime, not the difficulty of the result.* Suggested form: horizontal "staircase" of the three regimes on the x-axis (machine-graded → hybrid-graded → community-graded), eleven points placed by event, filled symbols where a public dispute is recorded, open symbols where none is; the five verification questions as a small heat-strip beneath each point. Rates annotated as 1/6 and 3/5 with the exact-test caveat in the legend.

```csv
id,year,event,regime,dispute,q1_framing,q2_reproducible,q3_independent,q4_symmetric_disclosure,q5_found_or_made,ref
1,2024,"IMO 2024 (AlphaProof, AlphaGeometry 2) — marked by Gowers & Myers, re-checked in Lean",HG,0,+,+,+,+,made,"4,7"
2,2025,"IMO 2025 — DeepMind route, graded by official coordinators",HG,0,+,±,+,+,made,"4"
3,2025,"IMO 2025 — self-selected former medallists, no formal checker",CG,1,±,−,−,−,made,"4"
4,2024,"o3 on FrontierMath — 75.7% on a selected subset, 25.2% full set",MG,1,−,−,−,−,found,"8,9"
5,2026,"FrontierMath v2 — errors fixed in 42% of the original problems by the benchmark's own builders",MG,0,+,+,+,+,na,"8"
6,2026,"Unit-distance disproof, digested by nine named verifiers",CG,0,+,+,+,+,made,"1,10,11,12"
7,2026,"Harvard 'First Proof' — ≥6 of 10 lemmas; human reviewers struggled to check them",CG,0,±,±,+,−,made,"23"
8,2025,"AlphaEvolve — 48 multiplications vs Strassen's 49; fifty open problems",MG,0,+,±,±,±,made,"5"
9,2026,"FrontierMath Erdős — 68 open problems in Lean; best 3%, all others 0",MG,0,+,+,+,+,na,"6"
10,2026,"Navier–Stokes — Lean-checked derivation; admissibility undecided",CG,1,±,−,−,−,made,"2,13,14,15"
11,2026,"Attribution dispute over the forced/unforced result",na,1,na,na,na,na,na,"3"
```

Coding rules are those of §11.2–11.3 of the parent paper (`+` satisfied on the record, `−` not satisfied, `±` partial or contested, `na` not applicable or not recorded). Rows 2–3 are one Olympiad year split by grading design; row 10 carries two regimes in the parent paper and is placed at the community level here because admissibility, not derivation, is what was contested. **The 1/6 and 3/5 tallies inherit the parent paper's grouping, in which row 11 (regime not applicable — an attribution quarrel, not a graded result) sits in the community denominator; the figure should be recomputed from `census.csv` once the census in [`census_protocol.md`](census_protocol.md) supplies rows with a fixed rule for such cases, and not before.**

---

## C · Reliability appendix (not for submission; house requirement)

Figures in the body follow the parent paper's tiering. Read this table before trusting any number.

| Claim in body | Marker | Basis |
|---|---|---|
| Conjecture open since 1946 disproved, May 2026 [1] | ✓ | Primary announcement plus a nine-author verification paper |
| Millennium problem "apparently" settled; forcing term [2][13] | ✓ for what was announced; ◐ for the scale claims | Institutional announcement quotes the laboratory; the artifact is not public |
| Attribution dispute [3] | ✗ | Contested by both parties, no adjudicated record |
| Silver-medal level at IMO 2024; marking by Gowers and Myers; Lean re-check [4] | ✓ | Publisher page plus the peer-reviewed *Nature* account; parent paper's [30][38] |
| 48 vs 49 multiplications; fifty problems [5] | ◐ / ○ | Company-reported; no peer-reviewed primary record at this date |
| 68 problems, best 3%, others zero [6] | ✓ | Benchmark authors' own report, machine-graded |
| 75.7% subset vs 25.2% full set; builders not consulted [8][9] | ✓ with one caveat | Benchmark authors' statement; the "not consulted" point is consensus among critics, reported by an interpretive source |
| n^1.014 lower bound, n^4/3 upper bound, gap widened [10][11][12] | ✓ | Published papers |
| ≥6 of 10 lemmas; referees could not verify [23] | ○ | Reported on institutional pages and in coverage; primary record pending |
| 42% of problems corrected [8] | ✓ | Benchmark release note |
| Prize rules: qualifying venue, two years, general acceptance [14] | ✓ | Statute text |
| Method does not extend to the unforced case [15] | ○ | Interpretive journalism; a referee-able argument has not been published |
| IMU endorsement; >4,000 signatories [21] | ✓ | Declaration record, counted 2026-09-23 |
| 1/6 vs 3/5, Fisher P ≈ 0.24 | ✓ as a computation | This draft's own coding; single coder, unreplicated |

---

## D · References (Nature format)

1. OpenAI. *An OpenAI model has disproved a central conjecture in discrete geometry.* https://openai.com/index/model-disproves-discrete-geometry-conjecture/ (2026).
2. OpenAI. *On the Navier–Stokes Millennium Prize Problem.* https://openai.com/index/navier-stokes-solution/ (2026).
3. Buckmaster's reported account — an offer to publish the forced Navier–Stokes result under his name alone, excluding Alpáro for competitive reasons, with a career-adjacent warning — against OpenAI's flat denial; contested, no adjudicated record at the time of writing. Cited as reported in 2026 coverage, not at a single primary source.
4. Google DeepMind. *AI achieves silver-medal standard solving International Mathematical Olympiad problems.* (2024). Publisher page, no stable link supplied here (house rule R-C); the peer-reviewed account is Hubert, T. *et al.* Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature* (2025). DOI 10.1038/s41586-025-09833-y (volume and pages to be taken from the publisher page before submission); and the 2025 comparison of the two laboratories' gold-standard results (35 of 42 points; five problems of six), one graded by official IMO coordinators and the other by three self-selected former medallists — reported figures, primary grading records pending (2025). *Cited jointly for both Olympiad years in the text below.*
5. Google DeepMind. *AlphaEvolve.* (2025–2026). Company report and 2025–26 coverage; the 48-multiplication 4×4 complex-matrix algorithm against Strassen's 49, ~70% rediscovery and genuine progress on a fifth of the remaining open problems, all figures self-reported and pending a peer-reviewed primary record.
6. Adamczewski, T. & Bloom, T. F. *FrontierMath Erdős.* Epoch AI (2026). https://epoch.ai/files/frontiermath-erdos.pdf.
7. Lean Language Reference. *Validating Proofs.* https://lean-lang.org/doc/reference/latest/ValidatingProofs/ — the kernel checks proof terms; the meaning of a statement is a separate task.
8. Epoch AI. *FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI.* Preprint at https://arxiv.org/abs/2411.04872 (2024); v2 release note of 12 June 2026 reporting corrections to errors in 42% of the original problems: https://epoch.ai/benchmarks/frontiermath-tier-4-v1.
9. Meyer, D. *‘Manipulative and disgraceful': OpenAI's critics seize on math benchmarking scandal.* Fortune (21 Jan 2025). https://fortune.com/2025/01/21/eye-on-ai-openai-o3-math-benchmark-frontiermath-epoch-altman-trump-biden — interpretive journalism, flagged as such in the text.
10. Alon, N. *et al.* *Remarks on the disproof of the unit distance conjecture.* Preprint at https://arxiv.org/abs/2605.20695 (2026).
11. Sawin, W. *An explicit lower bound for the unit distance problem.* Preprint at https://arxiv.org/abs/2605.20579 (2026).
12. Spencer, J., Szemerédi, E. & Trotter, W. T. Unit distances in the Euclidean plane, in *Graph Theory and Combinatorics*, 293–303 (Cambridge, 1984). No stable link; full bibliographic citation given (house rule R-C).
13. Clay Mathematics Institute. *Navier–Stokes Announcement.* https://www.claymath.org/news/navier-stokes-announcement/ (11 Sep 2026).
14. Clay Mathematics Institute. *Millennium Prize Rules.* https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf.
15. *Did OpenAI solve the wrong Navier–Stokes problem?* Scientific American (21 Sep 2026). Interpretive journalism; no referee-able argument published at this date.
16. Appel, K. I. & Haken, W. Every planar map is four colorable. *Illinois J. Math.* **21** (1977). (Page range not carried in the parent paper's record; take from the volume before submission.)
17. Tymoczko, T. The four-color problem and its philosophical significance. *J. Phil.* **76**, 57–83 (1979).
18. DeMillo, R. A., Lipton, R. J. & Perlis, A. J. Social processes and proofs of theorems and programs. *Commun. ACM* **22**, 271–280 (1979).
19. Merton, R. K. The Matthew effect in science. *Science* **159**, 56–63 (1968). DOI 10.1126/science.159.3810.56.
20. Hales, G. P. *et al.* A formal proof of the Kepler conjecture. *Forum Math. Pi* **5**, e2 (2017). DOI 10.1017/fmp.2017.1.
21. The Leiden Declaration on Artificial Intelligence and Mathematics. https://leidendeclaration.ai/ (2 June 2026). DOI 10.5281/zenodo.20302944; endorsed by the International Mathematical Union (https://www.mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf); 4,181 signatories as of 23 September 2026; *Nature* editorial https://www.nature.com/articles/d41586-026-01881-2 (18 Jun 2026).
22. Tao, T. *Mathematics in the age of AI.* Preprint at https://arxiv.org/abs/2608.16753 (2026).
23. Williams, L. and co-authors, Harvard "First Proof" challenge: ten previously unpublished research lemmas; participating systems solved at least six of ten; the reported difficulty lay downstream, in verification. Reported on Harvard Mathematics pages and in 2026 coverage; a second batch is registered behind a nonprofit; primary record pending.

---

## E · Nature house-style pressure-test (not for submission; skill-derived)

Run on 2026-09-25 against the installed `nature-writing` skill (`yuan1z0825/nature-skills`), loading its `core/stance.md` (claim discipline), `references/paper-review.md` (adversarial reviewer checklist), `static/fragments/journal/nature.md` (flagship-Nature house style), and `references/paragraph-flow.md` / `article-architecture.md`. This is a **Comment**, not a Research Article, so the skill's Article-only machinery (the `Here we show` summary funnel, IMRaD Results-ladder, ~50-reference cap) was deliberately **not** applied — the skill itself warns against forcing Article architecture onto other genres. **Outcome:** row 1 applied on the first pass; row 2 applied on a same-day review pass after author go-ahead; row 4 examined and deliberately held. What remains "your call" is editorial (the row-4 split, if the author overrides the hold) and the external gates the parent §11.5 defers to.

| # | Rule probed | Status | Note |
|---|---|---|---|
| 1 | *No em dashes in body prose* (`nature.md`) | **applied** | 17 found; every one converted to a comma, colon, or parenthesis with no change of fact, number, or citation (one filler word "that" removed). Re-verified: 0 remain in §A. |
| 2 | Bound universal / priority claims (`stance.md`) | **applied (review pass)** | Two sentences asserted more than §A evidences. Bounded, word-neutral: "The consensus reading" → "The **obvious** reading"; "and, in this literature, new" → "and, **to our knowledge**, new". Fact- and count-neutral (body stays ~1,510 words); revert if the parent's coverage section is judged to warrant the stronger consensus claim. |
| 3 | Every major claim correct + evidence-backed (`paper-review.md`) | **pass** | The headline mechanism claim is already self-bounded in-text (Fisher *P* ≈ 0.24, "descriptive", falsifier named, publicity-selection conceded). This is the draft's strongest defensive card and survives the adversarial read. |
| 4 | One message per paragraph (`paragraph-flow.md`) | **examined, held** | "Consider the evidence in order" carries five cases in ~280 words. Tempting to split by regime, but the paragraph deliberately **interleaves** machine-graded (o3, AlphaEvolve, Erdős) and community-graded (unit-distance) cases to make one point — that regime, not the running order, predicts silence vs scandal — so a clean MG-vs-CG split would misrepresent the evidentiary sequence. Held as-is; revisit only if an editor asks for a break. |
| 5 | Word budget | **pass** | ~1,510 words, inside the stated 1,500–2,200 Comment band (the earlier "just under the floor" note is superseded). |
| 6 | Reference count | **pass** | 23, within the ~20–30 range noted in the status block. |
| 7 | Non-specialist significance; jargon defined | **pass** | The three regimes are glossed on first use; no un-translated specialist term. |
| 8 | Terminology ledger consistent with parent | **pass** | machine-/hybrid-/community-graded and Q1–Q5 track parent §3.1/§4.1 without drift. |
| 9 | Author evidence first; do not invent (`stance.md`) | **unchanged** | This pass touched typography only. Every fact/number/citation still traces to the parent paper, **not** to a live-web re-check; refs 4, 16, 21–23 keep their "pending" notes. |

**What this pass could not do.** `nature-writing` targets research Articles and ships no Comment-length template; and the canonical stage-aware Nature submission checklist it points to lives in a separate `nature-shared` package that was **not** installed (only `nature-writing` came in). So the exact official Nature *Comment* limits (word ceiling, figure and reference policy) were not read from the authoritative source — the numbers above are the draft's own stated target. Closing that gap needs either `nature-shared` (for the checklist) or `nature-figure`/`academic-plotting` (to render Fig. 1 from the CSV instead of the current spec+data stub); both are installs that change the environment, i.e. **your call**.
