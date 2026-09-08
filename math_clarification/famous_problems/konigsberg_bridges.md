# Bridges of Königsberg

<!-- L0 -->
<!-- dual -->
**The idea in a line:** Can you cross each of Königsberg's seven bridges exactly once? No — and Euler's 1736 reason (count degrees, don't try routes) founded graph theory: erase everything except *what connects to what*.

<!-- L0-end -->
<!-- L2 -->
<!-- en -->
## The Precise Statement (精确表述)

A (multi)graph — landmasses as vertices, bridges as edges, parallel edges allowed — has a trail using **every edge exactly once** (an *Eulerian trail*) if and only if:

1. it is connected (apart from isolated vertices), and
2. the number of vertices of odd degree is **0 or 2**.

Königsberg's seven bridges give degrees $3, 3, 3, 5$ — four odd vertices — so no such walk exists.

<!-- L2-end -->
<!-- L1 -->
<!-- en -->
## Intuition (譬喻)

Squash each landmass to a dot and each bridge to a line. Walk a route using every line once. At any dot that is neither start nor finish, every arrival needs a departure: bridges at such a dot come in *pairs*. So all middle dots must have an even number of bridges, and only the start and end may be odd. Königsberg: all four dots are odd — at most two are allowed. Impossible. No route-searching needed.

<!-- L1-end -->
<!-- L2 -->
<!-- en -->
## Premises & Conditions (前提·假设·成立条件)

- **"Each bridge exactly once"** — the condition. A walk visiting each *vertex* once is the different (Hamiltonian) question with no clean test at all.
- **Connectedness is the silent premise**: with the landmasses split into pieces, no single trail can cover edges in different components — the theorem quietly assumes you can reach every edge.
- The theorem counts **parallel edges separately** — Königsberg's doubled bridge 1–2 genuinely contributes 2 to each degree; this is why the problem needs multigraphs, not simple graphs.
- The theorem is about **existence**; a constructive version (Hierholzer, 1873) gives the route whenever the condition holds.

<!-- L2-end -->
<!-- L3 -->
<!-- en -->
## A Little Math

- Graph: vertices (dots), edges (lines); degree = edges meeting a vertex.
- Euler's theorem: Eulerian trail exists $\iff$ 0 or 2 odd-degree vertices (plus connectedness).
- Königsberg: degrees $3, 3, 3, 5$ → four odd → impossible. Add one bridge (2–3): degrees $5, 4, 4, 3$ → exactly two odd → a trail exists.

<!-- L3-end -->
<!-- L3 -->
<!-- en -->
## Directions of Attack & History (解题方向·历史的努力)

- **1735/1741**: Euler presents his solution (1735) and publishes it (1741) as *Solutio problematis ad geometriam situs pertinentis* — the solution that does not search routes but *counts degrees*; the paper's title ("geometry of position") is the birth certificate of topology and graph theory.
- **The bridges themselves**: the real layout changed over centuries; two bridges were destroyed in World War II, and today's Kaliningrad has five bridges — with exactly two odd-degree landmasses, so the walk is now *possible*. The theorem tracks the city.
- **1873**: Hierholzer gives the algorithm that actually constructs the trail — the proof turned into a method (used today in route planning and circuit design).
- **1857 → hard variant**: Hamilton's Icosian game (visit every vertex once) has no degree-counting shortcut — it seeds the traveling-salesman problem, famously hard to this day. Same dots and lines; different question; different century of difficulty.

<!-- L3-end -->
<!-- L5 -->
<!-- dual -->
## Where It Shows Up

GPS routing, circuit design, the Chinese postman problem, social networks, the web itself. The abstraction — keep only *connections*, drop distances, shapes, names — is the birth of topology.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
## What People Get Wrong

- The proof's power is in what it *erases*. Students want to draw routes; Euler counted. That act of choosing what to ignore is what made the problem general.
- Not the same problem: visiting every *vertex* once (the Hamiltonian question) has no clean test — it is famously hard.

<!-- L4-end -->
<!-- L5 -->
<!-- dual -->
## Sources (参考文献)

- 一手: Euler, L. (1741). "Solutio problematis ad geometriam situs pertinentis." *Commentarii academiae scientiarum Petropolitanae* 8, 128–140. Euler Archive E53（含英译）: <https://scholarlycommons.pacific.edu/euler-works/53/>
- 一手: Hierholzer, C. (1873). "Ueber die Möglichkeit, einen Linienzug ohne Wiederholung und ohne Unterbrechung zu umfahren." *Mathematische Annalen* 6, 30–32. <https://doi.org/10.1007/BF01442866>
- 考证注: 论文呈报于 1735 年、刊出于 1741 年（非 1736 年刊出）; 加里宁格勒今日桥梁布局的变化为后世史料转述（二手）.

<!-- L5-end -->
<!-- L4 -->
<!-- dual -->
**Machine-checked**: [Konigsberg.lean](../lean/core/Konigsberg.lean) — all $7! = 5040$ orderings checked: none works; add one bridge and a trail exists.

<!-- L4-end -->