/-! # Growth — 42 paper folds reach the Moon

Machine-checked companion to `../basics/growth.md`.

A sheet of paper is 0.1 mm = 100 µm thick; after n folds its thickness is
100 · 2ⁿ µm, kept in exact natural numbers — no floats. Mean Earth–Moon
distance ≈ 384 400 km = 384 400 000 000 000 µm.

Core Lean only, no imports. Check with: `lean Growth.lean`
-/

def thicknessUm (folds : Nat) : Nat := 100 * 2 ^ folds

def moonDistanceUm : Nat := 384400000000000

-- 41 folds: still short of the Moon.
example : thicknessUm 41 < moonDistanceUm := by
  native_decide

-- 42 folds: past the Moon (≈ 439 805 km). The last doubling did
-- as much work as all previous ones combined.
example : moonDistanceUm ≤ thicknessUm 42 := by
  native_decide

#eval thicknessUm 41
#eval thicknessUm 42

-- The rule of 70: at 7% growth the doubling time is *between* 10 and
-- 11 years (the rule of 70 gives ≈ 10; the truth is ≈ 10.24).
example : ((107 : Rat) / 100) ^ 10 < 2 := by
  native_decide

example : ((107 : Rat) / 100) ^ 11 > 2 := by
  native_decide
