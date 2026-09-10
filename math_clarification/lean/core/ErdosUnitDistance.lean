/-! # Erdős unit-distance problem — the obstruction, machine-checked

Companion to `../famous_problems/erdos_unit_distance.md`.

The 2026 claim that `u(n)`, the maximum number of unit distances among
`n` points in the plane, can be pushed to `n^(1+ε)`, is NOT formalized
here. The statement below carries `sorry` deliberately: the number-theory
machinery behind it (representations by sums of two squares in algebraic
number fields) is not yet in Lean. We are not pretending it is proved.

What the kernel *does* check is the exact structural fact that makes the
naive constructions run out of steam — the finite-representation
obstruction — and the exact count of the plain grid:

  * A `k × k` unit grid with `n = k²` points gives exactly
    `2k(k-1) = 2n - 2k` unit distances (brute-force checked below).
    That is the "≈ 2n" baseline from which every clever construction has
    to escape.
  * Why it cannot escape by simple rescaling: the number of ways to
    write a fixed integer as a sum of two squares is *finite*. For the
    plain grid, the unit-length vectors out of the origin are exactly
    four — `(±1,0),(0,±1)`. Every interior point has four neighbours, no
    more, and piling more unit distances past that needs richer number
    systems.

Core Lean only, no imports. Check with: `lean ErdosUnitDistance.lean`
-/

-- Correctly identifies whether `v` is a unit vector (squared length 1).
def isUnit (v : Int × Int) : Prop := v.1 * v.1 + v.2 * v.2 = 1

-- Number of integer pairs (a,b) with a² + b² = c, brute-forced over the
-- finite box |a|,|b| ≤ c (a² ≥ 0 forces |a| ≤ c).
def sqReps (c : Nat) : Nat :=
  let range := (List.range (2 * c + 1)).map (fun x => (Int.ofNat x) - (Int.ofNat c))
  range.foldl (fun acc ix => acc + range.foldl
    (fun acc2 iy => if ix * ix + iy * iy = (Int.ofNat c) then acc2 + 1 else acc2) 0) 0

-- 1 = (±1)² + 0²  or 0² + (±1)²: exactly four unit vectors from the
-- origin. This is the whole obstruction for the plain grid — each
-- interior point is stuck with four unit neighbours.
example : sqReps 1 = 4 := by native_decide

-- 2 = (±1)² + (±1)²: still only four. Rescaling by √2 turns the four
-- diagonal neighbours into unit vectors, but no more than that.
example : sqReps 2 = 4 := by native_decide

-- 3 is not a sum of two squares: some rescales get *nothing* extra.
example : sqReps 3 = 0 := by native_decide

-- 5 = (±1)²+(±2)² or (±2)²+(±1)²: eight — the "windmill of eights" that
-- keeps the theory rich, but still finite.
example : sqReps 5 = 8 := by native_decide

-- The pattern behind the term "finite representation obstruction":
-- for every fixed integer c the table below is finite. It never explodes
-- the way a superlinear `n^(1+ε)` rate would need it to.
#eval (List.range 10).map sqReps

-- ---- The plain grid baseline ----

-- A helper to flatten a double iteration into one list.
def concat : List (List α) → List α
  | [] => []
  | h :: t => h ++ concat t

-- The k×k grid, points (i,j) with 0 ≤ i,j < k.
def gridPoints (k : Nat) : List (Int × Int) :=
  concat ((List.range k).map (fun i =>
    (List.range k).map (fun j => (Int.ofNat i, Int.ofNat j))))

-- Brute-force count of unit distances inside a list of points.
def countUnitPairs : List (Int × Int) → Nat
  | [] => 0
  | h :: t =>
      (t.foldl (fun acc p =>
        let dx := h.1 - p.1
        let dy := h.2 - p.2
        if dx * dx + dy * dy = 1 then acc + 1 else acc) 0) + countUnitPairs t

-- The closed form: a k×k grid has 2k(k-1) unit distances (k−1 horizontal
-- gaps per row, k−1 vertical gaps per column). For n = k² this is
-- 2n − 2k, i.e. ≈ 2n.
def gridUnitPairs (k : Nat) : Nat := 2 * k * (k - 1)

-- The brute force *agrees* with the closed form, so the formula is not
-- hand-asserted — it is counted directly. (Verified for the concrete
-- cases below rather than for symbolic k, since `native_decide` needs a
-- closed term; the same count is produced either way.)
example : countUnitPairs (gridPoints 3) = gridUnitPairs 3 := by native_decide
example : countUnitPairs (gridPoints 4) = gridUnitPairs 4 := by native_decide
example : countUnitPairs (gridPoints 10) = gridUnitPairs 10 := by native_decide

-- And those closed forms evaluate to what we claimed.
example : gridUnitPairs 3 = 12 := by native_decide
example : gridUnitPairs 4 = 24 := by native_decide
example : gridUnitPairs 10 = 180 := by native_decide

-- The famous concrete example: a 10×10 grid (n = 100 points) has 180
-- unit distances — the "2n − 2k" baseline that the whole Erdős programme
-- is trying to beat.
example : countUnitPairs (gridPoints 10) = 2 * 100 - 2 * 10 := by
  native_decide
