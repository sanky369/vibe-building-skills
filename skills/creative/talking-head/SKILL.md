---
name: talking-head
description: "Plan presenter-led and UGC-style videos: choose the presenter archetype, define styling, setting, lighting, and framing, write the hook/body/CTA script skeleton, and produce keyframe prompts for the repo's FAL.ai pipeline. Use whenever the user wants a talking-head video, presenter video, UGC ad, testimonial, founder video, explainer with a person on camera, spokesperson content, or 'someone talking about my product' — even if they just say 'I need a video of a person explaining this'. Produces a Talking Head Video Spec: presenter definition, look/setting/lighting/framing decisions, timed script skeleton, and generation-ready keyframe prompts for fal-ai/nano-banana-pro."
---

# Talking Head

Turn a message and an audience into a complete **Talking Head Video Spec** — one presenter archetype fully specified (styling, setting, lighting, framing), a timed hook/body/CTA script skeleton, and keyframe prompts ready for `fal-ai/nano-banana-pro`. The governing principle: **credibility is cast, not scripted** — the presenter's look, setting, and register must match what the audience already trusts for this kind of message (a polished studio expert selling "authentic user review" reads as an ad and dies). You produce the plan and still keyframes; voice, motion, and editing happen downstream.

## When to use / when not to

- Use for any video fronted by a person: testimonials, UGC-style ads, educational/explainer videos, founder updates, product demos with a presenter, corporate training.
- Product-only motion (no person) → `skills/creative/product-video`.
- Programmatic/animated videos rendered in Remotion → `skills/creative/remotion-script-writer`.
- Static social assets → `skills/creative/social-graphics`.
- No brand style defined and consistency matters → run `skills/creative/creative-strategist` first; its style guide feeds presenter styling.

## Intake

Ask in one tight batch, only what's missing:

1. **Message and goal** — what is the presenter saying, and what should the viewer do after (CTA)?
2. **Audience and platform** — who watches, and where (TikTok/Reels, YouTube, landing page, internal training)?
3. **Trust mode** — should this feel like a peer's recommendation (authentic/UGC) or an expert's word (authority/polished)?
4. **Constraints** — real person to feature (founder, customer) or generated/hired presenter? Brand style guide from `skills/creative/creative-strategist`?

Infer instead of asking: platform → length and framing; product category → default trust mode (consumer social ad → UGC; B2B/finance/health → authority). **Don't stall:** with message + audience known, state assumptions ("Assuming UGC style, 30s, vertical — say otherwise") and proceed.

## Workflow

### 1. Cast the presenter (decision rule)

| If the content is… | Archetype | Register | Default setting |
|---|---|---|---|
| Educational, corporate, product demo | **Professional Presenter** | polished, business casual/formal, direct eye contact, confident | studio or professional office |
| Testimonial, social ad, relatable pitch | **UGC Creator** | casual clothes, natural look, authentic energy, imperfect is good | home, car, casual real-world spot |
| Thought leadership, reviews, authority claims | **Expert / Influencer** | polished but approachable, credible, high production | professional office or branded studio |
| Lifestyle content, product-in-life, aspirational | **Lifestyle Creator** | stylish, aspirational, engaging | lifestyle location matching the product |

Commit to one archetype with a one-line reason. Mismatches to catch: authority archetype for a "real customer" message (reads fake); UGC archetype for high-stakes B2B claims (reads unserious).

### 2. Lock the look — one choice per row

| Dimension | Options (pick one, driven by archetype + brand) |
|---|---|
| **Clothing** | business professional (suit) · business casual (blazer) · casual · stylish casual · industry-specific attire |
| **Background** | studio (neutral, clean) · office (blurred, modern) · home office · lifestyle setting · branded (brand colors/elements) |
| **Lighting** | studio (key + fill, even, no harsh shadows) · natural (soft, diffused, warm) · cinematic (dramatic, moody) |
| **Framing** | close-up (head/shoulders — intimacy, hooks) · medium (head-to-waist — default, allows gesture) · wide (full body — environment storytelling) |

Decision rules: UGC → casual clothing + natural lighting + close-up/handheld feel. Authority → business casual + studio lighting + medium shot. Clothing must contrast with the background color. Vertical platforms default to close-up or tight medium; landscape/YouTube tolerates medium and wide.

### 3. Write the script skeleton with hard timing

- **Hook (0–3s):** open with the viewer's problem, a bold claim, or the result — never "Hi, I'm…" on social. One sentence, ≤15 words.
- **Body (3s → CTA):** one core message, max 3 supporting points, spoken language (read it aloud — if a sentence can't be said in one breath, split it). Product shown on camera if relevant.
- **CTA (final 5s):** one action, stated once, plainly.

Length by platform: social ads/organic 15–60s; landing page 30–90s; training as needed. ~2.5 words/second is a workable speaking-pace heuristic for timing the script.

### 4. Write keyframe prompts

One keyframe per script section (hook, each body beat, CTA). Prompt formula: `[archetype] presenter, [clothing], [appearance/expression for this beat], [engaging with camera / demonstrating product], [background], [lighting], [framing], professional quality, 4K`. Keep presenter description, background, and lighting **identical across all frames** — only expression, gesture, and any product prop change; drift here breaks the illusion of one continuous video.

If `FAL_API_KEY` (or `FAL_KEY`) is set, generate via the repo CLI (`docs/fal_api.py`, model `fal-ai/nano-banana-pro`):

```bash
python docs/creative_cli.py custom \
  --category "talking-head" --name "hook-frame" \
  --prompt "<keyframe prompt>" --aspect-ratio 9:16 --resolution 2K
```

Otherwise deliver prompts as ready-to-run commands. Note: this produces still frames for casting/storyboarding — voice, lip-sync, and motion come from downstream tools or a real shoot; audio quality is out of scope but flag to the user that it makes or breaks the video.

### 5. Self-check against the quality bar, deliver the spec.

## Required output format

Always deliver this structure:

```markdown
# Talking Head Video Spec — [Topic]

## Overview
- **Message (one sentence):** ...
- **Archetype:** Professional | UGC Creator | Expert | Lifestyle — [one-line reason]
- **Platform:** ... · **Aspect ratio:** ... · **Length:** ...s · **CTA:** ...

## Presenter definition
- Clothing: ... · Appearance: ... · Background: ... · Lighting: ... · Framing: ...
- Real person or generated: ... · Brand elements in frame: ...

## Script skeleton
| Section | Time | Spoken line(s) | On camera |
|---|---|---|---|
| Hook | 0–3s | "..." (≤15 words) | [expression/action] |
| Body 1 | 3–Xs | "..." | ... |
| Body 2 | ... | "..." | ... |
| CTA | last 5s | "..." | ... |

## Keyframes
### KF-hook
> [full prompt — archetype, clothing, expression, background, lighting, framing, quality tags]
`python docs/creative_cli.py custom --category "talking-head" --name "kf-hook" --prompt "..." --aspect-ratio [x] --resolution 2K`
(one per section; presenter/background/lighting identical across all)

## Production notes
- Audio: [clean VO essential; mic/recording note]
- Downstream: [real shoot / avatar tool / editor] · B-roll or product inserts: ...
```

## Quality bar (check before delivering)

- Archetype matches the trust mode — no polished studio look on a "real customer" testimonial, no sloppy UGC for high-stakes authority claims.
- Hook ≤15 words and contains no self-introduction (for social); value stated in the first 3 seconds.
- One core message, ≤3 supporting points; every line survives being read aloud.
- Clothing contrasts with background; lighting style named explicitly (never left implicit).
- Keyframe prompts share identical presenter, background, and lighting descriptors — only expression/gesture varies.
- Direct eye contact specified in every keyframe unless the beat deliberately breaks it.
- Timings sum to the stated length; CTA is one action, stated once.
- No invented performance claims about formats or hooks; pacing guidance is heuristic.

## Integration

- `skills/creative/creative-strategist` → feeds in: style guide governing presenter styling, palette, and setting.
- `skills/creative/original-design` → feeds in: a design-language brief when the video must live inside an original visual world (backgrounds, props, overlays).
- `skills/creative/brand-asset` → feeds in: logos/brand elements placed in the background or as overlays.
- `skills/creative/image-generation` → consumes: keyframe prompts when the user wants finer generation control than the CLI one-liners.
- `skills/creative/social-graphics` → consumes: keyframes as thumbnails and supporting post visuals.
- `skills/creative/orchestrator` → routes campaign work that includes presenter video through this skill.
