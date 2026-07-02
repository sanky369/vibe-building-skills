# Token Architecture — full reference

Read this when writing a complete tokens file or wiring tokens into a specific stack. The SKILL.md carries the decision rules; this file carries the full listings and stack-specific wiring.

## The three-layer hierarchy

### Layer 1 — Global tokens (raw values)

```
Colors
├── brand ramp:   brand-50 … brand-950 (11 steps)
├── neutral ramp: gray-50 … gray-950 (tinted toward brand hue)
└── status:       success #10B981 · warning #F59E0B · error #EF4444 · info #06B6D4

Typography
├── font-family-base: Inter, system-ui, sans-serif
├── font-family-mono: ui-monospace, monospace
├── font-size-base: 16px · line-height-base: 1.5
└── weights: 400, 500, 600, 700 (3–4 max)

Spacing (4px base)
└── space-0: 0 · space-1: 4px · space-2: 8px · space-3: 12px · space-4: 16px
    space-6: 24px · space-8: 32px · space-12: 48px · space-16: 64px

Shadows (elevation)
├── shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05)
├── shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.10)
└── shadow-lg: 0 20px 25px -5px rgb(0 0 0 / 0.10)

Border radius
└── radius-sm: 4px · radius-md: 6px · radius-lg: 8px · radius-xl: 12px · radius-full: 9999px

Motion
└── duration-fast: 100ms · duration-base: 200ms · duration-slow: 300ms
    ease-out: cubic-bezier(0.16, 1, 0.3, 1)

Z-index
└── z-dropdown: 10 · z-sticky: 20 · z-overlay: 30 · z-modal: 40 · z-toast: 50
```

### Layer 2 — Semantic tokens (meaning; the dark-mode flip point)

```
Background:   bg-primary {gray-50} · bg-secondary {gray-100} · bg-tertiary {gray-200}
Text:         text-primary {gray-900} · text-secondary {gray-600} · text-tertiary {gray-500}
              text-inverse {gray-50} · text-disabled {gray-400}
Border:       border-primary {gray-200} · border-secondary {gray-300} · border-focus {brand-500}
Interactive:  interactive-primary {brand-600} · interactive-hover {brand-700}
              interactive-active {brand-800} · interactive-disabled {gray-300}
State:        state-success / warning / error / info → status colors
Elevation:    elevation-1 {shadow-sm} · elevation-2 {shadow-md} · elevation-3 {shadow-lg}
Spacing:      padding-component {space-4} · padding-section {space-8} · gap-component {space-4}
```

### Layer 3 — Component tokens (only with a component library)

```
Button:  button-primary-bg {interactive-primary} · button-primary-bg-hover {interactive-hover}
         button-primary-text {text-inverse} · button-padding-x {space-4} · button-radius {radius-md}
Card:    card-bg {bg-primary} · card-border {border-primary} · card-padding {padding-component}
         card-radius {radius-lg} · card-shadow {elevation-1}
Input:   input-bg {bg-primary} · input-border {border-primary} · input-border-focus {border-focus}
         input-text {text-primary} · input-radius {radius-md}
```

## Stack wiring

### Tailwind v4 (CSS-first)

```css
@import "tailwindcss";

@theme {
  --color-brand-500: #3B82F6;
  --color-brand-600: #2563EB;
  --color-gray-50: #F8FAFC;
  /* … full ramps. These generate utilities: bg-brand-600, text-gray-50, … */
  --spacing: 0.25rem; /* 4px base drives the whole spacing scale */
  --radius-md: 0.375rem;
}

/* Semantic layer as plain custom properties (flipped by .dark) */
:root {
  --color-bg-primary: var(--color-gray-50);
  --color-text-primary: var(--color-gray-900);
}
.dark {
  --color-bg-primary: var(--color-gray-950);
  --color-text-primary: var(--color-gray-50);
}
```

### Tailwind v3 (config-first)

```javascript
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: { 50: '#EFF6FF', 500: '#3B82F6', 600: '#2563EB', 700: '#1D4ED8', 950: '#172554' },
        gray:  { 50: '#F8FAFC', 200: '#E2E8F0', 500: '#64748B', 700: '#334155', 900: '#0F172A', 950: '#020617' },
        // Semantic layer routed through CSS variables so dark mode flips without dark: prefixes:
        'bg-primary': 'var(--color-bg-primary)',
        'text-primary': 'var(--color-text-primary)',
        'interactive-primary': 'var(--color-interactive-primary)',
      },
      borderRadius: { md: '0.375rem', lg: '0.5rem' },
    },
  },
};
```

Define the `--color-*` variables in `globals.css` under `:root` and `.dark` exactly as in the v4 example.

### No Tailwind (vanilla CSS / CSS Modules / styled-components)

Put all three layers as custom properties on `:root`, semantic overrides under `.dark` (class strategy) or `@media (prefers-color-scheme: dark)` (system strategy). Class strategy is preferred when the product will ever need a manual toggle.

## Patterns

### Dark mode

- Components consume **only** semantic tokens; the flip happens in one place.
- Dark backgrounds: dark gray (`gray-950` ≈ `#020617`), never `#000000`.
- Desaturate and lighten brand colors one step in dark mode if they vibrate (`brand-500` in dark where light used `brand-600`).
- Re-verify every text/background pair in dark mode separately — contrast does not carry over.

### Component variants

```css
.button--primary   { background: var(--color-interactive-primary); color: var(--color-text-inverse); }
.button--secondary { background: var(--color-bg-secondary);        color: var(--color-text-primary); }
.button--ghost     { background: transparent;                      color: var(--color-interactive-primary); }
```

Variants differ only in which semantic tokens they bind — never in raw values.

### Responsive tokens

Prefer fluid values inside the token over per-breakpoint overrides:

```css
:root {
  --font-size-h1: clamp(1.75rem, 1.2rem + 2.5vw, 3rem);
  --padding-section: clamp(2rem, 1rem + 4vw, 6rem);
}
```

## Extraction heuristics (formalizing an existing codebase)

- Frequency wins: the most-used value in a cluster becomes the token value, unless it breaks the scale — then snap to the nearest scale step.
- A cluster = values within ~10% of each other serving the same role (15/16/17px body text → one token).
- Anything used once or twice and off-scale is a bug, not a token — map it to the nearest token in the migration map.
- Keep Tailwind's default names where the project already uses them heavily (`gray`, `space`, `text-sm`); renaming utilities across a codebase is churn without payoff.

## Governance (for the summary you hand the user)

- New raw hex/px values in components are lint-worthy; new design decisions become tokens first.
- Additions go to the global layer; meanings to the semantic layer. A PR that adds a semantic token must say which global it references and which components consume it.
