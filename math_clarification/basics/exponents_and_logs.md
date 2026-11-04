# Exponents & Logarithms

<!-- L0 -->
<!-- dual -->
**The idea in a line:** An exponent counts repeated multiplication ($2^3 = 2 \cdot 2 \cdot 2 = 8$); a logarithm is the undo button ($\log_2 8 = 3$) — and it compresses huge ranges into readable ones.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

- For $b > 0$: $b^0 = 1$, $b^{x+y} = b^x \cdot b^y$, $(b^x)^y = b^{xy}$, $b^{-x} = 1/b^x$.
- $\log_b(x)$ := the unique $y$ with $b^y = x$, defined for $b > 0$, $b \neq 1$ and $x > 0$.
- The one theorem behind all log scales: **$\log_b(xy) = \log_b x + \log_b y$** — logs turn multiplication into addition. (And $\log_b x = \ln x / \ln b$: bases differ by a constant.)

<!-- zh -->
## 精确表述 (The Precise Statement)

- 对 $b > 0$：$b^0 = 1$，$b^{x+y} = b^x \cdot b^y$，$(b^x)^y = b^{xy}$，$b^{-x} = 1/b^x$。
- $\log_b(x)$ := 使 $b^y = x$ 的唯一 $y$；定义域要求 $b > 0$、$b \neq 1$ 且 $x > 0$。
- 一切对数标度背后的同一条定理：**$\log_b(xy) = \log_b x + \log_b y$**——对数把乘法变成加法。（且 $\log_b x = \ln x / \ln b$：底与底之间只差一个常数。）

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

"Log base 2 of 8 is 3" just answers: *how many doublings from 1 to 8?* That's the whole concept. How many folds of paper to reach the Moon? $\log_2(4.4 \times 10^{12}) \approx 42$. How many halvings until 1% of a sample remains? $\log_2 100 \approx 6.6$ half-lives. The log asks "how many ×'s?" — and the answer turns out to be the number of digits your calculator needs. That is why every "×10 is +1" scale in the world — decibels, pH, Richter, star magnitudes — is a logarithm.

<!-- zh -->
## 譬喻 (Intuition)

「8 的以 2 为底对数是 3」只回答一件事：*从 1 到 8 需要翻倍几次？*概念全在这。纸对折多少次能到月球？$\log_2(4.4 \times 10^{12}) \approx 42$。样品衰减到剩 1% 要几轮减半？$\log_2 100 \approx 6.6$ 个半衰期。对数问的是「乘了几次？」——而答案恰好就是计算器上需要的位数。这就是为什么世间一切「×10 记 +1」的标度——分贝、pH、里克特震级、星等——都是对数。

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- The base must satisfy **$b > 0$, $b \neq 1$**. $\log_1 x$ is nonsense ($1^y = 1$ for every $y$ — the undo button has no unique answer), and non-positive bases break $b^x$ for non-integer $x$.
- The argument must satisfy **$x > 0$**: no real exponent of a positive base gives a negative or zero result. Logs of negatives are undefined over $\mathbb{R}$; the complex extension is multi-valued (the premise fails and the tool gains a branch cut).
- The addition law holds *because* $b^{x+y} = b^x \cdot b^y$ — one premise, two faces.

<!-- zh -->
## 前提·假设·成立条件 (Premises & Conditions)

- 底数必须满足 **$b > 0$，$b \neq 1$**。$\log_1 x$ 是无意义的（$1^y = 1$ 对一切 $y$ 成立——撤销键没有唯一答案）；非正底数会让 $b^x$ 在非整数指数处崩坏。
- 真数必须满足 **$x > 0$**：正底的实指数幂永远不会给出负数或零。负数的对数在 $\mathbb{R}$ 上无定义；复数扩张后成为多值——前提失效之处，工具长出一条分支切割线。
- 加法律之所以成立，*正因为* $b^{x+y} = b^x \cdot b^y$——一条前提，两副面孔。

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- $\log_2 8 = 3$; $\log_{10} 1000 = 3$; $2^3 \cdot 2^4 = 2^7$.
- Slide rules: multiply numbers by *adding* lengths — $\log(ab) = \log a + \log b$, physically.
- Bits: a message with $N$ equally likely outcomes carries $\log_2 N$ bits of information.

<!-- zh -->
## 一点数学 (A Little Math)

- $\log_2 8 = 3$；$\log_{10} 1000 = 3$；$2^3 \cdot 2^4 = 2^7$。
- 计算尺：靠*加法*完成乘法——$\log(ab) = \log a + \log b$ 的物理化身。
- 比特：一个有 $N$ 种等可能结果的消息，携带 $\log_2 N$ 比特的信息。

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1614**: Napier publishes his logarithm tables — computing by addition instead of multiplication, built to speed Kepler's astronomy. Briggs (1624) re-based them to 10.
- **~1622**: Oughtred's slide rule — the same idea as hardware, in use until the 1970s.
- **1748**: Euler (Introductio) names $e$, defines the natural logarithm, and ties logs to growth — the exponential/log pair becomes one object.
- **1860**: Weber–Fechner law — perception (brightness, loudness) is roughly logarithmic in stimulus; the log lives in our senses.
- **1948**: Shannon measures information in $\log_2$ — the modern career of the logarithm.

<!-- zh -->
## 解题方向·历史的努力 (Directions of Attack & History)

- **1614 年**：纳皮尔发表对数表——以加法代替乘法，为开普勒的天文计算提速。布里格斯（1624）改底为 10。
- **约 1622 年**：奥特雷德的计算尺——同一思想做成硬件，一直用到 1970 年代。
- **1748 年**：欧拉（《无穷分析引论》）命名 $e$、定义自然对数，并把对数与增长系于一线——指数/对数自此成为一个对象的两面。
- **1860 年**：韦伯–费希纳定律——感知（亮度、响度）对刺激大致成对数；对数活在感官里。
- **1948 年**：香农以 $\log_2$ 度量信息——对数的现代生涯自此开启。

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

Decibels (sound), Richter (earthquakes — 地), pH (acidity), stellar magnitudes (5 steps = ×100 brightness — 天, see [heaven_climate](../../heaven_climate/README.md)), information in bits, Moore's-law charts.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- A logarithm is not "slow growth" — it is growth that keeps slowing, forever.
- Confusing the pair inverts the story: plotted on a log axis, an explosion looks calm. "Logarithmic growth" of cases on a log chart is still exponential spread (see [growth](growth.md)).

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手: Napier, J. (1614). *Mirifici Logarithmorum Canonis Descriptio.* Edinburgh. 无稳定在线链接（数字化副本散见于 archive.org，链接待考证）.
- 一手: Euler, L. (1748). *Introductio in analysin infinitorum*, vol. 1 — Euler Archive E101: <https://scholarlycommons.pacific.edu/euler-works/101/>（e 与自然对数由此定名）.
- 一手: Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal* 27(3), 379–423. <https://doi.org/10.1002/j.1538-7305.1948.tb01338.x>
- 一手: Fechner, G. T. (1860). *Elemente der Psychophysik.* 无稳定在线链接（Weber–Fechner 定律出处，二手转述常见，此处据原书）. 

<!-- L5-end -->