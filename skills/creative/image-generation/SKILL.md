---
name: image-generation
description: "Turns any request for an AI-generated image into precise, generation-ready prompt specs and — when automation is configured — the generated files themselves. FAL.ai remains the default provider; Atlas Cloud is an explicit opt-in. Use whenever the user asks to 'generate an image', 'make a picture of X', 'create a thumbnail / hero image / illustration / infographic', 'write me a prompt for this image', or any visual that isn't specifically product photography, a social-platform graphic, or a brand mark (hand those to the sibling skills). Produces one prompt-spec block per asset plus file-naming and variant conventions, and runs docs/creative_cli.py to generate."
---

# Image Generation

Convert a fuzzy image request into prompt specs precise enough that any competent
image model — and specifically `fal-ai/nano-banana-pro` on FAL.ai, the one model
this repo's automation uses — renders what the user actually pictured. The prompt
spec is the deliverable; generated files are the bonus when the automation is
configured. **Prime rule: never generate from a vague prompt.** A weak prompt
costs a generation credit and teaches you nothing; a sharp spec is reusable
forever.

## When to use / when not to

Use for general-purpose images: hero images, illustrations, thumbnails,
infographics, textures, concept art, any one-off visual. Hand off instead when
the request is really:

- **Product shots for commerce/marketing** → `skills/creative/product-photography`
- **Platform-sized social content** → `skills/creative/social-graphics`
- **Logos, icons, patterns, brand marks** → `skills/creative/brand-asset`
- **No visual direction exists yet and consistency matters** → run
  `skills/creative/creative-strategist` first and consume its style block
- **A whole multi-asset campaign** → `skills/creative/orchestrator` routes it

## Intake

Ask in one batch, only what's missing:

1. **Subject** — what exactly is in the image? (object, scene, people, text?)
2. **Use** — where does it go? (this decides aspect ratio and resolution)
3. **Style anchor** — existing style guide / creative-strategist style block,
   reference images, or 3 adjectives for the mood?
4. **Automation** — use FAL.ai by default. Use Atlas Cloud only if the user explicitly selects it; `ATLASCLOUD_API_KEY` access is not permission to spend.

Infer, don't ask: aspect ratio from the stated destination (thumbnail → `16:9`,
story → `9:16`, feed → `1:1` or `4:5`); resolution from stakes (`2K` default,
`4K` hero/print, `1K` drafts). **Don't stall:** if subject and use are clear,
state your assumptions for the rest and proceed.

## Workflow

1. **Check for a style block.** If the user has run
   `skills/creative/creative-strategist`, reuse its style block verbatim in every
   prompt. If not, and this is a one-off, derive a minimal one (style + palette +
   mood) from context and label it an assumption.
2. **Draft the prompt with the 5-part formula.** Every prompt contains, in order:
   **subject** (the main thing, specific: "a luxury leather watch with gold
   accents", never "a watch") → **descriptive detail** (materials, colors, text
   to render) → **style** ("professional product photography", "flat modern
   illustration", "photorealistic") → **technical treatment** (lighting,
   composition, focus, "4K, highly detailed") → **mood** ("warm and inviting").
   Add negative constraints as plain prohibitions ("no text overlay", "no
   watermark", "no busy background").
3. **Decide variant strategy.** If it's a throwaway draft → 1 image at `1K`. If
   it's a keeper asset → propose 3–4 genuinely distinct prompt specs (different
   composition or style angle, not synonym swaps), generate 1 of each or
   `num_images` 3–4 of the winner, and have the user pick. Never present one
   option for a hero asset.
4. **Generate or deliver.** If `FAL_API_KEY` (or `FAL_KEY`) is set, use the default command:

   ```bash
   python docs/creative_cli.py custom \
     --category "<category>" --name "<asset-name>" \
     --prompt "<full prompt>" \
     --aspect-ratio 16:9 --resolution 2K --num-images 3
   ```

   Use `--web-search` only when the image must reflect current real-world data
   (e.g. "2026 trends infographic"). If no key is set, deliver the prompt-spec
   blocks and the exact command the user can run later — do not fake results or
   claim images were generated.

   For Atlas Cloud, first run the same command with `--provider atlas` before the subcommand and without `--confirm-submit`. This performs read-only live catalog/schema validation and reports the current quote without generating. After the user approves that quote and final payload, rerun with `--confirm-submit`. Atlas sends one image per submission and never retries the generation POST.
5. **Review and iterate.** Compare output to the spec's mood/style/negative
   constraints. Fix misses by editing the prompt (more specific subject, explicit
   lighting, stronger prohibitions) — there are no other model knobs. One
   iteration round maximum before checking in with the user.

Read `references/automation.md` before writing any generation command — it has
the full, verified parameter set, CLI flags, Python helpers, and output layout.

## Required output format

Deliver one block per asset (this exact structure, whether or not you generate):

```
## Prompt Spec — [asset name]
- **Use / destination:** [where it will live]
- **Subject:** [the main thing, concretely]
- **Style:** [artistic treatment]
- **Composition:** [framing — centered / rule of thirds / negative space / overhead]
- **Lighting:** [studio / natural golden hour / dramatic rim / high-key]
- **Mood:** [2–3 adjectives]
- **Aspect ratio:** [one of 21:9 16:9 3:2 4:3 5:4 1:1 4:5 3:4 2:3 9:16] · **Resolution:** [1K/2K/4K] · **Format:** [png/jpeg/webp]
- **Negative constraints:** [what must NOT appear]
- **Prompt (final, paste-ready):**
  > [single flowing prompt assembled from the fields above]
- **Variants:** [n] — [what varies between them]
- **File naming:** assets/<category>/<asset-name>/<asset_name>_<n>_<timestamp>.png (automation default)
- **Generate with:** `python docs/creative_cli.py custom --category ... --name ... --prompt "..." --aspect-ratio ... --resolution ... --num-images n`
```

If images were generated, append the saved paths under **Results** and say which
variant you recommend and why (one line).

## Quality bar

Before delivering, verify every spec:

- [ ] Subject is concrete enough that two strangers would picture the same image
- [ ] Style, lighting, composition, and mood are each explicitly stated — none left to model default
- [ ] Aspect ratio matches the stated destination (no `1:1` "because default")
- [ ] Negative constraints listed (at minimum: no watermark; state text policy explicitly — models mangle long text)
- [ ] No invented parameters — only the ones in `references/automation.md`; FAL.ai is the default, and Atlas Cloud is used only after explicit selection and quote confirmation
- [ ] Keeper assets got 3+ distinct variants, not one take
- [ ] If automation wasn't run, the deliverable says so and includes runnable commands

Hard don'ts: never claim an image was generated when it wasn't; never put brand
color hex codes in quotes and hope — name the colors in words too ("deep navy
#004E89"); never render paragraphs of text inside an image.

## Integration

- `skills/creative/creative-strategist` → feeds this skill its **style block**
  (paste into every prompt's style/mood/lighting fields).
- `skills/creative/product-photography`, `skills/creative/social-graphics`,
  `skills/creative/brand-asset` → specialized front-ends that produce their own
  prompt specs and use the same automation; route there when the request fits.
- `skills/creative/product-video` and `skills/creative/remotion-script-writer` →
  consume generated stills as source frames / assets.
- `references/automation.md` — full FAL.ai client, CLI, and Python-helper
  reference. Read it whenever you're about to run a generation command.
