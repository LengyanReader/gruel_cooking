# Growth

<!-- L0 -->
<!-- dual -->
**The idea in a line:** Linear growth adds the same amount each step; exponential growth multiplies by the same factor — which is why it sneaks: 30 doublings from 1 is over a billion.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

- **Linear**: $x_n = x_0 + n \cdot d$ — a constant *amount* added per step.
- **Exponential**: $x_n = x_0 \cdot r^n$ ($r > 1$ grows, $0 < r < 1$ decays) — a constant *factor* per step; equivalently, the increment is proportional to the stock: $x_{n+1} - x_n = (r - 1) \cdot x_n$.
- **Doubling time** $= \ln 2 / \ln r \approx 70 \div (\text{percent rate})$ — the rule of 70.
- **Half-life** $= \ln 2 / \lambda$ — the same number for every starting amount.
- **Logistic**: exponential at first, then bending to a ceiling as limits bind — the S-curve.

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

A pond of lily pads doubles daily. On day 29 the pond is half covered; one day later it's full. *The last doubling does as much work as all previous doublings combined* — that asymmetry is the entire secret of compounding. The same curve run backwards is decay: after each half-life, half remains. Growth and decay are one idea with the sign flipped. And folding paper: 42 folds of a 0.1 mm sheet reach the Moon — because thickness doubles each fold.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- Exponential growth requires a **mechanism where rate ∝ stock**: interest on interest, infection through contacts, fission. Without that mechanism the claim is just a fitted curve.
- It assumes **$r$ constant** and **resources unlimited**. Both fail in reality — which is why every real exponential is a *phase*, bending into an S-curve.
- Decay assumes **memoryless elimination** (a constant fraction per unit time, independent of amount and age). That is the premise that makes half-life independent of how much you start with; when elimination saturates (enzymes busy), decay stops being exponential.
- The rule of 70 is an approximation ($\ln 2 \approx 0.693$): at 7%, the true doubling time is $\approx 10.24$ years — $1.07^{10} < 2 < 1.07^{11}$.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- Linear: $1, 3, 5, 7, \ldots$; exponential: $1, 2, 4, 8, \ldots$, and $2^{30} \approx 10^9$.
- Doubling time from rate: $T_2 = \ln 2 / \ln(1 + r/100)$.
- The pond story's moral is about timing: at any fixed "days to full", the pond looks half-empty right before it isn't.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1798**: Malthus — population grows geometrically, food arithmetically; the first clear statement of exponential pressure (his model, minus innovation).
- **1838**: Verhulst proposes the logistic curve — exponential growth *with* its ceiling.
- **1949**: Libby's radiocarbon dating — half-life as a clock for the past (a workhorse of [heaven_climate](../../heaven_climate/README.md)'s paleoclimate records).
- **20th century**: the S-curve becomes the standard model of technologies and epidemics; Moore's law (1965) is an exponential in transistor density — and itself an S-curve in slow motion.

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

Epidemics (R₀ spread), compound interest ([economics_cross_culture](../../economics_cross_culture/README.md)), radiocarbon dating ([heaven_climate](../../heaven_climate/README.md)), supernova light curves, your fridge's cooling curve.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- "Exponential" as slang for "big/fast" misses its real meaning — *self-amplifying*: growth proportional to what's already there.
- Everything that compounds forever eventually hits a wall. Exponential is a phase of every real system, not its fate — the S-curve is the honest shape.

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手: Malthus, T. R. (1798). *An Essay on the Principle of Population.* 无稳定在线链接（1798 初版有数字化副本，链接待考证）.
- 一手: Verhulst, P.-F. (1838). "Notice sur la loi que la population suit dans son accroissement." *Correspondance Mathématique et Physique* 10, 113–121. 无稳定在线链接.
- 一手: Libby, W. F., Anderson, E. C., Arnold, J. R. (1949). "Age Determination by Radiocarbon Content: World-Wide Assay of Natural Radiocarbon." *Science* 109(2827), 227–228. <https://doi.org/10.1126/science.109.2827.227>
- 一手: Moore, G. E. (1965). "Cramming more components onto integrated circuits." *Electronics* 38(8). 无稳定在线链接（IEEE 有授权重印）.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
**Machine-checked**: [Growth.lean](../lean/core/Growth.lean) — 41 folds fall short of the Moon, 42 reach it; $1.07^{10} < 2 < 1.07^{11}$.

<!-- L4-end -->