# Probability & Expectation

<!-- L0 -->
<!-- dual -->
**The idea in a line:** Probability is a fraction of possibility — favorable outcomes over all outcomes; the craft is counting those correctly — and expectation is the long-run average, not a promise.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

- **Kolmogorov's axioms (1933)**: $P(A) \geq 0$; $P(\Omega) = 1$; for disjoint events, probabilities add (even countably many).
- **Conditional**: $P(A \mid B) = P(A \cap B) / P(B)$, requiring $P(B) > 0$.
- **Independence**: $A$ and $B$ independent $\iff P(A \cap B) = P(A) \cdot P(B)$.
- **Bayes' rule**: $P(A \mid B) = P(B \mid A) \cdot P(A) / P(B)$ — flip the condition by weighting with base rates.
- **Expectation**: $\mathbb{E}[X] = \sum_x x \cdot P(X = x)$; linear ($\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$) — but only a *long-run average*.

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

$P(\text{six}) = 1/6$ doesn't mean every sixth roll — it means that over many rolls, the fraction of sixes settles near $1/6$. "70% chance of rain" means 70% of days *like this one* rain. Dice don't remember — that's independence. But when someone who *knows* filters your choices, the odds shift — that's dependence (see [Monty Hall](../famous_problems/monty_hall.md)). And "expected value" is what the average over many runs approaches; a single run can go anywhere.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- "Equally likely" is the silent premise of $P(A) = \text{favorable}/\text{total}$: the die must actually be fair. The whole craft is deciding what counts as equally likely (see [birthday paradox](../famous_problems/birthday_paradox.md)).
- Conditioning requires **$P(B) > 0$** — "given $B$" with $B$ impossible is undefined, not zero.
- Independence is a strong, often-false assumption: real events (rain yesterday/today, market moves) are correlated. Claiming independence without checking it is the most common modeling error.
- Expectation is the destination of *many runs*, not the guarantee of one: a bet with positive expectation is right on average and can still ruin you on the way.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- Either: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- Bayes in one line of algebra: $P(A \mid B) \cdot P(B) = P(A \cap B) = P(B \mid A) \cdot P(A)$.
- The 99%-test trap: $P(\text{sick} \mid +) = \dfrac{0.99 \cdot 0.0001}{0.99 \cdot 0.0001 + 0.01 \cdot 0.9999} \approx 1\%$ — mostly false positives.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1654**: the Pascal–Fermat correspondence (the problem of points) — probability born from a gambling dispute; expectation defined for the first time.
- **1713**: Bernoulli's law of large numbers — the frequency interpretation gets its first theorem.
- **1763**: Bayes' posthumous essay — conditioning made rigorous two centuries before it was fashionable.
- **1933**: Kolmogorov's axioms — probability placed on measure theory; "the foundations problem" closed.
- **20th century**: subjective probability (de Finetti, Savage) vs frequentism — the *interpretation* of probability is still argued even though the mathematics is settled.

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

Insurance and option pricing ([economics_cross_culture](../../economics_cross_culture/README.md)), quantum mechanics — whose probabilities are apparently fundamental, not ignorance — epidemiology, polling, and every "studies show" headline.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- **Gambler's fallacy**: "red has come up six times, black is due" — the wheel has no memory.
- **Base-rate neglect**: 99% accuracy on a 1-in-10,000 disease still yields mostly false positives — 99% of a tiny number loses to 1% of a huge one.
- **Expectation ≠ outcome**: the average is the destination, not the journey.

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手: Pascal–Fermat 书信 (1654) — 原始信件收入 *Œuvres de Fermat*（1891–1922 版）; 无稳定在线链接.
- 一手: Bernoulli, J. (1713). *Ars Conjectandi.* Basel. 无稳定在线链接.
- 一手: Bayes, T. (1763). "An Essay towards solving a Problem in the Doctrine of Chances." *Philosophical Transactions* 53, 370–418. <https://doi.org/10.1098/rstl.1763.0053>
- 一手: Kolmogorov, A. N. (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung.* Springer. <https://doi.org/10.1007/978-3-642-49888-6>（1956 年 Chelsea 英译本为通行权威英译，二手）.

<!-- L5-end -->