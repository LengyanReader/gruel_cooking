# Citation and claim audit — *Mathematical truth is not a matter of consensus*

**Date 记录日期**: 2026-09-26 (fourth pass, §§6–7 and final compression) · **Scope 范围**: the
72-entry bibliography, plus every quantitative and institutional claim in the text.
**Status 状态**: audit complete for the claims listed below; the per-item table for all entries
was **not persisted** and must be regenerated before submission (see *Residual risk*).
**AI-drafted, unreviewed.** A human author must confirm each entry against the canonical source.

---

## 1 · Method

Each entry was resolved against at least one of: the publisher or journal DOI landing page,
arXiv, the Crossref or Semantic Scholar record, the issuing institution's own page, or a
canonical reference work (MacTutor for history). Where only an abstract or a secondary page
was reachable, the claim in the text was downgraded rather than the entry being trusted.
Where an entry could not be resolved at all, it was replaced or removed. No bibliographic
field was reconstructed from memory.

## 2 · Corrections that changed the argument

These are the findings that altered the manuscript's substance, not its wording.

| # | Claim as drafted | Finding | Action |
|---|---|---|---|
| 1 | o3 "75.7% on a selected FrontierMath subset, 25.2% full set" | **False as stated.** o3's FrontierMath score is 25.2%. 75.7% is o3's ARC-AGI result on a semi-private set under reduced compute. The two numbers belong to different benchmarks. | Corrected throughout; `checks/review_scope.py` now fails the build if 75.7% appears without ARC-AGI nearby. |
| 2 | FrontierMath v2: errors fixed in 42% of problems | Version-confused. 42% describes v2; the original release's error rate was higher. | Restated as a version-specific claim with the version named. |
| 3 | IMO 2025: "gentleman's agreement" on embargo, adjudicated by one reviewer | Overstated. A release-timing dispute existed; the IMU asked for a delay; accounts differ on what was agreed and by whom. | Reduced to a documented disagreement about timing, with the disagreement itself as the evidence. |
| 4 | AlphaEvolve: 48 vs 49 "multiplications" | Wrong object. The result is the rank-48 tensor decomposition for 4×4 complex matrix multiplication, against Strassen's 49. | Corrected; the kissing-number result is now stated as a **lower** bound 592 → 593. |
| 5 | IMO 2024 as a simulation of olympiad conditions | Misleading. Problems were translated into a formal language by humans, and some searches ran up to three days, against a 4.5-hour human sitting. | Stated as a real result obtained under conditions that are not the human contest. |
| 6 | Navier–Stokes "solved" | Conflates a forced-Euler statement with the unforced Navier–Stokes problem, and an announcement with a Clay determination. | The Review now reports the derivation as valid for the stated statement and admissibility as undecided. |
| 7 | A dispute-rate claim of 1/6 vs 3/5, Fisher exact *P* ≈ 0.24 | Unusable. The `na` row was folded into the community denominator, the corpus was selected through publicity, and n = 11 supports no rate. | Figure, tally and test **removed**. Retained only as a withdrawn archive (`figure1_data.csv`). |
| 8 | Pre-registration P1: machine-graded dispute rate 0 | Contradicted by the pilot's own machine-graded dispute row. | Census kit marked **withdrawn**; the Review proposes the study as future work instead. |

## 3 · Reference-level corrections

**Replaced (5).** A non-existent "Toward Today's Mathematics" attributed to Wang was replaced
by Wang 1960, *Toward mechanical mathematics*, *IBM J. Res. Dev.* **4**, 2–22,
doi:10.1147/rd.41.0002. A Logic-Theorem-Project citation with a wrong venue was replaced by
Newell & Simon 1956, *RAND* P-868, with the 2.85 figure marked as historical rather than
current. Three further entries were replaced where the original could not be resolved to a
canonical record.

**Venue, title or pagination corrected.** Hadamard (title/venue); Newell & Simon 1976
*CACM* **19**, 113–126, doi:10.1145/360018.360022; Dreyfus (subtitle); Searle 1980 *BBS*
**3**, 417–424, doi:10.1017/S0140525X00005756; Wang 1954 *J. Symbolic Logic* **19**, 241–266,
doi:10.2307/2267732. Appel, Avigad, Hales, Robinson, de Bruijn, McCune, Lean, Polanyi, Pólya,
Lakatos, Merton, Kuhn, Gowers, Tymoczko and DeMillo resolved to canonical records.

**Downgraded to weaker support (9).** Company and personal pages are cited as *claims by the
issuer*, never as certification: the OpenAI unit-distance announcement, the FrontierMath and
Erdős-problems pages, the Lean documentation, the Clay announcement, the arXiv preprint for
AlphaEvolve, the Harvard "First Proof" item, and (second pass) the Anthropic nine-loops post.
Where the underlying claim matters, the Review says what was announced and by whom.

**Historical claims narrowed.** The Maya zero-date and *khipu* narrative claims were corrected
against Salomon's work; khipu is not a narrative device and the date was revised. The anxiety
source supports a negative association between mathematics anxiety and performance, not a
five-factor framework; it is now cited for the association only. The Katz source supports a
global view of the history of mathematics, not the specific editorial judgement the draft
attributed to it, and the text now marks that judgement as the author's.

## 4 · Claims removed instead of repaired

- Every frequency, rate and significance statement about where disputes arise.
- Every "AI has produced X independent discoveries of rank Y" formulation that counted
  self-reported targets rather than certified results.
- The characterisation of peer review as a certification mechanism, which the historical
  literature in the same draft contradicts.
- Adjectives of settledness ("decisive", "transformative") applied to results whose
  admissibility was open at the time of writing.

## 5 · Residual risk

1. **The per-item table is not in this file.** The audit was run in batches and the
   verdicts were returned in working sessions, not written down per entry. What is recorded
   above is everything that changed the text. Before submission, every one of the 72 entries in
   the Review's reference list must be re-verified individually and this file completed with a
   row per entry: entry, resolved URL or DOI, verdict (verified / downgraded / replaced /
   removed), and the claim it supports.
2. **Three entries were not re-verified online during the final editing pass**, because the
   editing pass was offline: Penrose 1989 (no DOI supplied, publisher only), the Katz source
   (used for an editorial judgement the text now attributes to the author), and Green (cited as
   expository notes, not as a theorem).
3. **Nature's reference ceiling is not the binding constraint**; the count is 72 against a limit
   of about 150. The binding constraints are recency and the share of peer-reviewed primary
   sources, which has not been measured yet and should be, since a Review is expected to lean
   on recent peer-reviewed work. The eight entries added on 2026-09-26 make this worse, not
   better: five are scholarly monographs or documentary editions whose age is the point of the
   citation, one is an arXiv preprint not yet peer reviewed, and two are publisher or
   institutional web pages cited as claims by their issuers.
4. **The 2026 items are close to the boundary of the record.** Several central sources are
   2025–2026 announcements and preprints. Their status can change, and the Review's own
   argument about admissibility applies to them as much as to the results it describes. The
   Clay status label checked on 2026-09-26 is the kind of claim that decays fastest and should
   be re-checked immediately before submission.

## 6 · Second verification pass (2026-09-26)

Five user-supplied links plus leads drawn from them were checked. Three became new
references, inserted at first-appearance position 27; **the old entries 27 to 63 are
therefore renumbered 30 to 66.** Compare by title, not by number, against any earlier draft.

| Source | Tier | Finding | Action |
|---|---|---|---|
| Clay Mathematics Institute, Navier–Stokes problem page | **primary, institutional** | Fetched 2026-09-26. The page carries the status label **Active**, footer "© 2026 Clay Mathematics Institute". Clay has issued no resolution. | **New ref 27.** Upgrades §2 from a news report about Clay's response to Clay's own live record. One sentence added, worded as a dated check. |
| Guevara, Lupsasca, Skinner, Strominger & Weil, arXiv:2602.12176 | preprint, not yet peer reviewed | Verified: *Single-minus gluon tree amplitudes are nonzero*; v1 2026-02-12, v2 2026-03-09. Listed **on behalf of OpenAI**. States the key formula "was first conjectured by GPT-5.2 Pro and then proved by a new internal OpenAI model", hand-checked against the Berends–Giele recursion and checked against soft theorem, cyclicity, Kleiss–Kuijf and U(1) decoupling. | **New ref 28.** Used as a preprint claim, explicitly. Chosen over the blog material because the attribution is on the face of a citable paper with named human authors. |
| Anthropic, "Yes, Claude can do nine loops" (25 Sept 2026) | **company blog, commissioned guest post** | A paid, invited contribution by Matt von Hippel, with Anthropic staff review and Claude usage credits extended to the independent validator Lance Dixon. Every strong claim (two independent routes, ≈$100 of Python compute, ≈2 weeks of validation) is the issuer's or the guest's account. | **New ref 29**, cited as *claims by the parties*. The Review states that neither account is independently certified. The "toy model" caveat is stated so the episode is not read as physics of the observed universe. |

### Leads checked and deliberately not cited

| Source | Why not |
|---|---|
| Zenodo DOI 10.5281/zenodo.22800071 (He, Jing & Li, six-particle 2→9 loop data) | **Unreachable.** `zenodo.org/records/…`, the DOI resolver and the Zenodo REST API all returned transport errors on three attempts. The 17 September release date, the authorship and the GPT-6 contribution are known only from secondary reporting. Per instruction, no media report is to stand in for the artifact, so **nothing about this team entered the body text.** Retrieve and add if it matters. |
| 新智元 / ASI 启示录, WeChat article on the nine-loop result | Secondary, promotional register ("截胡", "杀疯了", "神级挑战"). It is the Reporting-quality source of the 17 Sept Zenodo date, the 景继荣/李想 authorship, Lance Dixon's and Kyle Cranmer's remarks, and the 1.85M→76,000 unknown reduction. All of it is recorded here as leads and none of it is cited. |
| Anthropic X post `2103541577083719888` | Unreachable (transport error). The WeChat article reproduces it as a reference, which is corroboration of existence only. |
| Quanta, "AI has solved one of maths' 1 million Millennium Prize problems" (8 Sept 2026) | Reachable and directly on point, but adding it was judged out of proportion to a one-example brief. **Held as the strongest available strengthening**: it records that the remaining human task is to guarantee the Lean statement is logically equivalent to the target, and it documents the Buckmaster/Alpöge priority dispute and OpenAI's concession of 3D Euler. Adding it would be one reference and roughly 120 words, and would need §3 line 110 strengthened at the same time. |
| ITP CAS profile, 何颂 (Song He) | A personnel page: research interests and honours. It can establish who someone is; it cannot support a nine-loop result. Not cited. |

### Net effect

Review body 5,966 → 6,213 words (ceiling ≈7,000; superseded by §8.5, which records the final
figure after §§6 and 7 were added); references 63 → 66 (ceiling 150; likewise superseded by the
final 72); Chinese body
8,769 → 9,194 CJK characters after §7. One paragraph and one sentence were added to §2 in both
languages; the further Chinese growth in §7 is the language pass recorded below. The English
Synopsis is unchanged at 431 words; the Chinese Synopsis moved 697 → 706 CJK characters, still
inside the 380–800 gate.

## 7 · Third pass: Chinese language (2026-09-26)

A full rewrite of the Chinese for idiomatic scholarly Chinese. **The standard applied is
correspondence of content and meaning, not word-for-word mirroring of the English.** No fact,
number, citation, evidential status or paragraph was added, removed or moved.

| Check | Result |
|---|---|
| Paragraphs rewritten | 59 (5 Synopsis + 9 Preface/§1 + 9 §2 + 8 §3 + 7 §4 + 7 §5 + 8 §6 + 6 §7) |
| Facts, numbers, citations, hedges | unchanged; 111 in-text markers → 66 entries, contiguous, first-appearance order |
| Em dash (U+2014) | none introduced; `refcheck.py` still passes |
| `进行`, 空转词 (*值得注意的是*, *众所周知* …), stacked `的` | 0 occurrences |
| `分开` | 14 nominal uses now read 区别 / 区分 / 有别; the 4 survivors are all verb uses meaning *to separate X from Y*, which is correct |
| Passive `被` | retained only where the passive is the accurate Chinese claim |
| 楊-米尔斯 | 楊-米尔斯 throughout; 米克斯 does not occur |

Corrections of substance found while rewriting, not merely of register:

- `单位距离反例由一位署名的数学家群体核验` carried a number/word error. The source says **nine
  named mathematicians**; now 九位具名数学家 [17]. Same meaning as the English, which was
  already correct.
- `没有分数能推翻内核的裁决` was a literal rendering of a slightly odd English phrase. The claim
  is that the verdict is final, now 内核的裁决无从推翻.
- Preface: 前一类 / 后一类分数 was ambiguous. Now bound explicitly to 基准分数 and to the
  questions raised by formal checking, matching the English antecedent.
- 标题分数 → 宣传分数 throughout, for *headline score*.
- 直译 leftovers removed: 指称 (twice, → 指的是 / 指的是…), 宣布流传 (→ 传开), 四处携带而旅行
  (→ 便于转手), 把它削尖 (→ 把它打磨得更为精确), 无处附着 (→ 不会发生), 熬不过 (→ 撑不过),
  凑出 (→ 梳理), 无论算术多么谨慎 (→ 无论它自己那一套多么谨慎), 同样的推理 (→ 这套道理, the
  antecedent was a set of distinctions, not a derivation).

Paragraphs judged already idiomatic were left alone, per the register checklist's instruction not
to rewrite for its own sake: §2 line 55 (IMO 2025) and §2 line 59 (AlphaEvolve).

## 8 · Fourth pass: the two added sections, and what was cut to pay for them (2026-09-26)

The plan had two open scope items: whether the Review had anything to say about originativity,
and whether it treated modern mathematics as standing for all of mathematics. Both are now
sections, §6 and §7. Adding them put the body over the ceiling, so the older sections were
compressed rather than the ceiling raised. This section records the eight new entries, the
leads that were rejected, and the removals, so that the two can be checked against each other.

### 8.1 New entries

| Source | Tier | Finding | Action |
|---|---|---|---|
| Smith, K., *Descartes' life and works*, Stanford Encyclopedia of Philosophy, rev. 1 March 2023 | reference work, encyclopaedic, editor-revised | Resolved. States that Descartes took a law degree at Poitiers in 1616, held no academic post in mathematics, entered the Nassau-Maurice military service at twenty-two, and learned mathematics chiefly through correspondence with Beeckman. It does not adjudicate any claim about originality. | **New ref 65**, §6. Cited for the biographical facts that make the case, and for nothing about priority. |
| Newton, I., *Philosophiæ Naturalis Principia Mathematica*, new translation by Cohen & Whitman, University of California Press, 1999 | primary source, critical edition | Resolved. The inverse-square law is established from the motions of Jupiter's satellites and then applied to the Moon by analogy, with the Moon's centripetal force identified with terrestrial gravity; Book I names Wren, Hooke and Halley as having already observed the same fact. The order of the argument is the reverse of the popular telling. | **New ref 66**, §6. The text follows the source's order and does not present the analogy as a later addition. |
| Crippa, D., *The Impossibility of Squaring the Circle in the 17th Century*, Birkhäuser, 2019 | peer-reviewed monograph | Resolved. Leibniz's result is attached to an unpublished manuscript and closes a controversy between Gregory, Huygens and Leibniz. | **New ref 67**, §6. |
| Wittmann, A. D., *Carl Friedrich Gauss and the Gauss Society*, History of Geo- and Space Sciences **11**, 199–205, 2020 | peer-reviewed article | Resolved. Gauss held a doctorate and never a mathematics chair; he was appointed professor of astronomy and director of the Göttingen Observatory, and the Hanover triangulation and the magnetic network with Weber were field programmes, not applications of a completed theory. | **New ref 68**, §6. This is the load-bearing case for the asymmetry claimed in §6, and it is a documented appointment record rather than an inference from dates. |
| Martzloff, J.-C., *A History of Chinese Mathematics*, Springer, 1997 | scholarly monograph | Resolved. Chinese mathematics is organised by reasoning method and structural theme. | **New ref 69**, §7. Cited for organisation of material only, with no priority claim and no claim about the modern register's relation to it. |
| Plofker, K., *Mathematics in India*, Princeton University Press, 2009 | scholarly monograph | Resolved. Indian mathematics is organised by the decimal place-value system and by an algebra treated as a general method rather than as a technique for solving equations. | **New ref 70**, §7. Same restriction as 69. |
| Caviola, G., et al., *Test anxiety effects, predictors, and correlates: a 30-year meta-analytic review*, Educational Psychology Review **34**, 363–399, 2022; Namkung, H., Peng, S. & Lin, R., *A meta-analysis of mathematics anxiety*, Review of Educational Research **89**, 459–496, 2019 | peer-reviewed meta-analyses | Both resolved. Both support a negative association between mathematics anxiety and achievement. Neither supports a causal claim, a five-factor structure, or any statement about talent. | **New refs 71 and 72**, first cited together in §8 and used in §9 as the standing warrant for treating anxiety as a fact about instruction rather than about ability. |

First-appearance positions after this pass: 1 to 64 unchanged, 65 to 68 in §6, 69 and 70 in §7, 71
and 72 in §8. `checks/refcheck.py` re-verifies the order, so a later edit that moves a citation
will fail the build rather than pass unnoticed.

### 8.2 Leads checked and deliberately not cited

| Lead | Why not |
|---|---|
| Restivo; Rashed; Krämer; Fleischer | Checked during this pass and not cited. The retrieved record does not support the specific claim each was sought for, and none of them is named in the text. If any is wanted later, it must be resolved to a canonical record first. |
| The circulating AI "problem shifting" literature | Not cited. The claim that machine systems are generating genuinely new lines of attack rather than recombining existing techniques is exactly the §6 question, and the available material asserts it rather than measuring it. Citing it would concede the Review's own thesis to a secondary source. |
| The withdrawn census apparatus, Figure 1, the dispute-rate tally and the Fisher test | Removed in the second pass and retained only as a withdrawn archive. `checks/review_scope.py` fails the build if any of it reappears in a manuscript. |

### 8.3 What was removed to make room

The body went from 7,691 words as it stood before this pass to 6,996 as measured by
`checks/refcheck.py`, which counts headings and excludes the reference list. Nothing was cut
from §§6, 7 or 9. The reductions came from four places, in descending order of size:

1. **A duplicated methodology paragraph.** The closing paragraph of §8 had been inserted twice,
   once at the end of the section and once at the head of what is now §9. The §8 copy was
   deleted and the §9 copy kept, and the malformed comment boundary between the two sections
   was repaired at the same time.
2. **A duplicated benchmark paragraph in §2.** The Erdős-problem benchmark appeared twice in
   English, once as a complete paragraph and once as an orphan remainder, and twice in Chinese
   as two half-paragraphs. The remainder was deleted and the two Chinese halves merged. All of
   `[20]`'s content was kept.
3. **A duplicated formalization pair in §1.** Two paragraphs, one in each language, each
   restating the same distinction. Each language now has one.
4. **The Harris sentence in §5.** The point it made, that the danger is the loss of the research
   agenda, is made in the same section by the two positions it was sitting between. The claim
   survives; the attribution does not, so `[62]` is now carried by the aggregated citation in
   that paragraph.

The remaining reductions were sentence-level joins inside §§2, 5, 6 and 7, applied in both
languages together so that no paragraph came to stand for a different claim in one language than
in the other.

### 8.4 Language findings from the compression

Seven wrong characters entered the Chinese text because those paragraphs were written with
`\u` escapes rather than literal characters, and were then found and corrected:
`譚写` to `誊写`, `猞想` to `猜想`, `贼低` to `贬低`, `学术争论` to `哲学争论`, `无从置嗝` to
`无从置喙`, `意虑` to `忧虑`, and `一小捏` to `一小撮`. Each was a plausible-looking character
in a plausible-looking position, which is why the paragraph-level proofread did not catch them.

The register checklist should carry a standing rule as a result: **write Chinese as literal
characters, never as escapes**, and after any batch edit run a character-frequency sweep and
read the singletons, since a corrupted character is almost always rare in the document.

### 8.5 Net effect

Body 7,691 to 6,996 words by the `refcheck.py` measure, and 7,691 to 6,911 excluding headings.
Chinese body 11,517 to 10,822 CJK characters. References 66 to 72. In-text citation markers 111
to 120. The Review has ten first-level blocks, Preface and nine sections, with parallel English
and Chinese paragraph counts in every one. The English Synopsis is unchanged at 431 words and
the Chinese Synopsis at 706 CJK characters, both inside their gates.

## 9 · How to re-run the mechanical part

```
python submission/build_reader.py         # regenerate the five derived files
python submission/checks/refcheck.py       # em dash, citation closure, first-appearance order
python submission/checks/review_scope.py   # withdrawn apparatus, 75.7% bound to ARC-AGI, lengths
python submission/checks/table1_tally.py   # archive arithmetic, labelled archive-only
python submission/build_reader.py --check  # generated views current, no orphans
```

`checks/figure1.py` re-renders the withdrawn figure. Its data layer needs no third-party
package; rendering needs matplotlib, and the script says so and exits cleanly without it.

## 10 · Addendum: bibliography change of 2026-09-26 (five-part rewrite)

**Scope.** The Review was rewritten on 2026-09-26 into a Preface + ten sections that absorb
the founding seven-point brief (see `venue_memo.md` §0). The bibliography changed from 72 to
**75 entries**, renumbered by first appearance. Gates re-run green:
`build_reader.py`, `checks/refcheck.py`, `checks/review_scope.py`.

**Carried from the audited 72: 55 entries**, unchanged in wording. The audit's verdicts for
them remain in force (§§2–8).

**Dropped: 17 entries**, removed with their supporting passages to make room for the seven-point
content: Spencer–Szemerédi–Trotter (unit-distance upper bound), Avigad 2006 and 2022 (folded
into the verification-bottleneck discussion without dedicated citations), Appel & Haken I and
II, Tymoczko, DeMillo–Lipton–Perlis (the four-colour social-process passage), Searle, Dreyfus,
Polanyi (the older philosophical arguments), Hardy 1937, Berndt & Rankin, Schneider, Berndt's
lost notebooks, Halberstam, MacTutor Hua (the Ramanujan–Hua apparatus), and Green's parity
notes. They remain available for later restorations; nothing in their removal contradicts the
audit's earlier verdicts.

**Added: 20 entries, all marked for human verification before any external submission**
(per-entry table not persisted, as before): Feng et al., *Towards Autonomous Mathematics
Research*, arXiv:2602.10177 (Aletheia autonomy scale); the long-chain Lean autoformalization
benchmark paper arXiv:2606.29493 (placeholder-fabrication case); the 25 Fields Medalists'
open letter, *A Severe Misalignment of AI in Mathematics*, mathandai.org, 11 September 2026
(URL to be confirmed against a primary mirror); Park, *Automation Without Understanding*,
arXiv:2607.06377; Bessis, *Mathematica*, Yale UP 2024; SEP *Philosophy of Mathematics*,
*Gödel's Incompleteness Theorems*, *The Church–Turing Thesis*; Wigner 1960; Cohen 1963;
Tegmark 2014; Dyson, *Birds and Frogs* 2009; Langlands, letter to Weil 1967; Porter, *Trust
in Numbers* 1995; Kolmogorov 1933; Wu Wen-tsun 1978; Poincaré 1908; Whitehead, *Process and
Reality* 1929; Friston 2010; Leibniz, *Monadologie* 1714. All but the 2025–2026 items are
canonical classics with standard bibliographic records; the 2025–2026 items need live-source
checks as the audit's method requires.

**Consciously excluded from the Review** (retained in `articles/proofs_no_longer_scarce.md` with 待审 marks):
the He Song team's 17 September 2026 Zenodo release of two-to-nine-loop data, which is known
only through press reporting with no primary record yet confirmed; the EMS non-endorsement of
the Leiden Declaration (er2-sourced); and Smirnov's excavator metaphor (press-transmitted).
The rule applied is the audit's standing one: a media report must not stand in for the artifact.
