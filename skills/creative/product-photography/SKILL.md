---
name: product-photography
description: "Produces professional AI product photography — clean e-commerce shots, lifestyle scenes, hero images, macro detail shots, and flat lays — as generation-ready prompt specs, and generates the files via FAL.ai fal-ai/nano-banana-pro when the automation is configured. Use when the user says 'product photos', 'shots of my product', 'images for my store / listing / landing page', 'hero image for my product', 'lifestyle photos', or shares a product needing marketing imagery. Produces one prompt-spec block per shot (shot type, lighting, background, composition, aspect ratio, negative constraints) with a shot list, variant plan, and file-naming conventions; runs docs/creative_cli.py product when FAL_API_KEY is set."
---

# Product Photography

Turn a product description into a coherent **shot list** of prompt specs that
generate commerce-grade product imagery. **Prime rule: one product, one visual
world.** Every shot in a set shares the brand's lighting, palette, and treatment
so listings, landing pages, and social posts read as one brand — a stunning hero
next to a mismatched lifestyle shot is worse than two average matching ones.

## When to use / when not to

Use for any imagery whose subject is a product: e-commerce listings, landing-page
heroes, marketing shots, detail close-ups. Hand off instead when:

- The asset is a platform-sized post *about* the product (text overlays, promo
  layouts) → `skills/creative/social-graphics`
- The user needs a logo/icon/pattern → `skills/creative/brand-asset`
- It's a general image with no product subject → `skills/creative/image-generation`
- No visual direction exists and multiple assets are coming →
  `skills/creative/creative-strategist` first; consume its style block here
- The product should move → `skills/creative/product-video` (stills from this
  skill are its source frames)

## Intake

Ask in one batch, only what's missing:

1. **Product** — what is it, exactly? Materials, colors, distinguishing details.
   (If a real photo exists, ask for it as reference for accuracy.)
2. **Destination** — listing, landing page, ads, social? (drives shot types and
   aspect ratios)
3. **Positioning** — premium/luxury, accessible, playful, technical?
4. **Style anchor** — Creative Direction Brief / style block, or brand colors?
5. **Automation** — `FAL_API_KEY` set, or deliver specs only?

Infer, don't ask: aspect ratios from destination (listing → `1:1`, landing hero →
`16:9`, social feed → `4:5`); resolution `2K` default, `4K` for heroes.
**Don't stall:** with product + destination known, assume the rest, label it, go.

## Workflow

1. **Build the shot list.** Map destination → shot types (decision rules):
   - E-commerce listing → 1 clean shot + 1–2 detail shots (+ 1 lifestyle if the
     platform allows gallery images)
   - Landing page → 1 hero shot + 1 lifestyle + 1 detail
   - Social/ads → 1–2 lifestyle + 1 flat lay (product families) or hero
   - "Just one image" → pick the single type that serves the stated use; say why
2. **Fix the shared treatment.** Choose one lighting style and palette for the
   whole set from the style block (or infer from positioning: premium → dramatic
   or studio; approachable → natural golden hour; minimal brand → high-key).
   Every spec in the set uses it.
3. **Write one prompt spec per shot** using the templates in
   `references/shot-library.md` — read it now; it has the five shot-type
   templates plus the lighting/background/composition prompt language. Name
   colors in words and hex. Always state what must NOT appear (no watermark, no
   invented logos or label text unless the exact text is supplied, no clutter).
4. **Variants.** Hero and clean shots get 3–4 variants (`--num-images 3` or
   distinct specs varying composition/background); detail and lifestyle shots
   get 2. The user picks winners.
5. **Generate or deliver.** If `FAL_API_KEY` (or `FAL_KEY`) is set:

   ```bash
   python docs/creative_cli.py product \
     --product-name "Luxury Watch" \
     --prompt "<full prompt>" \
     --aspect-ratio 1:1 --resolution 2K --num-images 3
   ```

   Images save to `assets/product-photography/<product-slug>/` as
   `<product>_<n>_<timestamp>.png`. If no key, deliver the specs plus the exact
   commands — never claim generation happened. Full parameter reference:
   `skills/creative/image-generation/references/automation.md`.
6. **Review against the quality bar**, fix misses with the fix-it phrases in
   `references/shot-library.md` (one iteration round), then present winners with
   file paths and a one-line recommendation per slot.

## Required output format

Deliver a shot list of these blocks (one per shot):

```
## Shot Spec — [shot name, e.g. hero-01]
- **Shot type:** clean / lifestyle / hero / detail / flat lay
- **Destination:** [listing / landing hero / ad / social]
- **Subject:** [product, concretely — materials, colors, orientation]
- **Setting / background:** [white / gradient X→Y / lifestyle setting / textured]
- **Lighting:** [studio / natural golden hour / dramatic rim / high-key]
- **Composition:** [centered / rule of thirds / negative space / overhead]
- **Mood:** [2–3 adjectives, from the style block]
- **Aspect ratio:** [ratio] · **Resolution:** [1K/2K/4K] · **Format:** png
- **Negative constraints:** [no watermark, no invented label text, ...]
- **Prompt (final, paste-ready):**
  > [single flowing prompt]
- **Variants:** [n] — [what varies]
- **File naming:** assets/product-photography/<product-slug>/<product>_<n>_<timestamp>.png
- **Generate with:** `python docs/creative_cli.py product --product-name "..." --prompt "..." --aspect-ratio ... --resolution ... --num-images n`
```

Close with a **Set summary**: shared lighting/palette line, shot count per type,
and (if generated) recommended winner per slot with saved paths.

## Quality bar

- [ ] Every shot in the set shares one lighting style and palette (the set reads as one brand)
- [ ] Each spec names shot type, background, lighting, composition, and mood explicitly
- [ ] Aspect ratio matches the destination, not the `1:1` default by inertia
- [ ] Product details (materials, colors) match what the user described — no invented features, engravings, or label text
- [ ] Negative constraints present on every spec
- [ ] Hero/clean shots have 3+ variants; nothing shipped as a single take
- [ ] Only real automation parameters used (model is `fal-ai/nano-banana-pro`; no size/steps/guidance knobs exist)

Hard don'ts: never render readable brand/label text unless the user supplied the
exact string; never mix premium dramatic lighting and casual snapshot styles in
one set; never present AI shots as real photographs of the user's actual unit —
if fidelity to the exact physical product matters, say so and recommend
compositing or a reference-photo workflow.

## Integration

- `skills/creative/creative-strategist` → upstream; its style block sets this
  set's lighting, palette, and mood fields.
- `skills/creative/image-generation` → shared automation and prompt discipline;
  its `references/automation.md` is the parameter source of truth.
- `skills/creative/social-graphics` → consumes winning shots as raw material for
  platform posts.
- `skills/creative/product-video` → consumes the hero/lifestyle stills as frames
  and art direction.
- `references/shot-library.md` — full shot-type templates, lighting/background/
  composition prompt language, and fix-it phrases. Read before writing specs.
