# Typography Details — fonts, scales, and patterns

Read when choosing fonts, styling long-form content, or needing the full scale tables.

## Modular scale tables (16px base)

| Ratio | Name | Character | Sequence |
|---|---|---|---|
| 1.125 | Major second | Subtle, dense UIs | 16, 18, 20, 23, 26, 29, 33, 37 |
| 1.2 | Minor third | Compact but distinct | 16, 19, 23, 28, 33, 40, 48 |
| 1.25 | Major third | Balanced (default) | 16, 20, 25, 31, 39, 49, 61 |
| 1.333 | Perfect fourth | Assertive marketing | 16, 21, 28, 38, 51, 67 |
| 1.414 | Augmented fourth | Dramatic | 16, 23, 32, 45, 64 |
| 1.5 | Perfect fifth | Bold, few levels | 16, 24, 36, 54, 81 |
| 1.618 | Golden ratio | Editorial heroes | 16, 26, 42, 68, 110 |

Snap computed values to whole pixels (or clean rem quarters). Add 12/14px below base for captions and labels regardless of ratio.

## Font pairing by personality

| Heading | Body | Personality | Typical use |
|---|---|---|---|
| Playfair Display | Inter | Elegant, sophisticated | Luxury, editorial |
| Montserrat | Open Sans | Modern, geometric | Tech, SaaS |
| Merriweather | Lato | Warm, friendly | Publishing, lifestyle |
| Space Grotesk | Inter | Technical, contemporary | Developer tools |
| Poppins | Poppins | Rounded, approachable | Consumer apps |
| Fraunces | Source Sans 3 | Characterful, warm | Brand-led products |
| (none — system stack) | system-ui stack | Neutral, fastest | Internal tools, MVPs |

Pairing rules: contrast in classification (serif + sans, or geometric + humanist), never two similar sans faces; the body font must stay readable at 14–16px with tabular-friendly numerals if the UI shows data.

System stack (zero network cost):

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
```

## Font loading

- Prefer the framework loader (`next/font`, Nuxt fontaine) — it self-hosts, subsets, and sets `font-display` correctly.
- Manual: `<link rel="preload" as="font" type="font/woff2" crossorigin>` for the 1–2 critical files, `font-display: swap` in `@font-face`.
- Variable fonts: one file covers all weights — prefer when the family offers one.

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/InterVariable.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
}
```

- Budget: ≤2 families, ≤4 static weights (or 1 variable file per family). Every extra weight is a network request and a layout-shift risk.

## OpenType features

```css
body   { font-feature-settings: 'liga' 1; }        /* ligatures */
.table, .stat, .price { font-variant-numeric: tabular-nums; }  /* aligned digits — always for data columns */
.small-caps { font-variant-caps: all-small-caps; letter-spacing: 0.05em; }
```

Tabular numbers in any column of figures is the single highest-value feature — proportional digits make tables shimmer on update.

## Long-form article pattern

```css
article {
  font-size: 1.125rem;      /* 18px for sustained reading */
  line-height: 1.7;
  max-width: 65ch;
  margin-inline: auto;
  padding: var(--space-8) var(--space-4);
}
article h1 { font-size: var(--text-4xl); line-height: 1.1; margin-block: 2rem 1rem; letter-spacing: -0.02em; }
article h2 { font-size: var(--text-3xl); line-height: 1.2; margin-block: 1.5rem 0.75rem; }
article p  { margin-bottom: 1.5em; }
article a  { color: var(--color-interactive-primary); text-decoration: underline; text-underline-offset: 2px; }
```

Heading margins: more space above than below (2:1) — headings belong to the content that follows (proximity).

## UI text pattern

```css
button      { font-size: var(--text-base); font-weight: 600; line-height: 1.5; }
label       { font-size: var(--text-sm); font-weight: 500; line-height: 1.4; }
.caption    { font-size: var(--text-xs); color: var(--color-text-secondary); line-height: 1.4; }
.overline   { font-size: var(--text-xs); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; }
```

## Fluid type formula

For a size that should be `min`px at 320px viewport and `max`px at 1280px:

```
slope = (max − min) / (1280 − 320)
preferred = (min − slope × 320) px + (slope × 100) vw
font-size: clamp(minPx, preferred, maxPx);
```

Example 31→39px: `clamp(1.9375rem, 1.77rem + 0.83vw, 2.4375rem)`. Only headings ≥ ~24px need fluidity; body stays fixed.

## Emphasis rules

- **Bold (600/700)** for inline emphasis and headings — never whole paragraphs.
- *Italic* for citations and asides; avoid in UI chrome (renders poorly at small sizes in some faces).
- ALL CAPS only for short labels/overlines, always with `letter-spacing: 0.05em`.
- Underline reserved for links.
- Color as emphasis only on interactive elements; hierarchy comes from size/weight/lightness first (see `skills/frontend-design/visual-hierarchy-refactoring`).
