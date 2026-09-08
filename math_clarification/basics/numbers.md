# Numbers

<!-- L0 -->
<!-- dual -->
**The idea in a line:** One idea, four avatars — counting, integers, fractions, irrationals — together filling the number line; each avatar was *forced into existence* by a problem the previous ones could not solve.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

- $\mathbb{N}$ naturals $1, 2, 3, \ldots$; $\mathbb{Z}$ integers; $\mathbb{Q}$ rationals $a/b$ ($a, b \in \mathbb{Z}$, $b \neq 0$); $\mathbb{R}$ reals — the complete ordered field. $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$.
- $\sqrt{2} \notin \mathbb{Q}$: no integers $p, q$ ($q \neq 0$) satisfy $p^2 = 2q^2$.
- $\pi$ := circumference ÷ diameter of *any* circle (Euclid: the ratio is constant); $e$ := the unique number such that the curve $x \mapsto e^x$ is its own rate of change.
- $\mathbb{R}$ is complete: every sequence that "should" converge, does. $\mathbb{Q}$ is not — that is precisely why the gaps (like $\sqrt{2}$) exist.

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

Numbers grew because reality demanded them. Count sheep → naturals. Keep accounts → subtraction demands negatives. Cut a cake → division demands fractions. Then geometry drops the bomb: the diagonal of a unit square cannot be written as any fraction — the Pythagoreans (legend says) were horrified. It *is* a number; it just refuses the fraction form. The number line is not a decoration we drew on $\mathbb{Q}$ — it is where $\mathbb{Q}$ was missing things.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- Each extension exists because the smaller system **lacks closure**: $\mathbb{N}$ lacks subtraction ($2 - 5 \notin \mathbb{N}$), $\mathbb{Z}$ lacks division ($5 \div 2 \notin \mathbb{Z}$), $\mathbb{Q}$ lacks limits (the sequence $1, 1.4, 1.41, \ldots$ converges to nothing in $\mathbb{Q}$).
- Fractions require **$b \neq 0$** — division by zero is not a small gap, it is the absence of a definition.
- "The ratio is constant for any circle" needs Euclidean geometry; in curved spaces (non-Euclidean) $\pi$ changes its meaning.
- Completeness is a *premise* of real analysis: on the hyperreal line, infinitesimals exist and $0.999\ldots < 1$ has a consistent reading — the premise is what differs, not the arithmetic.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- $\sqrt{2}$ is irrational, in one line: suppose $\sqrt{2} = p/q$ in lowest terms. Then $p^2 = 2q^2$, so $p$ is even; $p = 2k$ gives $q^2 = 2k^2$, so $q$ is even — contradiction ($p/q$ wasn't in lowest terms). See [proofs](proofs.md).
- $0.999\ldots = 1$: see [infinity](infinity.md).
- $e \approx 2.718$ appears wherever *rate ∝ amount* (interest, populations, radioactivity — see [growth](growth.md)).

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **~450 BCE**: Pythagoreans prove $\sqrt{2}$ irrational (Hippasus, per legend) — the discovery that rattled "all is number".
- **~350 BCE**: Eudoxus' theory of proportions — the classical workaround for comparing irrational lengths, centuries before limits.
- **19th century**: the rigor crisis. Dedekind (cuts) and Cantor/Cauchy (sequences) give $\mathbb{R}$ a *definition*; $\pi$ proved transcendental by Lindemann (1882) — settling the ancient "squaring the circle" impossibility.
- **1891**: Cantor's diagonal argument — almost every real number can never be named. The numbers we write down are the rare, lucky few.

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

$\pi$ in orbits and calendars ([heaven_climate](../../heaven_climate/README.md)), $e$ in compound interest ([economics_cross_culture](../../economics_cross_culture/README.md)), $\sqrt{2}$ in the diagonal of your square tile.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- "Irrational" means *unreasonable* — it only means *not a ratio*.
- The digits of $\pi$ look random, but that is an artifact of writing in base 10, not a property of the circle.

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手: Cantor, G. (1891). "Über eine elementare Frage der Mannigfaltigkeitslehre." *Jahresbericht der DMV* 1, 75–78. 无稳定在线链接；英译见 Ewald (1996)（二手/权威版本）.
- 一手: Lindemann, F. (1882). "Über die Zahl $\pi$." *Mathematische Annalen* 20, 213–225. 无稳定在线链接.
- 权威版本: Heath, T. L. (trans.), *The Thirteen Books of Euclid's Elements* — $\sqrt{2}$ 无理性见卷 X 命题 117（Hippasus 因泄露而溺亡是**传说**，非信史）.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
**Machine-checked**: [Sqrt2.lean](../lean/mathlib/Sqrt2.lean) — Mathlib's proof that $\sqrt{2}$ is irrational (needs a Mathlib project).

<!-- L4-end -->