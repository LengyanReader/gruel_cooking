# Monty Hall

<!-- L0 -->
<!-- dual -->
**The idea in a line:** After the host opens a goat door, your first pick still wins only $1/3$ of the time — so the other closed door holds the car $2/3$ of the time: switching doubles your chances. *(prereq: [probability](../basics/probability.md))*

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

You pick door 1 of 3; the car is placed uniformly. The host must then open a door that (a) is not yours, and (b) hides a goat. Under this host strategy:

$$P(\text{car behind door 1} \mid \text{host opened 3}) = \frac{1}{3},$$

hence $P(\text{car behind the other closed door}) = 2/3$. Switching wins with probability $2/3$; staying wins with $1/3$. If instead the host opens a *random* non-yours door and it merely happens to be a goat, the answer genuinely changes to $1/2$.

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

Pick one of three doors; your pick locks in $1/3$. The other two doors *jointly* hold $2/3$. Then the host — who knows where the car is and will never reveal it — opens a goat door among those two. He is not a random event; he is *information*. His reveal doesn't move the car, so your door stays at $1/3$, and the whole remaining $2/3$ concentrates on the one unopened door. Blow it up to 100 doors: you pick one, the host opens 98 goats — switch, obviously. Three doors is the same game, just weaker tea.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- **The host's strategy is the premise.** "Never opens the car, must open a door" is what keeps your $1/3$ frozen. Change it and the answer changes:
  - Host opens a random un-picked door, goat by luck → $1/2$ (verified in the Lean file).
  - Host malicious (only offers the switch when you've picked the car) → switching wins $0$.
  - Host generous (only offers when you've picked a goat) → switching wins $1$.
- The car is placed **uniformly** — an assumption, stated, not smuggled.
- The host's tie-breaking rule (which goat door when both are available) does **not** affect the $2/3$.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- $P(\text{car at your door}) = 1/3$ — unchanged by the reveal, because the host was *always* going to open a goat door, whichever door you chose.
- $P(\text{car at the other closed door}) = 1 - 1/3 = 2/3$.
- Weights, exactly: outcomes $(\text{car}, \text{hostOpens})$ are $(1,2): 1/6$, $(1,3): 1/6$, $(2,3): 1/3$, $(3,2): 1/3$. Then $P(\text{car}=1 \mid \text{host}=3) = \dfrac{1/6}{1/6 + 1/3} = \dfrac{1}{3}$. With a random host: $(2,3)$ drops to $1/6$ and the conditional becomes $\dfrac{1/6}{1/6 + 1/6} = \dfrac{1}{2}$.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1975**: Steve Selvin poses the problem (and names it "Monty Hall") in two letters to *The American Statistician* — including the first explicit treatment of the host-strategy variants.
- **1990**: Marilyn vos Savant's *Parade* column prints "switch" and receives ~10,000 letters — many from PhDs — insisting on 50/50. She was right; the episode became the canonical demonstration that conditional probability outrages intuition.
- **The general lesson**: the field of "Monty Hall variants" is now a standard exercise in stating host strategies precisely — a teaching case for why premises must be written down before computing.

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

Anywhere an informed actor filters your options: medical testing, intelligence, markets with insiders. The structure — someone who *knows* choosing what to show you — is the same structure as biased sampling.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

"Two doors left, so 50/50" — that is the whole illusion. The reveal only *looks* free of information. The host's constraint — never reveal the car — leaks information about the door he didn't open.

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手: Selvin, S. (1975). "A Problem in Probability" (letters to the editor). *The American Statistician* 29(1), 67. <https://doi.org/10.1080/00031305.1975.10479121>（首次陈述与「Monty Hall」命名均出于此）
- 一手但难回查: vos Savant, M. (1990–91). "Ask Marilyn." *Parade* 杂志专栏（1990-09-09、1990-12-02、1991-02-17）. *Parade* 无官方在线档案，链接不可回查；事件经过（万封来信、PhD 质疑）为学界共识.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
**Machine-checked**: [MontyHall.lean](../lean/core/MontyHall.lean) — exact weights: switching wins $2/3$ with a knowing host, and $1/2$ with a lucky random host.

<!-- L4-end -->