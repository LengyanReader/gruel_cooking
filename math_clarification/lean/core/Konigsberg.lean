/-! # Bridges of Königsberg — the impossible walk, machine-checked

Companion to `../famous_problems/konigsberg_bridges.md`.

Euler's insight was *not* to search routes — he counted degrees. Here
the machine does the thing Euler refused to do (search every ordering)
and confirms the verdict, while the degree counts carry the real
theorem: at most two vertices may have odd degree.

The four landmasses are 1, 2, 3, 4. The seven bridges: 1–2 twice,
1–3 twice, 1–4 once, 2–4 once, 3–4 once (degrees 5, 3, 3, 3).

Core Lean only, no imports. Check with: `lean Konigsberg.lean`
-/

def edge : Nat → Nat × Nat
  | 0 => (1, 2)
  | 1 => (1, 2)
  | 2 => (1, 3)
  | 3 => (1, 3)
  | 4 => (1, 4)
  | 5 => (2, 4)
  | _ => (3, 4)

-- The 8th bridge for the walkable variant below: 2–3.
def edge8 : Nat → Nat × Nat
  | 7 => (2, 3)
  | i => edge i

def sharesVertex (e1 e2 : Nat × Nat) : Bool :=
  e1.1 = e2.1 || e1.1 = e2.2 || e1.2 = e2.1 || e1.2 = e2.2

-- A trail is valid when it can actually be *walked*: standing at a
-- vertex v, the next bridge must be incident to v, and crossing it
-- moves you to its other end. (Merely sharing a vertex is not enough:
-- consecutive edges sharing the "wrong" vertex strand the walker.)
def walkFrom (v : Nat) : List Nat → Bool
  | [] => true
  | a :: rest =>
      let e := edge a
      if e.1 = v then walkFrom e.2 rest
      else if e.2 = v then walkFrom e.1 rest
      else false

-- Try both ends of the first bridge as the starting point.
def validTrail (p : List Nat) : Bool :=
  match p with
  | [] => true
  | a :: _ => walkFrom (edge a).1 p || walkFrom (edge a).2 p

def walkFrom8 (v : Nat) : List Nat → Bool
  | [] => true
  | a :: rest =>
      let e := edge8 a
      if e.1 = v then walkFrom8 e.2 rest
      else if e.2 = v then walkFrom8 e.1 rest
      else false

def validTrail8 (p : List Nat) : Bool :=
  match p with
  | [] => true
  | a :: _ => walkFrom8 (edge8 a).1 p || walkFrom8 (edge8 a).2 p

-- All permutations of a list (insert x in every position, recursively).
def insertAll (x : Nat) : List Nat → List (List Nat)
  | [] => [[x]]
  | y :: ys => (x :: y :: ys) :: (insertAll x ys).map (fun zs => y :: zs)

def perms : List Nat → List (List Nat)
  | [] => [[]]
  | x :: xs => (perms xs).flatMap (insertAll x)

-- The degree counts — Euler's theorem in one line each: all four are odd.
def degree (v : Nat) : Nat :=
  (List.range 7).countP (fun i => (edge i).1 = v || (edge i).2 = v)

example : degree 1 = 5 := by native_decide
example : degree 2 = 3 := by native_decide
example : degree 3 = 3 := by native_decide
example : degree 4 = 3 := by native_decide

-- Brute force: none of the 7! = 5040 orderings is a valid trail.
example : (perms (List.range 7)).all (fun p => !validTrail p) = true := by
  native_decide

-- Add one bridge (2–3): degrees become 5, 4, 4, 3 — exactly two odd —
-- and a valid trail exists (found by exhaustive search).
example : (perms (List.range 8)).any validTrail8 = true := by
  native_decide
