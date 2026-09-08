/-! # Monty Hall — the host's knowledge, quantified

Machine-checked version of `../famous_problems/monty_hall.md`.

You pick door 1. Outcomes are (car, hostOpens) with exact weights.

Variant A — the real game: the host knows the car and *never* opens it.
  (1,2) : 1/6   (1,3) : 1/6   (2,3) : 1/3   (3,2) : 1/3
Given the host opened 3, P(car behind 1) = 1/3, so switching wins with
probability 2/3.

Variant B — the trap: the host opens a *random* un-picked door and it
merely happens to be a goat (the cases where he shows the car are
excluded, as in the real show). The weights become
  (1,2) : 1/6   (1,3) : 1/6   (2,3) : 1/6   (3,2) : 1/6
and now, conditioned on "he opened a goat door", it genuinely is 50/50.
The host's knowledge is the entire trick.

Core Lean only, no imports. Check with: `lean MontyHall.lean`
-/

def gameA : List (Nat × Nat × Rat) :=
  [(1, 2, 1 / 6), (1, 3, 1 / 6), (2, 3, 1 / 3), (3, 2, 1 / 3)]

def gameB : List (Nat × Nat × Rat) :=
  [(1, 2, 1 / 6), (1, 3, 1 / 6), (2, 3, 1 / 6), (3, 2, 1 / 6)]

-- P(event) = sum of weights of the outcomes satisfying `event`.
def prob (g : List (Nat × Nat × Rat)) (event : Nat × Nat → Bool) : Rat :=
  g.foldl (fun acc (car, host, w) => if event (car, host) then acc + w else acc) 0

-- Variant A, the real game: given the host opened door 3, the car is
-- behind your door 1 only 1/3 of the time…
example : prob gameA (fun o => o.1 = 1 && o.2 = 3) / prob gameA (fun o => o.2 = 3) = (1 : Rat) / 3 := by
  native_decide

-- …so the other closed door wins 2/3 of the time: switching doubles
-- your chances.
example : prob gameA (fun o => o.1 ≠ 1 && o.2 = 3) / prob gameA (fun o => o.2 = 3) = (2 : Rat) / 3 := by
  native_decide

-- Variant B, the trap: with a lucky random host it really is 50/50.
example : prob gameB (fun o => o.1 = 1 && o.2 = 3) / prob gameB (fun o => o.2 = 3) = (1 : Rat) / 2 := by
  native_decide

-- The two games differ in the *marginal* too: in game A the host opens
-- door 3 half the time; in game B only 1/3 of the time — the other 1/3
-- of the time he would have opened the car door and spoiled the game
-- (those outcomes are excluded by "it happens to be a goat").
example : prob gameA (fun o => o.2 = 3) = (1 : Rat) / 2 := by
  native_decide

example : prob gameB (fun o => o.2 = 3) = (1 : Rat) / 3 := by
  native_decide
