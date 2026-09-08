# Proofs

<!-- L0 -->
<!-- dual -->
**The idea in a line:** A proof is an argument that compels — from accepted truths, each step forced, to a conclusion that cannot be denied; examples suggest, proofs settle.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

- **A proof**: a finite chain from axioms through allowed rules to the conclusion. Natural deduction / sequent calculus (Gentzen 1935) formalize what "allowed rule" means.
- **Soundness & completeness**: first-order logic proves exactly the statements true in every model (Gödel 1929–30).
- **Incompleteness** (Gödel 1931): any consistent system strong enough for arithmetic has true statements it cannot prove.
- **Four proof forms**: direct; contradiction (assume the negation, derive nonsense); induction ($P(1)$ and $P(n) \Rightarrow P(n+1)$ give all $n$); counterexample (one is enough).

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

"3, 5, 7 are prime and odd, so all primes are odd" — true for every prime you'll ever name, except 2. A billion confirming cases prove nothing; one counterexample destroys everything. That asymmetry is why mathematics runs on proof, not polling. The tool kit is small: argue directly, suppose the opposite and crash into a wall, knock down dominoes, or find the single counterexample.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- Every proof is **conditional on its axioms**: Euclidean vs non-Euclidean geometry differ in one axiom, and both are consistent — different premises, different theorems, no contradiction.
- The **logic** is a premise too: proof by contradiction (excluded middle) is rejected in intuitionistic logic — the same statement can be provable classically and unprovable constructively.
- **Induction needs a well-ordered set** — it works on $\mathbb{N}$, not on $\mathbb{R}$.
- A proof proves only what it actually assumes; change a hidden assumption (as in [Monty Hall](../famous_problems/monty_hall.md)) and the theorem silently becomes false.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- Contradiction: the $\sqrt{2}$ proof in [numbers](numbers.md) — the contradiction is "a fraction wasn't in lowest terms".
- Induction: show $P(1)$, and $P(n) \Rightarrow P(n+1)$ — the dominoes all fall.
- Counterexample: 2 is prime and even. Done.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **~300 BCE**: Euclid's *Elements* — the axiomatic method as a standard: definitions, axioms, proofs, for 2,000 years the model of certainty.
- **1900–1931**: Hilbert's program — prove mathematics consistent from within — meets Gödel's incompleteness theorems. The program dies; the limits of proof become a field.
- **1935**: Gentzen's natural deduction — proof itself becomes an object of mathematics.
- **1967**: de Bruijn's Automath — the first proof assistant; the lineage runs through Coq, Isabelle, and [this folder's Lean files](../lean/README.md), where the compiler is the referee.
- **1976**: Appel–Haken's four-color theorem — 1,834 cases checked by machine, a proof no human has read in full. *Does that count?* The question is still argued.

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

Impossibility results are proofs too: the circle cannot be squared, the halting problem cannot be solved. Cryptography and bridge engineering are the proof method at industrial scale. The open problems in [../famous_problems](../famous_problems/README.md) are exactly the places where no proof has been found — see [Collatz](../famous_problems/collatz.md).

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- "I tried many examples" is evidence, not proof — the number of *unchecked* cases is infinite either way.
- A proof only proves what it actually assumes (see the premises above — the theorem is only as strong as its axioms).
- "No proof yet" ≠ "no proof exists" — between "true" and "provable" there is a permanent gap (Gödel, above).

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手: Gödel, K. (1931). "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I." *Monatshefte für Mathematik und Physik* 38, 173–198. <https://doi.org/10.1007/BF01700692>
- 一手: Gentzen, G. (1935). "Untersuchungen über das logische Schließen." *Mathematische Zeitschrift* 39, 176–210. <https://doi.org/10.1007/BF01201353>
- 一手: Appel, K., Haken, W. (1977). "Every planar map is four colorable. Part I: Discharging." *Illinois Journal of Mathematics* 21(3), 429–490. <https://doi.org/10.1215/ijm/1256049011>
- 一手: de Bruijn, N. G. (1968). "Automath, a language for mathematics." TH Eindhoven technical report. 无稳定在线链接.

<!-- L5-end -->