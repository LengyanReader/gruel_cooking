# Census runbook — how to take the instruments from blank to a registered, gated study

> **Status 状态**: Operating procedure for the census kit. **AI-drafted, unreviewed** (harness §I.6). Adds no design; it sequences the files that already carry the design (`census_protocol.md` = the protocol, `census_prereg.md` = the registry wrapper, `census_coding_template.csv` = the blank schema, `census_coder2_packet.md` = the second-coder workflow, `checks/kappa_csv.py` = the reliability gate, `checks/power_fisher.py` = the sample-size table). Everything below is the author's to run; nothing here is a result.

---

## 0 · Files in the kit

| File | Role | State now |
|---|---|---|
| [`census_protocol.md`](census_protocol.md) | the design: frames, queries, endpoint, power, coding rules | complete |
| [`census_prereg.md`](census_prereg.md) | registry-ready wrapper (OSF / asPredicted) | `⟨author⟩` fields open |
| [`census_coding_template.csv`](census_coding_template.csv) | the one canonical schema, blank | header only |
| [`census_pilot_11events.csv`](census_pilot_11events.csv) | **worked exemplar** — coder 1 = a faithful transcription of the parent §11.4 Table 1 into that schema | coder 1 filled, coder 2 empty |
| [`census_coder2_packet.md`](census_coder2_packet.md) | what an independent human second coder is given and does | ready |
| [`census_pilot_paired_DEMO.csv`](census_pilot_paired_DEMO.csv) | **ILLUSTRATIVE smoke test** for the gate — not a reliability measurement | ready |
| [`checks/kappa_csv.py`](checks/kappa_csv.py) | per-column Cohen's κ vs the 0.6 gate | verified (self-test + DEMO) |
| [`checks/power_fisher.py`](checks/power_fisher.py) | exact-enumeration sample size (13/stratum → 82/stratum) | verified |

## 1 · Why a pilot and a DEMO exist (and what they are *not*)

- `census_pilot_11events.csv` shows a real row of the abstract template filled the way the protocol means it: regime mapped M/H/C, Q1–Q5 in the parent's own `+ / − / ±`, `dispute` 0/1, blank cells left **blank** (blank ≠ zero), the split-regime Navier–Stokes row carrying `rule_clause = 11.2(a)`. It is coder 1's coding **already published in the paper**, transcribed — no new facts, no new events.
- `census_pilot_paired_DEMO.csv` is a **fabricated second sheet** whose only job is to prove the gate parses the real column names and drops blanks. It is *not* inter-coder reliability and must never be reported as such.

## 2 · The two commands, and what they print

```
python checks/kappa_csv.py census_pilot_11events.csv       # → "no paired coding columns found", exit 1
python checks/kappa_csv.py census_pilot_paired_DEMO.csv     # → per-column κ table, exit 0
```

The first is the point, not an error: with coder 2 empty the gate **refuses to compute** — the pipeline will not manufacture a κ from a single coder (the circularity the census exists to avoid). The second runs on the real schema and prints, for the DEMO:

```
dispute            n= 11  1.0000  [almost perfect] -> PASS
q1_framing         n= 11  1.0000  [almost perfect] -> PASS
q5_found_or_made   n=  9  1.0000  [almost perfect] -> PASS     (2 blanks dropped)
regime             n= 10  0.8485  [almost perfect] -> PASS     (one C/H divergence, row 3)
```

(The FAIL branch is already proven by `python checks/kappa_csv.py` with no file — its self-test reproduces κ = 0.4318, which fails the gate, matching `checks/kappa.py`.)

## 3 · Sequence to actually run the census (each step is the author's)

1. **Before** collecting anything: complete the `⟨author⟩` fields in [`census_prereg.md`](census_prereg.md) (§2 registry, §7 end date, §8 pilot counts) and **deposit it** so the timestamp precedes coding. Do not deposit after opening a post-registration leaderboard snapshot.
2. Enumerate the three frames (census_protocol §3); log every query with date and hit count. Build PRISMA counts.
3. Code coder 1 into a copy of `census_coding_template.csv` using the parent §11.2 rule and §11.3 cards **unchanged** (the pilot is the format model).
4. Recruit a **human** coder 2; give them only the packet + event list (blind), never coder 1's sheet ([`census_coder2_packet.md`](census_coder2_packet.md) §2).
5. Emit a paired CSV (WIDE `NAME_a/NAME_b` or LONG `column,coder_a,coder_b`) and run `python checks/kappa_csv.py paired.csv`. Any reliability column < 0.6 is reported descriptively, not pushed into the primary analysis; recode-to-raise-κ is forbidden (packet §6).
6. Only if the gated columns clear 0.6: run the pre-declared one-sided Fisher (M vs C) and the Cochran–Armitage trend (power_fisher.py / census_protocol §6). Report a P1 failure with the same prominence as a confirmation (prereg §13).

## 4 · What this staging does *not* settle

Registration, human recruitment, and collection are outside anything a draft can do. This kit makes the study executable and auditable as a design; it does not, and must not, pretend the census has run. Until it has, the Comment's candour paragraph stays exactly as worded: descriptive, P ≈ 0.24, publicity-selected.
