# Venue strategy memo — Comment now, Article next, or both at once?

> **Status 状态**: Internal decision memo, not a submission artifact. **AI-drafted, unreviewed** (harness §I.6) — a human author must own every judgement here before acting on it. Companion to [`comment_draft.md`](comment_draft.md) (the argument piece) and [`census_protocol.md`](census_protocol.md) (the study it points to).
> **Question 问题**: Should the manuscript in `comment_draft.md` go to *Nature* as a Comment, or should the effort go into a Research Article instead?
> **Short answer 结论**: They are sequential, not competing. Send the Comment first; the Article *is* the census, and it cannot be started until the protocol is registered. This memo makes that case against published venue rules, and lists the steps that need a human author.

---

## 1 · What the draft actually is (evidence inventory)

The genre decision follows from what is on the page, so the inventory first.

| Property | Current state | Genre consequence |
|---|---|---|
| Body length | ~1,670 words after the e1 pass and live-web correction (recounted, §E row 5) | Argument-piece length, not Article length |
| References | 23, all cited, integrity-gated (`checks/refcheck.py`) | Comment band |
| Primary data collection | **None.** The piece states this explicitly in its status block | Disqualifies it as a Research Article |
| Display items | One figure (Fig. 1), rendered from an eleven-event coding table | Interpretive figure, not a results figure |
| Statistic | Fisher exact P ≈ 0.24 on 1/6 vs 3/5, self-labelled descriptive and publicity-selected | A *hypothesis-flagging* number, not a confirming one |
| Coder | Single, unreplicated (parent §11.4) | Not yet a study; the study needs double coding |
| Falsifier named in-text | Yes (a machine-graded false positive) | Argument discipline, Comment-appropriate |

The draft's own logic is the decisive fact: its strongest paragraph (the "candid about our evidence" one) says the eleven-row table *cannot* separate regime from grader prestige, that only the census can, and that the census must be registered *before* the next results. The Comment is written to hand off to the Article. Publishing them as one paper would mean either dropping the hand-off or smuggling a primary dataset into an argument piece.

## 2 · The three venues, against their published rules

### 2.1 *Nature* flagship — Comment (News & Comment)
The argument-forward, named-author, one-figure form the draft is built for. **Caveat found this session**: the exact official Comment word/figure/reference limits are *not* in Nature's public [formatting guide](https://www.nature.com/nature/for-authors/formatting-guide) — that guide covers Articles (2,500–4,300 words, ≤50 references) and only points to a separate "News and Comment" page, which sits behind an editorial-authorisation redirect and could not be read. The draft's "1,500–2,200 words" band is therefore an **author-stated target consistent with observed flagship Comments**, not a figure copied from an authoritative Nature page. It stands as a reasonable working band; it is not verified against the canonical source.

### 2.2 *Nature* flagship — Research Article
Requires original research representing "a substantial advance" (formatting guide, §Articles). The draft contains no primary collection and says so, so it is **not** an Article. The Article this project can honestly aim at is the **census study** in `census_protocol.md`, which *is* primary collection (frames A/B/C, PRISMA counts, double coding, κ ≥ 0.6 gates) and must be registered before its first post-registration snapshot is coded.

### 2.3 *Humanities and Social Sciences Communications* — Comment Article
A real, peer-reviewed Nature-partner venue with **authoritative published limits** (guidelines PDF, v. 2025-02-25): 2,000–4,000 words excluding references, abstract ≤250 words, **maximum two** visuals, "figures and tables only when absolutely essential". Three of its stated rejection criteria bear directly on us:
- **Rejects work that "presents new methods or datasets (i.e., presents original research)"** — our eleven-event coding must be framed as illustrative of an argument, never as a dataset contribution, or this venue is wrong for the Comment (and right for the census instead).
- **Rejects pieces "generated wholly by AI"** — this collides head-on with harness §I.6 (AI-drafted, unreviewed). Nothing can go here until a human author has accepted or deleted every claim and owns the text.
- Its **2,000-word floor** is above the current body (~1,670). If HSSC Comms is chosen, the body must grow ~330 words without new facts (deeper mechanism, an added worked objection), or the piece is out of format.

## 3 · Recommendation

1. **Lead with the flagship Comment.** It is the venue whose form the draft already matches (argument, one figure, no primary data), and it stakes the priority of the "regime, not difficulty" claim while the census is run. Before submission: (a) expand the body toward the flagship norm if an editor flags length, but do not manufacture facts to fill it; (b) confirm the Comment limits with the editor via a **presubmission enquiry** (the guide's own route), since the public page does not state them.
2. **Do not merge Comment and Article.** The Comment's own argument depends on the separation. Merging would either delete the hand-off or turn an argument piece into undisclosed primary research, which is the fastest route to desk-rejection at any of the three venues.
3. **Treat HSSC Comms as the fallback, gated on human ownership.** Its rules are clearer and verifiable, but its "no new datasets" + "not AI-generated" criteria mean it only becomes viable once (i) a human author owns every claim, and (ii) the coding table is positioned as illustrative. Keep it as a sensible Plan B if the flagship declines on fit.
4. **Start the census on the registration clock, not the writing clock.** `census_protocol.md` §8 fixes the rule: registration (timestamped, public) must precede inspection of any post-registration leaderboard snapshot. The instruments for that step are now staged in this folder (`census_prereg.md`, `census_coding_template.csv`, `census_coder2_packet.md`, `checks/kappa_csv.py`).

### Why not "Article first, skip the Comment"?
Because the census needs a registration date that predates the next batch of results to be worth anything (parent §11.8, prediction P-series). Waiting for the Article forfeits the timing advantage the Comment exists to capture, and the Comment adds no primary claim the Article would have to disavow. The Comment is the cheap, reversible move; the Article is the slow, load-bearing one. They do not compete for the same evidence.

## 4 · What needs the author (cannot be done autonomously)

- **Authorship and AI-disclosure decision** — who is named, and how the use of drafting tools is disclosed (the Leiden Declaration's "disclose tool use" recommendation [21] is directly on point for a paper *about* disclosure). Harness §I.6: a human must accept or delete every claim.
- **The presubmission enquiry** to the flagship Comment editors (the guide's route to confirm Comment fit and length) — a human correspondence act.
- **Owning the eleven-event coding** as a human judgement, since a single unreplicated coder is the draft's admitted weakest link and the fallback venue rejects AI-generated text outright.
- **Registering the census** (OSF / arXiv-annex / dated public commit): the choice of venue and the actual deposit are author actions; the draft `census_prereg.md` is ready to paste.

*Nothing in this memo adds facts to the manuscript; it reads published venue rules and the draft's own inventory to decide where the draft belongs.*
