# Creative Skills

10 agent skills for AI-powered visual content: strategy, design language, image generation, and video/script planning. The generation skills share one automation stack — FAL.ai's `fal-ai/nano-banana-pro` model driven by the Python scripts in `docs/` at the repo root.

Every skill follows the authoring standard in [`docs/SKILL_SPEC.md`](../../docs/SKILL_SPEC.md): each is an operating procedure the agent executes, with intake questions, decision rules, a required output format, and a quality bar.

## The Skills

| Skill | Produces |
|---|---|
| **orchestrator** | Routes a creative request to the right skill sequence (6 routes: brand-from-zero, product launch, social campaign, rebrand, video-led, web design) |
| **creative-strategist** | Creative Direction Brief with a paste-ready style block that downstream skills consume |
| **original-design** | Design Language Brief — an original, coherent visual "world" for infographics, storyboards, websites, or app UI, built from live web inspiration |
| **image-generation** | Prompt Specs and generated images via the shared automation; owns `references/automation.md`, the parameter source of truth |
| **product-photography** | Shot Specs and product image sets (listing, landing, social treatments) |
| **product-video** | Production Spec: beat sheet, keyframe prompts, audio and production notes |
| **social-graphics** | Platform-sized graphic specs with copy-first design and master-then-adapt variants |
| **brand-asset** | Asset Specs for logos, icons, patterns, illustrations, textures + brand-guide entries |
| **talking-head** | Talking Head Video Spec: presenter casting, timed script, keyframes |
| **remotion-script-writer** | Remotion-ready JSON video script (see its `rules/` files for the schema) |

## Where to Start

- **Full brand or campaign** → `orchestrator` diagnoses and routes.
- **Need a visual identity first** → `creative-strategist` (fast brief) or `original-design` (deep, question-driven design language).
- **Just need assets and you know what you want** → go straight to the specialist skill; it will ask for a style anchor if none exists.

## Automation Setup

The generation skills invoke the real scripts — no separate download exists:

```bash
pip install -r docs/requirements.txt
export FAL_API_KEY="your_fal_key"        # FAL_KEY also works
python docs/creative_cli.py test         # verify connectivity
```

CLI subcommands: `product`, `social`, `brand`, `custom`, `test` (see `python docs/creative_cli.py --help`). Generated files land under `assets/` with timestamped names.

**Model facts (honest limits):**
- Single model: `fal-ai/nano-banana-pro`. Parameters: `num_images` (1–4), `aspect_ratio`, `resolution` (1K/2K/4K), `output_format` (png/jpeg/webp).
- It produces **stills only** — video skills plan keyframes, not rendered video.
- Rendered text in images is unreliable; overlay copy in post.
- Output is raster (PNG/JPEG/WebP). "SVG logos" require a tracing step afterward.

Never commit your API key — see [SECURITY.md](../../SECURITY.md).

## How the Skills Connect

`creative-strategist` / `original-design` produce the style anchor → every generation skill embeds it in prompts so all assets share one visual world → `image-generation`'s `references/automation.md` defines the parameters everyone uses → planning skills (`product-video`, `talking-head`, `remotion-script-writer`) consume the same anchor for keyframes and scripts.
