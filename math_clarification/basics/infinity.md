# Infinity & Limits

<!-- L0 -->
<!-- dual -->
**The idea in a line:** Infinity is not a number you reach but a direction: limits say where a sequence is heading — and "how many" itself comes in different sizes.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

- **Limit ($\varepsilon$–$N$)**: $a_n \to L$ means: for *every* $\varepsilon > 0$ there is an $N$ such that $n \geq N \Rightarrow |a_n - L| < \varepsilon$.
- **The infinite sum is defined as that limit**: $\sum a_n = L \iff$ partial sums $s_n \to L$. $1/2 + 1/4 + 1/8 + \cdots = 1$; **$0.999\ldots := \lim (0.9, 0.99, 0.999, \ldots) = 1$**.
- **Sizes**: a set is *countable* if it can be listed ($\mathbb{N}, \mathbb{Z}, \mathbb{Q}$ are; $\mathbb{R}$ is not — Cantor's diagonal argument).
- **The continuum hypothesis** (no size strictly between countable and $\mathbb{R}$) is independent of the standard axioms — Gödel 1938, Cohen 1963.

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

Zeno's arrow: to go 1 meter, go $1/2$, then $1/4$, then $1/8$ … — no last step, yet the total is exactly 1. The arrow arrives. There is no mystery once you see the trick: the *infinite sum* doesn't mean "do infinitely many things", it means "the place the partial totals are heading" — $1/2, 3/4, 7/8, \ldots$ head to 1. A limit is a destination, not a journey. Hotels with infinitely many rooms still have surprises: shift every guest one room up and a new guest fits — infinity + 1 = infinity. But *how many real numbers are there?* Strictly more than the naturals — sizes of infinity exist.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- The infinite sum is *defined as* the limit — no last step is assumed. That definition, not deep philosophy, is what makes Zeno's paradox dissolve.
- $0.999\ldots = 1$ relies on the **completeness of $\mathbb{R}$**. On the hyperreal line (a consistent enlargement of $\mathbb{R}$ with infinitesimals), a version of $0.999\ldots < 1$ holds — the premise differs, the answer differs. The equality is a theorem *about* $\mathbb{R}$.
- Comparing sizes needs a definition: same size $\iff$ a bijection exists. Under it, $\mathbb{Q}$ is countable and $\mathbb{R}$ is not — "bigger" means no list can hold it, nothing more.
- "$\infty - \infty$" is undefined — infinity is a direction, not an entry on the number line.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- Geometric series: $\sum_{k \geq 1} 2^{-k} = 1$ (partial sums $1 - 2^{-n} \to 1$).
- $0.999\ldots = 1$: let $x = 0.999\ldots$; then $10x = 9.999\ldots$; so $10x - x = 9$; hence $x = 1$.
- Cantor's diagonal: given *any* list of decimals, build one differing from the $n$-th entry in the $n$-th digit — it's missing from the list. So no list is complete.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **~450 BCE**: Zeno's paradoxes — motion described by infinite subdivision.
- **Aristotle**: potential vs actual infinity — the distinction that kept infinity out of mathematics for two millennia.
- **1820s**: Cauchy's rigorous limits; Weierstrass' $\varepsilon$–$N$ definition (the modern form).
- **1874/1891**: Cantor — uncountability of $\mathbb{R}$, the diagonal argument, and the hostile reception (Kronecker: "the scientific charlatan") that became the standard story of mathematics resisting its own expansions.
- **1900**: Hilbert's first problem — settle the continuum hypothesis. Gödel (1938) shows it can't be disproved; Cohen (1963) shows it can't be proved. Undecidable: a true *limit on what can be proven* (see [proofs](proofs.md)).

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

All of calculus (the slope and area questions behind [heaven_climate](../../heaven_climate/README.md)'s differential equations), probability over infinite sample spaces, and Gödel's incompleteness theorems.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- Treating $\infty$ as a number: $\infty + 1 = \infty$, but $\infty - \infty$ is meaningless.
- Expecting an infinite process to have a last step — it doesn't; that's why the limit's "closeness" is the definition.
<!-- L4-end -->
<!-- L1 -->
<!-- en -->
- "The hotel is full, therefore nobody fits" — a full *infinite* hotel fits infinitely more. Intuition trained on finite things is exactly what infinity is not.

<!-- L1-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手: Aristotle, *Physics* VI — Zeno 悖论的最早文字记载. 无稳定在线链接（英译本以 Oxford/Hackett 版为准，权威版本）.
- 一手: Cantor, G. (1891). "Über eine elementare Frage der Mannigfaltigkeitslehre." *Jahresbericht der DMV* 1, 75–78. 无稳定在线链接.
- 一手: Gödel, K. (1938). "The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis." *PNAS* 24(12), 556–557. <https://doi.org/10.1073/pnas.24.12.556>
- 一手: Cohen, P. J. (1963). "The Independence of the Continuum Hypothesis." *PNAS* 50(6), 1143–1148. <https://doi.org/10.1073/pnas.50.6.1143>

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
**Machine-checked**: [Infinity.lean](../lean/mathlib/Infinity.lean) — the n-th truncation of $0.999\ldots$ is $1 - 1/10^n$, and the infinite series sums to 1 (needs a Mathlib project).

<!-- L4-end -->