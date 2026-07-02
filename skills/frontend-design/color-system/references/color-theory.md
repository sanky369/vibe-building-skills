# Color Theory Reference

Read when choosing a palette from scratch, constructing ramps by hand, or debugging a palette that looks wrong.

## Harmony techniques

**Monochromatic** — tints/shades of one hue.
```
Primary #3B82F6 → tints #93C5FD #DBEAFE #EFF6FF · shades #1D4ED8 #1E40AF #172554
```
Use for minimalist, focused products. Risk: flat; lean on lightness contrast and one status accent.

**Analogous** — hues 30–60° apart on the wheel.
```
#3B82F6 (blue) · #8B5CF6 (violet) · #06B6D4 (cyan)
```
Cohesive and calm; good default for a secondary hue.

**Complementary** — ~180° apart.
```
#3B82F6 (blue) · #F59E0B (amber)
```
Maximum energy; use the complement only for CTAs/highlights (~10% of surface) or it turns garish.

**Triadic** — three hues 120° apart.
```
#3B82F6 · #F59E0B · #10B981
```
For products that must color-code 3+ categories. Mute two, let one lead.

## Color psychology (heuristics, not laws)

| Hue | Associations | Common in |
|---|---|---|
| Blue | Trust, calm, competence | Tech, finance, health |
| Green | Growth, success, nature | Fintech gains, sustainability |
| Red | Urgency, error, passion | Alerts, sales, food |
| Purple | Creativity, premium | Creative tools, luxury |
| Orange | Energy, friendliness | Consumer, social, CTAs |
| Yellow | Optimism, caution | Warnings, highlights |
| Teal/Cyan | Clarity, modern | Info states, data products |

Cultural context shifts these; treat as defaults, not rules.

## Constructing a ramp by hand

Work in HSL or OKLCH (OKLCH keeps perceived lightness honest across hues):

1. Place the brand color at 500 or 600 (600 if white text must sit on it).
2. Step lightness roughly evenly toward 98% (step 50) and 10–15% (step 950).
3. Hold hue steady, but allow small hue drift toward yellow in light steps and toward blue in dark steps — it reads more natural than a mechanical lightness slide.
4. Reduce chroma at both extremes (very light and very dark can't hold saturation).
5. Sanity-check: convert each step to greyscale — the ramp should read as an even staircase.

Tinted neutrals: take the brand hue, drop saturation to ~5–15%, run the same lightness staircase. Higher saturation (~15%) suits warm brands; ~5% suits corporate/cool.

## Contrast math

WCAG ratio = (L1 + 0.05) / (L2 + 0.05), with L = relative luminance. Thresholds:

| Level | Normal text | Large text (≥24px or ≥18.7px bold) | UI components |
|---|---|---|---|
| AA | 4.5:1 | 3:1 | 3:1 |
| AAA | 7:1 | 4.5:1 | — |

Compute in-session (the formula is simple) or via a quick script; never eyeball. WCAG 2.x under-penalizes some pairs (light text on saturated orange/mid-blue passes but reads poorly) — when a pair passes AA yet looks weak, check APCA (aim Lc 60+ for body text, 75+ for small text) and darken the background a step.

## Color-blind-safe design

~8% of men have some color-vision deficiency, mostly red-green.

- Never encode meaning in color alone: pair with icon, label, or pattern.
- Safest high-contrast hue pair: **blue vs orange**.
- Avoid red-vs-green as the only distinction between success/error or chart series.
- Wong palette (safe categorical set): `#0173B2` blue, `#DE8F05` orange, `#029E73` green, `#CC78BC` purple, `#CA9161` brown, `#ECE133` yellow, `#56B4E9` sky.
- Test with a simulator (Coblis, Color Oracle, or browser devtools "Emulate vision deficiencies").

## Dark mode pitfalls

1. **Pure black backgrounds** cause smearing on OLED and halation for astigmatic users → use gray-900/950 (`#0F172A`/`#020617` region).
2. **Unmodified brand colors vibrate** on dark — lighten one ramp step and/or cut chroma ~10%.
3. **Shadows die on dark** — convey elevation with lighter surface tints (surface +1 elevation = one gray step lighter), not bigger shadows.
4. **Ratios don't transfer** — a 4.6:1 light-mode pair can drop below 3:1 after remap; re-verify everything.
5. **Don't invert images/illustrations**; provide dark variants or wrap in a light surface.
6. Respect the user: honor `prefers-color-scheme` by default; a manual toggle overrides via `.dark` class.

## Interactive-state ramp convention

```
default  → brand-600
hover    → brand-700 (one step darker in light mode; one lighter in dark mode)
active   → brand-800
disabled → gray-300 bg + gray-500 text (and drop the pointer cursor)
focus    → 2px ring in brand-500 at 3:1 vs adjacent colors, offset 2px
```

One-step moves per state keep the system predictable; never invent off-ramp hover colors.
