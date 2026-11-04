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

<!-- zh -->
## 精确表述 (The Precise Statement)

- $\mathbb{N}$ 自然数 $1, 2, 3, \ldots$；$\mathbb{Z}$ 整数；$\mathbb{Q}$ 有理数 $a/b$（$a, b \in \mathbb{Z}$，$b \neq 0$）；$\mathbb{R}$ 实数——完备的有序域。四者层层相含：$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$。
- $\sqrt{2} \notin \mathbb{Q}$：不存在整数 $p, q$（$q \neq 0$）满足 $p^2 = 2q^2$。
- $\pi$ := *任何*圆的周长 ÷ 直径（欧几里得：该比值恒定）；$e$ := 使曲线 $x \mapsto e^x$ 以自身变化率为变化率的唯一数。
- $\mathbb{R}$ 是完备的：凡「应当」收敛的序列皆收敛。$\mathbb{Q}$ 不完备——这正是缝隙（如 $\sqrt{2}$）存在的原因。

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

Numbers grew because reality demanded them. Count sheep → naturals. Keep accounts → subtraction demands negatives. Cut a cake → division demands fractions. Then geometry drops the bomb: the diagonal of a unit square cannot be written as any fraction — the Pythagoreans (legend says) were horrified. It *is* a number; it just refuses the fraction form. The number line is not a decoration we drew on $\mathbb{Q}$ — it is where $\mathbb{Q}$ was missing things.

<!-- zh -->
## 譬喻 (Intuition)

数的每一次扩张，都是现实逼出来的。数羊 → 自然数。记账 → 减法逼出负数。分蛋糕 → 除法逼出分数。然后几何投下炸弹：单位正方形的对角线写不成任何分数——传说毕达哥拉斯学派为此大为惊骇。它*是*一个数，只是拒绝以分数的形式现身。数轴并不是我们画在 $\mathbb{Q}$ 上的装饰——它是 $\mathbb{Q}$ 缺了东西的地方。

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- Each extension exists because the smaller system **lacks closure**: $\mathbb{N}$ lacks subtraction ($2 - 5 \notin \mathbb{N}$), $\mathbb{Z}$ lacks division ($5 \div 2 \notin \mathbb{Z}$), $\mathbb{Q}$ lacks limits (the sequence $1, 1.4, 1.41, \ldots$ converges to nothing in $\mathbb{Q}$).
- Fractions require **$b \neq 0$** — division by zero is not a small gap, it is the absence of a definition.
- "The ratio is constant for any circle" needs Euclidean geometry; in curved spaces (non-Euclidean) $\pi$ changes its meaning.
- Completeness is a *premise* of real analysis: on the hyperreal line, infinitesimals exist and $0.999\ldots < 1$ has a consistent reading — the premise is what differs, not the arithmetic.

<!-- zh -->
## 前提·假设·成立条件 (Premises & Conditions)

- 每一次扩张都因小系统**缺乏封闭性**而生：$\mathbb{N}$ 缺减法（$2 - 5 \notin \mathbb{N}$），$\mathbb{Z}$ 缺除法（$5 \div 2 \notin \mathbb{Z}$），$\mathbb{Q}$ 缺极限（序列 $1, 1.4, 1.41, \ldots$ 在 $\mathbb{Q}$ 中无收敛点）。
- 分数要求 **$b \neq 0$**——除以零不是小缝隙，而是「定义不存在」。
- 「比值对任何圆恒定」依赖欧氏几何；在弯曲空间（非欧几何）中 $\pi$ 会改变含义。
- 完备性是实分析的*前提*：在超实数线上，无穷小存在，$0.999\ldots < 1$ 有一致的读法——分歧在前提，不在算术。

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- $\sqrt{2}$ is irrational, in one line: suppose $\sqrt{2} = p/q$ in lowest terms. Then $p^2 = 2q^2$, so $p$ is even; $p = 2k$ gives $q^2 = 2k^2$, so $q$ is even — contradiction ($p/q$ wasn't in lowest terms). See [proofs](proofs.md).
- $0.999\ldots = 1$: see [infinity](infinity.md).
- $e \approx 2.718$ appears wherever *rate ∝ amount* (interest, populations, radioactivity — see [growth](growth.md)).

<!-- zh -->
## 一点数学 (A Little Math)

- $\sqrt{2}$ 是无理数，一行证完：设 $\sqrt{2} = p/q$ 为最简分数。则 $p^2 = 2q^2$，故 $p$ 为偶数；代 $p = 2k$ 得 $q^2 = 2k^2$，故 $q$ 也是偶数——与「最简」矛盾。见 [proofs](proofs.md)。
- $0.999\ldots = 1$：见 [infinity](infinity.md)。
- 凡 *变化率 ∝ 存量* 之处（利息、种群、放射性——见 [growth](growth.md)），$e \approx 2.718$ 必然现身。

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **~450 BCE**: Pythagoreans prove $\sqrt{2}$ irrational (Hippasus, per legend) — the discovery that rattled "all is number".
- **~350 BCE**: Eudoxus' theory of proportions — the classical workaround for comparing irrational lengths, centuries before limits.
- **19th century**: the rigor crisis. Dedekind (cuts) and Cantor/Cauchy (sequences) give $\mathbb{R}$ a *definition*; $\pi$ proved transcendental by Lindemann (1882) — settling the ancient "squaring the circle" impossibility.
- **1891**: Cantor's diagonal argument — almost every real number can never be named. The numbers we write down are the rare, lucky few.

<!-- zh -->
## 解题方向·历史的努力 (Directions of Attack & History)

- **约前 450 年**：毕达哥拉斯学派证明 $\sqrt{2}$ 为无理数（传说归功希帕索斯）——动摇「万物皆数」的发现。
- **约前 350 年**：欧多克索斯的比例论——在极限概念诞生数百年前处理不可公度量的经典方案。
- **19 世纪**：严格性危机。戴德金（分割）与康托尔/柯西（序列）给 $\mathbb{R}$ 一个*定义*；林德曼（1882）证明 $\pi$ 为超越数——一锤定音地判死古老的「化圆为方」。
- **1891 年**：康托尔对角线法——几乎所有实数永远无法被命名。我们能写下的数，只是稀少而幸运的少数。

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