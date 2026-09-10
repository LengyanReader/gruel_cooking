# 舟洲粥 Zhōu Zhōu Zhōu

> **一叶小舟，渡万洲之远；一碗清粥，暖天地之心。**
>
> *A small boat, sailing across distant continents; a warm bowl of porridge, soothing heaven and earth.*

---

## 项目概览 / Project Overview

以最朴素的食材熬粥——用**第一性原理**解读天地人三域现象，不止于应用，更追问：这些"基本"原理为何成立？其边界何在？

Cooking porridge from the simplest ingredients — using **first principles** to interpret phenomena across heaven, earth, and society. Beyond application, we ask: why do these "basic" principles hold at all? Where are their boundaries?

粥是最简单的食物，用最根本的食材熬成。本项目追寻的是能解释复杂现象的最简内核。

Porridge is the simplest food, made from the most fundamental ingredients. This project seeks the minimal kernels that explain complex observed phenomena.

---

## 五大板块 / Five Pillars

### 1. 第一性原理 · 元思考 / First Principles & Metathinking (`/core`)

从物理、逻辑、信息论与系统思维中提炼根本原理，应用于三域：

Distilling fundamental principles from physics, logic, information theory, and systems thinking, applied across three domains:

| 域 Domain | 内容 Content |
|---|---|
| **天 Heaven** | 天体运行、宇宙结构、天文观测 / Celestial mechanics, cosmological structure, astronomical observation |
| **地 Earth** | 气候系统、地质过程、生态动力学 / Climate systems, geological processes, ecological dynamics |
| **人 Society** | 人类行为、制度结构、经济模式 / Human behavior, institutional structures, economic patterns |

每个原理附带**元思考**：不仅问"这个原理如何运作"，更问"它为何成立？在何处失效？"

Each principle includes **metathinking**: not just "how does it work" but "why does it hold, and where does it break?"

### 2. 天文 · 天象 · 气候 / Heaven & Climate (`/heaven_climate`)

研究的起点——追踪前沿课题：

The starting point for investigation — tracking leading topics:

- 天象观测与历史天象记录 / Celestial phenomena and historical records
- 气候动力学与古气候证据 / Climate dynamics and paleoclimate evidence
- 相关文献溯源与思想谱系 / Source tracking and intellectual genealogy

### 3. 跨文化经济学 / Cross-Culture Economics (`/economics_cross_culture`)

各文明经济智慧的独立收集、比较与分析：

An independent collection, comparison, and analysis of economic wisdom across civilizations:

- **西方经济学** Western economics：古典、新古典、奥地利、凯恩斯、制度学派
- **中国经济思想** Chinese economic thought：历史财政体系、关系经济学、王朝经济思想
- **其他传统** Other traditions：伊斯兰、印度、非洲经济思想
- **比较分析** Comparative analysis：各传统的共识、分歧与互照

### 4. 数学释疑 / Math Clarification (`/math_clarification`)

第一性原理的语言，极简阐释——基础数学与名题，一屏读完，先图后式，直觉先行：

The language of first principles, explained with radical simplicity — basics and famous problems, one page each, visuals first, formulas second, intuition always:

- **`basics/`** 基础：数、指数与对数、增长、概率、无穷、证明
- **`famous_problems/`** 名题：蒙提霍尔、生日悖论、柯尼斯堡七桥、哥德巴赫与孪生素数、考拉兹、费马大定理、2026 Erdős 单位距离反证
- **`lean/`** Lean 4 机器验证：核心命题的形式化证明，编译器即裁判
- **`proof_narratives/`** 证明叙事：将证明讲成故事，Erdős 反证为第一篇
- **`web/`** Web 查看器：按受众等级（L0–L5）与语言（en/zh/dual）渲染

### 5. 活态文化廊道 · 博士研究 / Living Cultural Corridors — PhD (`/living_heritage`)

以田野为基础、以比较为方法、以数字技术为支撑——

Fieldwork-based, comparative in method, digitally-enabled —

探究人类文化关系如何通过流动、地方、物质生活和交换网络而持续、转型与再生。

Investigating how human cultural relations persist, transform, and regenerate through movement, place, material life, and exchange networks.

- 核心田野实验室：**北京大运河** / Primary field laboratory: **Beijing Grand Canal**
- 主要瑞典比较案例：**哥特兰** / Main Swedish comparative case: **Gotland**
- 聚焦：大运河与丝绸之路体系之间的微妙接口 / Focus: subtle interfaces between the Grand Canal and Silk Roads systems

---

## 目录结构 / Directory Structure

```
gruel_cooking/
├── README.md
├── docs/                           # GitHub Pages 首页 / Landing page
├── core/                           # 第一性原理 & 元思考 / First principles & metathinking
│   ├── heavenly/                   # 解读"天" / Interpreting "heaven"
│   ├── earthly/                    # 解读"地" / Interpreting "earth"
│   ├── societal/                   # 解读"人" / Interpreting "society"
│   └── metathinking/               # 原理为何成立？/ Why do these principles hold?
├── heaven_climate/                 # 天文 & 气候 / Astronomy & climate
│   ├── celestial_appearance/       # 天象观测 / Observable sky phenomena
│   ├── climate_dynamics/           # 气候系统 / Climate systems
│   ├── history_of_ideas/           # 思想史 / Intellectual history
│   └── current_research/           # 前沿课题 / Leading topics
├── economics_cross_culture/        # 跨文化经济学 / Cross-culture economics
│   ├── western/                    # 西方 / Western
│   ├── chinese/                    # 中国经济思想 / Chinese
│   ├── other_traditions/           # 其他传统 / Other traditions
│   ├── comparative/                # 比较 / Comparative
│   └── cases/                      # 案例 / Cases
├── math_clarification/             # 数学释疑 / Math clarification
│   ├── basics/                     # 基础 / Basics
│   ├── famous_problems/            # 名题 / Famous problems
│   ├── lean/                       # Lean 4 形式化 / Lean 4 formalization
│   ├── proof_narratives/           # 证明叙事 / Proof narratives
│   └── web/                        # Web 查看器 / Web viewer
└── living_heritage/                # 活态文化廊道 / Living Cultural Corridors
    ├── app/                        # 应用层 / Application layer
    ├── data/                       # 数据层 / Data layer
    └── scripts/                    # 脚本 / Scripts
```

---

## 运行原则 / Operating Principles

1. **从可感处起** Start from the observable — 一切追问始于一个可见的现象或具体的问题 / Every inquiry begins with a concrete phenomenon or question.
2. **化至最简** Reduce to the minimal — 用第一性原理找到最小解释模型 / Find the smallest model that explains using first principles.
3. **反问解释本身** Question the explanation — 这个原理为何成立？预设了什么？在哪里失效？/ Why does it hold? What does it assume? Where does it fail?
4. **追溯谱系** Trace the genealogy — 每个想法都有来历，记录影响的链条 / Every idea has an origin; record the chain of influence.
5. **跨界授粉** Cross-pollinate — 经济学滋养气候学，气候学滋养天文学，让连接活着 / Economics nourishes climate, climate nourishes astronomy; keep connections alive.
6. **以最朴素的食材** The simplest ingredients — 复杂性从简单规则的交互中涌现，相信那碗粥 / Complexity emerges from simple rules; trust the porridge.
7. **来源先于叙述** Sources before narrative — 引用一手文献，核实来源，标注可靠度 / Cite primary sources, verify origins, mark reliability.

---

## 如何参与 / How to Contribute

- 在 `/core` 中添加原理及其元思考 / Add a principle with its metathinking to `/core`
- 在 `/heaven_climate` 中研究天象/气候课题，附完整溯源 / Research a celestial/climate topic with full source tracking to `/heaven_climate`
- 在 `/economics_cross_culture` 中记录任一文化传统的经济案例 / Document an economic case from any cultural tradition to `/economics_cross_culture`
- 在 `/math_clarification` 中以极简方式阐释数学概念 / Explain a math concept with radical simplicity to `/math_clarification`

始终回答：**"这个现象最简单的解释版本是什么？"**

Always ask: **"What is the simplest version of this that still explains what we observe?"**
