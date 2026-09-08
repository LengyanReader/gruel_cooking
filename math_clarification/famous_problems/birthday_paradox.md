# Birthday Paradox

<!-- L0 -->
<!-- dual -->
**The idea in a line:** With 23 people, a shared birthday is already more likely than not — the "paradox" is that people compare 23 to 365, but the real comparison is 253 *pairs* to 365.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

$n$ people, birthdays independent and uniform over 365 days. Then

$$P(\text{no match}) = \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{365 - n + 1}{365},$$

and:

- $n = 23$: $P(\text{match}) \approx 50.7\%$ (the "paradox")
- $n = 50$: $\approx 97\%$; $n = 70$: $\approx 99.9\%$
- The *fixed-date* version — "someone shares *my* birthday" — needs 253 people, not 23.

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

Two different questions, two different answers. "Someone shares *my* birthday" — a fixed date — needs ~253 people. "Some *pair* shares a birthday" — any date — passes 50% at 23. Every pair of people is a fresh chance at a match, and pairs don't grow linearly: 23 people make 253 pairs, and each pair has a $1/365$ shot. Small chance per pair, but *many* independent tries — that is how unlikely-looking coincidences quietly become likely.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- **Independent, uniform birthdays** — the modeling premise. Real birthdays are neither (seasonality, twins, scheduled births); the effect shifts the answer slightly, not the lesson: $n \approx 23$ stays.
- **"Any pair" vs "fixed date"** — the structural condition. Change it and the answer moves from 23 to 253.
- Leap days change the denominator (366) — immaterial to the takeaway.
- The collision bound: matches appear around $\sqrt{N}$ ($\approx \sqrt{365} \approx 19$) — this scaling, not the exact 23, is the transferable fact.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- $P(\text{no match}) = \prod_{k=1}^{n-1} \dfrac{365 - k}{365}$ — each new person must dodge every birthday already taken.
- Collision formula: $P(\text{match}) \approx 1 - e^{-n^2 / 2k}$ for $n$ people, $k$ days — $n^2/2$ pairs is the engine.
- $23 \cdot 22 / 2 = 253$.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1939**: Richard von Mises poses the problem — it enters the literature as a probability exercise.
- **Mid-20th century**: mathematicians note the generalization — collisions appear at $\sqrt{N}$; the "paradox" becomes a standard demonstration that coincidences are *many unnoticed chances*.
- **Cryptography era**: the birthday attack on hash functions — to find two documents with the same digest, try $\sim\sqrt{N}$ hashes, not $N$. A number-theory toy becomes a security bound (hash sizes are chosen with $\sqrt{N}$ in mind).

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

The "birthday attack" breaks hash signatures in computer security (collisions arrive at $\sqrt{N}$, not $N$); shared keys, retweets, and "what are the odds!" life events — all collisions. The lesson generalizes: *any* coincidence is not one chance, it's many unnoticed chances.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- Comparing to one fixed date (my birthday) instead of *any* pair — 23 vs 253 is the entire paradox.
- Feeling that a coincidence "was meant to be" — we simply never count how many chances there were (see [probability](../basics/probability.md)).

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手但难回查: von Mises, R. (1939). "Über Aufteilungs- und Besetzungswahrscheinlichkeiten." *Revue de la Faculté des Sciences de l'Université d'Istanbul* 4, 145–163. 无稳定在线链接（问题最早的系统陈述; 常见二手转述，此处据原刊）.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
**Machine-checked**: [Birthday.lean](../lean/core/Birthday.lean) — exact rational arithmetic: 23 people pass 50%, 50 people pass 97%, and the fixed-date version really does need 253.

<!-- L4-end -->