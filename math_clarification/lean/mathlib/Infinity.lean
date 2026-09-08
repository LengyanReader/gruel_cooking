import Mathlib

/-! # Infinity & limits — 0.999… = 1

Companion to `../basics/infinity.md`. Needs a Mathlib `lake` project
(see `../README.md`); not executable with the core toolchain alone.

Two readings of 0.999…, both stated here:
1. Finite truncations: the n-th term is exactly 1 − 1/10ⁿ — the gap
   is never zero, and it vanishes without bound.
2. The infinite series: 9/10 + 9/100 + 9/1000 + … = 1, the geometric
   series. That is what "0.999… = 1" *means*: the destination of the
   partial sums, not a last step.

(Not executed in this environment — no Mathlib project is set up yet.
If a lemma name differs in your Mathlib version, `#check` the names
used below and adjust; the statements themselves are stable.)
-/

-- n decimal digits of 0.999…, exactly.
def nineN (n : ℕ) : Rat := ((10 : ℕ) ^ n - 1) / (10 : ℕ) ^ n

-- The n-th term leaves a gap of exactly 1/10ⁿ.
theorem nineN_gap (n : ℕ) : 1 - nineN n = 1 / ((10 : ℕ) ^ n : Rat) := by
  have hne : ((10 : ℕ) ^ n : Rat) ≠ 0 := by
    exact pow_ne_zero n (by norm_num : (10 : Rat) ≠ 0)
  field_simp [nineN, hne]
  ring

-- As a true infinite series: 0.999… = 1.
example : (∑' k : ℕ, (9 / 10 : ℝ) * (1 / 10 : ℝ) ^ k) = 1 := by
  have hgeo : (∑' k : ℕ, (1 / 10 : ℝ) ^ k) = (1 - (1 / 10 : ℝ))⁻¹ :=
    tsum_geometric_of_norm_lt_one (by norm_num)
  -- Pull the constant 9/10 out of the series, then  (9/10) · (10/9) = 1.
  simpa [tsum_mul_left] using congrArg (fun t : ℝ => (9 / 10 : ℝ) * t) hgeo
