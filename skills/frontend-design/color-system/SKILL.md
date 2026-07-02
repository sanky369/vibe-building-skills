---
name: color-system
description: "Build or repair a color system: full brand and neutral ramps, semantic color tokens, contrast-verified pairings, dark mode, and status colors — delivered as a tokens file (CSS variables / Tailwind theme) with every text pairing's contrast ratio computed. Use when the user says 'the colors look off', 'colors clash', 'add dark mode', 'is this accessible', 'pick a palette', 'too many blues in the codebase', 'make it match our brand', or when contrast failures are found. Extracts the de facto palette from the code first, consolidates drift into ramps, chooses harmony deliberately, and verifies WCAG AA on every shipped pair in both modes."
---

# Color System

Produce a contrast-verified color token file for this codebase — ramps, semantic layer, dark mode — with the math shown, not a color-theory lecture. Governing principle: **color is a system, not a list**: every hue ships as a full lightness ramp, components consume only semantic tokens, and no text/background pair ships without a computed contrast ratio.

## When to use / handoffs

- Use for palettes, ramps, dark mode, contrast fixes, status/interactive colors, theming.
- No token infrastructure exists → run `skills/frontend-design/design-foundation` first, or create the color slice as its start.
- "Everything is grey and flat / can't tell what's important" is usually hierarchy, not palette → `skills/frontend-design/visual-hierarchy-refactoring`.
- Full WCAG audit beyond color → `skills/frontend-design/accessibility-excellence`.

## Step 1 — Inspect the codebase

1. **Harvest the palette.** Grep for `#[0-9a-fA-F]{3,8}\b`, `rgba?\(`, `hsla?\(`, `oklch\(` across source + config. Deduplicate, count frequencies. Cluster near-identical values (ΔL < ~5) — each cluster is one intended color that drifted.
2. **Read existing tokens.** Tailwind `theme.colors` / `@theme` variables / CSS custom properties. Determine whether ramps exist or just single hexes.
3. **Identify the de facto brand color** — the most-used saturated hue.
4. **Check dark mode state**: `dark:` classes, `prefers-color-scheme`, a `.dark` block.
5. **Spot-check contrast** on the 3–5 most common text/background pairs found in code — compute the WCAG ratios; failures go straight into your rationale.

## Step 2 — Intake

Ask in one batch, only what's missing: **brand color to keep, or pick fresh** (and the personality if picking: trustworthy/energetic/premium/friendly), and **dark mode: now, later, or never**. Infer the rest. **Don't stall:** with a clear de facto brand color, keep it, state the assumption, proceed.

## Step 3 — Build the system

1. **Brand ramp.** Expand the brand color into an 11-step lightness ramp (50–950), holding hue roughly constant, adjusting chroma down at the extremes. Base usable for white text lands around step 600 for most hues.
2. **Neutral ramp — tinted, never true grey.** Desaturate the brand hue heavily (roughly 5–15% saturation) and build gray-50…950 from it. `#808080` and pure `#000` are banned; they read as foreign next to any brand color.
3. **Accent/secondary (only if the product needs one).** Choose by harmony rule: analogous (±30–60°) for cohesive/calm products; complementary (~180°) for a high-energy CTA accent used sparingly; triadic when the UI must color-code ≥3 categories. Don't add hues without a job.
4. **Status colors.** Success ≈ green, warning ≈ amber, error ≈ red, info ≈ cyan/blue — nudged toward the brand's temperature, each with at least a 100/600/700 mini-ramp (background tint, base, text-on-tint).
5. **Semantic layer.** `bg-primary/secondary/tertiary`, `text-primary/secondary/tertiary/disabled/inverse`, `border-primary/focus`, `interactive-primary/hover/active/disabled` — mapped from the ramps. Components never touch ramp values directly.
6. **Dark mode (if in scope).** Remap semantic tokens only: backgrounds to gray-900/950 (never `#000`), text to gray-50/300, brand shifted one step lighter (light mode's 600 → dark's 500) and slightly desaturated if it vibrates. Re-verify every pair — light-mode ratios don't transfer.
7. **Verify contrast on every shipped pairing.** Compute WCAG relative-luminance ratios: ≥4.5:1 normal text, ≥3:1 large text (≥24px, or ≥18.7px bold) and UI components/focus rings. That's the pass/fail gate. Where a pair passes WCAG but looks weak (light text on saturated mid-tone), treat APCA (Lc ≈ 60+ for body) as an advisory tiebreaker and darken a step.
8. **Color-blind safety.** Status colors must not be the only signal — pair with icon/label (red/green alone fails ~8% of male users). Avoid red-vs-green as the sole category distinction; blue/orange is the safest contrast pair.

### Canonical shape (CSS variables; adapt to detected stack)

```css
:root {
  --brand-600: #2563EB;  --brand-700: #1D4ED8;   /* full 50–950 ramp in the real file */
  --gray-600: #475569;   --gray-900: #0F172A;    /* brand-tinted neutrals, full ramp */
  --red-600: #DC2626;    --red-100: #FEE2E2;     /* status mini-ramps: green/amber/red/cyan */

  --color-bg-primary: #FFFFFF;
  --color-text-primary: var(--gray-900);      /* on bg-primary: 17.8:1 ✓ */
  --color-text-secondary: var(--gray-600);    /* on bg-primary: 7.6:1 ✓ */
  --color-interactive-primary: var(--brand-600); /* white on it: 5.2:1 ✓ */
}
.dark {
  --color-bg-primary: var(--gray-950);
  --color-text-primary: var(--gray-50);
  --color-interactive-primary: var(--brand-500);
}
```

Harmony theory, color psychology, ramp-construction technique, and color-blind palettes: `references/color-theory.md`.

## Step 4 — Wire in and migrate

Write tokens into the detected entry point (extend, don't fork). Migrate the top drift clusters from Step 1 in 1–3 high-traffic files; map the rest.

## Required output format

Deliver code plus this summary:

```
## Color tokens
[file path + full code]

## Palette decisions
- Brand: [hex] — [kept from code / chosen for [personality]]
- Neutrals: tinted toward [hue]
- Harmony: [mono/analogous/complementary/triadic] because [job it does]
- Dark mode: [shipped/deferred] — strategy: [.dark class / media query]

## Contrast verification
| Pair | Ratio | Standard | Pass |
| text-primary on bg-primary (light) | 17.8:1 | 4.5:1 | ✓ |
| white on interactive-primary | 5.2:1 | 4.5:1 | ✓ |
| text-secondary on bg-primary (dark) | ... | ... | ... |
[every shipped text and UI pairing, both modes]

## Migration map
| Found (cluster) | Count | Replace with |
| #3B82F6 / #3b82f7 / #3a80f0 | 23 | var(--color-interactive-primary) |
| ... |

## Migrated now
[files edited]
```

## Quality bar (check before delivering)

- [ ] Every text/background pair shipped has a computed ratio in the table; all ≥4.5:1 (normal) / ≥3:1 (large + UI), **both modes**
- [ ] Neutrals brand-tinted; no `#808080`, no pure `#000` backgrounds
- [ ] Every hue exists as a ramp, not a lone hex; each hue has a stated job
- [ ] Components/examples reference only semantic tokens
- [ ] Status meaning never carried by color alone (icon/label paired)
- [ ] Dark mode: backgrounds are dark grey, brand lightened a step, all pairs re-verified
- [ ] Focus indicator color ≥3:1 against adjacent colors
- [ ] Migration map covers every drift cluster found in Step 1

## Integration

- Consumes: token skeleton from `skills/frontend-design/design-foundation`; text sizes (for the large-text contrast threshold) from `skills/frontend-design/typography-system`.
- Produces: color tokens consumed by `skills/frontend-design/visual-hierarchy-refactoring` (lightness-based contrast hierarchy), `skills/frontend-design/component-architecture` (component color bindings), and audited by `skills/frontend-design/accessibility-excellence`.

## References

- `references/color-theory.md` — harmony techniques with examples, color psychology by hue, how to construct a ramp by hand, color-blind-safe palettes, and dark-mode pitfalls in depth. Read when picking a palette from scratch or debugging a ramp that looks wrong.
