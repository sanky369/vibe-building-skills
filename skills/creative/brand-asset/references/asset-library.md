# Brand asset library — templates, styles, specifications

Full prompt templates per asset type, style vocabularies, and delivery specs.
Fill bracketed fields from the Creative Direction Brief
(`skills/creative/creative-strategist`). Generate with `fal-ai/nano-banana-pro`
via `python docs/creative_cli.py brand --asset-type <type> ...` — the CLI's
`--asset-type` choices are exactly this taxonomy: `logo`, `icon`, `pattern`,
`illustration`, `texture`.

## Asset-type templates

### logo — primary brand mark
```
Logo design for [brand name], [style], [color palette], minimalist,
scalable, professional, modern, [mood], vector-style flat design,
clean lines, plain background, 4K
```
Example: `Logo design for tech startup, geometric style, blue and white colors, minimalist, scalable, professional, modern, innovative mood, vector-style flat design, clean lines, plain background, 4K`

### icon — supporting UI/marketing symbols
```
Icon set for [brand/purpose], [number] icons on one sheet, [style],
[color palette], consistent stroke weight and corner radius, professional,
scalable, [mood], vector-style flat design, plain background, 4K
```
Example: `Icon set for SaaS product, 6 icons on one sheet, minimalist line style, blue and gray colors, consistent stroke weight and corner radius, professional, scalable, modern mood, vector-style flat design, plain background, 4K`

### pattern — repeating surface design
```
Seamless repeating brand pattern, [pattern type], [color palette],
[style], subtle, professional, [mood], tileable, edge-to-edge, 4K
```
Example: `Seamless repeating brand pattern, geometric pattern, blue and white colors, minimalist style, subtle, professional, modern mood, tileable, edge-to-edge, 4K`

### illustration — custom branded scenes/spots
```
Brand illustration for [brand], [subject], [style], [color palette],
consistent line weight, professional, [mood], on-brand, 4K
```
Example: `Brand illustration for wellness company, person meditating, minimalist flat style, green and white colors, consistent line weight, professional, calm mood, on-brand, 4K`

### texture — subtle background surfaces
```
Brand texture design, [texture type], [color palette], subtle,
low-contrast, seamless, professional, [mood], suitable for backgrounds
and overlays, 4K
```
Example: `Brand texture design, soft paper grain texture, warm cream tones, subtle, low-contrast, seamless, professional, calm mood, suitable for backgrounds and overlays, 4K`

## Style vocabulary (pick ONE per brand and keep it)

| Style | Prompt language |
|---|---|
| Minimalist | `minimalist design, simple shapes, clean lines, generous white space` |
| Geometric | `geometric design, precise geometric shapes, symmetrical, clean lines` |
| Organic | `organic design, flowing shapes, natural forms, smooth curves` |
| Illustrative | `illustrative design, artistic, detailed, expressive` |
| Abstract | `abstract design, conceptual abstract shapes, artistic` |

## Color application patterns

- Role-based: `use [primary] for main elements, [secondary] for accents, [accent] for highlights`
- Monochromatic: `monochromatic design using [primary color], varying shades for depth`
- Complementary: `complementary color scheme with [color1] and [color2], balanced`

Always name colors in words *and* hex ("deep navy #004E89").

## Delivery specifications (post-generation targets)

The model outputs raster PNG/JPEG/WebP only. For production use:

- **Logos** — trace/redraw the chosen concept to true vector (SVG/PDF); derive
  full-color, monochrome, and white-on-dark variants; verify legibility at 16px
  and 512px; define clear-space and minimum-size rules.
- **Icons** — normalize to a shared grid (16/24/32/48/64px), equalize stroke
  weight, export as SVG.
- **Patterns/textures** — verify the tile actually repeats without visible
  seams (butt two copies edge-to-edge); regenerate with stronger
  `seamless, tileable` language if it doesn't; 4K masters.

## Brand asset guidelines skeleton

Record every approved asset in the brand guide:

```
1. LOGO — primary, variations, minimum size, clear space, color variants
2. ICON SET — style, sizes, stroke weight, color usage
3. COLOR PALETTE — primary/secondary/accents with hex, usage rules
4. TYPOGRAPHY — headline font, body font, sizes
5. PATTERNS & TEXTURES — descriptions, where used
6. CONSISTENCY RULES — must-always / never-include / quality standards
```

## Fix-it phrases

- Logo looks amateur → simplify: `minimalist, simple shapes, flat design`; drop gradients and effects
- Icon set inconsistent → generate as ONE sheet in one call; `consistent stroke weight and corner radius, same style throughout`
- Pattern seams visible → `seamless, tileable, edge-to-edge repeating`; test-tile before accepting
- Colors drift off-brand → words + hex in the prompt, from the Creative Direction Brief palette
