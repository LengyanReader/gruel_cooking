# famous_problems — Famous Problems (名题)

Problems with simple statements and stubborn (or surprising) solutions. Each entry is self-contained and states any prerequisites. They are collected not for trivia but for what they teach about how mathematics works — that a simple question can hide a hard proof, that checking a million cases proves nothing, that abstraction is the art of choosing what to erase.

## Entries

- [Monty Hall](monty_hall.md) — should you switch doors? A game show that taught the world conditional probability. *(prereq: [probability](../basics/probability.md))*
- [Birthday paradox](birthday_paradox.md) — with 23 people a shared birthday is already more likely than not: collisions grow faster than intuition expects.
- [Bridges of Königsberg](konigsberg_bridges.md) — the impossible walk that founded graph theory: Euler solved it by erasing everything except connections.
- [Goldbach & twin primes](goldbach_and_twin_primes.md) — two elementary claims about primes, checked astronomically far and still unproven; one half fell in 2013.
- [Collatz](collatz.md) — the simplest rule in mathematics: nobody can prove every number reaches 1. The cookbook thesis in miniature: trivial rules, wild behavior.
- [Fermat's Last Theorem](fermat_last_theorem.md) — 358 years from a margin note to Wiles; why the proof had to go around the mountain.
- [Erdős Unit Distance Conjecture](erdos_unit_distance.md) — $n$ points, how many pairs exactly 1 apart? An 80-year-old conjecture about square grids, overturned in 2026 by an AI model using tools from algebraic number theory no one had connected to geometry. The first AI-disproved conjecture in a core field.

## On the stove (planned)

- P vs NP — is finding ever as easy as checking?
- Riemann hypothesis — pinning down exactly where the primes sit; one of the Clay Millennium problems.
- Four-color theorem — any map needs only four colors; first major proof by computer (1976) — what should count as a proof?
- $1 + 2 + 3 + \cdots = -1/12$ — the famous viral "sum" that is not a sum, and what analytic continuation actually does.
- Gödel's incompleteness theorems — proofs themselves have limits.

## House Style

Every entry follows the anatomy in [../README.md](../README.md): idea in a line → precise statement (精确表述) → intuition (譬喻) → premises & conditions (前提·假设·成立条件) → a little math → directions & history (解题方向·历史的努力) → where it shows up → what people get wrong → **sources (参考文献)**. Entries with machine-checkable claims carry a **Machine-checked** line linking to [../lean](../lean/README.md); open conjectures are stated there with `sorry`, and only there. Sources follow the source rules in the folder README: first-hand where possible, reliability note, verified link.
