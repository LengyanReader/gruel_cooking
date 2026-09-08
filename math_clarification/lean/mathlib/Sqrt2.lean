import Mathlib

/-! # √2 is irrational — machine-checked

Companion to `../basics/numbers.md`. Needs a Mathlib `lake` project
(see `../README.md`); not executable with the core toolchain alone.

Mathlib carries the classical parity proof; the theorem name *is* the
one-liner. The prose entry tells the same argument in words; here it
is settled.

(Not executed in this environment — no Mathlib project is set up yet.
`irrational_sqrt_two` is a long-standing Mathlib name; if it moves,
`#check irrational_sqrt_two` will point to the current one.)
-/

example : Irrational (Real.sqrt 2) := by
  exact irrational_sqrt_two

-- The same fact in the form the prose tells it: no square is twice a
-- square. (Equivalent to the above: p² = 2q² would make p/q a rational
-- square root of 2.) Left as a stated corollary — uncomment once a
-- Mathlib project is available and fill the two-line equivalence:
--
-- example : ¬ ∃ p q : ℕ, q ≠ 0 ∧ p * p = 2 * q * q := by
--   rintro ⟨p, q, hq, h⟩
--   have hsqrt : ((p : ℝ) / q) ^ 2 = 2 := by
--     field_simp [hq]
--     norm_num [h] ...
--   -- (p/q)² = 2 makes p/q a rational root of x² − 2; both real roots
--   -- are √2 and −√2, both irrational.
