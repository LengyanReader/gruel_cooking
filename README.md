# gruel_cooking

> Cook a pot of understanding — heaven, earth, and society — from the simplest ingredients.

## Project Overview

This project uses **basic and first principles** to interpret and demonstrate phenomena across three domains: **heaven** (天), **earth** (地), and **society** (人). It goes beyond application — it includes **metathinking** on why these so-called "basic" principles hold at all, which itself opens doors to deeper inquiry and further research.

The name "gruel_cooking" is deliberate: gruel is the simplest food, made from the most fundamental ingredients. This project seeks the simplest explanatory kernels that can account for complex observed phenomena.

## Three Pillars

### 1. First Principles Interpretation (`/core`)

Using foundational principles from physics, logic, information theory, and systems thinking to interpret phenomena across:

- **Heaven** (天): celestial mechanics, cosmological structure, astronomical observation
- **Earth** (地): climate systems, geological processes, ecological dynamics
- **Society** (人): human behavior, institutional structures, economic patterns

Each principle is paired with a **metathinking** component: not just "how does this principle work" but "why does this principle hold, and what are the boundaries of its applicability?"

### 2. Astronomy, Celestial Appearance & Climate (`/heaven_climate`)

The starting point for investigation: recent and leading topics in:

- Astronomical phenomena and celestial appearance (visible sky, historical records)
- Climate dynamics and paleoclimate evidence
- Trackable history of relevant works, papers, and intellectual lineages

Each topic includes source tracking, key references, and research genealogy.

### 3. Cross-Culture Economics (`/economics_cross_culture`)

An independent directory collecting cases, principles, and concepts from various economic traditions across cultures:

- **Western economics**: classical, neoclassical, Austrian, Keynesian, institutional
- **Chinese economics** (中国经济思想): historical fiscal systems, guanxi economics, dynastic economic thought
- **Comparative analysis**: where different traditions agree, diverge, or illuminate each other

### 4. Math Clarification (`/math_clarification`)

The language of first principles, explained minimally — basic mathematics and famous math problems in one-screen entries, following the cookbook's rules: picture first, notation only after meaning, and every entry ends with the place intuition breaks (数学释疑):

- **`basics/`**: the ingredients — numbers, exponents & logarithms, growth, probability, infinity, proofs (with more planned)
- **`famous_problems/`**: solved and open problems chosen for what they teach about how mathematics works — Monty Hall, the birthday paradox, the bridges of Königsberg, Goldbach & twin primes, Collatz, Fermat's Last Theorem, the 2026 Erdős unit-distance disproof
- **`lean/`**: the key claims as machine-checked Lean 4 — a proof assistant where the compiler is the referee; open conjectures are stated openly with `sorry`, proved claims carry none
- **`proof_narratives/`**: proofs retold as stories anyone can follow — the first is the Erdős disproof, the AI's leap from counting dots to the symmetries of number fields
- **`web/`**: a FastAPI viewer that renders every entry by audience level (`?level=L0..L5`) and language (`?lang=en|zh|dual`)

## Directory Structure

```
gruel_cooking/
├── README.md
├── core/                          # First principles & metathinking
│   ├── heavenly/                  # Principles for interpreting "heaven"
│   ├── earthly/                   # Principles for interpreting "earth"
│   ├── societal/                  # Principles for interpreting "society"
│   └── metathinking/              # Why do these principles hold?
├── heaven_climate/                # Astronomy & climate research
│   ├── celestial_appearance/      # Observable sky phenomena
│   ├── climate_dynamics/          # Climate systems & paleoclimate
│   ├── history_of_ideas/          # Trackable intellectual history
│   └── current_research/          # Recent & leading topics
├── economics_cross_culture/       # Cross-culture economics
│   ├── western/                   # Western economic traditions
│   ├── chinese/                   # Chinese economic thought
│   ├── other_traditions/          # Other cultural economic thought
│   ├── comparative/               # Cross-tradition analysis
│   └── cases/                     # Specific historical cases
├── math_clarification/            # Math basics & famous problems, minimally explained
│   ├── basics/                    # Numbers, exponents & logs, growth, probability, infinity, proofs
│   ├── famous_problems/           # Monty Hall, birthday paradox, Königsberg, Goldbach, Collatz, FLT, Erdős
│   ├── lean/                      # Key claims as machine-checked Lean 4
│   ├── proof_narratives/          # Proofs retold as stories (Erdős disproof first)
│   └── web/                       # FastAPI viewer: level (L0-L5) × language (en/zh/dual)
└── test
```

## Principles of Operation

1. **Start from the observable**: Every inquiry begins with a concrete phenomenon or question.
2. **Reduce to the simplest sufficient explanation**: Apply first principles to find the minimal explanatory model.
3. **Question the explanation itself**: Metathink — why does this principle work? What assumptions does it carry? Where does it break?
4. **Track the genealogy**: Every idea has a history. Document the chain of influence.
5. **Cross-pollinate**: Economics informs climate, climate informs astronomy, astronomy informs economics. Keep the connections alive.
6. **Cook with simple ingredients** (以最朴素的食材熬粥): Complexity emerges from the interaction of simple rules. Trust the gruel.
7. **Sources before stories** (来源先于叙述): cite first-hand documents over retellings; verify sources and grade their reliability; give checkable links where they exist, and say so where they don't — an unverifiable link is worse than none.

## How to Contribute

- Add a principle with its metathinking to `/core`
- Research a celestial/climate topic with full source tracking to `/heaven_climate`
- Document an economic case from any cultural tradition to `/economics_cross_culture`
- Always answer: "What is the simplest version of this that still explains what we observe?"
