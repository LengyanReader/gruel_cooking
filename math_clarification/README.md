# math_clarification — Math Clarification (数学释疑)

Basic mathematics and famous math problems, each given a **complete and accurate statement** plus a working **analogy** — with the premises laid bare, the conditions of validity spelled out, the directions of attack surveyed, and the historical efforts tracked. Everything else is decoration.

## Purpose

The other folders explain heaven (天), earth (地), and society (人) from first principles — and the language those principles are written in is mathematics. When a `/core` explanation says "grows exponentially" or an economics entry leans on expected value, the reader should find here the minimal unpacking, without opening a textbook.

The core deliverable of every entry is its **precise statement** (表述) and its **intuition** (譬喻) — because a problem you cannot state exactly, you have not begun; a problem you cannot picture, you have not understood. Around those two, each entry fixes:

- **Premises, assumptions, conditions** (前提·假设·成立条件) — what must hold for the claim to be true, and where it breaks when a premise fails.
- **Directions of attack** (解题方向) — the routes people have tried, why the obvious ones fail, what the winning one needed.
- **Historical efforts** (历史的努力) — the timeline: who tried, what broke, what fell, what stands.

## House Style — Anatomy of an Entry

1. **The idea in a line** — the whole entry compressed into one sentence.
2. **The precise statement** (精确表述) — the exact claim, with its quantifiers and constants.
3. **Intuition** (譬喻) — an everyday picture or a tiny concrete example.
4. **Premises & conditions** (前提·假设·成立条件) — the hidden assumptions; change one, watch the answer change.
5. **A little math** — only the notation needed for precision.
6. **Directions of attack & history** (解题方向·历史的努力) — how people tried, in order, and where it stands.
7. **Where it shows up** — at least one real appearance in 天, 地, or 人 (usually somewhere else in this cookbook).
8. **What people get wrong** — the boundary of the intuition; that is where understanding actually lives.
9. **Sources** (参考文献) — per the source rules below.

Entries with checkable claims carry a **Machine-checked** line at the end.

## Sources & References (参考文献与来源原则)

1. **第一手优先**: cite the original — Euler's 1736 paper, not a graph-theory textbook; Zhang's *Annals* paper, not a news article. Secondary sources are allowed only when the primary is lost or inaccessible, and are then flagged as 二手 (secondary).
2. **考证与信度评估**: every source carries a reliability note — 一手 (primary, digitized original), 权威版本 (scholarly edition/translation), 学界共识 (consensus view — interpretive, flagged), 存疑 (contested). Claims that live only in legend (the Fermat margin note, the Hippasus story, the oral origin of Collatz) are labeled as legend, never as fact.
3. **可回查链接**: stable identifiers where they exist — DOI, arXiv, publisher page, institutional digitization (Euler Archive, JSTOR, PNAS). Links are verified against the DOI resolver before being written down.
4. **宁缺毋滥**: an unverifiable link is worse than none. Where no stable link exists (e.g., Chen 1973, *Sci. Sinica*), give the full bibliographic citation — author, title, journal, volume, pages, year — and say so.

## Subdirectories

- [basics/](basics/README.md) — the ingredients: numbers, exponents & logarithms, growth, probability, infinity, proofs. More are planned.
- [famous_problems/](famous_problems/README.md) — famous problems and paradoxes, solved and open, each chosen because it teaches something about *how mathematics works*: why a simple question can be hard, why examples are not proofs, what abstraction buys.
- [lean/](lean/README.md) — the **appendix**, not the main text: the entries' key claims as Lean 4 code. Its job is to pin the premises into exact statements and to referee the computable claims. It cannot do analogies, history, or directions of attack — those live in the prose.
- [web/](web/README.md) — a **FastAPI viewer** that renders the entries by audience level and language: `?level=L0..L5` crops the depth, `?lang=en|zh|dual` picks the language. The same Markdown source, layered for different readers.
- `proof_narratives/` — **proof narratives (证明叙事)**: proofs retold as stories anyone can follow. Every step motivated, no unexplained leaps, dead ends shown as part of the road. The guiding creed: **math is never a difficult thing** — when a proof feels hard, the exposition has failed, not the reader. Each narrative retells one entry's proof as an arc: the puzzle → the false starts → the one key idea → the click.
  - [Erdős unit distance disproof](proof_narratives/erdos_unit_distance.md) *(first narrative — the AI's leap from a count of dots to the symmetries of number fields)*

## Suggested Order

Read [numbers](basics/numbers.md) → [exponents & logarithms](basics/exponents_and_logs.md) → [growth](basics/growth.md) first — they form the spine. The other basics entries stand alone. Each famous problem is self-contained and states any basics prerequisite.

## Contributing

Add an entry as one small file in `basics/`, `famous_problems/`, or `proof_narratives/` following the house style, then add a one-line index entry in the folder's README. Whenever another folder leans on a math idea, link to the entry here. Sources follow the rules above — no unverified links, no unsourced claims.

To make an entry render across the audience levels and languages in the [web viewer](web/README.md), wrap its sections with `<!-- L0 --> … <!-- L1 --> … <!-- L5 -->` level markers and `<!-- zh --> … <!-- zh-end -->` language markers. The markers are optional — a plain Markdown file still renders. The [Erdős unit distance entry](famous_problems/erdos_unit_distance.md) is the worked example of the full tagged format.
