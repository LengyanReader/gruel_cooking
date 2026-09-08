# Collatz

<!-- L0 -->
<!-- dual -->
**The idea in a line:** Take any number: if even, halve it; if odd, triple it and add 1. Every number ever tried falls to 1 — but proving that for *all* numbers is open: trivial rules, wild behavior.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

Define $f: \mathbb{N} \to \mathbb{N}$ by $f(n) = n/2$ if $n$ is even, $f(n) = 3n + 1$ if $n$ is odd.

**Conjecture (Collatz, 1937)**: for every $n \geq 1$ there is a $k$ with $f^k(n) = 1$ (equivalently: every orbit reaches the cycle $1 \to 4 \to 2 \to 1$). **Open.** Verified computationally for every $n \leq 2^{68}$ (Barina 2021).

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

$6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$. One line of rules. Now try 27: it climbs past 9,000 (reaching 9,232 at step 77), wanders for 111 steps, and falls to 1. Nobody has found a number that escapes to infinity or falls into a different loop — the rule has been run on every starting point up to $2^{68}$ — and yet nobody can prove there isn't one. The statement is the easy part; the orbit of 27 is the warning.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- The conjecture is about **this exact function**. The "3" and the "+1" are load-bearing: $3n - 1$ has other cycles ($5 \to 14 \to 7 \to 20 \to 10 \to 5$); $5n + 1$ has orbits that look divergent. Tiny changes in the premises change the verdict entirely.
- A counterexample would be one of exactly two things: a **non-trivial cycle** or an **unbounded orbit**. Nobody knows which kind could exist — or that neither does.
- The standard heuristic (each step multiplies by $\approx 3/4$ on average, so orbits drift down) **assumes the parity pattern is random** — an unproven premise. That assumption is the whole difficulty: the parity pattern is the number itself, in disguise.
- "Verified to $2^{68}$" is evidence, not a premise of truth — see [proofs](../basics/proofs.md).

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- Odd step: $3n + 1$ (even); even steps: divide by 2 — an odd step followed by a halving multiplies by $\approx 3/2$, so drift is governed by how often odd steps occur.
- 27's orbit: 9,232 at step 77, 1 at step 111 (verified in the Lean file).
- Conway's theorem (1972): *generalized* Collatz-like rules (with mod-$m$ branching) can simulate any computation — so for general rules the question is undecidable. The innocent $3n + 1$ sits on the edge of undecidability, and nobody knows which side it's on.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1937**: Lothar Collatz states the problem — orally, in circulation; it acquires a dozen names (Syracuse problem, Ulam's problem, Hasse's algorithm, Kakutani's problem) from its wanderings.
- **1972**: Conway — generalized Collatz systems are universal (they can encode Turing machines): the difficulty is not an accident of presentation.
- **1976/1979**: Terras proves the set of numbers whose orbit dips below their start has density 1 — most numbers behave; "most" is not "all".
- **1985**: Lagarias' survey ("The 3x+1 problem and its generalizations") and his remark that mathematics is not yet ready for such problems — the standard citation for the state of the art.
- **2019**: Tao proves *almost all* orbits get arbitrarily small (in logarithmic density) — the strongest statement ever proven, and still not the conjecture.
- **2021**: Barina publishes verification of all $n \leq 2^{68}$ (announced 2020).
- **Where it stands**: the gap between "almost all" and "all" has swallowed every known method.

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

The cookbook thesis in miniature: complex behavior from simple rules — the same engine as cellular automata, chaos, and complexity science. Also the undecidability neighborhood: Conway's result shows the problem's hardness is structural.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- "$3n + 1$ obviously must fall" — run 27 by hand, then reconsider.
- Checking to $2^{68}$ is evidence, not proof — the set of unchecked numbers is infinite (see [proofs](../basics/proofs.md)).
- "Simple rule ⇒ simple behavior" — the entire field of dynamical systems exists to bury this assumption.

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 存疑/考证点: Collatz 1937 年口头提出，**无原始发表文献** — 猜想经由口头流传进入数学界（首次系统书面陈述见 Lagarias 1985 综述，二手）.
- 一手: Conway, J. H. (1972). "Unpredictable iterations." *Proceedings of the 1972 Number Theory Conference* (Univ. of Colorado, Boulder), 49–52. 无稳定在线链接.
- 一手: Terras, R. (1976). "A stopping time problem on the positive integers." *Acta Arithmetica* 30(3), 241–252. <https://doi.org/10.4064/aa-30-3-241-252>
- 一手: Tao, T. (2019). "Almost all orbits of the Collatz map attain almost bounded values." arXiv:1909.03562 <https://arxiv.org/abs/1909.03562>
- 一手: Barina, D. (2021). "Convergence verification of the Collatz problem." *The Journal of Supercomputing* 77, 2681–2688. <https://doi.org/10.1007/s11227-020-03368-x>

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
**Machine-checked**: [Collatz.lean](../lean/core/Collatz.lean) — the conjecture stated; 27's orbit verified: step 77 hits 9,232, step 111 reaches 1.

<!-- L4-end -->