# Fermat's Last Theorem

<!-- L0 -->
<!-- dual -->
**The idea in a line:** $a^n + b^n = c^n$ has no positive whole-number solutions for $n \geq 3$ — a 1637 margin note, proven 358 years later with mathematics Fermat could not have imagined.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

**Fermat's Last Theorem**: there are no positive integers $a, b, c$ and exponent $n \geq 3$ with

$$a^n + b^n = c^n.$$

(It suffices to prove it for $n = 4$ and for odd primes $n = p$ — a standard reduction; and "no positive integer solutions" is equivalent to "no nonzero rational solutions", by clearing denominators.)

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

For squares: $3^2 + 4^2 = 5^2$ — and infinitely many more Pythagorean triples. Add one to the exponent and *everything* vanishes: not a single positive whole-number triple for any $n \geq 3$. The step from squares to cubes kills them all, and showing *why* took three and a half centuries. The cubes nearly make it: $6^3 + 8^3 = 728$, and $9^3 = 729$ — off by exactly one, which is why no amount of poking finds a cube.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- **"$n \geq 3$" is the whole premise**: $n = 2$ has infinitely many solutions; $n = 1$ is trivial. The theorem lives entirely in the jump from squares to cubes and beyond.
- **Positive integers**: over the reals, solutions trivially exist (take $c = (a^n + b^n)^{1/n}$); the hardness is the *integer* condition.
- **The reduction to prime exponents** is a premise-tightening, not a weakening: if a solution exists for composite $n = k \cdot p$, then $(a^k)^p + (b^k)^p = (c^k)^p$ gives a solution for $p$.
- The **margin note** is contested history: scholars overwhelmingly believe Fermat had the $n = 4$ proof and over-claimed — the "too large for the margin" proof is generally regarded as a mirage.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- $n = 4$: Fermat's own descent proof survives. $n = 3$: Euler (with a gap later fixed by Legendre).
- Frey (1984): a counterexample would produce an elliptic curve "too weird to exist" — no such curve can exist if every semistable elliptic curve is modular.
- Ribet (1986): proves Frey's link rigorously — the whole problem reduces to modularity of elliptic curves.
- Wiles (with Taylor, 1994–95): proves exactly that (semistable case). ~100 pages, standing on decades of machinery.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1637**: Fermat's margin note; his own descent proof for $n = 4$ survives.
- **~1770**: Euler proves $n = 3$ (a gap, fixed by Legendre).
- **1820s**: Sophie Germain — her primes split the problem for a century of exponents.
- **1847**: Lamé and Cauchy announce flawed proofs using factorization; Kummer's correction — ideals, regular primes — is the moment algebraic number theory is born. The theorem starts *paying for itself* in new mathematics.
- **1908**: the Wolfskehl Prize — 100,000 marks for a proof — floods the field with amateurs; the Gödel-like lesson: naive attacks fail, the problem was never elementary.
- **1984–86**: Frey's elliptic-curve idea; Serre's conjecture; Ribet's proof of the epsilon conjecture — the detour that made the problem attackable.
- **1993**: Wiles announces; the gap is found; **1994**: with Richard Taylor, the gap is closed; **1995**: published. The Shimura–Taniyama–Weil modularity theorem route is complete (full modularity for all elliptic curves: BCDT, 2001).
- **Where it stands**: FLT is proved; the Beal conjecture (a generalization) carries a million-dollar prize, open.

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

The elliptic-curve machinery now powers modern cryptography (ECC). The saga itself is the flagship example of proof by *connection*: a number-theory statement about cubes, settled by geometry and analysis — see the planned entries on the Riemann hypothesis and P vs NP for problems still waiting for their bridge.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- That Fermat truly had "a proof too large for the margin" — the $n = 4$ argument is what historians credit him with.
- That computers could settle it — no finite check can (see [proofs](../basics/proofs.md)); infinitely many exponents remain. Only the proof counts.

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手: Wiles, A. (1995). "Modular elliptic curves and Fermat's last theorem." *Annals of Mathematics* 141(3), 443–551. <https://doi.org/10.2307/2118559>
- 一手: Taylor, R., Wiles, A. (1995). "Ring-theoretic properties of certain Hecke algebras." *Annals of Mathematics* 141(3), 553–572. <https://doi.org/10.2307/2118560>（1994 年补上的缺口即出于此篇）
- 一手: Ribet, K. (1990). "On modular representations of $\mathrm{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$ arising from modular forms." *Inventiones Mathematicae* 100, 431–476. <https://doi.org/10.1007/BF01231195>
- 一手: Frey, G. (1986). "Links between stable elliptic curves and certain Diophantine equations." *Annales Universitatis Saraviensis, Ser. Math.* 1(1), 1–40. 无稳定在线链接.
- 一手但难回查: Fermat 的页边注 — 载于 Diophantus *Arithmetica*（1670 年版，由其子 Samuel de Fermat 刊行并附注）. BnF Gallica 有数字化本，链接待考证. 「页边证明」本身为**存疑**史料.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
**Machine-checked**: [Fermat.lean](../lean/core/Fermat.lean) — FLT stated (Wiles 1995); $3^2 + 4^2 = 5^2$ verified, and the near-miss $6^3 + 8^3 = 9^3 - 1$ checked.

<!-- L4-end -->