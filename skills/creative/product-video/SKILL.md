---
name: product-video
description: "Plan an animated product video end-to-end: pick the video type, define the animation style and pacing, write a beat-by-beat shot list, and produce ready-to-run keyframe prompts. Use whenever the user wants a product video, product animation, launch video, promo or ad video, animated product reveal, 360 spin, feature showcase, or 'a short video for my product' — even if they only say 'I need a video for the launch' or 'make my product look good in motion'. Also use to storyboard a video another tool will render. Produces a Product Video Production Spec: concept, beat sheet with timings and transitions, keyframe prompt list for fal-ai/nano-banana-pro, and audio/CTA direction."
---

# Product Video

Turn a product and a goal into a complete **Product Video Production Spec** — one chosen video concept, a beat-by-beat shot list with timings, an animation and pacing plan, and generation-ready keyframe prompts. The governing principle: **one video communicates one thing.** Every beat either builds toward the single message (the reveal, the benefit, the transformation) or it gets cut. You produce the plan and the keyframes; rendering the motion happens downstream.

## When to use / when not to

- Use for product-centric motion content: reveals, feature showcases, product-in-action, transformations, 360 spins.
- If the video is fronted by a person (presenter, testimonial, UGC) → use `skills/creative/talking-head`.
- If the video will be rendered programmatically in Remotion (UI demos, code tutorials, data viz) → use `skills/creative/remotion-script-writer`; you can still run this skill first to define concept and beats, then hand the beat sheet over.
- If the user needs static assets (posts, banners) → `skills/creative/social-graphics`.
- If there is no brand style guide yet and the user cares about brand consistency → run `skills/creative/creative-strategist` first; its style guide feeds this skill.

## Intake

Ask in one tight batch, only what's missing:

1. **Product** — what is it and what's the one thing the video must communicate (new launch? a feature? a benefit? a before/after)?
2. **Where it runs** — TikTok/Reels/Shorts, product page, YouTube pre-roll, trade show loop? (This decides aspect ratio, duration, pacing.)
3. **What the viewer should do after** — the CTA.
4. **Brand style** — is there a `skills/creative/creative-strategist` style guide or existing brand assets to match?

Infer from context instead of asking: aspect ratio from platform, mood from product category, style from any existing brand materials in the project. **Don't stall:** if the product and goal are clear, state your assumptions for the rest ("Assuming Reels, 12s, vertical, energetic — say otherwise") and proceed.

## Workflow

### 1. Choose the video type (decision rule, not a menu)

| If the message is… | Type | Duration | Beat structure |
|---|---|---|---|
| "This exists / it's new" | **Reveal** | 5–15s | hidden/obscured → reveal animation (fade, slide, rotate) → hero shot |
| "It does these 2–4 things" | **Feature Showcase** | 15–30s | feature 1 highlight → feature 2 → feature 3 → full product |
| "Here's the benefit in use" | **In Action** | 10–20s | product in environment → product being used → outcome shown |
| "Look at the change" | **Transformation** | 10–15s | before state → morph → after state |
| "Just show the object" (e-commerce, listings) | **360 Spin** | 5–10s | continuous smooth rotation, clean background |

Commit to one type with a one-line reason. Offer a single backup only if two genuinely fit. Never showcase more than 4 features — cut to the strongest.

### 2. Set pacing from platform

- **Fast** (5–10s, quick snappy cuts): social feeds, ads, anything skippable. Hook in the first 2 seconds.
- **Medium** (10–20s, smooth transitions): product pages, marketing site, email embeds.
- **Slow** (20–30s, deliberate luxurious moves): premium/luxury products, storytelling. Only choose slow if the product's price point earns the patience.

Aspect ratio by placement: 9:16 vertical (TikTok/Reels/Shorts/Stories), 16:9 (YouTube, web hero), 1:1 or 4:5 (feed posts). These map directly to `--aspect-ratio` values in the CLI.

### 3. Pick one animation style

Match to brand personality — pick exactly one and use its phrase verbatim in every keyframe prompt so frames stay consistent:

| Brand feel | Style | Prompt phrase |
|---|---|---|
| Elegant, calm | Smooth Fade | "smooth fade transitions, gentle pacing, elegant" |
| Modern, energetic | Dynamic Slide | "dynamic slide transitions, elements slide in, energetic pacing" |
| Cinematic, bold | Zoom & Rotate | "zoom and rotate moves, dynamic pacing, cinematic" |
| Sophisticated, fluid | Morphing | "smooth morphing transitions, fluid animation, sophisticated" |
| High-tech | Particle Effects | "particle effects, product materializes/dissolves, high-tech" |

### 4. Write the beat sheet

Break the duration into 3–6 beats. For each beat: time range, what's on screen, camera/motion, and the transition out. Every beat must advance the single message; the last beat always holds the product + CTA for ≥2 seconds.

### 5. Write keyframe prompts

One keyframe per beat (two for a transformation's before/after). Each prompt = subject + state at that beat + the animation-style phrase + lighting + the same style/lighting descriptors across all frames (consistency is what makes frames read as one video). All keyframes use identical background and lighting descriptions unless the beat explicitly changes location.

If `FAL_API_KEY` (or `FAL_KEY`) is set, generate the keyframes now with the repo CLI — model `fal-ai/nano-banana-pro` via `docs/fal_api.py`:

```bash
python docs/creative_cli.py custom \
  --category "video-keyframes" --name "beat-1-hero" \
  --prompt "<keyframe prompt>" --aspect-ratio 9:16 --resolution 2K
```

If no key is set, deliver the prompts as ready-to-run commands. Note: nano-banana-pro generates still keyframes only — the motion between them is produced downstream (Remotion, a video generation tool, or an editor).

### 6. Self-check against the quality bar, then deliver the spec.

## Required output format

Always deliver this structure:

```markdown
# Product Video Production Spec — [Product]

## Overview
- **Message (one sentence):** ...
- **Type:** Reveal | Feature Showcase | In Action | Transformation | 360 Spin — [one-line reason]
- **Platform / placement:** ... · **Aspect ratio:** ... · **Duration:** ...s · **Pacing:** Fast/Medium/Slow
- **Animation style:** [style + verbatim prompt phrase]
- **CTA:** ...

## Beat sheet
| # | Time | On screen | Camera / motion | Transition out |
|---|------|-----------|-----------------|----------------|
| 1 | 0–3s | ... | ... | ... |
| 2 | 3–7s | ... | ... | ... |
(final beat: product + CTA, held ≥2s)

## Keyframes
### KF-1 (beat 1) — [label]
> [full nano-banana-pro prompt]
`python docs/creative_cli.py custom --category "video-keyframes" --name "kf-1" --prompt "..." --aspect-ratio [ratio] --resolution 2K`
(repeat per beat; identical style/lighting descriptors across all)

## Audio direction
- Music: [genre/energy matched to pacing] · Sound design: [key moments] · VO: [none, or one line per beat]

## Production notes
- [render path: Remotion via skills/creative/remotion-script-writer / video gen tool / editor]
- [anything beat-specific: logo timing, text overlays, loop point for trade-show/spin videos]
```

## Quality bar (check before delivering)

- One message; if you can't state it in one sentence, restart at step 1.
- Hook lands within the first 2 seconds for Fast pacing, 4 for Medium.
- Beat count 3–6; no beat shorter than 1.5s; timings sum exactly to the stated duration.
- Every keyframe prompt contains the same animation-style phrase and the same lighting/background descriptors (unless the beat changes location) — inconsistent frames are the #1 failure mode.
- Prompts specify "smooth", "fluid" motion language — never leave motion quality implicit.
- CTA present in the final beat, held ≥2 seconds.
- No invented performance claims ("this format gets 3x engagement") — pacing/duration guidance above is heuristic, label it as such if asked.

## Integration

- `skills/creative/creative-strategist` → feeds in: the style guide (colors, mood, lighting language) that all keyframe prompts must obey.
- `skills/creative/product-photography` → feeds in: existing hero-shot prompts/lighting setups reused as the video's hero frame for consistency.
- `skills/creative/image-generation` → consumes: keyframe prompts, if the user wants deeper control over generation than the CLI one-liners.
- `skills/creative/remotion-script-writer` → consumes: the beat sheet + keyframes, when the video will be rendered as a Remotion composition.
- `skills/creative/social-graphics` → consumes: hero keyframes as source imagery for supporting static posts.
