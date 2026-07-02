---
name: frontend-orchestrator
description: "Diagnose a codebase's frontend design maturity and route the work through the right sequence of frontend-design skills. Use when the user makes a broad or vague design request — 'make this look better', 'polish the UI', 'this feels like an MVP', 'our frontend is a mess', 'where do I start with design', 'make it feel professional', 'plan a design system' — or when a request spans multiple design concerns and it's unclear which single skill applies. Assesses maturity by inspecting the actual code (Tailwind config, CSS variables, component structure, hex-code drift), picks one of five implementation paths, and produces a design roadmap: an evidence-backed maturity diagnosis plus an ordered skill sequence with the artifact each step passes to the next. If the request clearly maps to one concern (only spacing, only color, only type), skip this and invoke that skill directly."
---

# Frontend Design Orchestrator

You are a dispatcher, not a lecturer. Given a broad design request, inspect the codebase, diagnose its design maturity from evidence (never from a questionnaire), pick one implementation path, and hand off to concrete skills in dependency order — stating what artifact each step produces for the next. The governing principle: **fix foundations before surfaces**. Polishing animations on top of 50 drifted hex codes is wasted work.

## When to use / when not to

- Use for broad, multi-concern, or vague requests ("make it better", "it looks amateur", "plan our design system").
- Do NOT use when the request names a single concern. Route directly:
  - Spacing/type/color tokens missing or drifting → `skills/frontend-design/design-foundation`
  - "Spacing/alignment/responsive is broken" → `skills/frontend-design/layout-system`
  - "Fonts/text look off" → `skills/frontend-design/typography-system`
  - "Colors clash / need dark mode" → `skills/frontend-design/color-system`
  - "Cluttered / can't tell what's important" → `skills/frontend-design/visual-hierarchy-refactoring`
  - Errors, loading, animation, a11y, perf → the matching skill in `skills/frontend-design/`

## Step 1 — Inspect the codebase (do this before asking anything)

Run these checks and record findings as evidence:

1. **Token infrastructure.** Glob for `tailwind.config.{js,ts,cjs,mjs}`, `**/globals.css`, `**/index.css`, `**/tokens*`, `**/*theme*`. Read what exists. Tailwind v4 projects define tokens in CSS via `@theme`; v3 in the config file.
2. **Color drift.** Grep component/CSS files for `#[0-9a-fA-F]{3,8}\b` and `rgb\(|rgba\(|hsl\(`. Count distinct values. >15 raw colors outside a token file = no working color system.
3. **Spacing/type drift.** Grep for `font-size:|text-\[|\d+px`. Arbitrary Tailwind values (`p-[13px]`, `text-[15px]`) and one-off px values = no scale.
4. **Component structure.** Is there a `components/` (or `ui/`) directory? Are buttons/inputs reused components or copy-pasted markup? Grep for `<button` occurrences vs. a `Button` component.
5. **Dark mode & a11y signals.** Grep for `prefers-color-scheme|dark:` and `aria-|sr-only|prefers-reduced-motion`.
6. **Interaction signals.** Grep for `transition|animation|@keyframes` — none at all, or `transition: all` everywhere, both tell you something.

## Step 2 — Intake (one tight batch, only what code can't tell you)

Ask at most: **primary goal right now** (ship fast / retention / reduce support load / brand polish) and **the screen or flow that matters most**. Infer stack, framework, and maturity from the code. **Don't stall:** if the user already stated a goal or the repo makes it obvious, state your assumptions and proceed.

## Step 3 — Diagnose maturity from evidence

| Level | Code signals |
|---|---|
| 1 — Functional MVP | No token file; heavy raw hex/px; copy-pasted markup; no dark mode; no a11y attributes |
| 2 — Consistent-ish | Partial Tailwind theme or a few CSS variables; components exist but drift; arbitrary values common |
| 3 — System-driven | Tokens defined and mostly used; component library; a11y present; but generic feel, mechanical interactions |
| 4 — Refined | Tokens semantic and layered; consistent motion; strong a11y; refinement work is at the margins |
| 5 — Transcendent | Rare; only refinement/maintenance routing applies |

State the level with 2–3 pieces of concrete evidence (file paths, counts).

## Step 4 — Route: pick exactly one path

Decision rules, evaluated in order:

- **Accessibility complaints, legal exposure, or a failing audit → Path E** (regardless of maturity).
- **Users complain it's slow, or Core Web Vitals are the stated pain → Path D.**
- **Level 1 (little to formalize) → Path A.**
- **Level 2 (patterns exist but drift) → Path B.**
- **Level 3–4 (system solid, feels generic/unloved) → Path C.**

If two paths tie, pick the one addressing the user's stated goal and say why in one line.

### Path A — Build from scratch (Level 1)
1. `design-foundation` → produces the **tokens file** (colors, type, spacing, radii, shadows) every later step consumes
2. `layout-system` → page shell + responsive patterns built on spacing tokens
3. `typography-system` → type scale wired into the tokens file
4. `color-system` → full palette + semantic/dark-mode layer replacing placeholder colors
5. `visual-hierarchy-refactoring` → key screens refactored using the finished tokens
6. `component-architecture` → reusable components encoding all of the above
7. `loading-states` → `error-handling-recovery` → states for those components
8. `interaction-physics` → motion on top of stable components
9. `performance-optimization` → `accessibility-excellence` → final audits across everything

### Path B — Formalize existing design (Level 2)
1. `design-foundation` → **extract** tokens from what exists (most-used values win); produces tokens file + migration map
2. `visual-hierarchy-refactoring` → audit worst screens against new tokens; produces before/after refactors
3. `component-architecture` → extract repeated markup into components using the tokens
4. `typography-system`, `color-system`, `layout-system` → in order of measured drift (most distinct rogue values first)
5. `accessibility-excellence` → audit the now-consistent system
6. `loading-states`, `error-handling-recovery`, `interaction-physics`, `performance-optimization` → as pain dictates

### Path C — Refine a mature system (Level 3–4)
1. `interaction-physics` → motion and feel (the usual gap at this level)
2. `visual-hierarchy-refactoring` → margin-level refinement of key screens
3. `loading-states` + `error-handling-recovery` → upgrade functional states to designed states
4. `performance-optimization` → perceived-speed polish
5. `typography-system` / `color-system` → only if the diagnosis found specific weaknesses

### Path D — Performance-first
1. `performance-optimization` → measure, then fix perceived latency; produces a metrics baseline
2. `loading-states` → skeletons/progress where waits remain
3. `interaction-physics` → GPU-friendly animation fixes
4. `accessibility-excellence` → verify optimizations didn't regress a11y

### Path E — Accessibility-first
1. `accessibility-excellence` → audit + baseline fixes; produces an issue list other steps consume
2. `color-system` → fix every failing contrast pair at the token level
3. `typography-system` → readable sizes, line-height, line length
4. `error-handling-recovery` + `loading-states` → accessible feedback
5. `component-architecture` → bake fixes into reusable components
6. `interaction-physics` → `prefers-reduced-motion` compliance

All paths refer to skills under `skills/frontend-design/`.

## Step 5 — Deliver the roadmap, then offer to execute

After presenting the roadmap, ask whether to start executing step 1 now. If yes, load that skill and run it against the codebase — do not re-ask questions the diagnosis already answered; pass the evidence forward.

## Required output format

```
## Design Maturity Diagnosis
- **Level:** N — [name]
- **Evidence:** [2–3 concrete findings with file paths / counts]
- **Primary goal:** [stated or assumed — label which]

## Recommended Path: [A–E] — [name]
[One-line reason this path beats the runner-up]

## Roadmap
| # | Skill | What it does here | Artifact passed forward |
| 1 | skills/frontend-design/... | [specific to THIS codebase] | [e.g. tokens file at src/styles/tokens.css] |
| ... |

## Start here
Step 1 is [skill] because [dependency reason]. Want me to run it now?
```

## Guardrails

- **Never route by questionnaire alone.** Every maturity claim needs a code citation. If there is no code yet (greenfield), say so and default to Path A.
- **One path, committed.** Present the chosen path with a one-line reason, not a menu of five.
- **Sequence by dependency, not calendar.** No week-by-week timelines; each step is gated by the artifact before it.
- **Trim aggressively.** Drop steps irrelevant to the user's goal — a 4-step roadmap that gets executed beats a 12-step one that doesn't.
- Don't invent metrics (Lighthouse scores, user counts). Only cite what you measured or the user reported.
