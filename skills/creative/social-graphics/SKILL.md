---
name: social-graphics
description: "Produce platform-correct social media graphics: pick the right dimensions and layout per platform, write the headline/body/CTA copy, build the generation prompt, and generate the image via the repo's FAL.ai pipeline. Use whenever the user wants a social post visual, Instagram post/story/carousel, LinkedIn graphic, Twitter/X image, TikTok thumbnail, Pinterest pin, launch announcement graphic, or 'something to post about X' — even if they never name a platform. Also use to adapt one design across several platforms. Produces a Social Graphic Spec per asset (platform, dimensions, layout, copy, full generation prompt) plus generated images when FAL_API_KEY is available."
---

# Social Graphics

Turn a message and a platform into ready-to-post graphics. For each asset you produce a **Social Graphic Spec** — platform, exact dimensions, layout, overlay copy, and a complete generation prompt — then generate the image through the repo pipeline (`docs/creative_cli.py`, model `fal-ai/nano-banana-pro`). The governing principle: **a social graphic is read for under two seconds** — one message, one focal point, one CTA; if a viewer can't get the point from a thumbnail-sized glance, the design fails regardless of how good it looks full-size.

## When to use / when not to

- Use for platform-bound static visuals: feed posts, stories, pins, link-preview images, announcement graphics, quote cards, carousels.
- Logos, icons, patterns, brand marks → `skills/creative/brand-asset`.
- Standalone product hero shots (no platform framing, no overlay copy) → `skills/creative/product-photography`.
- Motion content → `skills/creative/product-video` (product-led) or `skills/creative/talking-head` (person-led).
- No brand style yet and the user wants a consistent look → run `skills/creative/creative-strategist` first; its style guide feeds this skill.
- If the visual language itself feels generic and needs an original identity → `skills/creative/original-design` first.

## Intake

Ask in one tight batch, only what's missing:

1. **Message** — what is this post saying, in one sentence? What should the viewer do (CTA)?
2. **Platform(s) and format** — Instagram feed/story/carousel, LinkedIn, Twitter/X, TikTok, Pinterest? One platform or a multi-platform set?
3. **Brand constraints** — style guide from `skills/creative/creative-strategist`, brand colors/fonts, product imagery to feature?
4. **Tone** — professional, trendy, minimalist, playful?

Infer instead of asking: tone from the platform (LinkedIn → professional; TikTok → energetic), colors from any brand materials in the project. **Don't stall:** with a clear message and platform, state assumptions for the rest and proceed.

## Platform specifications (source of truth for dimensions)

| Platform | Format | Pixels | CLI aspect-ratio | Design posture |
|---|---|---|---|---|
| Instagram | Feed post | 1080×1080 | `1:1` | vibrant, high contrast, trending aesthetic |
| Instagram | Story / Reel cover | 1080×1920 | `9:16` | full-bleed vertical, text in safe zone |
| Instagram | Carousel | 1080×1350 | `4:5` | one idea per card, visual continuity across cards |
| LinkedIn | Feed post | 1200×627 | `16:9`* | professional, credible, value-led copy |
| LinkedIn | Document page | 1200×1500 | `4:5` | clean, readable, business imagery |
| Twitter/X | Post image | 1200×675 | `16:9` | bold, simple, instant visual impact |
| TikTok | Thumbnail/graphic | 1080×1920 | `9:16` | bold text overlays, energetic, authentic feel |
| Pinterest | Standard pin | 1000×1500 | `2:3` | vertical, inspiring, high-quality imagery |

*Closest supported ratio; the CLI supports `21:9, 16:9, 3:2, 4:3, 5:4, 1:1, 4:5, 3:4, 2:3, 9:16` — always pick the nearest and note any crop.

## Workflow

### 1. Resolve platform and format

If the user named a platform, use the table above. If not, decide: B2B/professional audience → LinkedIn; consumer/lifestyle → Instagram; discovery/how-to/aspirational → Pinterest; announcement to an existing following → the platform where they have one (ask only if truly unknown). Multi-platform request → design the **master** for the most constrained format first (usually 1:1 or 9:16), then adapt per platform; never stretch one image across all.

### 2. Write the copy before the visual

- **Headline:** ≤10 words, the message itself, not a teaser.
- **Body (optional):** ≤2 short lines supporting the headline.
- **CTA:** 2–4 words, action verb ("Shop now", "Get the guide", "Link in bio").

If the copy can't fit these limits, the post is carrying more than one message — split it into a carousel or multiple posts and tell the user why.

### 3. Design the layout

Pick one focal point (product shot, illustration, bold typography) and place copy against the quietest area. Decision rules: photo-led → headline top or bottom third over a darkened/blurred band; typography-led → headline IS the focal point, minimal imagery; carousel → identical layout grid on every card, only content changes. Rule of thirds, generous negative space, max 2–3 font roles (headline / body / CTA).

### 4. Build the generation prompt

Formula — every prompt contains all six parts, in order:

```
[Platform + format] graphic, [subject/focal point], [color palette from brand or chosen],
[composition: focal point + where copy space is reserved], [tone/mood words],
[dimensions], professional design, high contrast, eye-catching
```

Always reserve explicit "clean negative space at [position] for text overlay" in the prompt — nano-banana-pro renders text imperfectly, so plan to overlay final copy in a design tool rather than trusting generated text for anything longer than 2–3 words.

### 5. Generate

If `FAL_API_KEY` (or `FAL_KEY`) is set, run the repo CLI (`docs/fal_api.py` under the hood, model `fal-ai/nano-banana-pro`):

```bash
python docs/creative_cli.py social \
  --platform instagram --topic "Product Launch" \
  --prompt "<full prompt>" --aspect-ratio 1:1 --resolution 2K
```

`--platform` accepts `instagram|linkedin|twitter|tiktok|pinterest`. Generate `--num-images 2` when the user is choosing between directions. If no key is set, deliver the spec with ready-to-run commands instead.

### 6. Self-check against the quality bar, deliver the spec + images.

## Required output format

One block per asset; a multi-platform set is the master followed by adaptation blocks:

```markdown
# Social Graphic Spec — [Campaign/Message]

## Asset 1 — [Platform · Format]
- **Dimensions:** 1080×1080 (aspect `1:1`) · **Role:** master | adaptation
- **Message:** [one sentence]

### Copy
- Headline: "..." (≤10 words)
- Body: "..." (≤2 lines, or —)
- CTA: "..."

### Layout
- Focal point: ... · Copy placement: ... · Palette: [colors + source: brand guide / chosen]

### Generation prompt
> [full prompt, all six parts]

`python docs/creative_cli.py social --platform [x] --topic "[x]" --prompt "..." --aspect-ratio [x] --resolution 2K`

### Result
- [generated file path(s), or "pending — FAL_API_KEY not set"]
- Post-gen step: overlay final copy in design tool: [yes/no + what]

## Asset 2 — [Platform · Format]
(same structure; for adaptations, note only what changes from the master)
```

## Quality bar (check before delivering)

- Dimensions match the platform table exactly; aspect ratio is a supported CLI value.
- Headline ≤10 words; total text ≤3 elements (headline, body, CTA); one message per asset.
- Copy placement sits over reserved negative space, not over the focal point.
- Text-background contrast is explicitly handled (band, shadow, or blur called out in layout).
- Palette and tone match the brand style guide when one exists; deviations flagged to the user.
- Prompt contains all six formula parts, including reserved copy space.
- Multi-platform sets: adapted per format, never one image stretched; carousel cards share one grid.
- No invented engagement statistics; "best practice" guidance here is heuristic — label it if asked.

## Integration

- `skills/creative/creative-strategist` → feeds in: the style guide (palette, typography, mood) every spec must obey.
- `skills/creative/original-design` → feeds in: a design-language brief when the user wants an original visual world; every graphic becomes an artifact of it.
- `skills/creative/product-photography` → feeds in: product shots reused as focal-point imagery.
- `skills/creative/product-video` → feeds in: hero keyframes reused as post visuals; consumes: nothing.
- `skills/creative/brand-asset` → feeds in: logos/marks to place; consumes: nothing.
- `skills/creative/orchestrator` → routes multi-asset campaigns through this skill per platform.
