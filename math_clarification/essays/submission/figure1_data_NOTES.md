# `figure1_data.csv` — archival note (withdrawn)

**Status: WITHDRAWN from the manuscript. Retained as a research-design archive only.**
AI-drafted, unreviewed. Nothing on this page is a claim of the Nature Review.

## What this file is

The eleven-row coding table that used to sit in §B of `comment_draft.md` and fed
`checks/figure1.py`. The rows are transcribed **verbatim** from the pre-Review draft
(recoverable with `git show HEAD:math_clarification/essays/submission/comment_draft.md`).
They were not silently edited, because the point of an archive is to preserve what was
actually coded. The defects below are therefore still present in the data on purpose.

## Why it was withdrawn

The figure carried a headline tally, "1/6 machine-or-hybrid vs 3/5 community", and a
Fisher exact *P* ≈ 0.24. The audit that produced this Review found three defects, any
one of which is disqualifying:

1. **Row 4 misattributes a score.** The event text reads "75.7% on a selected subset,
   25.2% full set" and is filed under FrontierMath. This is wrong. o3's FrontierMath
   score is **25.2%**; **75.7%** is o3's ARC-AGI result on a semi-private evaluation
   set, under reduced compute. A coding table that puts 75.7% next to FrontierMath is
   not a near-miss; it is the exact error the Review is written to stop.
2. **The `na` bin is a silent reassignment.** Row 11 is an attribution quarrel with
   `regime = na`. The old tally folded `na` into the community denominator, so an
   episode that was never a graded result silently became community-graded evidence.
   The honest split is 4 community-graded plus 1 not-applicable, not "5 community".
   `checks/figure1.py` did the same folding, which is how the error survived.
3. **The test does not license the inference.** Eleven events, selected through
   publicity, is a convenience sample. A Fisher exact test on a 2×2 table this small
   reports *P* ≈ 0.24, which is the absence of evidence, not evidence of absence, and
   cannot support a frequency claim about where disputes arise.

There is a fourth, structural problem: the eleven events were chosen because they were
public. Controversy is the selection criterion, so the sample cannot be used to argue
about where controversy occurs.

## What replaces it

Nothing in the manuscript. The Review presents no figure and no tally. The argument
about dispute rates is now made qualitatively and is framed as a hypothesis to be
tested by a design that fixes the regime definition in advance, records `na` as its
own category, and does not select cases by notoriety. The pre-registration under
`census_prereg.md` is itself marked **withdrawn**, because its P1 prediction (machine
dispute rate 0) is contradicted by row 4, a machine-graded event that *did* produce a
dispute.

## How to use this folder now

- `python checks/figure1.py` still renders `figure1.png` / `figure1.pdf` for archival
  comparison. It now prints the withdrawal notice on the figure face and refuses to
  assert the 1/6 and 3/5 tallies as findings. The committed `figure1.png` and
  `figure1.pdf` are the **old** renders, made before the withdrawal stamp existed, so
  they do not carry the notice. Re-render to refresh them; the script needs matplotlib
  for the drawing step and says so, then exits cleanly, while its data check runs either way.
- `python checks/table1_tally.py` re-derives the historical arithmetic *as history*.
  It is a check on the archive, not a validation of any claim in the Review.
- Do not cite any number in this file from the Review, the Synopsis, or any derived
  document.
