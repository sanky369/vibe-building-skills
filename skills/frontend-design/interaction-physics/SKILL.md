---
name: interaction-physics
description: "Design and implement the motion layer of a UI — microinteractions, transitions, hover/press feedback, and animation timing/easing — as working CSS/JS plus a written animation spec. Use when the user says 'the app feels janky', 'animations feel off', 'make it feel smoother/snappier', 'add a transition', 'the modal just pops in', 'buttons feel dead', 'add some polish/delight', or when interactions give no feedback. Also use to audit existing animations for timing, easing, performance (GPU properties), and reduced-motion support. Produces an animation spec (duration/easing per interaction class) and the implemented transitions."
---

# Interaction Physics

Give every user action a physical response: consistent durations, meaningful easing, and feedback that arrives instantly. **The prime directive: every animation must do a job — confirm an action, guide attention, or explain a state change. Motion that does none of these gets deleted, not tuned.** Deliver two artifacts together: a project-wide animation spec (so future motion stays consistent) and the implemented code for the interactions in scope.

## When to use / when not to

Use for: hover/press/focus feedback, enter/exit transitions (modals, toasts, pages, list items), form feedback animation, animation audits, choosing durations and easings, `prefers-reduced-motion` support.

Hand off instead when the real need is:
- Which loading indicator to show and when → `skills/frontend-design/loading-states` (this skill animates it; that skill chooses it)
- Optimistic UI, perceived latency, Core Web Vitals → `skills/frontend-design/performance-optimization`
- Rendering pipeline, layout thrashing, frame budgets → `skills/frontend-design/design-engineer-mindset`
- Non-motion visual polish (spacing, contrast, hierarchy) → `skills/frontend-design/visual-hierarchy-refactoring`

## Step 0 — Inspect the codebase, then ask only what's left

1. Grep for existing motion: `transition`, `animation`, `@keyframes`, `framer-motion`, `motion.`, `react-spring`, `gsap`, Tailwind `transition-*`/`animate-*` classes. Record every duration and easing in use — inconsistency here (e.g. 150ms, 200ms, 250ms, 300ms all for hovers) is usually the first finding.
2. Check for `prefers-reduced-motion` handling anywhere. Absence is an automatic fix item.
3. Identify the animation vehicle: if the project already uses a motion library, implement with it; otherwise default to CSS transitions/keyframes. Never add a motion library for effects CSS can do.
4. Find dead interactions: buttons without hover/active states, modals/toasts that appear with no transition, form errors that pop in.

Ask the user (one batch, only if not inferable): **desired personality** (calm/professional vs playful — infer from the product's domain if obvious) and **scope** (whole app pass vs specific flows). If the user said "the app feels janky", don't interrogate — audit, state assumptions, and proceed.

## Workflow

### 1. Write the animation spec first

Fix the vocabulary before touching code. Standard duration classes:

| Class | Duration | Easing | Applies to |
|---|---|---|---|
| Micro feedback | 150–250ms | `ease-out` | hover, press, focus, toggle, color/state change |
| Structural transition | 300–500ms | `ease-out` in, `ease-in` out | modal, drawer, page, accordion, toast |
| Attention | 500–1000ms | `ease-in-out` | alerts, pulses, one-shot emphasis |
| Continuous | ~1s loop | `linear` | spinners, indeterminate progress |

Decision rules:
- **Easing by direction:** entering elements decelerate (`ease-out`); exiting elements accelerate (`ease-in`); on-screen moves use `ease-in-out`; only mechanical loops use `linear`. Bouncy curves like `cubic-bezier(0.34, 1.56, 0.64, 1)` are reserved for deliberate playfulness — at most one or two places in an app.
- **Duration by size and distance:** small elements moving short distances sit at the bottom of the range (hover tint: 150–200ms); large surfaces or long travel at the top (full-screen drawer: 400–500ms). A tooltip and a modal must not share a duration.
- **Exits faster than entrances** (~75% of the enter duration) — users have already decided to leave.
- Collapse whatever inconsistent values you found in Step 0 into at most 3–4 named tokens (e.g. `--duration-fast: 200ms; --duration-base: 300ms; --duration-slow: 450ms`), defined as CSS variables or theme tokens.

### 2. Specify each microinteraction with the four-part anatomy

For every interaction in scope, state: **Trigger** (user action / system event) → **Rules** (what changes, duration, easing) → **Feedback** (what the user perceives) → **Loops & modes** (does it repeat, can it be interrupted). Interruptibility rule: state-driven transitions (CSS `transition` or a motion library) beat fire-and-forget keyframes for anything a user can toggle rapidly — a half-open menu must reverse smoothly, not restart.

### 3. Implement under the performance and accessibility constraints

- **Animate only `transform` and `opacity`** (compositor-friendly). Never animate `width`, `height`, `top`, `left`, or `box-shadow` directly; fake shadow animation by crossfading a pseudo-element's opacity. Animating `background-color` is acceptable for small controls only.
- **Ship the reduced-motion block in the same change** — see the baseline in `references/patterns.md`. Decorative motion disappears; informational motion (progress) may remain as opacity-only.
- **Feedback never rides on motion alone:** pair every animated state change with a color/text/icon change so it survives reduced-motion.
- **Keyboard parity:** every `:hover` effect gets a `:focus-visible` equivalent.
- No flashing faster than 3 times per second, ever (seizure risk — this is a WCAG requirement, not a style preference).

Canonical micro-feedback example (full gallery — buttons, form validation, toasts, modals, page transitions — in `references/patterns.md`):

```css
button {
  transition: background-color 200ms ease-out, transform 200ms ease-out;
}
button:hover:not(:disabled)  { background-color: var(--color-primary-dark); }
button:active:not(:disabled) { transform: scale(0.98); }
button:focus-visible         { outline: 2px solid var(--color-focus); outline-offset: 2px; }
```

### 4. Verify

Run the app if possible (or reason through the render path): confirm transitions fire, exits animate (a common miss — elements unmount before the exit animation), rapid toggling doesn't stutter or restart, and the reduced-motion media query actually suppresses movement.

## Required output format

Deliver both artifacts:

**1. The code** — implemented transitions/animations, using the project's existing motion vehicle and tokens.

**2. Animation Spec** (markdown, becomes the project's motion reference):

```
## Motion tokens
| Token | Value | Easing | Used for |
| --duration-fast | 200ms | ease-out | hover, press, focus, toggles |
| --duration-base | 300ms | ease-out/ease-in | toasts, dropdowns, accordions |
| --duration-slow | 450ms | ease-out/ease-in | modals, drawers, page transitions |

## Interaction inventory
| Interaction | Trigger | Motion | Duration/easing | Status |
| Button hover | pointer/focus | bg tint + scale on press | fast / ease-out | implemented |
| Modal open | click | fade + 20px rise | slow / ease-out | implemented |
| Toast exit | timeout/dismiss | slide right + fade | base×0.75 / ease-in | implemented |

## Audit findings (for audit engagements)
| Issue | Location | Fix |
| 5 different hover durations | [files] | collapsed to --duration-fast |
| No reduced-motion support | global | baseline block added |

## Deliberately not animated
[List, with one-line reasons — restraint is part of the spec]
```

## Quality bar (check before delivering)

- [ ] Every animation in delivered code maps to a purpose (confirm / guide / explain) — name it if challenged
- [ ] All durations come from the spec's tokens; no magic numbers left in touched files
- [ ] Enter = ease-out, exit = ease-in, loops = linear — no exceptions without a stated reason
- [ ] Only `transform`/`opacity` animated (small-control color changes excepted)
- [ ] `prefers-reduced-motion` block present and effective
- [ ] Every `:hover` state has a `:focus-visible` twin
- [ ] Animated state changes also change color/text/icon (motion is not the only signal)
- [ ] Nothing flashes > 3×/second; no infinite decorative loops

Hard don'ts: no scroll-hijacking; no animation on keystroke in text inputs; no adding a motion library when CSS suffices; no animating layout properties.

## Integration

- `skills/frontend-design/component-architecture` → provides the component states (hover/active/loading/disabled) this skill animates; add tokens there if a token system exists.
- `skills/frontend-design/loading-states` → decides *which* indicator appears; this skill supplies its shimmer/spin/progress motion.
- `skills/frontend-design/performance-optimization` ← consumes the spec's constraint that only compositor properties animate; hands back findings if animations still drop frames.
- `skills/frontend-design/accessibility-excellence` ← audits reduced-motion and flash-rate compliance of what you ship.

## References

- `references/patterns.md` — full implementation gallery: complete button state set, form validation, skeleton/spinner/progress motion, toast enter/exit, page and modal transitions, the reduced-motion baseline block. Read it when writing the actual CSS.
