# Product photography shot library

Full prompt templates and treatment options for each shot type. Fill bracketed
fields from the brand's Creative Direction Brief
(`skills/creative/creative-strategist`), then assemble into a single flowing
prompt. Generate with `fal-ai/nano-banana-pro` via
`python docs/creative_cli.py product ...` (see
`skills/creative/image-generation/references/automation.md`).

## Shot types

### 1. Clean product shot — e-commerce listings, product pages, catalogs
```
[Product], professional product photography, white background,
studio lighting, sharp focus, 4K, centered composition, [color palette],
clean aesthetic, high-end product photography
```
Example: `Luxury leather wallet, professional product photography, white background, studio lighting, sharp focus, 4K, centered composition, brown and gold tones, clean aesthetic, high-end product photography`

### 2. Lifestyle shot — social media, marketing, lifestyle branding
```
[Product] in use, lifestyle photography, [setting], natural lighting,
[composition], [mood], professional quality, 4K, [color palette],
magazine quality photography
```
Example: `Coffee cup in use on a wooden desk, lifestyle photography, morning setting, natural golden hour lighting, rule of thirds composition, warm and inviting mood, professional quality, 4K, warm brown and cream tones, magazine quality photography`

### 3. Hero shot — landing pages, featured content
```
[Product] hero shot, dramatic professional photography, [background],
cinematic lighting, dynamic composition, [mood], 4K, [color palette],
award-winning photography
```
Example: `Smartphone hero shot, dramatic professional photography, gradient background, cinematic lighting, dynamic composition, premium mood, 4K, blue and silver tones, award-winning photography`

### 4. Detail / macro shot — features, textures, close-ups
```
Close-up of [product detail], macro photography, sharp focus,
professional studio lighting, [mood], 4K, [color palette], high detail
```
Example: `Close-up of watch face, macro photography, sharp focus, professional studio lighting, luxury mood, 4K, gold and black tones, high detail`

### 5. Flat lay — styled social content, product families
```
Flat lay of [product and accessories], styled photography, [background],
natural soft lighting, overhead composition, [mood], 4K, [color palette],
professional styling, magazine quality
```
Example: `Flat lay of skincare products and accessories, styled photography, marble background, natural soft lighting, overhead composition, luxury mood, 4K, white and rose gold tones, professional styling, magazine quality`

## Lighting styles

| Style | Prompt language | Best for |
|---|---|---|
| Studio | `studio lighting, controlled even illumination, no harsh shadows, clean aesthetic` | Clean shots, catalogs |
| Natural | `natural lighting, golden hour, soft diffused light, warm tones, gentle shadows` | Lifestyle, authentic feel |
| Dramatic | `dramatic lighting, rim lighting, moody atmosphere, cinematic shadows, high contrast` | Hero shots, premium positioning |
| High-key minimal | `minimalist lighting, soft key light, subtle shadows, high-key, clean and simple` | Minimal brands |

## Backgrounds

| Background | Prompt language |
|---|---|
| White/clean | `white background, clean aesthetic, minimal, professional` |
| Gradient | `gradient background, [color1] to [color2], smooth transition, modern aesthetic` |
| Textured | `[material] textured background, subtle texture, [color], professional` |
| Lifestyle | `[setting] background, lifestyle context, natural environment, [mood]` |
| Blurred/bokeh | `blurred background, bokeh, shallow depth of field, focus on product, [color] tones` |

## Compositions

| Composition | Prompt language | Best for |
|---|---|---|
| Centered | `centered composition, symmetrical, balanced` | E-commerce, clean shots |
| Rule of thirds | `rule of thirds composition, product at intersection, dynamic` | Lifestyle, editorial |
| Leading lines | `leading lines composition, lines guide eye to product` | Storytelling scenes |
| Negative space | `generous negative space, product off-center, minimalist` | Luxury, minimal brands |

## Fix-it phrases (when a draft misses)

- Looks cheap → add `premium, luxury, high-end`, switch flat lighting to dramatic
- Background competes → `minimal background, focus on product`, more negative space
- Lighting unnatural → name it exactly (`studio` / `golden hour`), add `soft, diffused, even illumination`
- Off-brand colors → name colors in words *and* hex, pull from the Creative Direction Brief palette
