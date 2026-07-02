---
name: orchestrator
description: "Dispatcher for the creative suite: diagnoses a multi-asset creative request with a few questions, then routes it through the right sequence of creative skills, naming the artifact each step passes to the next, and wires in the FAL.ai automation (single model fal-ai/nano-banana-pro via docs/creative_cli.py) when available. Use when the user asks for several creative deliverables at once or an outcome that implies them — 'assets for my product launch', 'set up my brand visuals', 'I need a logo, product shots, and social posts', 'a week of content', 'rebrand everything' — or when it's unclear which creative skill applies. Produces a Creative Production Plan: chosen route, ordered skill sequence with hand-off artifacts, generation checklist, and asset output map. For a single obvious asset, skip this and use the specific skill directly."
---

# Creative Orchestrator

Route multi-asset creative work through the right skills in the right order, so
style gets decided once and every downstream asset inherits it. **Prime rule:
strategy before pixels.** Never let generation start before a style anchor
exists — assets generated pre-brief get regenerated. You are a dispatcher, not a
lecturer: diagnose fast, pick one route, name what each step hands to the next.

## When to use / when not to

Use when the request spans multiple asset types, names an outcome rather than an
asset ("launch assets", "brand refresh", "content for the month"), or the right
skill is ambiguous. Do NOT use for a single clear asset — route directly:
one logo → `skills/creative/brand-asset`; one product shot →
`skills/creative/product-photography`; one Instagram post →
`skills/creative/social-graphics`; one generic image →
`skills/creative/image-generation`.

## Intake (diagnostic — one batch)

1. **Outcome** — what event/goal are these assets for (launch, rebrand, ongoing
   content, storefront, video)?
2. **What exists** — style guide or Creative Direction Brief? Logo/brand assets?
   Product photos? (Existing artifacts skip their producing step.)
3. **Deliverables & destinations** — which assets, where they'll live
   (platforms, store, site)?
4. **Automation** — is `FAL_API_KEY` (or `FAL_KEY`) set? If unknown, check:
   `python docs/creative_cli.py test`

**Don't stall:** with the outcome known, infer the rest from context, state
assumptions, and present the plan. If automation is unavailable, the plan still
runs — every step's deliverable becomes prompt specs plus runnable commands
instead of generated files.

## Routing table

Pick ONE route by the first rule that matches. Sequence is by dependency; each
arrow names the artifact passed forward.

**Decision rules**
- No style anchor exists and >1 asset is needed → every route below starts with
  `skills/creative/creative-strategist`.
- Brand marks are among the deliverables → `brand-asset` runs before any skill
  that reuses the marks.
- Video deliverables → stills first (they are the video's source material).

| Route | Trigger | Sequence (artifact passed forward) |
|---|---|---|
| **A — Brand identity from zero** | "new brand", "set up my brand visuals", nothing exists | `creative-strategist` (Creative Direction Brief + style block) → `brand-asset` (approved logo/icons/pattern + guide entries) → `social-graphics` and/or `product-photography` (launch-ready assets using marks + style block) |
| **B — Product launch, identity exists** | "launch assets", "images for my store/landing page" | `product-photography` (winning shot set) → `social-graphics` (platform posts reusing the shots) → optional `product-video` (script/plan consuming hero stills) |
| **C — Social campaign / content series** | "week of content", "posts for X", ongoing presence | `creative-strategist` (skip if brief exists) → `social-graphics` (per-platform graphics) → optional `image-generation` (thumbnails, misc visuals via `custom` CLI) |
| **D — Rebrand / refresh** | "rebrand", "new look", "our visuals feel stale" | `creative-strategist` (revised brief; diff vs old style) → `brand-asset` (regenerated marks) → `social-graphics` (announcement assets) → re-run B for product imagery if it exists |
| **E — Video-led** | "product video", "presenter video", "animated demo" | prerequisite stills via B or C → `product-video` or `talking-head` (plan/script) → `remotion-script-writer` if it's a coded Remotion video |
| **F — Web/app design** | "landing page", "app design", responsive UI | `skills/creative/original-design` (this is design, not asset generation); pull imagery needs back into B/C |

Cross-cutting rule: `skills/creative/image-generation` is the utility skill for
any asset the specialists don't cover (thumbnails, infographics, textures) — slot
it wherever needed; it consumes the style block like everything else.

## Automation wiring (facts, verified against the repo)

- One model only: **`fal-ai/nano-banana-pro`** on FAL.ai. No fast/quality model
  variants exist.
- Scripts at repo root: `docs/fal_api.py` (client), `docs/creative_cli.py` (CLI:
  `product` / `social` / `brand` / `custom` / `test`), `docs/claude_integration.py`
  (Python helpers incl. `batch_generate_assets`).
- Setup: `pip install requests`; `export FAL_API_KEY="..."`;
  verify with `python docs/creative_cli.py test`.
- Real knobs: `--num-images` 1–4, `--aspect-ratio` (21:9…9:16), `--resolution`
  1K/2K/4K, `custom` also `--format png|jpeg|webp` and `--web-search`.
- Outputs land in `assets/product-photography/…`, `assets/social-graphics/…`,
  `assets/brand-assets/…`, `assets/<category>/…` automatically.

Full reference: `skills/creative/image-generation/references/automation.md` —
read it before writing any generation command into a plan.

## Required output format

Deliver the plan, then execute it step by step (invoking each skill in order,
carrying its artifact forward):

```
# Creative Production Plan — [outcome]

**Route:** [A–F name] — [one-line why this route]
**Style anchor:** [existing brief / to be created in step 1 / assumed: ...]
**Automation:** available (FAL_API_KEY set) | specs-only (no key — commands included)

## Sequence
| # | Skill (path) | Produces | Feeds forward |
| 1 | skills/creative/... | [artifact] | [what step 2 consumes] |
| 2 | ... | ... | ... |

## Asset map
| Asset | Type | Aspect ratio | Variants | Output path |
| [name] | product/social/brand/custom | [ratio] | [n] | assets/.../ |

## Checkpoints
- After step [n]: user picks [what] before [next step] starts.

## First action
[The single next thing you will do — usually "run step 1 now".]
```

## Guardrails

- **One route.** Commit with a one-line reason; offer at most one alternative if
  it's genuinely close. No route menus.
- **Never generate before the style anchor exists** (or is explicitly waived for
  a throwaway).
- **User checkpoints at selection points** — after logo concepts, after hero-shot
  variants — not after every image.
- **No fake capability.** If `FAL_API_KEY` is missing, say so; deliverables are
  prompt specs + commands. Never report images that weren't generated.
- **Don't re-produce what exists.** An existing brief/logo/shot set skips its
  step; consume it instead.
- **Facts stay verified.** Model ID, script paths, and CLI flags come from the
  automation reference — never from memory.

## Integration

Feeds this skill: `skills/product-strategy/foundation-sprint` (positioning and
differentiators sharpen the brief in step 1 of routes A/D). Consumes its output:
every `skills/creative/*` skill listed in the routing table — the plan tells
each one what artifact it receives and what it must hand back.
