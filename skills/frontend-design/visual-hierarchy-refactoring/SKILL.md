---
name: visual-hierarchy-refactoring
description: "Refactor cluttered or flat interfaces so users instantly see what matters, using size, weight, contrast, and whitespace — not more color. Use when the user says 'it looks cluttered', 'everything competes for attention', 'it looks amateur/flat', 'users can't find the button', 'make this scannable', 'this screen is overwhelming', or shares a screen where nothing stands out. Audits the actual component: lists every element's current visual weight vs intended priority, then delivers refactored component code (CSS/TSX) with a before/after hierarchy table explaining each change. De-emphasizes secondary elements before amplifying primary ones, and applies Gestalt grouping via spacing."
---

# Visual Hierarchy Refactoring

Take a real screen or component and refactor it so the eye lands on the right things in the right order. The deliverable is refactored code plus a before/after hierarchy audit — not design commentary. Governing principles: **hierarchy is a function of size, weight, and lightness contrast — color is the last resort**, and **the fastest fix is de-emphasis: quiet the noise before amplifying the signal.**

## When to use / handoffs

- Use when a specific screen is cluttered, flat, unscannable, or "looks off" despite sane tokens.
- No consistent tokens exist at all (every fix would be a new magic number) → `skills/frontend-design/design-foundation` first.
- The problem is structural (columns misaligned, breaks on mobile) → `skills/frontend-design/layout-system`.
- Font sizes themselves are chaotic across the app → `skills/frontend-design/typography-system`.
- Palette is the problem (clashing hues, contrast failures everywhere) → `skills/frontend-design/color-system`.

## Step 1 — Inspect the target

1. **Get the actual component.** Read the file(s) for the screen the user named; if none named, ask for the one screen that matters most (this is the only intake question that blocks). Render or screenshot it if the environment allows.
2. **Read the available tokens** (spacing scale, text sizes, grey ramp) — every fix must use them.
3. **Detect hierarchy smells** in the code, with counts:
   - Emphasis inflation: how many elements per screen are bold, colored, large, or bordered? (>3 competing emphases = nothing is emphasized)
   - Cramped spacing: padding/margins ≤8px between unrelated groups
   - True greys / pure black: `#808080`-family, `#000`, `text-gray-500` on colored surfaces
   - Uniform sizing: title, body, and metadata within a step of each other
   - Even spacing everywhere: identical gap inside and between groups (kills Gestalt grouping)
   - Border overuse: boxes-in-boxes where spacing would separate

## Step 2 — Build the hierarchy audit

For the target screen, list every visible element and assign:

- **Intended priority**: P1 (the one thing this screen exists for — one, maybe two elements), P2 (supporting), P3 (metadata/chrome).
- **Current visual weight**: loud / medium / quiet, judged from size, weight, color, and surroundings.

Every mismatch is a work item. If you can't name the single P1, ask the user one question: "What should a user do or see first on this screen?" — then proceed.

## Step 3 — Refactor, in this order

Apply changes strictly in this sequence — each pass often removes the need for the next:

1. **Whitespace first.** Start with too much and pull back. Double the spacing between unrelated groups; keep related items close (label 8px from its input; 24px+ between form groups). If a standard margin is 16px, try 32–48px between sections. Spacing must come from the token scale.
2. **De-emphasize P2/P3** before touching P1: drop bold from labels, lighten metadata to a mid-grey step (`gray-500/600`), remove borders/backgrounds that box in secondary content, shrink or icon-ify tertiary actions. Secondary buttons go outline/ghost; destructive actions become quiet until confirmed.
3. **Then amplify P1** — usually needs only one move once the noise is gone: one size step up, or weight 600→700, or the darkest text step, or the single saturated CTA. Not all four.
4. **Contrast ladder via lightness, not hue:** P1 text = darkest grey step, P2 = gray-600/700, P3 = gray-500. Tinted greys only (matching brand temperature) — never `#808080`/`#000`. Reserve saturated color for interactive elements and status.
5. **Group with Gestalt rules:** proximity (spacing shows relationships — the gap between groups ≥2× the gap within), similarity (identical roles look identical), common region (a card/background only when spacing can't do the job). Full principle set with CSS: `references/gestalt-principles.md`.
6. **Size ratios:** adjacent hierarchy levels differ by ~1.25–1.5×; P1 vs body ~1.5–2×. If two levels are within 10% of each other, merge them.

### Canonical before/after (the shape of most fixes)

```css
/* BEFORE: cramped, uniform, grey-on-grey */
.card { padding: 8px; }
.card h2 { font-size: 16px; font-weight: 400; color: #666; margin-bottom: 4px; }
.card p  { font-size: 14px; color: #999; line-height: 1.3; }

/* AFTER: room, clear ladder, tinted greys */
.card { padding: var(--space-6); }
.card h2 { font-size: var(--text-xl); font-weight: 600; color: var(--gray-900); margin-bottom: var(--space-2); }
.card p  { font-size: var(--text-base); color: var(--gray-600); line-height: 1.6; }
.card .meta { font-size: var(--text-sm); color: var(--gray-500); }
```

## Required output format

Deliver code plus this audit:

```
## Hierarchy audit — [screen name]
| Element | Intended | Was | Problem | Change |
| Submit button | P1 | quiet (same as Cancel) | competing siblings | solid brand bg; Cancel → ghost |
| Section labels | P3 | loud (bold, dark) | emphasis inflation | weight 400, gray-500 |
| Card metadata | P3 | medium | too prominent | text-sm, gray-500 |
| ... every element with a mismatch |

## Refactored code
[full component/CSS — same styling system, tokens only]

## What changed and why (≤5 bullets)
- [pass applied → effect, e.g. "Doubled inter-group spacing (space-4 → space-8): groups now scannable"]

## Scan test
First / second / third thing the eye hits now: [P1] → [P2] → [P2]. Matches intent: [yes / remaining gap]
```

## Quality bar (check before delivering)

- [ ] Exactly one P1 per screen, and it wins the 5-second scan
- [ ] ≤3 emphasized elements per screen; everything else visibly quiet
- [ ] Gap between unrelated groups ≥2× gap within a group; all spacing on the token scale
- [ ] ≤3 font weights in the result; bold never applied to whole paragraphs
- [ ] Text ladder uses lightness steps of tinted greys; no `#808080`, no `#000`, no new hues introduced for emphasis
- [ ] De-emphasized text still meets WCAG AA (4.5:1) — quiet ≠ illegible; P3 may go 3:1 only at large size
- [ ] Adjacent size levels differ ≥1.25×; no two levels within 10%
- [ ] Borders/boxes removed wherever spacing alone groups the content
- [ ] Every change references a token — zero new magic numbers

## Integration

- Consumes: tokens from `skills/frontend-design/design-foundation`, type scale from `skills/frontend-design/typography-system`, grey ramp from `skills/frontend-design/color-system`, page structure from `skills/frontend-design/layout-system`.
- Produces: refactored components that `skills/frontend-design/component-architecture` generalizes into the library; contrast decisions verified by `skills/frontend-design/accessibility-excellence`.
- In `skills/frontend-design/frontend-orchestrator` paths, this runs after tokens exist (Path B step 2) or as margin-level refinement (Path C).

## References

- `references/gestalt-principles.md` — all six Gestalt principles (proximity, similarity, figure/ground, closure, symmetry, common region) with CSS applications, plus extended before/after refactor examples. Read when a grouping problem isn't solved by proximity alone or you need more worked examples.
