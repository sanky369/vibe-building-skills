---
name: design-foundation
description: "Create or extract a design-token foundation — colors, typography, spacing, radii, shadows — as a real tokens file (CSS variables and/or Tailwind theme) plus a migration map from current hardcoded values. Use when the user says 'set up a design system', 'our styles are inconsistent', 'we have 50 shades of the same blue', 'add design tokens', 'formalize our design', 'make new features match', or when starting a new frontend that needs a foundation before building screens. Also the first step whenever other design work keeps fighting ad-hoc values. Produces the tokens file, a global→semantic token structure wired for dark mode, and a short list of the worst drift to migrate first."
---

# Design Foundation

Produce a working tokens file for this specific codebase — not a document about tokens. A token is a named design decision (`--color-text-primary`, `--space-4`); centralizing them is what makes every later design skill (layout, type, color, components) land consistently. Governing principle: **extract before you invent** — in an existing codebase, the token system should formalize the best of what's already there, so migration is renaming, not redesigning.

## When to use / handoffs

- Use to create tokens from scratch or extract them from an existing codebase.
- If the user's pain is specifically color (palette, contrast, dark mode depth) → `skills/frontend-design/color-system` after the token skeleton exists.
- If specifically type (scale, fonts, readability) → `skills/frontend-design/typography-system`.
- If they want components built on tokens → `skills/frontend-design/component-architecture` next.
- For broad "where do I start" requests → `skills/frontend-design/frontend-orchestrator`.

## Step 1 — Inspect the codebase

Before asking anything, gather evidence:

1. **Find the current styling entry points.** Glob `tailwind.config.{js,ts,cjs,mjs}`, `**/globals.css`, `**/index.css`, `**/app.css`, `**/*theme*`, `**/tokens*`. Read them.
2. **Detect the stack.** Tailwind v4 (`@import "tailwindcss"` + `@theme` in CSS) vs v3 (config file `theme` object) vs CSS Modules / styled-components / vanilla CSS. Check `package.json` for the tailwindcss version.
3. **Measure drift.** Grep source for `#[0-9a-fA-F]{3,8}\b`, `rgba?\(`, `hsla?\(` → count distinct colors. Grep for `\d+px` and Tailwind arbitrary values `\[(\d+px|#)` → count rogue spacing/size values. These counts go in your rationale.
4. **Find the de facto system.** Sort found values by frequency. The most-used font sizes, spacing steps, and colors are the candidate tokens.
5. **Check dark mode** (`dark:`, `prefers-color-scheme`) — determines whether the semantic layer must ship two modes now.

## Step 2 — Intake

Ask in one batch, only what's missing: **brand color (or "pick for me")**, **product feel** (dense data tool vs. spacious marketing/consumer), and **dark mode now or later**. Infer everything else. **Don't stall:** if the codebase already answers these (an obvious brand blue, an existing `dark:` usage), state assumptions and proceed.

## Step 3 — Build the token system

Two layers minimum, three when a component library exists:

1. **Global tokens** — raw values: a neutral ramp (50–950, tinted toward the brand hue, never pure grey), the brand ramp, semantic status colors (success/warning/error/info), a spacing scale on a 4px base (4, 8, 12, 16, 24, 32, 48, 64), font sizes, radii, shadows, z-index steps, transition durations.
2. **Semantic tokens** — meaning, referencing globals: `bg-primary/secondary`, `text-primary/secondary/tertiary/inverse`, `border-primary`, `interactive-primary/hover/active/disabled`. **This is the layer that flips for dark mode** — components only ever consume semantic tokens.
3. **Component tokens** — only if a component library exists or is planned next (`--button-primary-bg: var(--color-interactive-primary)`).

Decision rules:

- **Tailwind v4** → define tokens as CSS variables in `@theme` in the main CSS file. **Tailwind v3** → `theme.extend` in the config, with semantic layer as CSS variables referenced from the config. **No Tailwind** → plain CSS custom properties on `:root` (+ `.dark` or media-query block).
- **Extraction rule:** when existing values cluster (15px, 16px, 17px), collapse to the scale value closest to the most frequent; list every collapse in the migration map.
- **Naming:** kebab-case, category-first (`--color-text-primary`, `--space-4`, `--radius-md`). Match Tailwind's names where Tailwind is present, so utilities keep working.

### Canonical shape (CSS variables; adapt to the detected stack)

```css
:root {
  /* global */
  --gray-50: #F8FAFC;  --gray-500: #64748B;  --gray-900: #0F172A; /* full 50–950 ramp, brand-tinted */
  --brand-500: #3B82F6; --brand-600: #2563EB; /* full ramp */
  --space-1: 0.25rem; --space-2: 0.5rem; --space-4: 1rem; --space-8: 2rem;
  --radius-md: 0.375rem; --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.10);

  /* semantic — the only layer components touch */
  --color-bg-primary: var(--gray-50);
  --color-text-primary: var(--gray-900);
  --color-text-secondary: var(--gray-600);
  --color-border-primary: var(--gray-200);
  --color-interactive-primary: var(--brand-600);
  --color-interactive-hover: var(--brand-700);
}
.dark {
  --color-bg-primary: var(--gray-950);   /* dark gray, never #000 */
  --color-text-primary: var(--gray-50);
  --color-text-secondary: var(--gray-300);
  --color-border-primary: var(--gray-700);
}
```

Full three-layer taxonomy, Tailwind v3/v4 wiring, and the variant/responsive-token patterns: read `references/token-architecture.md` when building the complete file.

## Step 4 — Write the file and migrate the worst offenders

1. Write the tokens into the detected entry point (don't create a parallel system beside an existing one — extend it).
2. Migrate 1–3 of the highest-traffic files (the ones your grep showed drifting most) as a demonstration, replacing raw values with tokens.
3. Produce the migration map for the rest.

## Required output format

Deliver code plus this summary:

```
## Tokens file
[path written, e.g. src/app/globals.css or tailwind.config.ts — full contents]

## Decisions
| Decision | Choice | Why |
| Stack wiring | Tailwind v4 @theme / v3 config / CSS vars | [detected how] |
| Neutral tint | [hue] | matches brand [color] |
| Spacing base | 4px | [most existing values already multiples / default] |
| Dark mode | now via .dark class / deferred | [user answer or inference] |

## Migration map (worst drift first)
| Found in code | Count | Replace with |
| #3c82f7, #3B82F6, #3a80f0 | 23 | var(--color-interactive-primary) |
| padding: 13px / p-[13px] | 9 | var(--space-3) (12px) |
| ... |

## Migrated now
[files actually edited as demonstration]

## Next step
[Which skill consumes this — typically skills/frontend-design/typography-system or color-system]
```

## Quality bar (check before delivering)

- [ ] Every semantic text/background pairing meets WCAG AA (4.5:1 normal text, 3:1 large text) in **both** modes if dark mode shipped
- [ ] Spacing scale is a single geometric-ish progression on one base; no orphan steps
- [ ] Neutrals are brand-tinted (nonzero saturation), no `#808080` / pure `#000`
- [ ] Components/examples reference only semantic tokens, never globals directly
- [ ] Token names collide with nothing existing; Tailwind utilities still resolve
- [ ] Migration map covers every value cluster found in Step 1, each mapped to exactly one token
- [ ] No second parallel token system introduced

## Integration

- Consumes: maturity diagnosis + drift counts from `skills/frontend-design/frontend-orchestrator` (if it ran).
- Produces the tokens file consumed by: `skills/frontend-design/typography-system` (extends the type tokens), `skills/frontend-design/color-system` (extends the color ramps + dark mode), `skills/frontend-design/layout-system` (spacing + breakpoints), `skills/frontend-design/visual-hierarchy-refactoring` (refactors screens onto tokens), `skills/frontend-design/component-architecture` (component layer).

## References

- `references/token-architecture.md` — full three-layer token taxonomy with complete listings, Tailwind v3 and v4 wiring, and patterns for dark mode, component variants, and responsive tokens. Read when writing the complete tokens file or wiring an unfamiliar stack.
