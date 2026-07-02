---
name: remotion-script-writer
description: "Write a complete, render-ready Remotion video script as structured JSON: analyze the user's codebase or product, break the video into timed scenes, specify every visual element, animation, transition, and voiceover line, and list required assets and Remotion packages. Use whenever the user wants a Remotion video, a programmatic/code-rendered video, a product demo video of their app, an animated coding tutorial, a data-visualization video, or short-form animated social content — trigger on 'make a video of my app', 'Remotion', 'animated demo', 'code walkthrough video', 'render a video from code'. Produces a Remotion Script JSON (videoMetadata, scenes[], requiredAssets, technicalRequirements) that Remotion agent tooling can implement directly."
---

# Remotion Script Writer

Turn a video goal plus (optionally) a codebase into a **Remotion Script JSON** — a scene-by-scene specification precise enough that a Remotion agent can implement it without asking follow-up questions. The governing principle: **the script is the single source of truth for the render** — every duration, element, animation, and voiceover line is stated in numbers and exact strings, never "about 5 seconds" or "some intro text". Two agents given the same input must emit structurally identical scripts.

## When to use / when not to

- Use when the output will be rendered programmatically with Remotion: product demos of web apps, coding tutorials with animated code, motion-graphics pieces, data-visualization videos, short-form social animations.
- Concept and beats not yet decided for a product video → run `skills/creative/product-video` first; its beat sheet becomes this skill's scene list.
- Person-on-camera video → `skills/creative/talking-head` (Remotion is not the tool).
- Static graphics → `skills/creative/social-graphics`.
- This skill writes the script only — implementing the React components, previewing in Remotion Studio, and rendering are done by Remotion's own agent skills downstream.

## Rules files — read before writing the script

- `rules/prompt-structure.md` — the input fields the script is built from (goal, targetAudience, code, videoType, duration, style, animations, transitions). Read it when normalizing intake into the input object.
- `rules/script-generation.md` — the authoritative output JSON structure and generation instructions. Read it before emitting the script; the skeleton below is a summary, that file is the contract.
- `rules/animation-patterns.md` — the approved animation/transition vocabulary with exact JSON shapes and timing guidelines. Read it when specifying any `animation` or `transitionToNextScene` value; do not invent animation types outside it.
- `rules/scene-templates.md` — ready-made scene JSON for common cases (title card, feature showcase, code walkthrough, data viz, outro/CTA). Read it when a scene matches a known pattern; start from the template and edit.
- `examples/product-demo-example.json` — a complete worked script. Read it for calibration on granularity.

## Intake

Ask in one tight batch, only what's missing (field names per `rules/prompt-structure.md`):

1. **goal** and **targetAudience** — what should the video achieve, for whom?
2. **videoType** — `product-demo` | `coding-tutorial` | `animation` | `data-visualization` | `social-media`?
3. **duration** (seconds) and destination platform (decides width/height/fps).
4. **code** — path to the codebase, repo URL, or snippets, if the video features an app or code.
5. **style** — visual/branding constraints (colors, fonts, logo; a `skills/creative/creative-strategist` style guide if one exists).

Infer instead of asking: `language` from the codebase; dimensions from platform (1920×1080 landscape default, 1080×1920 for vertical social, fps 30); animation/transition preferences from `style` if not given. **Don't stall:** with goal + videoType + duration known, state assumptions and proceed.

## Workflow

### 1. Analyze the source material

If `code` is provided, explore it: identify the key features, user flows, data structures, and UI surfaces worth showing. Rank features by relevance to `goal` — the video shows the top 3–5, not everything. If no code, extract the equivalent list from the user's description.

### 2. Structure the scenes

Decision rules by `videoType`:
- **product-demo** → title card → problem/context → one scene per feature (top 3–5) → outro/CTA.
- **coding-tutorial** → title → concept setup → one scene per code step (show code, then explain) → recap.
- **data-visualization** → title → context → one scene per chart/insight → takeaway.
- **social-media** → hook scene (≤3s) → 1–2 payoff scenes → CTA; total ≤60s.
- **animation** → derive beats from the creative concept (or the `skills/creative/product-video` beat sheet).

Timing math is mandatory: scene durations plus transition overlaps must sum exactly to `duration`. `TransitionSeries` transitions overlap adjacent scenes — account for the overlap, don't just add durations. Keep total under ~5 minutes (render performance heuristic).

### 3. Specify each scene completely

For every scene fill every field: `sceneNumber`, `title`, `durationInSeconds`, `visuals.background`, `visuals.elements[]` (type, exact content string, font, size, color, position, `animation` from `rules/animation-patterns.md`), `audio.voiceover` (the exact sentence(s) spoken — verify they fit the scene duration at ~2.5 words/second), and `transitionToNextScene`. Use `rules/scene-templates.md` templates where they match.

### 4. Compile assets and technical requirements

List every image, video clip, audio track, font, and logo referenced by any scene in `requiredAssets` — nothing referenced may be missing from the list. Asset generation is out of scope: mark each as user-provided or describe it precisely; still images can be produced via `skills/creative/image-generation` (repo pipeline: `docs/creative_cli.py`, model `fal-ai/nano-banana-pro`). List `remotionPackages` (e.g. `@remotion/transitions` whenever transitions are used) and any third-party libraries.

### 5. Validate against the quality bar, then deliver the JSON

Deliver the script plus the handoff note (below). The downstream Remotion agent generates components, sets up the composition, previews in Studio, and renders.

## Required output format

Emit one JSON object exactly matching the structure in `rules/script-generation.md`:

```json
{
  "videoMetadata": {
    "title": "...", "durationInSeconds": 60,
    "width": 1920, "height": 1080, "fps": 30,
    "videoType": "product-demo"
  },
  "scenes": [
    {
      "sceneNumber": 1, "title": "...", "durationInSeconds": 5,
      "visuals": {
        "background": "#RRGGBB or asset ref",
        "elements": [
          { "type": "text|image|code|chart", "content": "exact content",
            "animation": { "type": "<from rules/animation-patterns.md>", "durationInSeconds": 1 } }
        ]
      },
      "audio": { "voiceover": "Exact spoken sentence(s)." },
      "transitionToNextScene": { "type": "<from rules/animation-patterns.md>", "durationInSeconds": 1 }
    }
  ],
  "requiredAssets": { "images": [], "videos": [], "audio": [], "fonts": [], "logos": [] },
  "technicalRequirements": { "remotionPackages": [], "thirdPartyLibraries": [] }
}
```

Follow the JSON with a short markdown handoff note: total duration check (scene math shown), the 1–3 assumptions you made, and which assets the user must supply before rendering.

## Quality bar (check before delivering)

- Scene durations + transition overlaps sum exactly to `videoMetadata.durationInSeconds`; show the arithmetic in the handoff note.
- Every `animation` and transition `type` exists in `rules/animation-patterns.md` — no invented types.
- Every voiceover line fits its scene at ~2.5 words/second; no scene has visuals with no purpose stated by the voiceover or title.
- Every asset referenced in any scene appears in `requiredAssets`; fonts used by text elements are listed.
- Remotion correctness baked into the spec: frame-based timing via `useCurrentFrame()`, springs with `damping: 200` for reveals, typewriter via string slicing (not per-character opacity), deterministic randomness only (`random()` from remotion, never `Math.random()`), `premountFor` on heavy sequences, `<Sequence>/<Series>/<TransitionSeries>` for ordering.
- `content` fields are final copy, not placeholders like "feature description here".
- Voiceover is auto-drafted — flag in the handoff note that the user may want to refine it.

## Integration

- `skills/creative/product-video` → feeds in: concept + beat sheet + keyframes for product videos; each beat becomes a scene.
- `skills/creative/creative-strategist` → feeds in: style guide (colors, fonts, mood) applied to `visuals` and `style`.
- `skills/creative/original-design` → feeds in: a design-language brief; every scene's visual vocabulary must come from that world.
- `skills/creative/image-generation` → produces: still assets listed in `requiredAssets.images`.
- `skills/creative/social-graphics` → consumes: rendered stills/thumbnails for post assets.
- Downstream: Remotion agent skills (outside this repo) consume the JSON to build components, preview, and render.
