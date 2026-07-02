# Layout Patterns — copy-adaptable gallery

Adapt these to the project's styling system (Tailwind, CSS Modules, etc.) and spacing tokens. All are mobile-first.

## Breakpoint reference

| Token | Min-width | Context | What becomes possible |
|---|---|---|---|
| xs | 320px | Small mobile | Single column baseline |
| sm | 640px | Large mobile | Side-by-side small elements |
| md | 768px | Tablet | Two columns, visible sidebar |
| lg | 1024px | Small desktop | Three columns |
| xl | 1280px | Desktop | Full layout, capped content width |
| 2xl | 1536px | Wide | More whitespace, not more columns |

Use the project's existing tokens; these are defaults for greenfield only.

## 1. Card grid (no media queries)

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: var(--space-6);
}
```

`min(100%, 280px)` prevents overflow below 280px viewports. Use `auto-fill` instead of `auto-fit` if you want empty tracks to hold their space (e.g., form grids).

## 2. Hero (stack → two columns)

```css
.hero {
  display: grid;
  gap: var(--space-8);
  padding: var(--space-8) var(--space-4);
}
@media (min-width: 768px) {
  .hero {
    grid-template-columns: 1fr 1fr;   /* or 1fr 1.2fr for intentional asymmetry */
    align-items: center;
    gap: var(--space-12);
    padding: var(--space-16) var(--space-8);
  }
}
```

## 3. Sidebar + main (page shell)

```css
.shell {
  display: grid;
  gap: var(--space-4);
  grid-template-areas: "header" "main" "footer";
}
@media (min-width: 768px) {
  .shell {
    grid-template-columns: 250px minmax(0, 1fr);
    grid-template-areas:
      "header header"
      "sidebar main"
      "footer footer";
  }
  .sidebar { grid-area: sidebar; position: sticky; top: 0; height: fit-content; }
}
@media (min-width: 1280px) {
  .shell {
    grid-template-columns: 250px minmax(0, 1fr) 300px;
    grid-template-areas:
      "header header header"
      "sidebar main aside"
      "footer footer footer";
  }
}
```

Always `minmax(0, 1fr)` for the content track — bare `1fr` lets wide children (tables, code blocks, long URLs) blow the layout open.

## 4. Responsive navigation

```css
.nav { display: flex; flex-direction: column; gap: var(--space-4); }
@media (min-width: 768px) {
  .nav {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
}
```

On mobile, pair with a disclosure button (`aria-expanded`, `aria-controls`); don't hide navigation behind hover.

## 5. Container-query card

```css
.card-slot { container-type: inline-size; }

.card { display: grid; gap: var(--space-4); }           /* stacked by default */
@container (min-width: 400px) {
  .card { grid-template-columns: 160px 1fr; }            /* image beside text */
}
```

The card adapts wherever it's placed — sidebar, main column, modal — without knowing the viewport.

## 6. Content column (prose)

```css
.prose {
  max-width: 65ch;
  margin-inline: auto;
  padding-inline: var(--space-4);
}
```

## 7. Aspect-ratio media

```css
.media-16x9 { aspect-ratio: 16 / 9; width: 100%; object-fit: cover; }
.media-square { aspect-ratio: 1; width: 100%; object-fit: cover; }
.media-4x3 { aspect-ratio: 4 / 3; width: 100%; object-fit: cover; }
```

## 8. Sticky footer (short pages)

```css
body { min-height: 100dvh; display: grid; grid-template-rows: auto 1fr auto; }
```

## 9. Section rhythm (whitespace scale by viewport)

```css
.section { padding-block: clamp(2rem, 1rem + 4vw, 6rem); }
```

One fluid declaration replaces three media queries.

## 10. Centering

```css
/* Both axes, one child */
.center { display: grid; place-items: center; }

/* A content column */
.container { max-width: 1200px; margin-inline: auto; padding-inline: var(--space-4); }
```

## Accessibility notes for layouts

- Touch targets: minimum 44×44px (`min-height`/`min-width` + padding on buttons, links, inputs).
- Visual order vs DOM order: Grid placement and `order` change only visuals; keyboard/tab order follows the DOM. If the visual order diverges meaningfully from DOM order, reorder the DOM instead.
- Whitespace scales up with viewport: mobile `--space-8` section padding, desktop `--space-16`+.
- `prefers-reduced-motion` applies to layout animations (accordion, drawer) too.

## Flexbox vs Grid cheat sheet

| Situation | Use |
|---|---|
| Navbar, toolbar, button row | Flex row + gap |
| Tag/chip list that wraps | Flex + wrap |
| Media object (avatar + text) | Flex or Grid `auto 1fr` |
| Page shell | Grid + template-areas |
| Dashboard panels | Grid |
| Card list, gallery | Grid auto-fit/minmax |
| Form with aligned labels | Grid `auto 1fr` |
| Vertical centering of one thing | Grid `place-items: center` |
| Distribute leftover space along one axis | Flex `justify-content` |
