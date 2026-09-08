# Goldbach & Twin Primes

<!-- L0 -->
<!-- dual -->
**The idea in a line:** Two claims a child can read — every even number $\geq 4$ is a sum of two primes, and infinitely many prime pairs differ by 2 — the first wide open, the second half-cracked in 2013. *(prereq: [numbers](../basics/numbers.md))*

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

- **Goldbach (1742)**: every even integer $n \geq 4$ is $p + q$ for primes $p, q$ (the same prime may be used twice: $4 = 2+2$). **Open.** Verified computationally up to $4 \times 10^{18}$.
- **Odd Goldbach**: every odd integer $n \geq 7$ is a sum of three primes. **Proved — Helfgott, 2013.**
- **Twin prime conjecture**: infinitely many $n$ with $n$ and $n+2$ both prime. **Open.**

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

Goldbach: $4 = 2+2$, $6 = 3+3$, $8 = 3+5$, $10 = 3+7$, $12 = 5+7$, … — true every time anyone checks, beyond $10^{18}$. Twin primes: $(3,5)$, $(5,7)$, $(11,13)$, $(17,19)$, $(29,31)$, … — the primes thin out, so twins should get rarer; do they ever stop? The average gap between primes near $x$ is $\ln x$ — so twins are "expected" to be plentiful; but *expected* and *exists* are different things. Both statements are the canonical lesson: *simple to state is not simple to prove* (see [proofs](../basics/proofs.md)).

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- **"$n \geq 4$" is a real condition**: 2 is not a sum of two primes ($2 = 1+1$ and 1 is not prime) — the conjecture starts where it can be true.
- **"Two primes" allows $p = q$** — otherwise 4 fails.
- The odd version's **"$n \geq 7$"** likewise excludes 3 and 5, which are not sums of three primes.
- **Heuristics are premises, not theorems**: Hardy–Littlewood's density model predicts infinitely many twins — a probabilistic *assumption* about prime distribution that no one can justify rigorously.
- **Zhang's 70,000,000 bound** (below) is unconditional — but the jump from "bounded gaps" to "gap exactly 2" is where the proof still stops.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- Prime number theorem: primes near $x$ are spaced about $\ln x$ apart — the "expected" gap.
- Sieve methods estimate how many numbers survive after crossing out multiples of primes — the tool behind Brun, Chen, Zhang, Maynard.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1742**: Goldbach's letter to Euler states the even conjecture — 280+ years of checking, no counterexample.
- **1919**: Brun's sieve shows the *sum of reciprocals of twin primes converges* — progress by bounding, not by proving infinity.
- **1923**: Hardy & Littlewood's circle method + heuristic — the twin prime *density* conjecture.
- **1937**: Vinogradov proves odd Goldbach for sufficiently large odds; the bound is made explicit decades later.
- **1966/1973**: Chen Jingrun's "1+2" — every sufficiently large even number is $p + (q \text{ or } q_1 q_2)$; the closest anyone has gotten to Goldbach itself.
- **2013, twin primes**: Zhang proves bounded gaps — infinitely many pairs within 70,000,000, the first *finite* bound ever; Maynard independently gives 600; the Polymath project squeezes it to 246. Goldbach's *odd* half falls the same year: Helfgott.
- **Where it stands**: odd Goldbach done; even Goldbach open; twins open at gap 2 with 246 in hand.

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

Prime distribution powers cryptography (RSA and friends); the sieve techniques built for these problems drive analytic number theory. They are the standing exhibit of "elementary statement, unbounded difficulty" — see [Collatz](collatz.md) for the purest case.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- Checking a huge range is not a proof — infinitely many even numbers remain unchecked either way (see [proofs](../basics/proofs.md)).
- Heuristic "probability 1" is not truth: number theory is littered with plausible-sounding heuristics that fail at astronomically late points.

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手但难回查: Goldbach 致 Euler 的信（1742-06-07），收入 Euler 书信集 *Opera Omnia* IVA/4. 无公开稳定在线链接（考证注：Euler Archive 未收录该信件）.
- 一手: Brun, V. (1919). "La série $1/5 + 1/7 + 1/11 + 1/13 + \ldots$ est convergente ou finie." *C. R. Acad. Sci. Paris* 168, 544–546. 无稳定在线链接.
- 一手: Hardy, G. H., Littlewood, J. E. (1923). "Some problems of 'Partitio numerorum'; III: On the expression of a number as a sum of primes." *Acta Mathematica* 44, 1–70. <https://doi.org/10.1007/BF02403921>
- 一手: Zhang, Y. (2014). "Bounded gaps between primes." *Annals of Mathematics* 179(3), 1121–1174. <https://doi.org/10.4007/annals.2014.179.3.7>
- 一手: Maynard, J. (2015). "Small gaps between primes." *Annals of Mathematics* 181(1), 383–413. <https://doi.org/10.4007/annals.2015.181.1.7>
- 一手: Helfgott, H. A. (2013). "The ternary Goldbach conjecture is true." arXiv:1312.7748 <https://arxiv.org/abs/1312.7748>; 配套: "Major arcs for Goldbach's problem." arXiv:1305.2897 <https://arxiv.org/abs/1305.2897>
- 一手: Chen, J. R. (1973). "On the representation of a large even integer as the sum of a prime and the product of at most two primes." *Sci. Sinica* 16, 157–176. 无 DOI（1973 年期刊未数字化）.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
**Machine-checked**: [Goldbach.lean](../lean/core/Goldbach.lean) — both conjectures stated; 2, 3, 7 proved prime, 9 proved not, and $10 = 3 + 7$ verified.

<!-- L4-end -->