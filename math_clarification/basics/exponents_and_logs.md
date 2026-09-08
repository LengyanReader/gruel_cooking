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

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

"Log base 2 of 8 is 3" just answers: *how many doublings from 1 to 8?* That's the whole concept. How many folds of paper to reach the Moon? $\log_2(4.4 \times 10^{12}) \approx 42$. How many halvings until 1% of a sample remains? $\log_2 100 \approx 6.6$ half-lives. The log asks "how many ×'s?" — and the answer turns out to be the number of digits your calculator needs. That is why every "×10 is +1" scale in the world — decibels, pH, Richter, star magnitudes — is a logarithm.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- The base must satisfy **$b > 0$, $b \neq 1$**. $\log_1 x$ is nonsense ($1^y = 1$ for every $y$ — the undo button has no unique answer), and non-positive bases break $b^x$ for non-integer $x$.
- The argument must satisfy **$x > 0$**: no real exponent of a positive base gives a negative or zero result. Logs of negatives are undefined over $\mathbb{R}$; the complex extension is multi-valued (the premise fails and the tool gains a branch cut).
- The addition law holds *because* $b^{x+y} = b^x \cdot b^y$ — one premise, two faces.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- $\log_2 8 = 3$; $\log_{10} 1000 = 3$; $2^3 \cdot 2^4 = 2^7$.
- Slide rules: multiply numbers by *adding* lengths — $\log(ab) = \log a + \log b$, physically.
- Bits: a message with $N$ equally likely outcomes carries $\log_2 N$ bits of information.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1614**: Napier publishes his logarithm tables — computing by addition instead of multiplication, built to speed Kepler's astronomy. Briggs (1624) re-based them to 10.
- **~1622**: Oughtred's slide rule — the same idea as hardware, in use until the 1970s.
- **1748**: Euler (Introductio) names $e$, defines the natural logarithm, and ties logs to growth — the exponential/log pair becomes one object.
- **1860**: Weber–Fechner law — perception (brightness, loudness) is roughly logarithmic in stimulus; the log lives in our senses.
- **1948**: Shannon measures information in $\log_2$ — the modern career of the logarithm.

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