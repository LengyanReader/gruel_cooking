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

<!-- zh -->
## 精确表述 (The Precise Statement)

- **线性**：$x_n = x_0 + n \cdot d$——每步加一个固定的*量*。
- **指数**：$x_n = x_0 \cdot r^n$（$r > 1$ 增长，$0 < r < 1$ 衰减）——每步乘一个固定的*因子*；等价地说，增量正比于存量：$x_{n+1} - x_n = (r - 1) \cdot x_n$。
- **倍增时间** $= \ln 2 / \ln r \approx 70 \div (\text{百分比速率})$——七十法则。
- **半衰期** $= \ln 2 / \lambda$——对任何起始量都是同一个数。
- **Logistic（逻辑斯蒂）**：起初是指数，随后随限制收紧而弯向天花板——S 曲线。

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

A pond of lily pads doubles daily. On day 29 the pond is half covered; one day later it's full. *The last doubling does as much work as all previous doublings combined* — that asymmetry is the entire secret of compounding. The same curve run backwards is decay: after each half-life, half remains. Growth and decay are one idea with the sign flipped. And folding paper: 42 folds of a 0.1 mm sheet reach the Moon — because thickness doubles each fold.

<!-- zh -->
## 譬喻 (Intuition)

一池睡莲每天翻倍。第 29 天，池子半满；再过一天，全满。*最后一次翻倍所做之功，等于此前所有翻倍之和*——这个不对称就是复利的全部秘密。同一条曲线倒着放就是衰减：每过一个半衰期，剩下一半。增长与衰减是同一个想法翻了符号。还有折纸：0.1 毫米的纸折 42 次可达月球——因为厚度每次翻倍。

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- Exponential growth requires a **mechanism where rate ∝ stock**: interest on interest, infection through contacts, fission. Without that mechanism the claim is just a fitted curve.
- It assumes **$r$ constant** and **resources unlimited**. Both fail in reality — which is why every real exponential is a *phase*, bending into an S-curve.
- Decay assumes **memoryless elimination** (a constant fraction per unit time, independent of amount and age). That is the premise that makes half-life independent of how much you start with; when elimination saturates (enzymes busy), decay stops being exponential.
- The rule of 70 is an approximation ($\ln 2 \approx 0.693$): at 7%, the true doubling time is $\approx 10.24$ years — $1.07^{10} < 2 < 1.07^{11}$.

<!-- zh -->
## 前提·假设·成立条件 (Premises & Conditions)

- 指数增长要求一个**「速率 ∝ 存量」的机制**：利上滚利、接触传染、链式裂变。没有这个机制，指数说法就只是一条拟合曲线。
- 它假设 **$r$ 恒定**且**资源无界**。现实里两者都会失效——所以一切真实的指数都只是一个*阶段*，弯成 S 曲线。
- 衰减假设**无记忆消除**（单位时间消掉固定的比例，与总量和年龄无关）——正是这条前提使半衰期与起始量无关；当消除饱和（酶已忙满），衰减不再是指数。
- 七十法则是个近似（$\ln 2 \approx 0.693$）：按 7% 计，真实倍增时间 $\approx 10.24$ 年——$1.07^{10} < 2 < 1.07^{11}$。

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- Linear: $1, 3, 5, 7, \ldots$; exponential: $1, 2, 4, 8, \ldots$, and $2^{30} \approx 10^9$.
- Doubling time from rate: $T_2 = \ln 2 / \ln(1 + r/100)$.
- The pond story's moral is about timing: at any fixed "days to full", the pond looks half-empty right before it isn't.

<!-- zh -->
## 一点数学 (A Little Math)

- 线性：$1, 3, 5, 7, \ldots$；指数：$1, 2, 4, 8, \ldots$，且 $2^{30} \approx 10^9$。
- 由速率求倍增时间：$T_2 = \ln 2 / \ln(1 + r/100)$。
- 池塘故事的教训在于时机：无论固定「离全满还有几天」是几天，池塘总是在满掉前一刻看起来还半空。

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1798**: Malthus — population grows geometrically, food arithmetically; the first clear statement of exponential pressure (his model, minus innovation).
- **1838**: Verhulst proposes the logistic curve — exponential growth *with* its ceiling.
- **1949**: Libby's radiocarbon dating — half-life as a clock for the past (a workhorse of [heaven_climate](../../heaven_climate/README.md)'s paleoclimate records).
- **20th century**: the S-curve becomes the standard model of technologies and epidemics; Moore's law (1965) is an exponential in transistor density — and itself an S-curve in slow motion.

<!-- zh -->
## 解题方向·历史的努力 (Directions of Attack & History)

- **1798 年**：马尔萨斯——人口按几何级数增长，粮食按算术级数增长；指数压力的首次清晰表述（他的模型，减去创新变量）。
- **1838 年**：韦吕勒提出 logistic 曲线——*带着*天花板的指数增长。
- **1949 年**：利比放射性碳定年——半衰期作为给过去计时的钟（[heaven_climate](../../heaven_climate/README.md) 古气候记录的主力工具）。
- **20 世纪**：S 曲线成为技术与传染病模型的标准形；摩尔定律（1965）是晶体管密度上的指数——它自己也是一条慢放的 S 曲线。

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