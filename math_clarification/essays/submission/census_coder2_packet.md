# Second-coder packet — independent reliability coding for the census

> **Status 状态**: Working instrument for [`census_protocol.md`](census_protocol.md) §5 and §8. **AI-drafted, unreviewed** (harness §I.6). The coder named below must be a **human**: inter-coder reliability is a measure of human judgement agreement, and the protocol's whole point is to test a single unreplicated coder (the Comment's admitted weakest link). This packet adds no design; it operationalises §8.

---

## 1 · Why this packet exists
The census's dispute-vs-regime claim only survives review if the coding is reproducible by a second person. §8 sets the bar: **unweighted Cohen's κ ≥ 0.6 for each reliability-gated column** (regime, Q1–Q5, dispute, novelty screen). A column below 0.6 is reported descriptively and cannot enter the primary analysis. This packet is what a second coder needs to produce that number honestly.

## 2 · What the second coder is given
1. The **event list** (one row per included event) from `census.csv`, with everything *except* the reliability-gated columns filled in (identifiers, producer, date, result_one_line, sources).
2. The **instruments, unchanged**: decision rule §11.2 and coding cards §11.3 of [`../ai_and_math.md`](../ai_and_math.md). No paraphrase is authorised; if a card seems ambiguous, code it as written and note the ambiguity in `divergence_note`, do not improvise a rule.
3. This packet's value-code legend (§4).

The coder fills **only** these columns, independently: `regime`, `q1_framing`…`q5_found_or_made`, `dispute`, `novelty`. They must not see coder 1's sheet until their own is complete (blind, to keep the two codings independent).

## 3 · Coding rules that must not drift (from §5)
- **Regime** fires by ordered decision rule: clauses in order, tie-breakers (a)(b)(c) as written. Record the clause used in `rule_clause`.
- **Dispute = 1** only for a *public, attributable* objection on framing / subset / attribution / admissibility, documented against the event's own record. A producer's own statement of limitations is **not** a dispute.
- Blank ≠ zero: leave a cell empty only if the item genuinely does not apply; empty cells are dropped from that column's κ, not scored as agreement.

## 4 · Value-code legend
| Column | Allowed codes |
|---|---|
| regime | `M` machine-graded · `H` hybrid · `C` community-graded |
| q1_framing … q5_found_or_made | `+` satisfied on record · `−` not satisfied · `±` partial/contested · `n.r.` not recorded |
| dispute | `0` none · `1` documented (then fill `dispute_type`) |
| dispute_type | `framing` · `subset` · `attribution` · `admissibility` · `none` |
| novelty | `new` · `known` · `unresolved` |
| marker | `✓` verified · `◐` company-claim · `○` unconfirmed · `✗` disputed (harness §I.2; appendix/analysis only, never in any manuscript body) |

## 5 · Turning the two sheets into the gate
After **both** coders finish, build one paired CSV (either layout) and run the check. The script is hand-anchored to the same arithmetic as `checks/kappa.py`.

**WIDE layout** (one row per event, each column duplicated per coder):
```
event_id,regime_a,regime_b,dispute_a,dispute_b,novelty_a,novelty_b,q1_framing_a,q1_framing_b,...
1,C,M,0,0,new,new,+,+, ...
```
**LONG layout** (one row per event-per-column) if easier to emit from a merge:
```
column,coder_a,coder_b
regime,C,M
dispute,0,0
novelty,new,new
q1_framing,+,+
```
Then:
```
python checks/kappa_csv.py paired_codings.csv
```
It prints each column's κ with its Landis–Koch band and PASS/FAIL against 0.6, and exits non-zero if any column fails. Run `python checks/kappa_csv.py` with no file to see it reproduce `kappa.py`'s hand-checked 2×2 example (κ = 0.4318 → *fails* the gate), which is the sanity proof that the reader matches the verified arithmetic.

## 6 · After the gate
- **≥ 0.6**: column enters the primary analysis; keep both coders' original labels for the record.
- **< 0.6 or undefined**: do **not** silently recode to reach agreement. Adjudicate by discussion, record every changed cell in `divergence_note`, report the column descriptively with its divergence list, and state in the study that it missed the gate. Raising κ by discussing *after* seeing disagreement is a transparency, not a fix; the honest number is the pre-discussion κ.
- **Amendments**: any proposed change to a coding card after reliability fails is registered **before** recoding the corpus and applied corpus-wide (never event by event), per §5.1.

## 7 · Sign-off
| Role | Name (human) | Date | Sheet file |
|---|---|---|---|
| Coder 1 | ⟨author⟩ | | |
| Coder 2 | ⟨author⟩ | | |
| κ computed by | `python checks/kappa_csv.py …` on | | output archived with `census.csv` |

*Coding is a human act; this packet is scaffolding, not coder 2. A κ produced by a model re-coding its own scheme is exactly the circularity the census exists to avoid.*
