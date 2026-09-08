# Proof Narrative — The Day the Grid Fell (单位距离猜想的推翻：一则证明叙事)

> **The creed** (证明叙事的原则): *Math is never a difficult thing — when a proof feels hard, the exposition has failed, not the reader.* 数学从不难——当证明让人感到困难，是讲解的失败，而非读者的失败。
>
> This narrative retells one entry's proof as an arc: the puzzle → the false starts → the one key idea → the click. It pairs with [the formal entry](../famous_problems/erdos_unit_distance.md).

---

## Scene 1 — The Puzzle (谜题)

Put $n$ dots on an infinite flat table. Stretch a one-unit string between every pair of dots that is exactly one unit apart. How many strings can you possibly stretch?

Even before Erdős formalized it in 1946, everyone could see the floor. Line the dots up like beads:

- **A straight line**: neighboring dots one apart → about $n$ strings.
- **A chessboard**: each interior dot touches 4 neighbors → about $2n$ strings. Better.

Then Erdős found a trick. Take the chessboard but *rescale* it by a carefully chosen number — an irrational one. Now the distance-1 strings no longer come only from adjacent dots. Pairs that used to sit $\sqrt{2}$ apart, or $\sqrt{5}$, or $\sqrt{13}$ — after the rescaling, *all of them* become exactly one unit. The count jumps: instead of $2n$, you get roughly $n^{1 + C/\log\log n}$.

That exponent $1 + C/\log\log n$ is stubborn. As $n$ grows, $\log\log n$ grows too — agonizingly slowly — so the exponent creeps down toward 1, but never quite reaches it. The grid gives you "slightly better than linear, forever."

Erdős looked at this and made a bet: **nobody can do meaningfully better.** Not by a fixed polynomial amount. $u(n) = n^{1 + o(1)}$. Beat that if you can.

For eighty years, nobody could. And nobody proved it either. The problem just sat there, the most famous open question in discrete geometry, with a cash prize Erdős himself had put on it.

---

## Scene 2 — The False Starts (失败的起点)

Why is the problem hard? Because there are two directions of attack, and neither human instinct went far enough.

**Attack 1 — the upper bound (证明不能更好).** This is the "hard" direction: prove no clever arrangement beats the grid. It took until 1984 for Spencer, Szemerédi and Trotter to get *any* upper bound, and it was a weak one: $u(n) = O(n^{4/3})$. Not $n^{1+\epsilon}$ — a full $n^{1/3}$ above where anyone thought the truth lay. The gap between "we think it's about $n^1$" and "we can prove it's at most $n^{4/3}$" was enormous and would not budge.

**Attack 2 — the counterexample (寻找反例).** Mathematicians *did* try to beat the grid. They tried ragged point clouds, random scatterings, sphere packings. Nothing worked. Every cleverer arrangement fell back to about the same exponent. The grid, or its rescaled cousins, looked like the ceiling of what geometry alone could do.

Here is the trap. Everyone who attacked this problem thought of it *geometrically*. Dots on a plane, distances, arrangements. It's a picture. Of course you think in pictures.

The pictures were a cage. Nobody could beat the grid *because everyone was thinking in the wrong language.* The key wasn't hidden in geometry at all. It was hiding in a completely different branch of mathematics — one that has nothing, visually, to do with dots on a table.

---

## Scene 3 — The Key Idea (关键一步)

Stop thinking about *arrangements of dots*. Start thinking about where the distances $1,\sqrt{2},\sqrt{5},\sqrt{13}\ldots$ come from.

Erdős's grid works because the count of unit distances is secretly controlled by a **norm form**. Write a grid point as a Gaussian integer $a + bi$ (with $a,b$ integers and $i^2 = -1$). Its distance from the origin is $|a + bi| = \sqrt{a^2 + b^2}$. So the question "how many points are exactly distance 1 from the origin" is the same as "how many ways can 1 be written as $a^2 + b^2$ with $a,b$ integers."

And here's the hard wall: **1 has only finitely many such representations.** The Gaussian integers — the symmetries of the square grid — simply don't have enough room for the unit distances to pile up fast. That finiteness is *exactly* the reason the grid can't do better than $n^{1+o(1)}$. Erdős's lower bound and his conjectured ceiling both sit on this finiteness.

So the question became: *what if there were a number system with infinitely many ways to write 1 as a distance?*

That is the whole astonishing leap, and it took an AI to make it. The OpenAI model asked: **what if we replace the Gaussian integers with the ring of integers of a much richer number field $K$ — one whose symmetries are so vast that unit distances can pile up indefinitely?**

Two ingredients from algebraic number theory — utterly unused in this geometry problem for 80 years — turn that vague wish into a theorem:

1. **Dirichlet's unit theorem** says the unit group of a number field $K$ (its "symmetries") has rank $r_1 + r_2 - 1$, where $r_1$ counts real embeddings and $2r_2$ counts complex ones. Pick a field with many embeddings and its units explode.

2. **Golod–Shafarevich** (1964) guarantees you can build number fields whose *class group* — a measure of how "unbalanced" the arithmetic is — has arbitrarily large rank. And **Hajir–Maire–Ramakrishna** showed you can stack these into infinite towers with controlled behavior.

Through the *Minkowski embedding*, a number field with a huge unit group maps into the plane, and each unit becomes a lattice point. The more symmetries the field has, the more pairs at distance exactly 1 you can lay down — *without limit.*

The finiteness that had quietly capped the grid for 80 years was gone. Replace the Gaussian integers with a field of unbounded symmetry, and the exponent above $n$ stops being "a small amount toward 0" and becomes a *fixed positive number* $\delta$:

$$u(n) \geq n^{1 + \delta} \qquad \text{for infinitely many } n.$$

---

## Scene 4 — The Click (豁然开朗)

Look at what actually happened. The counterexample wasn't a cleverer arrangement of dots — it was a *change of number system*. The grid's ceiling wasn't a law of geometry; it was an artifact of ordinary integers having only finitely many representations of 1.

Once you see it, the whole shape of the 80-year failure makes sense:
- Humans thought geometrically → stayed inside the cage of finiteness.
- The key was *arithmetic* — a different language entirely.
- The AI, unbothered by the "obvious" way to look at a dots-and-distances problem, wandered into algebraic number theory and found the cage was made of glass.

Within days the result was sharpened and certified. Whit Sawin gave the explicit value $\delta = 0.014$. Nine mathematicians — including Fields medalist Tim Gowers — wrote the 19-page companion paper verifying the construction.

**And note what did *not* happen.** The problem is not solved. The gap is *wider* now, not narrower: we know $n^{1.014} \leq u(n) \leq n^{4/3}$. The true growth rate of $u(n)$ is still unknown. The AI demolished one conjecture and, in doing so, revealed how much terrain nobody has mapped — the space between the grid's true ceiling and the weak upper bound is enormous, and most of it is terra incognita.

The lesson of the whole arc is the cookbook's central creed made concrete: **a problem you cannot state exactly, you have not begun; a problem you cannot picture, you have not understood — but a problem you picture *too well* becomes a cage.** The unit distance conjecture fell not to harder work in the same direction, but to the refusal to stay inside the picture.

---

## Postscript — What this story is not (并非如此)

- **Not "AI solved it alone."** The model produced the construction; nine specialists wrote the human-verified proof, and Sawin found the constant. Collaboration — the model proposing, humans judging — is the accurate read.
- **Not a settled result overnight.** The disproof is human-verified and peer-reviewed by leading experts, but the full story of $u(n)$ is far from told. The gap tripled in mystery.
- **Not the end of algebraic geometry's use in combinatorics.** It's the beginning — the cross-domain pipeline this proof opened is likely to reappear.

---

## Sources (参考文献)

- 一手 (2026 disproof): OpenAI (2026-05-20). "An OpenAI model has disproved a central conjecture in discrete geometry." <https://openai.com/index/model-disproves-discrete-geometry-conjecture/>
- 一手 (verification): Alon, N., Bloom, T. F., Gowers, W. T., Litt, D., Sawin, W., Shankar, A., Tsimerman, J., Wang, V., Wood, M. M. (2026). "Remarks on the disproof of the unit distance conjecture." arXiv: <https://arxiv.org/abs/2605.20695>
- 一手 (exponent refinement): Sawin, W. (2026). "An explicit lower bound for the unit distance problem." arXiv: <https://arxiv.org/abs/2605.20579>
- 一手 (upper bound): Spencer, J., Szemerédi, E., Trotter, W. T. (1984). "Unit distances in the Euclidean plane." *Graph Theory and Combinatorics* (Cambridge, 1983), 293–303. Academic Press.
