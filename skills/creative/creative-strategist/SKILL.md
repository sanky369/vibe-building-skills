---
name: creative-strategist
description: "Establishes a brand's visual direction and compresses it into a Creative Direction Brief with a paste-ready 'style block' that every downstream image prompt reuses, so all generated assets look like they came from one brand. Use when the user says 'define my brand style', 'I want a consistent look', 'what should my visuals look like', 'help me pick an aesthetic / mood / color palette', 'my generated images all look different', or before any multi-asset creative work where no style guide exists yet. Produces the Creative Direction Brief: aesthetic profile, palette with hex codes, style block for prompts, and prohibitions."
---

# Creative Strategist

Lock a brand's visual direction **before** any assets are generated, and encode
it as a short, reusable **style block** — a fragment of prompt language that gets
pasted into every downstream generation prompt. **Prime rule: consistency beats
beauty.** Ten assets in one coherent style build a brand; ten gorgeous assets in
ten styles build noise. The brief exists so that image prompts written weeks
apart still produce siblings.

## When to use / when not to

Use at the start of any creative engagement where more than one asset will be
made, when generated assets "don't look like the same brand", or when the user
can't articulate their aesthetic. Hand off instead when:

- The direction already exists (a real style guide or a prior brief) → go
  straight to `skills/creative/image-generation` or the specialist skills.
- The user needs the actual assets, not direction → after this brief, route via
  `skills/creative/orchestrator` or the specific asset skill.
- The question is product strategy ("who is this for?"), not visuals →
  `skills/product-strategy/foundation-sprint` first; its customer/differentiators
  feed this brief.

## Intake

Ask in one batch, only what's missing:

1. **Brand & offer** — what is the product/company, in a sentence?
2. **Audience** — who must these visuals appeal to?
3. **Existing constraints** — logo, colors, fonts, or reference images already in
   use? (Ask for hex codes or links if they exist.)
4. **Mood in 3 adjectives** — how should someone *feel* seeing the brand?
5. **Anti-examples** — any brand or style they hate?

Infer, don't ask: industry conventions (fintech skews trustworthy/clean, D2C
lifestyle skews warm/photographic); primary destinations from context (an
e-commerce user needs product-photo direction more than illustration direction).
**Don't stall:** with brand + audience known, propose the rest as labeled
assumptions and proceed.

## Workflow

1. **Diagnose the aesthetic space.** From intake, place the brand on the core
   spectrums: photorealistic ↔ illustrative, minimal ↔ maximal, warm ↔ cool,
   playful ↔ serious, mass ↔ premium. Note where competitors sit — matching them
   is a choice, not a default; flag one deliberate point of visual contrast.
2. **Propose 3 distinct direction candidates.** Each gets a name, a one-line
   vibe, a 3–5 color palette (with hex codes), lighting + composition defaults,
   and one sentence on why it fits the audience. Make them genuinely different
   directions (e.g. "Warm Editorial" vs "Clinical Minimal" vs "Bold Flat
   Illustration"), not shades of one idea. **The user picks one**; you may
   recommend, with a one-line reason.
3. **Lock the aesthetic profile.** Fill every field of the profile in the output
   format below. No field may read "flexible" or "depends" — a value the user can
   overrule later beats a blank.
4. **Write the style block.** Compress the profile into 1–3 lines of literal
   prompt language, e.g.:
   `photorealistic, warm golden-hour lighting, rule-of-thirds composition, warm gold (#C9A227) and cream (#F5EFE0) palette, approachable premium mood, highly detailed, professional photography`
   Test it mentally against three different asset types (product shot, social
   graphic, illustration) — if it only works for one, generalize the wording and
   move medium-specific details into the per-medium adaptations.
5. **Set prohibitions and consistency rules.** 3–7 concrete "never" rules
   (e.g. "never neon colors", "no stock-photo handshake clichés", "no more than
   two typefaces") and the rule for when secondary style variants may be used.
6. **(Optional) Validate with a test generation.** If `FAL_API_KEY` is set,
   generate one probe image per finalist direction so the user picks from pixels,
   not adjectives:
   `python docs/creative_cli.py custom --category style-tests --name <direction-slug> --prompt "<representative subject>, <style block>" --resolution 1K`
   (Full automation reference:
   `skills/creative/image-generation/references/automation.md`.)

## Required output format

Deliver exactly this brief (markdown, concise):

```
# Creative Direction Brief — [brand]

## Chosen direction: [name] (rejected: [alt 1], [alt 2] — one-line why)

## Aesthetic profile
| Field | Value |
| Primary style | photorealistic / illustrative / minimal / abstract / mixed: ... |
| Color palette | [name #hex] x 3–5, with roles (primary / secondary / accent) |
| Mood | [3 adjectives] |
| Lighting default | [e.g. soft studio, natural golden hour, dramatic rim] |
| Composition default | [e.g. centered + negative space, rule of thirds] |
| Detail level | minimal / moderate / high |
| Audience | [who this must appeal to] |
| Deliberate contrast | [the one way we look different from the category] |

## Style block (paste into every image prompt)
> [1–3 lines of literal prompt language]

## Per-medium adaptations
- Product photography: [what changes — background, lighting]
- Social graphics: [what changes — contrast, text space]
- Brand assets / illustration: [what changes — flatness, line weight]

## Prohibitions
1. Never ...
2. Never ...

## Consistency rule
Every prompt for this brand includes the style block verbatim; deviations are
proposed to the user first, never improvised.
```

## Quality bar

- [ ] User chose from 3 genuinely distinct directions (or explicitly skipped the choice)
- [ ] Every palette color has a hex code and a role
- [ ] Style block is literal prompt language — paste-ready, no meta-instructions like "use brand colors"
- [ ] Style block works for at least three asset types via the per-medium adaptations
- [ ] Prohibitions are concrete and checkable, not "avoid bad design"
- [ ] No invented market claims about what "converts better" — label taste as taste, heuristics as heuristics

Hard don'ts: never deliver a brief with TBD fields; never let the user pick "all
three directions"; never restyle mid-project without updating this brief first.

## Integration

- `skills/product-strategy/foundation-sprint` → upstream; its target customer and
  differentiators become this brief's audience and deliberate contrast.
- `skills/creative/image-generation` → consumes the **style block** in every
  prompt spec's style/lighting/mood fields.
- `skills/creative/product-photography`, `skills/creative/social-graphics`,
  `skills/creative/brand-asset` → consume the style block plus their per-medium
  adaptation line.
- `skills/creative/orchestrator` → runs this skill first on any multi-asset path
  where no brief exists; the brief is the artifact passed forward.
