---
name: brand-asset
description: "Produces branded visual identity elements — logo concepts, icon sets, seamless patterns, brand illustrations, and textures — as generation-ready prompt specs, and generates them via FAL.ai fal-ai/nano-banana-pro when the automation is configured. Use when the user says 'design a logo', 'I need icons', 'brand pattern / texture', 'brand illustrations', 'visual identity elements', or 'make my brand assets'. Produces one prompt-spec block per asset (asset type, style, palette with hex, composition, negative constraints), a variant plan for user selection, file-naming conventions, and a brand-guidelines entry for each approved asset; runs docs/creative_cli.py brand when FAL_API_KEY is set."
---

# Brand Asset

Generate the visual identity elements a brand reuses everywhere — logo concepts,
icons, patterns, illustrations, textures — as prompt specs sharp enough that the
whole family looks designed by one hand. **Prime rule: cohesion over cleverness.**
A brand asset is judged by how well it matches its siblings and survives resizing,
not by how impressive it is alone. And be honest about the medium: the model
outputs **raster concepts**; production logos and icons still need vector tracing.

## When to use / when not to

Use for logos, icon sets, patterns, brand illustrations, and textures. Hand off
instead when:

- No visual direction exists → `skills/creative/creative-strategist` first; its
  brief supplies this skill's style, palette, and mood. For a single throwaway
  asset, derive a minimal style inline and label it an assumption.
- The asset is a product image → `skills/creative/product-photography`
- The asset is a platform post/banner → `skills/creative/social-graphics`
- It's a general non-branded image → `skills/creative/image-generation`
- The user wants a full identity system rolled out across asset types →
  `skills/creative/orchestrator` sequences it (strategist → this skill → the rest)

## Intake

Ask in one batch, only what's missing:

1. **Brand** — name, what it does, one sentence of personality.
2. **Asset type(s)** — logo, icon set, pattern, illustration, texture? (These are
   also the automation's exact `--asset-type` choices.)
3. **Style anchor** — Creative Direction Brief / existing logo to match, or
   palette hex codes? For icons/patterns joining an existing identity, matching
   it is mandatory, not optional.
4. **Usage** — where will it live (app icon, website, print, merch)? This drives
   simplicity requirements and variant needs.
5. **Automation** — `FAL_API_KEY` set, or deliver specs only?

Infer, don't ask: aspect ratio (logos/icons/patterns → `1:1`; wordmark
lockups → `3:2` or `16:9`); resolution `2K` (patterns/textures `4K`). **Don't
stall:** with brand + asset type known, assume the rest, label it, proceed.

## Workflow

1. **Lock the style line.** One style from the vocabulary (minimalist, geometric,
   organic, illustrative, abstract) + palette in words and hex + mood — taken
   from the Creative Direction Brief when it exists. Every asset in the family
   uses the same style line verbatim.
2. **Write prompt specs from the templates** in `references/asset-library.md` —
   read it now; it has the per-type templates, style vocabulary, color
   application patterns, and delivery specs. Decision rules:
   - **Logo** → always generate as concepts to choose from: 4 variants
     (`--num-images 4`) or 3–4 distinct specs (different style angles). Never
     one take. Flat, plain background, no photorealism, no tiny text.
   - **Icon set** → generate the whole set as ONE sheet in one call so stroke
     weight and corner radius stay consistent; never one icon per call.
   - **Pattern/texture** → demand `seamless, tileable, edge-to-edge` and
     test-tile the result before accepting.
   - **Illustration** → fix subject + line weight + palette; generate 2–3.
3. **Set negative constraints** on every spec: no watermark, no gradients-and-
   bevels clutter (unless the style calls for it), no readable text beyond the
   exact brand name supplied, no stock-clipart clichés.
4. **Generate or deliver.** If `FAL_API_KEY` (or `FAL_KEY`) is set:

   ```bash
   python docs/creative_cli.py brand \
     --asset-type logo --brand-name "TechCorp" \
     --prompt "<full prompt>" \
     --aspect-ratio 1:1 --resolution 2K --num-images 4
   ```

   Saves to `assets/brand-assets/<brand-slug>/<asset-type>/` as
   `<type>_<n>_<timestamp>.png`. No key → deliver specs + exact commands; never
   claim generation happened. Parameter source of truth:
   `skills/creative/image-generation/references/automation.md`.
5. **User selects; you verify.** Present variants, have the user pick one per
   slot (recommend one, one-line reason). Check winners against the quality bar;
   fix misses with the fix-it phrases in `references/asset-library.md` — one
   iteration round.
6. **Record in the brand guide.** Add each approved asset to the guidelines entry
   (format below) and state the production step honestly (e.g. "trace to SVG
   before shipping").

## Required output format

One block per asset:

```
## Asset Spec — [asset name, e.g. logo-concept-A]
- **Asset type:** logo / icon / pattern / illustration / texture
- **Brand:** [name] · **Usage:** [where it will live]
- **Style:** [one style line, shared across the family]
- **Palette:** [color name #hex, role] ...
- **Composition:** [e.g. centered mark, plain background / 6-icon sheet on grid / edge-to-edge tile]
- **Mood:** [2–3 adjectives]
- **Aspect ratio:** [ratio] · **Resolution:** [1K/2K/4K] · **Format:** png
- **Negative constraints:** [no watermark, no text beyond "<brand>", ...]
- **Prompt (final, paste-ready):**
  > [single flowing prompt]
- **Variants:** [n] — [what varies]
- **File naming:** assets/brand-assets/<brand-slug>/<asset-type>/<type>_<n>_<timestamp>.png
- **Generate with:** `python docs/creative_cli.py brand --asset-type ... --brand-name "..." --prompt "..." --aspect-ratio ... --num-images n`
- **Production note:** [raster concept — trace to SVG / normalize grid / verify tiling]
```

After selection, append per approved asset a **Brand guide entry**: asset name,
file path, color variants needed, minimum size / clear space (logos), and usage
rule — using the guidelines skeleton in `references/asset-library.md`.

## Quality bar

- [ ] Every asset in the family shares the same style line and palette verbatim
- [ ] Logos: 3+ distinct concepts offered; works in one color; still reads at thumbnail size (describe the check, don't assume)
- [ ] Icon sets: generated as one sheet; consistent stroke weight and corner radius
- [ ] Patterns/textures: `seamless, tileable` in the prompt AND tiling verified (or flagged unverified)
- [ ] All colors given in words + hex, pulled from the brief when one exists
- [ ] Negative constraints on every spec; no text rendered beyond the supplied brand name
- [ ] Deliverable states the raster→vector production step for logos/icons — never imply the PNG is print-ready vector
- [ ] Only real automation parameters (`fal-ai/nano-banana-pro`; no size/steps/guidance knobs exist)

Hard don'ts: never mix two styles in one asset family; never present a generated
logo as trademark-cleared (recommend a clearance search); never fake generation
results when the API key is absent.

## Integration

- `skills/creative/creative-strategist` → upstream; the Creative Direction Brief
  supplies style line, palette, mood, and prohibitions.
- `skills/creative/image-generation` → shared automation;
  `references/automation.md` there is the parameter source of truth.
- `skills/creative/social-graphics` and `skills/creative/product-photography` →
  downstream; consume approved logos/patterns as recurring elements.
- `skills/creative/orchestrator` → sequences this skill inside brand-identity and
  rebrand paths; the artifact passed forward is the approved asset set + brand
  guide entries.
- `references/asset-library.md` — full templates, style vocabulary, delivery
  specs, guidelines skeleton, fix-it phrases. Read before writing specs.
