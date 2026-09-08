/-! # Collatz — trivial rules, unproved fate

Formal statement of `../famous_problems/collatz.md`.

The conjecture is *stated* here with `sorry` — it is OPEN since 1937
(computationally verified up to 2^68 by Barina 2020, which is evidence,
not proof). Everything else in this file — the definition and the
verified example orbits — is checked by the kernel.

Core Lean only, no imports. Check with: `lean Collatz.lean`
-/

def collatz (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else 3 * n + 1

-- n after k Collatz steps.
def orbit (k n : Nat) : Nat :=
  match k with
  | 0 => n
  | k + 1 => collatz (orbit k n)

-- OPEN: every positive starting point reaches 1.
theorem collatz_conjecture :
    ∀ n : Nat, 0 < n → ∃ k : Nat, orbit k n = 1 := by
  sorry

-- 27 climbs past 9,000 (step 77) before falling…
example : orbit 77 27 = 9232 := by
  native_decide

-- …and reaches 1 in exactly 111 steps.
example : orbit 111 27 = 1 := by
  native_decide

-- The whole orbit, for the skeptical.
#eval (List.range 112).map (fun k => orbit k 27)

-- The cycle at the bottom: 1 → 4 → 2 → 1.
example : collatz 1 = 4 := by native_decide
example : collatz 4 = 2 := by native_decide
example : collatz 2 = 1 := by native_decide
