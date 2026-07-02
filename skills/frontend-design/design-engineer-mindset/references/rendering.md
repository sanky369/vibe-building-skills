# Design Engineering — Rendering, Performance & Testing Reference

Deep material behind the workflow in `../SKILL.md`.

## The rendering pipeline

```
1. Parse HTML/CSS/JS
2. Build DOM tree
3. Compute styles (CSSOM)
4. Layout   (calculate geometry — expensive)
5. Paint    (rasterize pixels — expensive)
6. Composite (combine GPU layers — cheap)
```

Cost model for changed properties:
- `transform`, `opacity` → composite only (cheap; animate freely)
- `background-color`, `box-shadow`, `color` → paint + composite
- `width`, `height`, `top`, `left`, `margin`, `font-size` → layout + paint +
  composite (most expensive; never animate)

## Layout thrashing

Interleaving reads (`offsetWidth`, `getBoundingClientRect`) with writes
(`style.*`) forces synchronous reflow on every iteration.

```javascript
// Bad — forces layout every loop
for (let i = 0; i < 100; i++) {
  element.style.width = i * 10 + 'px';   // write (invalidates layout)
  const w = element.offsetWidth;          // read (forces layout NOW)
}

// Good — batch reads, then batch writes
const widths = elements.map((el) => el.offsetWidth);   // all reads
elements.forEach((el, i) => {                          // all writes
  el.style.width = widths[i] * 2 + 'px';
});
```

In handlers, do reads first, schedule writes in `requestAnimationFrame`.

## GPU-accelerated animation

```css
/* Bad — layout property */
@keyframes moveLeftBad {
  from { left: 0; }
  to   { left: 100px; }
}

/* Good — compositor property */
@keyframes moveLeft {
  from { transform: translateX(0); }
  to   { transform: translateX(100px); }
}
```

Fake expensive-property animation: crossfade a pseudo-element's `opacity` for
shadows; `transform: scale()` for size emphasis (watch text distortion).

## Frame budget & measurement

60fps = 16.7ms per frame, shared with browser work — treat ~10ms as your JS
budget per frame. 120Hz displays halve it.

Measure with DevTools Performance panel (look for long tasks and forced
reflow warnings). Quick FPS meter:

```javascript
let last = performance.now();
let frames = 0;
const measureFPS = () => {
  frames++;
  const now = performance.now();
  if (now >= last + 1000) {
    console.log(`FPS: ${frames}`);
    frames = 0;
    last = now;
  }
  requestAnimationFrame(measureFPS);
};
measureFPS();
```

Easing functions as math (for JS-driven animation):

```javascript
const linear    = (t) => t;
const easeOut   = (t) => 1 - Math.pow(1 - t, 3);
const easeIn    = (t) => Math.pow(t, 3);
const easeInOut = (t) => (t < 0.5 ? 4 * t ** 3 : 1 - Math.pow(-2 * t + 2, 3) / 2);
```

## Design tokens as code

Tokens are the single source of truth; components consume variables, never
raw values.

```css
:root {
  /* Spacing (8-point base) */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-xxl: 48px;

  /* Color */
  --color-primary: #0EA5E9;
  --color-secondary: #64748B;
  --color-error: #EF4444;
  --color-success: #10B981;

  /* Type */
  --font-size-h1: 48px;
  --font-size-body: 16px;
  --font-weight-bold: 700;
  --font-weight-normal: 400;

  /* Elevation */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}

.button {
  padding: var(--spacing-md) var(--spacing-lg);
  background: var(--color-primary);
  font-size: var(--font-size-body);
  box-shadow: var(--shadow-md);
}
```

In Tailwind projects the theme config *is* the token layer — extend it there
instead of adding parallel CSS variables.

## React render-performance patterns

Apply when profiling shows re-render cost — not by default:

```javascript
const MemoizedRow = React.memo(Row);                    // skip unchanged props
const handleClick = useCallback(() => { ... }, []);     // stable identity for memoized children
const derived = useMemo(() => expensive(data), [data]); // cache heavy computation
```

## Quality gates

### Visual regression

```javascript
// Percy / Chromatic snapshot per component state
describe('Button', () => {
  it('matches design', () => {
    cy.mount(<Button variant="primary">Click me</Button>);
    cy.percySnapshot('button-primary');
  });
});
```

Snapshot every variant × state that the spec defines, not just the default.

### Performance assertions

```javascript
describe('Performance', () => {
  it('renders large list within frame budget', () => {
    const start = performance.now();
    render(<LargeList items={1000} />);
    expect(performance.now() - start).toBeLessThan(16);
  });
});
```

## Reading design intent

Every value in a mockup encodes a reason — recover it before coding:

| Observation | Likely intent |
|---|---|
| Button 44–48px tall | Touch target (44×44 is the iOS HIG / WCAG AAA norm; WCAG 2.2 AA minimum is 24×24) |
| Spacing all multiples of 8 (or 4) | Grid system — snap your values to it |
| Animation 200–300ms | Fast enough to feel responsive, slow enough to read as intentional |
| Two shadows, not five | Elevation scale — reuse, don't invent a third |

When a mockup value contradicts the system (a stray 13px in an 8-point
world), ask or flag it — don't silently propagate or silently "fix" it.
