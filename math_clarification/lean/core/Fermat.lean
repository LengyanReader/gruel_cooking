/-! # Fermat's Last Theorem — stated, and the n = 2 contrast checked

Companion to `../famous_problems/fermat_last_theorem.md`.

FLT was proved by Wiles (1995) — the statement below carries `sorry`
deliberately: this file does not pretend to contain a ~100-page detour
through elliptic curves. What the kernel *does* check here: squares
are abundant (3² + 4² = 5²), and the near-miss 6³ + 8³ = 9³ − 1 shows
why "just misses" is not a counterexample.

Core Lean only, no imports. Check with: `lean Fermat.lean`
-/

-- Wiles, 1995. Stated with `sorry` by design — not formalized here.
theorem fermat_last_theorem :
    ∀ n a b c : Nat, 3 ≤ n → 0 < a → 0 < b → 0 < c → a^n + b^n ≠ c^n := by
  sorry

-- For squares, solutions are everywhere — the smallest Pythagorean
-- triple, verified exactly.
example : 3^2 + 4^2 = 5^2 := by
  native_decide

-- Cubes: the famous near-miss. 6³ + 8³ = 728, and 9³ = 729 —
-- off by exactly one, which is why no amount of poking finds a cube.
example : 6^3 + 8^3 = 729 - 1 := by
  native_decide

example : 6^3 + 8^3 ≠ 9^3 := by
  native_decide
