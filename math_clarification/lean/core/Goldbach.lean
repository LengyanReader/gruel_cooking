/-! # Goldbach & twin primes — stated, not (yet) provable

Statements for `../famous_problems/goldbach_and_twin_primes.md`.

The two conjectures carry `sorry` — they are OPEN. The small proofs
below them (3 and 7 are prime, 10 = 3 + 7, 2 is the even prime, 9 is
not prime) are real, kernel-checked proofs.

Core Lean only, no imports. Check with: `lean Goldbach.lean`
-/

-- A self-contained definition of primality (equivalent to the
-- standard one; the bound `m ≤ n` keeps the quantification finite).
def Prime (n : Nat) : Prop :=
  2 ≤ n ∧ ∀ m : Nat, m ≤ n → m ∣ n → m = 1 ∨ m = n

-- OPEN: every even number ≥ 4 is a sum of two primes (Goldbach, 1742).
theorem goldbach_conjecture :
    ∀ n : Nat, 4 ≤ n → n % 2 = 0 → ∃ p q : Nat, Prime p ∧ Prime q ∧ n = p + q := by
  sorry

-- OPEN: infinitely many twin primes.
theorem twin_prime_conjecture :
    ∀ b : Nat, ∃ n : Nat, b < n ∧ Prime n ∧ Prime (n + 2) := by
  sorry

-- Verified: 2 is prime — the counterexample that destroys "all primes
-- are odd" (see `../basics/proofs.md`).
theorem prime_two : Prime 2 := by
  constructor
  · omega
  · intro m hm hdiv
    rcases hdiv with ⟨k, hk⟩
    have hm0 : m ≠ 0 := by
      intro hz
      have : 0 ∣ 2 := ⟨k, by simpa [hz] using hk⟩
      have : 2 = 0 := Nat.eq_zero_of_zero_dvd this
      omega
    have hcases : m = 1 ∨ m = 2 := by omega
    rcases hcases with h1 | h2
    · left; exact h1
    · right; exact h2

-- Verified: 3 is prime.
theorem prime_three : Prime 3 := by
  constructor
  · omega
  · intro m hm hdiv
    rcases hdiv with ⟨k, hk⟩
    have hm0 : m ≠ 0 := by
      intro hz
      have : 0 ∣ 3 := ⟨k, by simpa [hz] using hk⟩
      have : 3 = 0 := Nat.eq_zero_of_zero_dvd this
      omega
    have hcases : m = 1 ∨ m = 2 ∨ m = 3 := by omega
    rcases hcases with h1 | h2 | h3
    · left; exact h1
    · right; subst m; omega
    · right; subst m; omega

-- Verified: 7 is prime.
theorem prime_seven : Prime 7 := by
  constructor
  · omega
  · intro m hm hdiv
    rcases hdiv with ⟨k, hk⟩
    have hm0 : m ≠ 0 := by
      intro hz
      have : 0 ∣ 7 := ⟨k, by simpa [hz] using hk⟩
      have : 7 = 0 := Nat.eq_zero_of_zero_dvd this
      omega
    have hcases : m = 1 ∨ m = 2 ∨ m = 3 ∨ m = 4 ∨ m = 5 ∨ m = 6 ∨ m = 7 := by omega
    rcases hcases with h1 | h2 | h3 | h4 | h5 | h6 | h7
    · left; exact h1
    · right; subst m; omega
    · right; subst m; omega
    · right; subst m; omega
    · right; subst m; omega
    · right; subst m; omega
    · right; subst m; omega

-- Verified: 9 is *not* prime — trial divisors exist.
theorem not_prime_nine : ¬ Prime 9 := by
  intro h
  have hle : 3 ≤ 9 := by omega
  have hdiv : 3 ∣ 9 := ⟨3, rfl⟩
  have : 3 = 1 ∨ 3 = 9 := h.2 3 hle hdiv
  omega

-- A verified Goldbach split: 10 = 3 + 7.
example : ∃ p q : Nat, Prime p ∧ Prime q ∧ 10 = p + q := by
  exact ⟨3, 7, prime_three, prime_seven, rfl⟩
