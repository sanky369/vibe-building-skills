# Gestalt Principles & Extended Refactor Examples

Read when a grouping problem isn't solved by proximity alone, or you need worked before/after material beyond the canonical example in SKILL.md.

## The six principles, with CSS application

### 1. Proximity — close things read as related

The workhorse. Spacing *is* the grouping mechanism; borders and boxes are fallbacks.

```css
.form-group { margin-bottom: var(--space-6); }         /* between groups: far */
.form-group label { display: block; margin-bottom: var(--space-2); }  /* label ↔ input: near */
```

Rule of thumb: between-group gap ≥ 2× within-group gap. Heading margins follow the same logic — more space above than below (a heading belongs to what follows).

### 2. Similarity — same-looking things read as same-kind

- All primary buttons identical everywhere; all cards identical padding/radius/shadow.
- Conversely, difference must mean something: if two links are styled differently, users assume they behave differently.

```css
.button-primary { background: var(--color-interactive-primary); color: white; padding: var(--space-3) var(--space-6); border-radius: var(--radius-md); }
.button-primary:hover { background: var(--color-interactive-hover); }
```

### 3. Figure/Ground — foreground must separate from background

- Modals: darken the ground (`rgba(0,0,0,0.5)` overlay) + elevate the figure (shadow).
- Active vs inactive states: the active item is figure (solid bg), the rest are ground (transparent/tint).

```css
.modal-overlay { background: rgb(0 0 0 / 0.5); }
.modal { background: var(--color-bg-primary); box-shadow: var(--shadow-lg); border-radius: var(--radius-xl); }
.tab[aria-selected="true"]  { background: var(--color-bg-primary); color: var(--gray-900); box-shadow: var(--shadow-sm); }
.tab[aria-selected="false"] { background: transparent; color: var(--gray-600); }
```

### 4. Closure — the brain completes incomplete shapes

Lets you delete chrome: a list doesn't need a border if item spacing implies the container; icon sets can be stroke-only. Use to remove elements, not add them.

### 5. Symmetry & order — balance reads stable; asymmetry draws attention

- Grids for stable, trustworthy layouts.
- One deliberate asymmetry to point attention:

```css
.hero { display: grid; grid-template-columns: 1fr 1.5fr; gap: var(--space-12); align-items: center; }
```

If everything is asymmetric, nothing is emphasized — same inflation rule as bold text.

### 6. Common region — a boundary groups its contents

The strongest grouping cue, and therefore the most overused. Reach for it only when proximity is exhausted (e.g., dense dashboards where every gap is already meaningful).

```css
.card { background: var(--color-bg-primary); border: 1px solid var(--color-border-primary); border-radius: var(--radius-lg); padding: var(--space-6); }
.section-tinted { background: var(--gray-50); border-radius: var(--radius-xl); padding: var(--space-12); }
```

De-boxing move: when you find cards inside cards, delete the inner border/background and double the spacing instead.

## Extended before/after examples

### A. Dashboard stat row — emphasis inflation

Before: every stat had a colored icon, bold label, bold value, and a border. Nothing stood out.

```css
/* AFTER: value is the only loud element */
.stat        { padding: var(--space-4) 0; }              /* border removed; column gap groups */
.stat-value  { font-size: var(--text-2xl); font-weight: 700; color: var(--gray-900); font-variant-numeric: tabular-nums; }
.stat-label  { font-size: var(--text-sm); font-weight: 400; color: var(--gray-500); }
.stat-delta--up   { color: var(--green-600); }           /* color only where it carries meaning */
.stat-delta--down { color: var(--red-600); }
```

### B. Form — grouping by spacing instead of fieldset boxes

```css
/* AFTER */
.form-section        { margin-bottom: var(--space-10); }  /* section boundaries via space */
.form-section-title  { font-size: var(--text-lg); font-weight: 600; color: var(--gray-900); margin-bottom: var(--space-4); }
.form-group          { margin-bottom: var(--space-5); }
.form-group label    { font-size: var(--text-sm); font-weight: 500; color: var(--gray-700); margin-bottom: var(--space-2); }
.form-hint           { font-size: var(--text-xs); color: var(--gray-500); margin-top: var(--space-1); }
.form-actions        { margin-top: var(--space-8); display: flex; gap: var(--space-3); justify-content: flex-end; }
.form-actions .cancel { background: transparent; color: var(--gray-600); }  /* ghost: P2 */
.form-actions .submit { background: var(--color-interactive-primary); color: white; }  /* P1 */
```

### C. List row — the metadata demotion

Before: title 15px/#333, description 14px/#666, timestamp 14px/#666 — three levels, one voice.

```css
/* AFTER: three distinct voices */
.row-title { font-size: var(--text-base); font-weight: 600; color: var(--gray-900); }
.row-desc  { font-size: var(--text-sm);   font-weight: 400; color: var(--gray-600); }
.row-meta  { font-size: var(--text-xs);   font-weight: 400; color: var(--gray-500); font-variant-numeric: tabular-nums; }
```

## The tinted-grey rule (why #808080 looks wrong)

True grey has zero chroma; next to any branded surface it reads as a foreign object. Derive greys from the brand hue at 5–15% saturation (see `skills/frontend-design/color-system` for ramp construction). Same for "black": `--gray-900`/`950` (e.g. `#0F172A`) instead of `#000`, which is harsh on light backgrounds and smears on OLED in dark mode.

## Scan-test procedure

After refactoring, simulate a 5-second scan:

1. Blur test: squint or mentally downsample the screen — the surviving shapes should be the P1 element and the group boundaries.
2. First-fixation walk: name the first three things the eye hits (biggest/darkest/most isolated win). They must be P1 → P2 → P2.
3. Grey-scale test: convert mentally to greyscale — hierarchy must survive without hue. If it collapses, the design leans on color and fails color-blind users.
