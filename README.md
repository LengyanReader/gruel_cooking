# 舟洲粥 Zhōu Zhōu Zhōu

**[中文 README](README.zh-CN.md) | English**

> **一叶小舟，渡万洲之远；一碗清粥，暖天地之心。**
>
> *A small boat, sailing across distant continents; a warm bowl of porridge, soothing heaven and earth.*

---

## Project Overview

Cooking porridge from the simplest ingredients — using **first principles** to interpret phenomena across heaven, earth, and society. Beyond application, we ask: why do these "basic" principles hold at all? Where are their boundaries?

Porridge is the simplest food, made from the most fundamental ingredients. This project seeks the minimal kernels that explain complex observed phenomena.

---

## Five Pillars

### 1. First Principles & Metathinking (`/core`)

Distilling fundamental principles from physics, logic, information theory, and systems thinking, applied across three domains:

| Domain | Content |
|---|---|
| **Heaven (天)** | Celestial mechanics, cosmological structure, astronomical observation |
| **Earth (地)** | Climate systems, geological processes, ecological dynamics |
| **Society (人)** | Human behavior, institutional structures, economic patterns |

Each principle includes **metathinking**: not just "how does it work" but "why does it hold, and where does it break?"

### 2. Heaven & Climate (`/heaven_climate`)

The starting point for investigation — tracking leading topics:

- Celestial phenomena and historical records
- Climate dynamics and paleoclimate evidence
- Source tracking and intellectual genealogy

### 3. Cross-Culture Economics (`/economics_cross_culture`)

An independent collection, comparison, and analysis of economic wisdom across civilizations:

- **Western economics**: classical, neoclassical, Austrian, Keynesian, institutional
- **Chinese economic thought**: historical fiscal systems, guanxi economics, dynastic economic thought
- **Other traditions**: Islamic, Indian, African economic thought
- **Comparative analysis**: consensus, divergence, and mutual illumination across traditions

### 4. Math Clarification (`/math_clarification`)

The language of first principles, explained with radical simplicity — basics and famous problems, one page each, visuals first, formulas second, intuition always:

- **`basics/`**: numbers, exponents & logarithms, growth, probability, infinity, proofs
- **`famous_problems/`**: Monty Hall, birthday paradox, Königsberg bridges, Goldbach & twin primes, Collatz, Fermat's Last Theorem, the 2026 Erdős unit-distance disproof
- **`lean/`**: key claims as machine-checked Lean 4 — the compiler is the referee
- **`proof_narratives/`**: proofs retold as stories (the Erdős disproof first)
- **`web/`**: a web viewer rendering each entry by audience level (L0–L5) and language (en/zh/dual)

### 5. Living Cultural Corridors (`/living_heritage`)

Fieldwork-based, comparative in method, digitally-enabled —

Investigating how human cultural relations persist, transform, and regenerate through movement, place, material life, and exchange networks.

- Primary field laboratory: **Beijing Grand Canal**
- Main Swedish comparative case: **Gotland**
- Focus: the subtle interfaces between the Grand Canal and Silk Roads systems

---

## Directory Structure

```
gruel_cooking/
├── README.md                   # English readme
├── README.zh-CN.md             # Chinese readme
├── docs/                       # GitHub Pages landing page
├── core/                       # First principles & metathinking
│   ├── heavenly/               # Interpreting "heaven"
│   ├── earthly/                # Interpreting "earth"
│   ├── societal/               # Interpreting "society"
│   └── metathinking/           # Why do these principles hold?
├── heaven_climate/             # Astronomy & climate
│   ├── celestial_appearance/   # Observable sky phenomena
│   ├── climate_dynamics/       # Climate systems
│   ├── history_of_ideas/       # Intellectual history
│   └── current_research/       # Leading topics
├── economics_cross_culture/    # Cross-culture economics
│   ├── western/                # Western traditions
│   ├── chinese/                # Chinese economic thought
│   ├── other_traditions/       # Other traditions
│   ├── comparative/            # Comparative analysis
│   └── cases/                  # Specific cases
├── math_clarification/         # Math clarification
│   ├── basics/                 # Fundamentals
│   ├── famous_problems/        # Classic problems
│   ├── lean/                   # Lean 4 formalization
│   ├── proof_narratives/       # Proof narratives
│   └── web/                    # Web viewer
└── living_heritage/            # Living Cultural Corridors
    ├── app/                    # Application layer
    ├── data/                   # Data layer
    └── scripts/                # Scripts
```

---

## Operating Principles

1. **Start from the observable** — every inquiry begins with a concrete phenomenon or question.
2. **Reduce to the minimal** — find the smallest model that explains using first principles.
3. **Question the explanation** — why does it hold? What does it assume? Where does it fail?
4. **Trace the genealogy** — every idea has an origin; record the chain of influence.
5. **Cross-pollinate** — economics nourishes climate, climate nourishes astronomy; keep the connections alive.
6. **The simplest ingredients** — complexity emerges from the interaction of simple rules. Trust the porridge.
7. **Sources before narrative** — cite primary sources, verify origins, mark reliability.

---

## How to Contribute

- Add a principle with its metathinking to `/core`
- Research a celestial/climate topic with full source tracking to `/heaven_climate`
- Document an economic case from any cultural tradition to `/economics_cross_culture`
- Explain a math concept with radical simplicity to `/math_clarification`

Always ask: **"What is the simplest version of this that still explains what we observe?"**