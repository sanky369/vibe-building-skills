---
name: typography-system
description: "Build or repair a typography system: a modular type scale, font choices and loading, hierarchy, line-height/line-length, and fluid sizing — delivered as tokens (Tailwind fontSize config or CSS variables) applied to real components. Use when the user says 'the text looks off', 'fonts are inconsistent', 'headings don't stand out', 'pick fonts for me', 'it's hard to read', 'too many font sizes', or when an audit finds font-size sprawl. Chooses the scale ratio from product density (dense app vs marketing vs editorial), verifies contrast and measure, and produces the type tokens plus a migration map from existing rogue sizes."
---

# Typography System

Produce a working type scale for this codebase — tokens wired into the existing styling system and applied to real headings/body/UI text — not an essay about type. Governing principle: **sizes come from a modular scale chosen for the product's density; readability constraints (line-height, measure, contrast) are non-negotiable and override aesthetics.**

## When to use / handoffs

- Use for type scales, font selection/loading, heading hierarchy, readability fixes, fluid type.
- No token infrastructure at all yet → run `skills/frontend-design/design-foundation` first (or create the type tokens as its first slice).
- Text colors failing contrast is shared ground with `skills/frontend-design/color-system` — fix the pairs you touch here; send palette-wide work there.
- Headings sized right but the page still scans poorly → `skills/frontend-design/visual-hierarchy-refactoring`.

## Step 1 — Inspect the codebase

1. **Count font sizes.** Grep for `font-size:\s*[\d.]+(px|rem)`, Tailwind `text-(xs|sm|base|lg|xl|\dxl)` and arbitrary `text-\[`. Distinct count >8–10 = sprawl; record the list with frequencies.
2. **Find the fonts.** Grep for `font-family|@font-face|fonts.googleapis|next/font` and check `tailwind.config.*` / `@theme` for `fontFamily`. Count families and loaded weights.
3. **Check line-height and measure.** Grep `line-height|leading-` and `max-width.*ch|max-w-prose`.
4. **Check existing tokens.** If `design-foundation` ran, extend its file; never start a parallel system.
5. **Classify the product's density** from the screens themselves: data tables/dashboards/many controls = dense; landing/marketing = spacious; long-form reading = editorial.

## Step 2 — Intake

Ask in one batch, only what's missing: **brand feel in a few words** (or "pick for me"), and **keep current fonts or open to change?** Infer density from the code, base size 16px unless dense-data (then 14px body is acceptable). **Don't stall** — with visible screens, state assumptions and build.

## Step 3 — Build the scale

**Choose the ratio by product density** (the core decision rule):

| Product | Ratio | Why |
|---|---|---|
| Dense data app, dashboards, admin | 1.125–1.2 (major second) | Many levels must fit without giant headings |
| Standard product UI / SaaS | 1.25 (major third) | Balanced; the default when unsure |
| Marketing site, landing pages | 1.25–1.333 | Headlines need presence |
| Editorial / brand-heavy, big heroes | 1.414–1.618 | Few levels, dramatic jumps |

Generate from base × ratio^n, then **snap to sensible pixels** (a 1.25 scale from 16px → 16, 20, 25, 31, 39, 49, 61; round as needed). Add `xs`(12) and `sm`(14) below base for captions/labels. Cap the scale at the largest size actually used — don't ship a 76px display token to a settings app.

**Pair line-height inversely with size:** body 1.5–1.7, subheads 1.3, large headings 1.1–1.2, captions/labels 1.4. Ship line-height inside the size token (Tailwind fontSize tuples do this natively).

**Fluid headings:** for sizes ≥ ~31px, use `clamp(min, preferred vw formula, max)` instead of per-breakpoint overrides. Body text stays fixed (16px) — never fluid below the base.

**Fonts:** limit to ≤2 families, 3–4 weights (400/500/600/700 subset). If choosing: pick a workhorse UI sans (variable font if available) for body, optionally one display font for headings that matches the stated feel. Load via the framework's optimizer (`next/font` etc.) or `preload` + `font-display: swap`. Pairing table and font-feature details: `references/type-details.md`.

### Canonical shape (Tailwind v3; adapt to detected stack)

```javascript
fontSize: {
  xs:   ['0.75rem',  { lineHeight: '1.4' }],           // 12 — captions, labels
  sm:   ['0.875rem', { lineHeight: '1.5' }],           // 14 — secondary UI text
  base: ['1rem',     { lineHeight: '1.6' }],           // 16 — body
  lg:   ['1.125rem', { lineHeight: '1.6' }],           // 18 — lead paragraphs
  xl:   ['1.25rem',  { lineHeight: '1.3', fontWeight: '600' }],  // 20 — h4/h5
  '2xl': ['1.5625rem', { lineHeight: '1.3', fontWeight: '600' }], // 25 — h3
  '3xl': ['clamp(1.6rem, 1.2rem + 1.6vw, 1.9375rem)', { lineHeight: '1.2', fontWeight: '700' }], // h2
  '4xl': ['clamp(1.9rem, 1.3rem + 2.4vw, 2.4375rem)', { lineHeight: '1.1', fontWeight: '700' }], // h1
}
```

## Step 4 — Apply and migrate

1. Write the tokens into the project's system (Tailwind config / `@theme` / CSS variables).
2. Apply to the base elements or shared components (headings, `p`, labels, buttons) — not one-off classes per page.
3. Constrain prose: `max-width: 65ch` on long-form containers.
4. Migrate the top rogue sizes from Step 1 in 1–3 high-traffic files; map the rest.

## Required output format

Deliver code plus this summary:

```
## Type tokens
[file path + full code in the project's system]

## Scale decision
- Density: [dense/standard/marketing/editorial] — evidence: [what you saw]
- Ratio: [x] · Base: [16px] · Levels: [list, snapped px values]
- Fonts: [family/weights] — [kept existing / chosen because …] · Loading: [mechanism]

## Migration map
| Found | Count | Replace with |
| text-[15px], 15px | 12 | text-sm (14px) |
| ... |

## Applied now
[components/files actually restyled]

## Verify
[Contrast pairs checked with ratios; measure per breakpoint]
```

## Quality bar (check before delivering)

- [ ] ≤8–10 total sizes, all on the scale; every migrated value maps to exactly one token
- [ ] Body ≥16px (≥14px only in dense data UI, and never for long-form)
- [ ] Line-height: body 1.5–1.7, headings 1.1–1.3, nothing below 1.1
- [ ] Measure 45–75ch for body text at every breakpoint
- [ ] Text/background contrast ≥4.5:1 normal, ≥3:1 large (≥24px, or ≥18.7px bold) — state the ratios you computed
- [ ] ≤2 font families, ≤4 weights actually loaded; `font-display: swap` or framework equivalent
- [ ] Heading levels distinguishable at a glance (adjacent levels differ by ratio step AND/OR weight)
- [ ] Fluid `clamp()` on large headings only; body size fixed
- [ ] Letter-spacing: slightly negative on ≥39px headings (−0.01 to −0.02em), slightly positive on all-caps labels (+0.05em)

## Integration

- Consumes: tokens file from `skills/frontend-design/design-foundation` (extends its typography slice); layout containers from `skills/frontend-design/layout-system` (measure lives there).
- Produces: type tokens consumed by `skills/frontend-design/visual-hierarchy-refactoring` (size/weight hierarchy) and `skills/frontend-design/component-architecture` (component text styles).
- Contrast pairs feed `skills/frontend-design/color-system` and are audited by `skills/frontend-design/accessibility-excellence`.

## References

- `references/type-details.md` — font pairing table by personality, variable fonts, OpenType features (tabular numbers, small caps), full article/UI typography patterns, and the complete ratio → scale tables. Read when choosing fonts or styling long-form content.
