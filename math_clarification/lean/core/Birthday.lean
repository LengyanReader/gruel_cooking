/-! # Birthday paradox — 23 people, machine-checked

Exact computation of the claim in `../famous_problems/birthday_paradox.md`.

P(no shared birthday among n people) = ∏_{k=1}^{n-1} (365 − k)/365,
computed in exact rationals (`Rat`), so the proofs below are rigorous
arithmetic — not floating-point fudging.

Core Lean only, no imports. Check with: `lean Birthday.lean`
-/

-- P(no match) among n people: product over k = 1 .. n-1.
def noMatchAux : Nat → Rat
  | 0 => 1
  | k + 1 => ((365 - (k + 1) : Nat) : Rat) / 365 * noMatchAux k

def noMatchProb (n : Nat) : Rat := noMatchAux (n - 1)

-- P(everyone misses *my* fixed birthday): (364/365)^n for n others.
def myBirthdayMiss : Nat → Rat
  | 0 => 1
  | k + 1 => (364 : Rat) / 365 * myBirthdayMiss k

-- With 23 people, a shared birthday is already more likely than not…
example : noMatchProb 23 < (1 : Rat) / 2 := by
  native_decide

-- …because P(no match) is ≈ 0.4927, not some number near 0.
example : noMatchProb 23 > (49 : Rat) / 100 := by
  native_decide

-- The engine: 23 people make 253 *pairs*, not 23 chances.
example : 23 * 22 / 2 = 253 := by
  native_decide

-- The fixed-date question is genuinely different: sharing *my*
-- birthday needs 253 people, not 23.
example : myBirthdayMiss 252 > (1 : Rat) / 2 := by
  native_decide

example : myBirthdayMiss 253 < (1 : Rat) / 2 := by
  native_decide

-- By 50 people the shared-birthday chance is past 97%.
example : noMatchProb 50 < (3 : Rat) / 100 := by
  native_decide
