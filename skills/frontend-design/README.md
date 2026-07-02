# Frontend Design Skills

13 agent skills for building interfaces with uncommon care — design systems, visual craft, interaction feel, and quality gates. Each skill inspects the actual codebase first (tokens, drift, smells), decides via explicit rules, and produces working code plus an audit artifact, per the standard in [`docs/SKILL_SPEC.md`](../../docs/SKILL_SPEC.md).

## The Skills

**Foundation**

| Skill | Produces |
|---|---|
| **frontend-orchestrator** | Diagnosis + roadmap: assesses maturity from code signals (not a questionnaire) and routes through one of five paths |
| **design-foundation** | Design tokens extracted from the real codebase ("extract before you invent"), with migration map |

**Visual**

| Skill | Produces |
|---|---|
| **layout-system** | Refactored layouts with Grid-vs-Flexbox decision rules and 5-width verification |
| **typography-system** | Type scale chosen by product density, as tokens with contrast verification |
| **color-system** | Semantic palette with a mandatory contrast table (WCAG AA gate) in light and dark modes |
| **visual-hierarchy-refactoring** | Priority audit table (intended vs actual emphasis) + refactored code, fixed in strict order |

**Component**

| Skill | Produces |
|---|---|
| **component-architecture** | Refactored components + Component Architecture Audit (split rules, prop design, extraction thresholds) |

**Interaction**

| Skill | Produces |
|---|---|
| **interaction-physics** | Animation Spec: 3–4 motion tokens, duration/easing decision table, reduced-motion baseline |
| **loading-states** | Async-surface audit + skeletons/spinners/empty states chosen by latency and layout knowledge |
| **error-handling-recovery** | Error-state matrix (failure mode × message × placement × recovery) + fixed silent failures |
| **performance-optimization** | Before/after measurement audit; optimistic-vs-pessimistic strategy by failure cost; real CWV targets (LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1) |

**Quality**

| Skill | Produces |
|---|---|
| **accessibility-excellence** | WCAG 2.2 AA audit citing criteria, severity-ranked, with fixes and an honest "not verified" section |
| **design-engineer-mindset** | Design-to-code Fidelity Report: exact values, detected system, deviations flagged not silently fixed |

Most skills keep deep pattern galleries in their own `references/` directory, loaded only when needed.

## Where to Start

Run `frontend-orchestrator`. It inspects the codebase and commits to exactly one path:

- **Path A** — Building from scratch
- **Path B** — Formalizing an existing, inconsistent design
- **Path C** — Improving a mature system
- **Path D** — Fixing performance issues
- **Path E** — Improving accessibility

Accessibility and performance emergencies override maturity-based routing.

If you already know the single problem ("our spacing is inconsistent", "add loading states", "is this accessible?"), invoke that skill directly — each stands alone.

## Philosophy

These skills embody **"uncommon care"** (Interface Craft): reduce until it's clear, refine until it's right. The skills operationalize that instinct as checkable quality bars — contrast ratios computed, line lengths counted, motion tokens capped — so craft survives contact with deadlines. Background reading: [`docs/PHILOSOPHY.md`](../../docs/PHILOSOPHY.md) and [`docs/RESEARCH.md`](../../docs/RESEARCH.md).
