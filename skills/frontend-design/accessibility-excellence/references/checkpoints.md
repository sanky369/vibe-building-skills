# Accessibility — Checkpoints & Pattern Gallery

Audit checkpoints and canonical fixes, organized by POUR. The workflow and
decision rules live in `../SKILL.md`.

## POUR checkpoint tables

### Perceivable

| Checkpoint | Pass condition |
|---|---|
| Text alternatives (1.1.1) | Every informative image has descriptive `alt`; decorative images have `alt=""`; complex charts get a text description or link to one |
| Captions/transcripts (1.2.x) | Video has captions (`<track kind="captions">`); audio has a transcript link |
| Info not by color alone (1.4.1) | Every color-coded signal also has icon/text/pattern |
| Contrast, text (1.4.3 AA) | ≥4.5:1 normal text; ≥3:1 large text (≥24px, or ≥18.66px bold) |
| Contrast, non-text (1.4.11 AA) | ≥3:1 for UI component boundaries, focus indicators, meaningful graphics |
| Contrast AAA (1.4.6) | ≥7:1 normal, ≥4.5:1 large (only when AAA is in scope) |
| Reflow (1.4.10 AA) | Usable at 320px width / 400% zoom without horizontal scroll |
| Text resize (1.4.4 AA) | Readable and functional at 200% text size |

### Operable

| Checkpoint | Pass condition |
|---|---|
| Keyboard (2.1.1) | Every action reachable and operable by keyboard alone |
| No keyboard trap (2.1.2) | Focus can always leave any widget (modals trap intentionally but Escape/close works) |
| Skip link (2.4.1) | "Skip to main content" is first focusable element |
| Focus visible (2.4.7 AA) | Visible focus indicator on every interactive element; never `outline: none` without replacement |
| Focus order (2.4.3) | Tab order follows visual/logical order; no `tabindex` > 0 |
| Target size (2.5.8 AA, WCAG 2.2) | Pointer targets ≥24×24 CSS px (44×44 is the AAA guideline 2.5.5 and mobile-HIG norm) |
| Three flashes (2.3.1) | Nothing flashes more than 3×/second |
| Pointer alternatives (2.5.x) | Drag/swipe actions have single-pointer or button alternatives |

### Understandable

| Checkpoint | Pass condition |
|---|---|
| Page language (3.1.1) | `<html lang="…">` set |
| Labels (3.3.2) | Every input has a programmatic `<label>` — placeholder is not a label |
| Error identification (3.3.1) | Errors described in text, associated with the field |
| Error suggestion (3.3.3 AA) | Fix guidance given, not just "invalid" |
| Consistent navigation (3.2.3 AA) | Nav order consistent across pages |
| On focus/input (3.2.1/3.2.2) | Focusing or typing never triggers surprise context changes |

### Robust

| Checkpoint | Pass condition |
|---|---|
| Valid semantics (4.1.x) | Semantic elements for native meanings; unique ids referenced by ARIA exist |
| Name/role/value | Custom widgets expose role, accessible name, and state via ARIA |
| Status messages (4.1.3 AA) | Dynamic updates announced via live regions without stealing focus |

## Semantic HTML reference

| Element | Use for |
|---|---|
| `<header>` / `<footer>` | Page or section intro/outro |
| `<nav>` | Navigation blocks (label multiple: `aria-label="Breadcrumb"`) |
| `<main>` | The single main content region |
| `<article>` | Self-contained content (post, card with own heading) |
| `<section>` | Thematic grouping, ideally with a heading |
| `<aside>` | Tangential content |
| `<h1>–<h6>` | True hierarchy — one `<h1>`, no skipped levels |
| `<button>` | Actions. `<a>` | Navigation. Never swap them |
| `<label>` + `for` | Every form control |

Anti-pattern and its fix:

```html
<!-- Bad -->
<div class="btn" onclick="save()">Save</div>

<!-- Good -->
<button type="button" onClick={save}>Save</button>

<!-- Only when a native element is truly impossible -->
<div role="button" tabIndex={0} onClick={save}
     onKeyDown={(e) => (e.key === 'Enter' || e.key === ' ') && save()}>
  Save
</div>
```

## Keyboard patterns

### Focus indicator

```css
:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
/* Never: */
:focus { outline: none; }   /* without a visible replacement */
```

### Skip link

```html
<a href="#main-content" class="skip-link">Skip to main content</a>
...
<main id="main-content">
```

### Modal focus management

On open: move focus into the dialog. While open: trap Tab within it. On
Escape or close: return focus to the trigger.

```jsx
const Modal = ({ onClose }) => {
  const firstRef = useRef(null);
  const lastRef = useRef(null);

  const handleKeyDown = (e) => {
    if (e.key === 'Escape') onClose();
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstRef.current) {
        e.preventDefault(); lastRef.current?.focus();
      } else if (!e.shiftKey && document.activeElement === lastRef.current) {
        e.preventDefault(); firstRef.current?.focus();
      }
    }
  };

  return (
    <div role="dialog" aria-modal="true" aria-labelledby="dialog-title"
         onKeyDown={handleKeyDown}>
      ...
    </div>
  );
};
```

Prefer the native `<dialog>` element or an established headless library
(Radix, Headless UI, React Aria) over hand-rolled traps when available.

### Expected keys per widget

| Widget | Keys |
|---|---|
| Button | Enter, Space |
| Link | Enter |
| Modal | Escape closes; Tab trapped |
| Menu/listbox | Arrows move, Enter selects, Escape closes |
| Tabs | Arrows switch tabs, Tab exits the tablist |
| Checkbox | Space toggles |

## ARIA patterns

First rule of ARIA: prefer native HTML; use ARIA only to fill gaps.

```html
<!-- Accessible name for icon-only control -->
<button aria-label="Close menu">×</button>

<!-- Live region for status updates (does not steal focus) -->
<div aria-live="polite" aria-atomic="true">Item added to cart</div>

<!-- Urgent announcement -->
<div role="alert">Error: Please fill in all required fields.</div>

<!-- Disclosure state -->
<button aria-expanded={isOpen} aria-controls="menu">Menu</button>
<div id="menu" hidden={!isOpen}>…</div>

<!-- Current page in nav -->
<a href="/" aria-current="page">Home</a>

<!-- Field ↔ error association -->
<input type="email" aria-invalid="true" aria-describedby="email-error" />
<span id="email-error">Please enter a valid email address.</span>
```

Common ARIA mistakes to flag in audits: redundant roles (`<button role="button">`),
`aria-label` overriding useful visible text, live regions inserted after the
content changes (must exist in the DOM first), `aria-hidden="true"` on
focusable elements.

## Content & media

```html
<!-- Descriptive alt -->
<img src="chart.png" alt="Sales increased 25% in Q4 2025" />
<!-- Decorative -->
<img src="decoration.png" alt="" />

<!-- Descriptive link text: name the destination, not "read more" -->
<a href="/article">Read more about accessibility</a>

<!-- Captions -->
<video controls>
  <source src="video.mp4" type="video/mp4" />
  <track kind="captions" src="captions.vtt" srclang="en" label="English" />
</video>
```

## Readability defaults

```css
body { font-size: 16px; line-height: 1.5; }  /* ≥16px, line-height ≥1.5 */
main { max-width: 65ch; }                     /* readable measure */
```

## Testing tooling

- **Automated:** axe-core (via `@axe-core/react`, Playwright, or the browser
  extension), Lighthouse accessibility category. Automated tools catch
  roughly a third to half of issues — never claim conformance from a clean
  automated run alone.
- **Manual keyboard pass:** Tab through every flow; check reachability,
  visible focus, logical order, no traps, Escape behavior.
- **Screen reader spot-check:** VoiceOver (macOS/iOS), NVDA (Windows) on the
  critical flows; verify names, roles, states, and announcements.
- **Zoom/reflow:** 200% text zoom and 320px-wide viewport.
- **Contrast:** WebAIM Contrast Checker or devtools' contrast info against
  the actual computed colors.
