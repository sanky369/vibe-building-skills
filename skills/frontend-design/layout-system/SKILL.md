---
name: layout-system
description: "Fix or build responsive layout: page shells, grids, card layouts, sidebars, breakpoint strategy, container queries. Use when the user says 'this breaks on mobile', 'the layout is messy', 'things don't line up', 'our spacing is inconsistent between sections', 'make this responsive', 'center this properly', or asks for a dashboard/page/grid layout. Inspects existing CSS for layout smells (fixed widths, absolute positioning, media-query sprawl), then produces working layout code — refactored CSS/JSX with Grid/Flexbox decision rules applied, breakpoints derived from content, and a responsive verification checklist. Hands off pure spacing-token questions to design-foundation and text-readability questions to typography-system."
---

# Layout System

Produce working, mobile-first layout code for the user's actual screens — a refactored page shell, grid, or component layout — not a CSS tutorial. Governing principle: **content determines structure**. Choose Grid vs Flexbox by the shape of the content, place breakpoints where the content breaks, and let flexible tracks absorb the rest.

## When to use / handoffs

- Use for page structure, alignment, responsiveness, grids, overlap/overflow bugs, and breakpoint strategy.
- Spacing values themselves inconsistent across the app (no scale) → establish tokens first via `skills/frontend-design/design-foundation`.
- Text hard to read at some widths (line length, fluid type) → `skills/frontend-design/typography-system`.
- Layout is fine but the screen feels cluttered → `skills/frontend-design/visual-hierarchy-refactoring`.

## Step 1 — Inspect the codebase

1. **Locate the target.** If the user named a screen/component, read it plus its CSS. Otherwise glob the main layout files (`**/layout.*`, `**/App.*`, `**/*page*`, global CSS).
2. **Detect the styling system.** Tailwind classes vs CSS Modules vs styled-components — deliver in the same system.
3. **Grep for layout smells** and record counts:
   - `width:\s*\d+px|w-\[\d+px\]` — fixed widths (breakage source #1)
   - `position:\s*absolute` outside overlays/badges — layout by coordinates
   - `float:|margin-top:\s*-|margin-left:\s*-` — legacy/negative-margin hacks
   - `@media` — count distinct breakpoint values; >4 distinct min-widths = breakpoint sprawl
   - `overflow-x` and `100vw` — horizontal-scroll suspects
4. **Read existing breakpoints** (Tailwind `screens`, or media queries) — reuse them unless they're the problem.
5. **Check for spacing tokens** — if a scale exists, all new gaps/padding must use it.

## Step 2 — Intake

Ask in one batch, only if not inferable: **which screen/flow matters most**, and **the smallest and largest viewports that matter** (default: 320px–1440px, content capped ~1200–1280px). Infer density and stack from the code. **Don't stall** — with a named target and visible code, state assumptions and build.

## Step 3 — Build mobile-first, with these decision rules

1. **Start at 320px, single column, then add columns only where content earns them.** Never shrink a desktop design downward.
2. **Grid vs Flexbox:**
   - Rows AND columns must align (page shell, dashboard, gallery, form with aligned labels) → **Grid**.
   - One direction, sizes driven by content (navbar, button row, tag list, media-object) → **Flexbox**.
   - Card grid with unknown item count → Grid with `repeat(auto-fit, minmax(min(100%, 280px), 1fr))` — zero media queries.
   - If you're using Flexbox with percentage-width children to fake columns, switch to Grid.
3. **Page shell:** Grid with `grid-template-areas`; collapse areas at smaller widths. Canonical:

```css
.shell { display: grid; gap: var(--space-4); grid-template-areas: "header" "main" "footer"; }
@media (min-width: 768px) {
  .shell {
    grid-template-columns: 250px minmax(0, 1fr);
    grid-template-areas: "header header" "sidebar main" "footer footer";
  }
  .sidebar { position: sticky; top: 0; height: fit-content; }
}
```

   (`minmax(0, 1fr)` — not bare `1fr` — so wide children can't blow out the track.)
4. **Breakpoints from content:** resize until something breaks (line too long, column too squeezed, orphaned whitespace) and put the breakpoint there. Keep to 2–3 per component. Use the project's existing breakpoint tokens.
5. **Container queries** when a component renders in containers of different widths (card in sidebar AND main): `container-type: inline-size` on the wrapper, `@container (min-width: …)` on the component. Viewport media queries only for page-level structure.
6. **Media proportions:** `aspect-ratio` + `object-fit: cover`; never fixed height on responsive images.
7. **Units:** `rem` for space/type, `%`/`fr`/`minmax()` for tracks, `ch` for text measure, px only for borders and true pixel concerns.

For the full pattern gallery (hero, card grid, sidebar, responsive nav, holy-grail, sticky footer, container-query card), read `references/layout-patterns.md` and adapt rather than reinventing.

## Step 4 — Verify at the checkpoints

Test (or reason through, if you can't render) at 320, 375, 768, 1024, 1440. Look for: horizontal scroll, squeezed columns (<~250px of real content), text measure outside 45–75ch, touch targets <44px, content trapped under sticky elements.

## Required output format

Deliver code plus this summary:

```
## Layout changes
[Refactored files with full code — same styling system as the project]

## Decisions
| Question | Choice | Rule applied |
| Shell | Grid, template-areas | 2-D alignment needed |
| Card list | auto-fit minmax(280px, 1fr) | unknown item count → no media queries |
| Breakpoints | 768px, 1024px (existing tokens) | content broke at sidebar collapse |
| Container queries | card only | renders in 2 container widths |

## Smells removed
| Smell | Where | Replaced by |
| fixed width 960px | Header.tsx | max-width + margin-inline auto |
| ... |

## Verified
320 / 375 / 768 / 1024 / 1440 — [result per width, or "reasoned, not rendered" flagged]
```

## Quality bar (check before delivering)

- [ ] No horizontal scrollbar at 320px
- [ ] Zero fixed pixel widths on containers (max-width caps allowed)
- [ ] Grid for 2-D, Flexbox for 1-D — no percentage-width flex-column fakery
- [ ] Body text measure 45–75ch at every breakpoint
- [ ] Touch targets ≥ 44×44px on mobile
- [ ] All gaps/padding use the project's spacing scale (no new magic numbers)
- [ ] ≤3 breakpoints per component, all from the project's breakpoint set
- [ ] Visual reordering (Grid placement, `order`) doesn't scramble DOM/tab order
- [ ] `aspect-ratio` on media; no fixed-height image boxes

## Integration

- Consumes: spacing scale + breakpoint tokens from `skills/frontend-design/design-foundation`.
- Produces: the page shell and layout patterns that `skills/frontend-design/typography-system` (measure, fluid type) and `skills/frontend-design/visual-hierarchy-refactoring` (whitespace, grouping) refine, and that `skills/frontend-design/component-architecture` encodes as reusable layout components.
- Accessibility of the result is audited by `skills/frontend-design/accessibility-excellence`.

## References

- `references/layout-patterns.md` — copy-adaptable patterns: hero, card grid, sidebar+main, responsive nav, holy grail, sticky footer, container-query card, aspect-ratio media, plus the breakpoint table. Read when building any standard pattern.
