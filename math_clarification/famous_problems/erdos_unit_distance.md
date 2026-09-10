# Erdős Unit Distance Conjecture / 埃尔德什单位距离猜想

<!-- L0 -->
<!-- en -->
**The idea in a line:** Place $n$ points on a plane — how many pairs can sit exactly one unit apart? Erdős said the square grid is essentially best. In 2026, an AI model proved him wrong, using tools from algebraic number theory that nobody had connected to this geometry problem.
<!-- zh -->
**一行想法：** 在平面上放置 $n$ 个点——距离恰好为 1 的点对最多能有多少？Erdős 认为正方形网格本质上是最优的。2026年，一个AI模型用代数数论的工具推翻了这个猜想，而此前从未有人将这些工具与几何问题联系起来。
<!-- L0-end -->

<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

Imagine an infinite chessboard. Each square's corners are points, and neighboring corners are exactly 1 apart. With $n = 100$ points arranged as a $10 \times 10$ grid, each interior point has 4 neighbors at distance 1 — you count roughly $2n$ unit-distance pairs.

Erdős discovered something clever: if you *rescale* the grid by a carefully chosen irrational factor, the unit distances no longer come only from nearest neighbors. Pairs that were previously $\sqrt{2}$, $\sqrt{5}$, or $\sqrt{13}$ apart can all become distance 1 simultaneously. This pushes the count above $2n$, to roughly $n^{1 + C/\log\log n}$ — barely above linear, but above it.

The conjecture said: that's the best anyone can do. Nobody can beat the grid by a *fixed polynomial* margin. A square grid (or its rescaled cousins) is optimal. For 80 years, nobody proved it, but nobody found a counterexample either.

Then an AI looked at the problem and said: what if you stop using ordinary integers and switch to a completely different number system — one with infinitely many symmetries? That single cross-domain leap broke the conjecture open.
<!-- zh -->
## 譬喻 (Intuition)

想象一个无限棋盘。每个格子的角点就是点，相邻角点之间的距离恰好为 1。如果 $n = 100$ 个点排成 $10 \times 10$ 的网格，每个内部点有 4 个距离为 1 的邻居——你大约能数出 $2n$ 个单位距离点对。

Erdős 发现了一个巧妙的技巧：如果你用一个精心选择的无理数因子**缩放**网格，单位距离不再只来自最近邻。之前距离为 $\sqrt{2}$、$\sqrt{5}$ 或 $\sqrt{13}$ 的点对可以同时变成距离 1。这把计数推高到大约 $n^{1 + C/\log\log n}$——仅仅高于线性，但确实高于线性。

猜想说：这就是极限。没有人能以一个**固定的多项式**优势超越网格。正方形网格（或其缩放变体）是最优的。80年来，没人证明它，但也没人找到反例。

然后一个AI审视这个问题，问道：如果你停止使用普通整数，转而使用一个完全不同的数系——一个具有无限对称性的数系——会怎样？这一个跨领域的跳跃就打破了猜想。
<!-- L1-end -->

<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

**Definition.** For $n$ points in the Euclidean plane $\mathbb{R}^2$, let $u(n)$ denote the maximum number of pairs at distance exactly 1:

$$u(n) = \max_{P \subset \mathbb{R}^2, |P|=n} \big|\{\{a,b\} \subseteq P : \|a - b\| = 1\}\big|$$

**Erdős Conjecture (1946).** $u(n) = n^{1 + o(1)}$, i.e. no construction beats the grid by a fixed polynomial factor.

**Known bounds (before 2026):**
- Lower bound (Erdős 1946): $u(n) \geq n^{1 + C/\log\log n}$ via rescaled integer grids
- Upper bound (Spencer–Szemerédi–Trotter 1984): $u(n) = O(n^{4/3})$

**Disproof (OpenAI, May 2026).** There exists $\delta > 0$ such that for infinitely many $n$, $u(n) \geq n^{1+\delta}$. Will Sawin (Princeton) refined $\delta = 0.014$.

## Premises & Conditions (前提·假设·成立条件)

- The points live in the **Euclidean plane** $\mathbb{R}^2$ with the standard metric.
- $n$ is a **positive integer**; the conjecture concerns asymptotic behavior as $n \to \infty$.
- "Infinitely many $n$" — the construction produces an **infinite family** of configurations, not one clever finite arrangement. A single finite counterexample would not suffice.
- The upper bound $O(n^{4/3})$ is **unaffected** by the disproof: we now know $n^{1+\delta} \leq u(n) \leq n^{4/3}$, with a still-enormous gap.
- The conjecture was never formally proved — it was a **believed lower bound**, not a theorem. Disproving it means beating the grid construction, not overturning a proven result.
<!-- zh -->
## 精确表述 (The Precise Statement)

**定义。** 对于欧几里得平面 $\mathbb{R}^2$ 中的 $n$ 个点，令 $u(n)$ 表示距离恰好为 1 的点对的最大数量：

$$u(n) = \max_{P \subset \mathbb{R}^2, |P|=n} \big|\{\{a,b\} \subseteq P : \|a - b\| = 1\}\big|$$

**Erdős 猜想 (1946)。** $u(n) = n^{1 + o(1)}$，即没有任何构造能以固定的多项式优势超越网格。

**已知界（2026年之前）：**
- 下界 (Erdős 1946)：$u(n) \geq n^{1 + C/\log\log n}$，通过缩放整数网格
- 上界 (Spencer–Szemerédi–Trotter 1984)：$u(n) = O(n^{4/3})$

**推翻 (OpenAI, 2026年5月)。** 存在 $\delta > 0$，使得对无穷多个 $n$，$u(n) \geq n^{1+\delta}$。Will Sawin (普林斯顿) 精化为 $\delta = 0.014$。

## 前提·假设·成立条件 (Premises & Conditions)

- 点位于**欧几里得平面** $\mathbb{R}^2$ 中，使用标准度量。
- $n$ 是**正整数**；猜想关注 $n \to \infty$ 时的渐近行为。
- "无穷多个 $n$"——构造产生的是**无穷族**的配置，而非一个巧妙的有限排列。单个有限反例是不够的。
- 上界 $O(n^{4/3})$ **不受推翻影响**：我们现在知道 $n^{1+\delta} \leq u(n) \leq n^{4/3}$，之间仍有巨大空白。
- 该猜想从未被形式化证明——它是一个**被相信的下界**，而非定理。推翻它意味着超越了网格构造，而非推翻一个已证明的结果。
<!-- L2-end -->

<!-- L3 -->
<!-- en -->
## A Little Math

**Erdős's construction (Gaussian integers).** Take the Gaussian integers $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$, scale by $\alpha$, and project to the plane. The number of representations of 1 as a norm form $|a+bi|^2 = a^2 + b^2 = 1/\alpha^2$ controls the unit-distance count. Since 1 has only finitely many representations as a sum of two squares, the exponent gain is sub-polynomial.

**The AI's construction (number field towers).** Replace $\mathbb{Z}[i]$ with the ring of integers $\mathcal{O}_K$ of a carefully chosen number field $K$. The key insight:

1. **Golod–Shafarevich theorem** guarantees the existence of number fields $K$ whose class group has arbitrarily large rank — meaning $\mathcal{O}_K$ has "many" independent ideal classes.
2. **Hajir–Maire–Ramakrishna** showed one can construct **infinite class field towers** with controlled ramification — giving towers of number fields with ever-larger class groups.
3. The unit group $\mathcal{O}_K^\times$ has rank $r_1 + r_2 - 1$ (Dirichlet's unit theorem). By choosing $K$ with large $r_1 + r_2$, the unit group is large.
4. **Embedding** $\mathcal{O}_K$ into $\mathbb{R}^2$ via the Minkowski embedding, each unit $\varepsilon \in \mathcal{O}_K^\times$ gives a lattice point, and the unit group's structure generates many pairs at distance 1.

The net effect: $u(n) \geq n^{1 + 0.014}$ — a genuine polynomial improvement, beating the grid for all sufficiently large $n$ in the family.

## Directions of Attack & History (解题方向·历史的努力)

- **1946**: Erdős poses the problem, gives the grid lower bound $n^{1 + C/\log\log n}$, conjectures this is essentially optimal.
- **1984**: Spencer, Szemerédi, Trotter prove $u(n) = O(n^{4/3})$ — the best upper bound, still unmatched.
- **1997**: Székely improves bounds using crossing-number arguments.
- **2000s–2020s**: Various improvements to constants and related problems; the core gap $n^{1+o(1)}$ to $n^{4/3}$ remains.
- **May 2026**: OpenAI model autonomously produces a counterexample using algebraic number theory. Verified by Gowers, Alon, Sawin, Bloom, Litt, Shankar, Tsimerman, Wang, Wood (19-page companion paper).
- **Same week**: Will Sawin refines the exponent to $\delta = 0.014$.
<!-- zh -->
## 数学细节 (A Little Math)

**Erdős的构造（高斯整数）。** 取高斯整数 $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$，缩放因子 $\alpha$，投影到平面。1 作为范数形式 $|a+bi|^2 = a^2 + b^2 = 1/\alpha^2$ 的表示数量控制单位距离计数。由于 1 作为两平方和只有有限多种表示，指数增益是次多项式的。

**AI的构造（数域塔）。** 用精心选择的数域 $K$ 的整数环 $\mathcal{O}_K$ 替换 $\mathbb{Z}[i]$。关键洞察：

1. **Golod–Shafarevich 定理** 保证存在类群具有任意大秩的数域 $K$——意味着 $\mathcal{O}_K$ 有"很多"独立的理想类。
2. **Hajir–Maire–Ramakrishna** 证明可以构造具有可控分歧的**无限类域塔**——给出类群越来越大的数域塔。
3. 单位群 $\mathcal{O}_K^\times$ 的秩为 $r_1 + r_2 - 1$（Dirichlet 单位定理）。选择 $r_1 + r_2$ 大的 $K$，单位群就大。
4. 通过 Minkowski 嵌入将 $\mathcal{O}_K$ 嵌入 $\mathbb{R}^2$，每个单位 $\varepsilon \in \mathcal{O}_K^\times$ 给出一个格点，单位群的结构产生许多距离为 1 的点对。

最终效果：$u(n) \geq n^{1 + 0.014}$——真正的多项式改进，在该族中所有足够大的 $n$ 上超越网格。

## 解题方向·历史的努力 (Directions of Attack & History)

- **1946年**: Erdős 提出问题，给出网格下界 $n^{1 + C/\log\log n}$，猜想这本质上是最优的。
- **1984年**: Spencer, Szemerédi, Trotter 证明 $u(n) = O(n^{4/3})$——最佳上界，至今未被超越。
- **1997年**: Székely 使用交叉数论证改进了界。
- **2000年代–2020年代**: 常数和相关问题的各种改进；核心空白 $n^{1+o(1)}$ 到 $n^{4/3}$ 依然存在。
- **2026年5月**: OpenAI 模型使用代数数论自主产生反例。由 Gowers, Alon, Sawin, Bloom, Litt, Shankar, Tsimerman, Wang, Wood 验证（19页伴随论文）。
- **同一周**: Will Sawin 将指数精化为 $\delta = 0.014$。
<!-- L3-end -->

<!-- L4 -->
<!-- en -->
## Machine-checked

The original disproof is a theoretical construction, not a computable finite object — it cannot be directly verified by Lean in the style of the core files. However:

- **The structural obstruction is verified locally** — see [`../lean/core/ErdosUnitDistance.lean`](../lean/core/ErdosUnitDistance.lean). The kernel checks the exact fact that makes the naive constructions stall: the number of ways to write a fixed integer as a sum of two squares is finite, so the plain $k \times k$ grid yields exactly $2k(k-1) \approx 2n$ unit distances and no simple rescaling escapes. This is the precise "baseline" the AI construction has to beat.
- **Golod–Shafarevich theorem**: formalized in Lean 4 Mathlib (`Mathlib.RingTheory.Polynomial.Irreducible.Basic` area — the group-theoretic version lives in a related module).
- **Dirichlet's unit theorem**: partially formalized in Mathlib.
- **The specific construction**: the infinite family is defined by a sequence of number fields; finite instances (specific $K$ with small discriminant) can in principle be checked for the claimed unit-distance count, but the full asymptotic proof requires analytic number theory beyond current formalization scope.

**Status**: Open — the proof is human-verified (9 mathematicians, 19 pages) but not machine-formalized.

## What People Get Wrong (常见误解)

- **"Erdős proved the grid is optimal."** No — he conjectured it. The claim was a lower bound with an upper-bound belief, never a theorem.
- **"AI solved it alone."** The model produced the construction; 9 mathematicians wrote the 19-page verification paper, and Sawin sharpened the constant. Collaboration, not replacement.
- **"This settles the unit distance problem."** Far from it. We now know $n^{1.014} \leq u(n) \leq n^{4/3}$ — the gap is enormous. The true growth rate of $u(n)$ remains unknown.
- **"The AI just searched literature."** No — the construction uses Golod–Shafarevich theory in a way no prior paper connected to this problem. Cross-domain novelty, not retrieval.
<!-- zh -->
## 机器验证 (Machine-checked)

原始推翻是一个理论构造，而非可计算的有限对象——它无法像核心文件那样被 Lean 直接验证。然而：

- **结构障碍已在本地验证**——参见 [`../lean/core/ErdosUnitDistance.lean`](../lean/core/ErdosUnitDistance.lean)。内核精确检查了让朴素构造失效的关键事实：将固定整数表示为两数平方和的方式是有限的，因此普通的 $k \times k$ 网格恰有 $2k(k-1) \approx 2n$ 个单位距离，简单的缩放无法逃离。这正是 AI 构造必须超越的精确"基线"。
- **Golod–Shafarevich 定理**：在 Lean 4 Mathlib 中有形式化（群论版本在相关模块中）。
- **Dirichlet 单位定理**：在 Mathlib 中有部分形式化。
- **具体构造**：无穷族由数域序列定义；有限实例（具有小判别式的特定 $K$）原则上可以检查所声称的单位距离计数，但完整的渐近证明需要超出当前形式化范围的解析数论。

**状态**：开放——证明已通过人工验证（9位数学家，19页），但未被机器形式化。

## 常见误解 (What People Get Wrong)

- **"Erdős证明了网格是最优的。"** 没有——他猜想如此。该声明是一个带有上界信念的下界，从未成为定理。
- **"AI独自解决了它。"** 模型产生了构造；9位数学家撰写了19页的验证论文，Sawin 精化了常数。是协作，不是替代。
- **"这解决了单位距离问题。"** 远非如此。我们现在知道 $n^{1.014} \leq u(n) \leq n^{4/3}$——空白巨大。$u(n)$ 的真实增长率仍然未知。
- **"AI只是检索了文献。"** 不——该构造以此前没有论文将此问题联系起来的方式使用了 Golod–Shafarevich 理论。是跨领域的新颖性，而非检索。
<!-- L4-end -->

<!-- L5 -->
<!-- en -->
## Where It Shows Up (应用)

- **Discrete geometry**: the foundational extremal problem for point configurations.
- **Number theory**: the construction reveals deep connections between class field theory and Euclidean geometry.
- **AI for science**: the first AI-disproved conjecture in a core mathematical field, verified by top human mathematicians. A landmark for AI-assisted research.

## Sources (参考文献)

- **一手 (Primary)**: Erdős, P. (1946). "On sets of distances of $n$ points." *American Mathematical Monthly* 53(5), 248–250. JSTOR: [link](https://www.jstor.org/stable/2305220)
- **一手**: Spencer, J., Szemerédi, E., Trotter, W. T. (1984). "Unit distances in the Euclidean plane." *Graph Theory and Combinatorics* (Cambridge, 1983), 293–303. Academic Press.
- **一手 (2026 disproof)**: OpenAI (2026-05-20). "An OpenAI model has disproved a central conjecture in discrete geometry." [openai.com](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)
- **一手 (verification)**: Alon, N., Bloom, T. F., Gowers, W. T., Litt, D., Sawin, W., Shankar, A., Tsimerman, J., Wang, V., Wood, M. M. (2026). "Remarks on the disproof of the unit distance conjecture." arXiv: [2605.20695](https://arxiv.org/abs/2605.20695)
- **一手 (exponent refinement)**: Sawin, W. (2026). "An explicit lower bound for the unit distance problem." arXiv: [2605.20579](https://arxiv.org/abs/2605.20579)

**Machine-checked line**: The companion paper's correctness has been certified by peer review (Fields Medalist + 8 specialists). The Lean-formalization of the underlying Golod–Shafarevich theorem exists in Mathlib; the specific asymptotic construction has not been formalized.
<!-- zh -->
## 应用 (Where It Shows Up)

- **离散几何**：点配置的基础极值问题。
- **数论**：该构造揭示了类域论与欧几里得几何之间的深刻联系。
- **AI for science**：首个在核心数学领域被AI推翻的猜想，由顶尖人类数学家验证。AI辅助研究的里程碑。

## 参考文献 (Sources)

- **一手 (Primary)**: Erdős, P. (1946). "On sets of distances of $n$ points." *American Mathematical Monthly* 53(5), 248–250. JSTOR: [link](https://www.jstor.org/stable/2305220)
- **一手**: Spencer, J., Szemerédi, E., Trotter, W. T. (1984). "Unit distances in the Euclidean plane." *Graph Theory and Combinatorics* (Cambridge, 1983), 293–303. Academic Press.
- **一手 (2026年推翻)**: OpenAI (2026-05-20). "An OpenAI model has disproved a central conjecture in discrete geometry." [openai.com](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)
- **一手 (验证)**: Alon, N., Bloom, T. F., Gowers, W. T., Litt, D., Sawin, W., Shankar, A., Tsimerman, J., Wang, V., Wood, M. M. (2026). "Remarks on the disproof of the unit distance conjecture." arXiv: [2605.20695](https://arxiv.org/abs/2605.20695)
- **一手 (指数精化)**: Sawin, W. (2026). "An explicit lower bound for the unit distance problem." arXiv: [2605.20579](https://arxiv.org/abs/2605.20579)

**Machine-checked line**: 伴随论文的正确性已通过同行评审认证（菲尔兹奖得主 + 8位专家）。基础 Golod–Shafarevich 定理的 Lean 形式化存在于 Mathlib 中；具体渐近构造尚未被形式化。
<!-- L5-end -->
