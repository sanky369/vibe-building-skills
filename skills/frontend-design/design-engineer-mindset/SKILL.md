---
name: design-engineer-mindset
description: "Translate a design (Figma mockup, spec, screenshot, or verbal description) into code with pixel- and motion-level fidelity, using the browser's rendering pipeline as a constraint: exact spacing/timing via tokens, GPU-safe animations, no layout thrashing, 60fps interactions. Use when the user says 'implement this design', 'make it match the mockup', 'it doesn't look like the Figma', 'the animation stutters/drops frames', 'set up design tokens', or when a diff between design and implementation needs to be closed. Produces the faithful implementation plus a fidelity report (design value → implemented value → any deviation and why) and performance notes."
---

# Design Engineer Mindset

Close the gap between what was designed and what ships: implement designs exactly — real values, real timing, real physics — while treating the browser's rendering pipeline as part of the design material. **The prime directive: fidelity is non-negotiable and measurable. "Approximately the mockup" is a bug; every deviation is either justified in writing or fixed.** Deliver the implementation plus a fidelity report; never eyeball-and-ship.

## When to use / when not to

Use for: design-to-code implementation, closing design/implementation drift, setting up design tokens as code, fixing stuttering animations at the rendering level (layout thrashing, non-compositor properties), frame-budget work.

Hand off instead when the real need is:
- Choosing durations/easings and motion vocabulary → `skills/frontend-design/interaction-physics` (that skill decides the spec; this one implements it faithfully and keeps it at 60fps)
- Network/perceived latency, Core Web Vitals → `skills/frontend-design/performance-optimization`
- Structuring the components you're about to build → `skills/frontend-design/component-architecture`
- Inventing the design itself (no mockup exists) → `skills/frontend-design/design-foundation` and the visual-layer skills

## Step 0 — Inspect design and codebase, then ask only what's left

1. Extract exact values from the design source: spacing, sizes, radii, colors, shadows, type styles, animation durations/easings. If it's a Figma link and Figma tooling is available, pull real values; from a screenshot, measure and mark measured values as approximations in the fidelity report.
2. Inspect the code side: existing token system (CSS variables, Tailwind theme, styled-system)? Map every design value to an existing token first; list values with no token as either new tokens or spec deviations to raise.
3. Detect the design's underlying system: are spacings multiples of 8 (or 4)? A consistent elevation scale? Duration pattern? Implementing the *system* beats transcribing pixel values.
4. Check rendering hygiene of code you'll touch: grep for animations on `width/height/top/left/margin`, interleaved DOM reads/writes in handlers, scroll handlers doing layout reads.

Ask the user (one batch, only when the design source doesn't answer): target breakpoints/responsive behavior if the mockup shows one width, and interaction behavior not visible in a static mockup (hover/press/loading states). If unanswerable, implement sensible defaults consistent with the design system and log them as assumptions — don't stall.

## Workflow

### 1. Recover intent before transcribing values

For each notable value, name its reason (touch target, grid step, elevation level, timing class). Rule: when a value contradicts the design's own system (a stray 13px in an 8-point layout), flag it to the user as a probable spec error rather than silently copying or silently correcting it. Intent table examples: `references/rendering.md`.

### 2. Implement through tokens, not literals

- Every color/spacing/size/shadow/duration in your code is a token reference; raw literals appear only when defining tokens.
- If no token layer exists and more than a handful of values recur, create one (CSS variables, or extend the Tailwind theme if that's the stack) — but keep it minimal and derived from the actual design, not a speculative system.
- Exactness rule: 44px is 44px, 300ms is 300ms, the easing curve is the specified cubic-bezier — not "close enough" approximations.

### 3. Animate within the pipeline's physics

- **Property rule:** animate `transform` and `opacity` only (composite-only). Layout properties (`width/height/top/left`) trigger layout+paint+composite — never animate them; fake shadows via pseudo-element opacity crossfade, size emphasis via `scale()`.
- **Thrashing rule:** batch DOM reads before writes; in handlers, read geometry first, schedule writes in `requestAnimationFrame`. Interleaved read/write in a loop is an automatic fix.
- **Frame budget:** 60fps = 16.7ms/frame; budget ~10ms for your JS. When an animation stutters, profile (DevTools Performance) and identify the phase — long JS task, forced reflow, or paint storm — before changing code.
- **Memoization** (`React.memo`, `useMemo`, `useCallback`) is applied where profiling shows re-render cost, not sprinkled by default.

Canonical patterns (pipeline table, thrash fix, GPU keyframes, FPS meter, token block): `references/rendering.md` — read it when implementing.

### 4. Verify fidelity and performance

- Build the fidelity report: design value → implemented value, side by side, deviation column with a reason for every mismatch. Take a screenshot comparison if the environment supports rendering.
- Exercise every specified state (hover, press, focus, loading, error, empty) — mockups usually show one; the implementation must cover all, and states you invented get flagged as assumptions.
- If the project has visual regression tooling (Percy/Chromatic/Storybook), add snapshots for the new states; if not, recommend it once in the report — don't install it uninvited.
- For animation work: confirm no layout-property animation remains, and profile or reason through the frame cost of the heaviest interaction.

## Required output format

Deliver both artifacts:

**1. The code** — the faithful implementation, token-based, using the project's existing stack and conventions.

**2. Fidelity Report** (markdown):

```
## Implementation summary
What was implemented, from which design source, into which files.

## Fidelity table
| Property | Design | Implemented | Token | Deviation & why |
| Button height | 44px | 44px | --size-control-lg | — |
| Card shadow | y4 b6 10% | same | --shadow-md | — |
| Modal duration | 300ms ease-out | 300ms cubic-bezier(0.16,1,0.3,1) | --duration-base | curve per motion spec, approved values |
| Sidebar gap | 13px (off-grid) | 12px | --spacing-sm+xs | flagged: mockup off its own 4pt grid — confirm |

## States implemented
| State | Source | Notes |
| hover/press/focus | inferred (not in mockup) | assumption — matches system patterns |
| loading | mockup frame 3 | — |

## Performance notes
- All animations on transform/opacity ✓
- [Any profiling done, frame costs, thrash fixes applied]

## Assumptions & open questions
[Responsive behavior chosen, off-grid values flagged, unverifiable measurements from screenshots]
```

## Quality bar (check before delivering)

- [ ] Every design value either matches exactly or has a written deviation reason — zero silent approximations
- [ ] No raw magic numbers in component code; all values route through tokens
- [ ] No animation touches layout properties; no interleaved read/write loops in touched code
- [ ] All interactive states implemented, with invented ones labeled as assumptions
- [ ] Off-system values in the mockup flagged, not silently propagated or corrected
- [ ] Screenshot-derived measurements marked approximate; no false precision
- [ ] Accessibility not traded for fidelity: focus visibility, contrast, and touch-target minimums (24×24 CSS px WCAG 2.2 AA; 44×44 preferred for touch) survive the implementation
- [ ] Performance claims (fps, render cost) only stated if actually measured

Hard don'ts: don't "improve" the design while implementing it — propose changes separately; don't install visual-regression or animation tooling uninvited; don't claim 60fps without profiling; don't build a speculative token architecture beyond what the design actually uses.

## Integration

- `skills/frontend-design/interaction-physics` → supplies the motion spec (durations/easings) this skill implements at full fidelity and frame rate.
- `skills/frontend-design/component-architecture` → structures what you build; implement fidelity *inside* its component boundaries and prop conventions.
- `skills/frontend-design/design-foundation` → owns the token system's design; this skill encodes and consumes it in code.
- `skills/frontend-design/performance-optimization` → takes over when slowness is network/data-shaped rather than render-shaped; hand it findings about fetch waterfalls you notice.

## References

- `references/rendering.md` — the rendering pipeline cost model, layout-thrashing fixes, GPU-safe animation patterns, frame-budget measurement code, the design-token CSS block, React memoization patterns, visual-regression and performance test examples, and the design-intent table. Read it when implementing or when debugging a stuttering interaction.
