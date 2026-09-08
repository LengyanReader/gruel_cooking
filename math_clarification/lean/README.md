# lean — The Appendix: Machine-Checked Statements (Lean 4)

## Role in this folder (角色)

The prose entries carry the real content — the statement, the analogy, the premises, the history. This folder is the **referee, not the teacher**. Its two jobs:

1. **Pin the premises** (前提钉扎). Lean forces every assumption to appear explicitly in a theorem statement. The Monty Hall premise "the host knows the car and never reveals it" cannot be smuggled in silently; the birthday assumption "independent, uniformly distributed" is a visible hypothesis; Euler's "connected, 0 or 2 odd vertices" is spelled out. This is the part that matches the folder's core mission — a claim's premises and conditions of validity — and it is the one thing Lean does that prose cannot enforce.
2. **Referee the computable claims** (小结论裁判). Exact arithmetic — birthday probabilities, paper folds, brute-forced Königsberg orderings — checked by the kernel, eliminating "did I compute this right?"

What Lean does **not** do here, by design: no analogies, no historical narrative, no survey of failed approaches, no formalization of the FLT proof (a multi-year research project on its own). Open conjectures are *stated* — precisely — with `sorry`, and only in these files.

## Structure

- **`core/`** — files using only Lean 4's built-in library (no Mathlib). Check any file with `lean <file>.lean` — no project needed. The proofs are real: exact rational arithmetic, verified by the kernel.
- **`mathlib/`** — files that need [Mathlib](https://github.com/leanprover-community/mathlib4) (the main math library). These live in a `lake` project; see below. Optional tier.

## What is stated & checked where

| Entry | File | What the machine sees |
|---|---|---|
| [Growth](../basics/growth.md) | `core/Growth.lean` | 41 paper folds fall short of the Moon, 42 reach it — exactly |
| [Birthday paradox](../famous_problems/birthday_paradox.md) | `core/Birthday.lean` | $P(\text{shared birthday}, 23\ \text{people}) > 1/2$; fixed-date version needs 253 people — exact rationals |
| [Monty Hall](../famous_problems/monty_hall.md) | `core/MontyHall.lean` | $P(\text{car} \mid \text{switch}) = 2/3$ — and the random-host variant is exactly $1/2$: the host's knowledge, quantified |
| [Collatz](../famous_problems/collatz.md) | `core/Collatz.lean` | The function and the conjecture (stated, **not** provable); 27's orbit computed |
| [Goldbach & twin primes](../famous_problems/goldbach_and_twin_primes.md) | `core/Goldbach.lean` | The two open conjectures (stated); $10 = 3 + 7$ verified with a real proof of primality |
| [Königsberg](../famous_problems/konigsberg_bridges.md) | `core/Konigsberg.lean` | All $7! = 5040$ orderings fail; add one bridge and a trail exists — search confirms what Euler's degree theorem predicts |
| [Fermat](../famous_problems/fermat_last_theorem.md) | `core/Fermat.lean` | FLT stated (Wiles 1995, unformalized); $3^2 + 4^2 = 5^2$ and the near-miss $6^3 + 8^3 = 9^3 - 1$ checked |
| [Numbers](../basics/numbers.md) | `mathlib/Sqrt2.lean` | $\sqrt{2}$ is irrational |
| [Infinity](../basics/infinity.md) | `mathlib/Infinity.lean` | $0.999\ldots = 1$ as a geometric series |

## Checking the core files

With `lean` on PATH (see Install below):

```bash
cd math_clarification/lean/core
lean Growth.lean      # silence = success; anything printed is an error
lean Birthday.lean
lean MontyHall.lean
lean Collatz.lean
lean Goldbach.lean
lean Konigsberg.lean
lean Fermat.lean
```

**Verification record**: all 7 core files compile clean under Lean 4.33.1 (2026-09-06) — 0 errors. The only warnings are the intentional `sorry`s on the open conjectures (Collatz, Goldbach, twin primes, FLT) and three linter style notes in Goldbach.lean.

## Checking the mathlib files

Mathlib needs a `lake` project (it is a large library, fetched from its own cache):

```bash
cd math_clarification/lean
lake new mathlib_check math      # one-time scaffold
cd mathlib_check
lake update                      # fetches Mathlib (several GB the first time)
cp ../mathlib/*.lean MathlibCheck/  # or wherever sources live
lake build
```

Or, in an editor: open the folder with the Lean 4 VS Code extension (`lean4`), which drives the same checks interactively.

## Install

- **Via elan (recommended, per-user, no admin):** `https://leanprover-community.github.io/install/` — installs `lean`, `lake`, and `elan` under `%USERPROFILE%\.elan`.
- **Via conda:** the `lean4` package is *not* on conda-forge at the time of writing; use elan.

## House rules for this folder

1. Core files must not import Mathlib — anything else can.
2. Conjectures are stated with `theorem ... := by sorry` and a loud `-- OPEN` comment; `sorry` in a *verified* proof is forbidden — the compiler refuses to be polite about it.
3. Every file starts with a comment pointing back to its prose entry.
