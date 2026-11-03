# `archive/` — superseded generated drafts (withdrawn)

**Status: SUPERSEDED. Retained as a version archive only.**
Do not cite, do not resubmit, do not restore to `manuscripts/`.
Nothing on this page is a claim of the Nature Review.

## What this directory is

The four generated files from the previous, pre-Restructuring draft pair, kept
verbatim so the revision history is auditable rather than reconstructed from memory.

| File | Bytes | Blob (at `e73da6d`) | Built from |
| --- | --- | --- | --- |
| `comment_EN.md` | 16,975 | `27347ef` | `comment_draft.md` (short form) |
| `comment_ZH.md` | 10,372 | `55782e0` | `comment_draft.md` (short form) |
| `paper_EN.md` | 113,862 | `e488672` | `ai_and_math.md` (full form) |
| `paper_ZH.md` | 101,404 | `786a7f9` | `ai_and_math.md` (full form) |

## Provenance

All four are byte-identical to their state in commit `e73da6d`, verified with
`git hash-object` after extraction. They were originally added in `a58c53c` and
were **deleted** in `29c790b` (current `HEAD`).

Recover or re-verify at any time with:

```
git archive --format=tar -o oldman.tar e73da6d math_clarification/essays/submission/manuscripts/
tar -xf oldman.tar
```

Do not use `git restore --source=HEAD` or `git checkout HEAD --` for these paths:
`HEAD` no longer contains them, so both commands fail with
`error: pathspec ... did not match any file(s) known to git`. That failure is the
expected behaviour, not a repository fault.

## Why they were superseded

These drafts carry the withdrawn empirical apparatus and the pre-Review framing:

1. **The eleven-event census and its headline tally.** The `1/6` versus `3/5`
   split and the Fisher exact *P* ≈ 0.24 are unsound. See
   [`../figure1_data_NOTES.md`](../figure1_data_NOTES.md) for the three disqualifying
   defects, chiefly the FrontierMath `75.7%` misattribution and the silent folding of
   the `na` bin into the community denominator. These files still contain the
   apparatus, defects included, on purpose.
2. **A title and thesis that the rewrite rejected.** `paper_EN.md` argues that the
   2026 events constitute "a crisis of mathematics or of the mathematicians" and
   builds a five-rung sociology on a preliminary census. The Review instead argues
   that what is under renegotiation is the *admissibility* arrangement, and it does
   not rest an argument on a self-selected event list.
3. **No source-of-record discipline.** The present `build_reader.py` writes to
   `manuscripts/` and treats any unrecognised file there as an orphan. Files in this
   directory are outside that guard, which is why archiving here is safe and
   restoring into `manuscripts/` is not.

## What replaced them

| Retired file | Replaced by |
| --- | --- |
| `comment_EN.md`, `comment_ZH.md` | [`../manuscripts/synopsis_EN.md`](../manuscripts/synopsis_EN.md), [`../manuscripts/synopsis_ZH.md`](../manuscripts/synopsis_ZH.md) |
| `paper_EN.md`, `paper_ZH.md` | [`../manuscripts/review_EN.md`](../manuscripts/review_EN.md), [`../manuscripts/review_ZH.md`](../manuscripts/review_ZH.md) |

Sources of record are [`../../ai_and_math.md`](../../ai_and_math.md),
[`../comment_draft.md`](../comment_draft.md) and [`../comment_draft_zh.md`](../comment_draft_zh.md).
Edit those and run `python build_reader.py`; never edit the files in this directory.
