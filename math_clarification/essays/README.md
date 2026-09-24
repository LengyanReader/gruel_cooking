# essays — 论说 (Essays & Meta-Reflections)

Long-form essays on mathematics itself: what it is, who does it, how it is judged, and what happens when the work of doing it changes hands. The nine-part entry anatomy (house style) is for *concepts and problems*; an essay argues. This folder keeps the argumentative pieces.

## The first essay

- [ai_and_math.md](ai_and_math.md) — **数学的危机，还是数学家的危机？——AI 时代关于数学的七问** / *A Crisis of Mathematics — or of the Mathematicians? Seven Questions in the Age of AI*. Seven interlocking chapters on AI and mathematics: the claims and their verification, the voices in the community, mathematics as a language, who mathematicians are, the division of labor under formalization, the question of groundbreaking problems, and a plain-spoken closing reflection. Anchored on this folder's own [Erdős unit distance record](../famous_problems/erdos_unit_distance.md) and its [proof narrative](../proof_narratives/erdos_unit_distance.md).

## Reference drafts (参考稿)

- [ref1/](ref1/) keeps working drafts and reference material consulted while writing the essay (er2/qw1/rf3/fr4 — English outlines, a full Chinese draft, and critical analyses). They are research material, not entries: the viewer never lists them (`web/parser.py` scans `essays/*.md` non-recursively), and they are not covered by the anatomy below. Keep them out of the essay index if you reorganize the folder.

## Essay anatomy (论说体例)

House style's nine parts are built around a *problem you can state and picture*. An essay has no such anchor. It is written in the register of philosophy of science and critical humanism — flowing prose, argument carried inside the paragraph, no thesis labels, no bullet scaffolding. But the prose is disciplined by a fixed internal sequence, which is the same five moves every time, even when none of them appears as a heading:

1. **论点 (Claim)** — the chapter's position, stated up front.
2. **论据 (Evidence)** — sourced facts, with the source's reliability tier attached (per house rules: 一手 / 权威版本 / 学界共识·解读 / 存疑, and **legend** never stated as fact).
3. **论证 (Argument)** — why the evidence supports the claim, and the counter-arguments dealt with in their strongest form.
4. **反诘 (Pushback)** — the honest limits: what this chapter cannot settle, which claims the author treats as 解读 (interpretation) rather than fact.
5. **来源 (Sources)** — consolidated at the file's end in an `<!-- L5 -->` block, following the same stable-link rules as entries.

Rules that differ from concept entries:

- No **Machine-checked** line. An essay contains no checkable claim; where it reports a checkable result (e.g. the unit-distance bounds), it cites the entry that carries the check.
- Level markers are minimal by design: `<!-- L1 -->` for the whole argument, `<!-- L5 -->` for the sources. The web viewer's level cropping is for school-like depth layering, which an essay does not need.
- The bilingual default for essays is **逐段并列** (paragraph-interleaved en/zh), because an essay's force lives in the prose, not in a diagram.
- The scholar's apparatus — signpost headings like "Claim." or "Pushback.", enumerations, tables — is *not* part of the register. The skeleton above is the discipline the prose obeys, and obedience is exactly what must stay invisible.

## Self-evolution

This folder registers a **new entry type** (论说/essay) alongside basics·famous_problems·proof_narratives. It is wired into the web viewer via `web/parser.py` `list_entries()`. If the essay skeleton starts to fork, the authoritative description moves up to `docs/workflows.md` (§ Self-evolution).