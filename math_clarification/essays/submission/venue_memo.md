# Venue decision memo — Nature Review, and what it cost

> **Status 状态**: Decision record. **AI-drafted, unreviewed** (harness §I.6). A human author
> must own the submission decision. Supersedes the earlier Comment-versus-Article memo, which
> argued for a Comment first and a census-based Article afterwards; both routes are now closed.
> Sources of record: [`../../articles/ai_and_math.md`](../../articles/ai_and_math.md), [`comment_draft.md`](comment_draft.md),
> [`citation_audit.md`](citation_audit.md).

## 0 · Superseding decision (2026-09-26, author)

The author has lifted the Nature format constraints: the article is to be judged as an article,
written to the spirit of the highest standards rather than to a word ceiling. The bilingual
Review now runs **Preface + 10 sections**, absorbing the founding seven-point brief (event-by-
event audit with per-event verdicts; the six voices and the four-layer crisis diagnosis; what
mathematics is, its place, ground and limits; who the mathematician is and the intelligence
myth; formalization, computability, quantifiability and the division of labour; what counts as
originative; consensus as evidence; institutional rules; what counts as progress; and a closing
synthesis of mutual dependence). Measured state: **75 references** (55 carried from the audited
72, 20 added, see `citation_audit.md` §9), EN body about **10,000 words**, ZH body about
**16,700 characters**. The English and Chinese sides correspond in content and spirit rather
than sentence by sentence. The Synopsis word band and the citation gates in
`checks/refcheck.py` and `checks/review_scope.py` remain in force as repo quality checks, not
as submission requirements. Sections 1–5 below describe the earlier Nature-shaped draft and
are retained as the record of how the format came about.

## 1 · Decision

The flagship *Nature* **Review** is the target, and the 300–500-word piece is its **Synopsis**.
A Research Article remains a possible later destination, but only after the study proposed in
section 9 of the Review actually exists. The census kit is not that study and has been
withdrawn.

## 2 · Why the earlier routes closed

| Route | Why it closed |
|---|---|
| Comment (1,500–2,200 words) | The argument could not be made at that length. Separating truth, validity and admissibility, and then arguing about certification regimes, needed the space of a Review. |
| Comment + figure | The figure encoded the eleven-event tally, and the audit showed the tally was not usable: the `na` row was binned with community-graded events, the corpus was publicity-selected, and n = 11 supports no rate. |
| Research Article (the census) | The pilot contradicted the protocol's own primary prediction, so there is no dataset to report. The Review now proposes the study as future work instead. |
| Comment + Article sequentially | The sequencing argument depended on the census being registrable before the next results. It is not. |

## 3 · Nature's stated requirements, and where the draft stands

Checked against [Other Subs](https://www.nature.com/nature/for-authors/other-subs) and the
[formatting guide](https://www.nature.com/nature/for-authors/formatting-guide).

| Requirement | Rule | Current state |
|---|---|---|
| Synopsis | 300–500 words | 431 words. Checked by `checks/review_scope.py`. |
| Preface | about 200 words | present, section "Preface" |
| Body | typically under 7,000 words | 6,996 words including headings, excluding references. Measured by `checks/refcheck.py`. |
| Display items | up to 4 | 0. The figure was withdrawn. |
| References | usually up to 150 | 72 |
| Recency | a Nature Review should be informed by recent peer-reviewed literature | **not yet measured** — see residual risk in `citation_audit.md` |
| Original data | no unpublished primary data in a Review | none claimed; the Review says so in its status block |
| Punctuation | no em dash in English prose | enforced by `checks/refcheck.py` |

## 4 · What the Review gives up, and why that is a feature

The withdrawn material was the most quotable part of the old draft: a number, a figure and a
significance test. A Review has no dataset and does not need one. The argument is now carried
by the separation of three questions and by a set of institutional proposals that are stated so
that they can fail. Section 9 names the measures that would refute the Review's own position,
which is the only property that makes a Review's forward claims worth reading.

Two sections were added on 2026-09-26 to close the planned scope gaps, and the body was then
compressed to stay under the ceiling. Section 6 defines originativity as a relation between a
question and a body of work, which makes it a checkable claim about supply rather than a
compliment about minds, and Section 7 argues that the modern mathematical register is one
curated tradition among several. Together they move the Review from a defence of mathematical
practice to a claim about what any practice has to answer to. The cost was paid in the older
sections: the duplicated Erdős benchmark, the duplicated methodology paragraph and the Harris
sentence were removed rather than kept alongside the new sections, so the Review now argues each
point once.

## 5 · Steps that require a human author

1. Read the Review end to end and accept or reject every claim. Nothing here has been
   peer-reviewed.
2. Complete the 72-row per-entry verification table in `citation_audit.md`. The audit's
   verdicts were produced in working sessions and only the text-changing findings were written
   down.
3. Measure the share of peer-reviewed primary sources and raise it if it is low.
4. Decide the author list and obtain permission for any personal-page sources, or drop them.
5. Confirm that no 2025–2026 source has changed status since the audit.
6. Decide whether the withdrawn census is revived as a separate paper, and if so re-register it
   with `na` as its own stratum and a two-sided hypothesis.
