---
name: brand-voice
description: "Define a brand's voice and produce a working voice guide: a personality archetype, settings on eight voice dimensions, do/don't rules, word choices, a tone matrix by context, and before/after rewrites of the user's real content. Use when the user says 'define my brand voice', 'what should our tone be', 'make this sound like us', 'our content sounds generic/inconsistent', 'write tone-of-voice or brand guidelines', or before producing copy at scale across channels. Also use in audit mode when existing content needs to be checked against a voice. Produces a Voice Guide document that other skills consume when writing any copy."
---

# Brand Voice

Produce a **voice guide**: a compact, enforceable document that makes every future piece of copy sound like the same brand, whoever (or whatever) writes it. Voice is *how* the brand sounds; positioning is *what* it claims — keep them separate. The governing principle: **a voice guide is only real if it changes sentences.** Every rule in it must be concrete enough that you can point at a line of copy and say pass or fail.

## When to use / when not to

- Use before writing copy at scale, when content across channels sounds inconsistent, or when the user asks for tone/voice/brand guidelines.
- If the user's actual problem is *what to say* — differentiation, the core claim — use `skills/marketing/positioning-angles` first; voice without positioning is a costume on an empty claim.
- If the user wants one specific page written, use `skills/marketing/direct-response-copy` (it consumes the voice guide; a lightweight voice sketch from its own intake is acceptable if no guide exists).
- **Audit mode:** if a voice guide already exists and the user says "our content drifted", skip to Step 6 and score existing content against the guide.

## Intake

Ask in one batch, only for what's missing from context:

1. What do you sell and to whom? (If a positioning statement exists from `skills/marketing/positioning-angles`, use it — don't re-ask.)
2. Paste 2–3 samples of your current writing (site copy, emails, posts) — or share a URL.
3. Name 2–3 brands or writers whose voice you admire, and one you never want to sound like.
4. Any words your brand insists on or bans?

**Don't stall:** if samples or a site exist, infer answers 3–4 from them, state your inferences as assumptions, and proceed.

## Workflow

### 1. Extract the current voice (if any content exists)
Before prescribing, describe. Read the samples and write a 3-line diagnosis: what the voice currently is, where it's inconsistent, what's distinctive worth keeping. Skip only for pre-launch brands with no content.

### 2. Propose an archetype — user decides
Propose the **top 2–3** archetype candidates with a one-line case for each; have the user pick one. Never present all ten as a menu.

| Archetype | Character | Example brand |
|---|---|---|
| Sage | Analytical, knowledgeable, truth-seeking | TED |
| Hero | Courageous, bold, inspiring | Nike |
| Lover | Passionate, emotional, intimate | Tiffany & Co. |
| Creator | Innovative, imaginative, expressive | Apple |
| Innocent | Optimistic, cheerful, simple | Coca-Cola |
| Everyman | Relatable, friendly, down-to-earth | Target |
| Caregiver | Compassionate, supportive, helpful | Dove |
| Ruler | Authoritative, commanding, organized | IBM |
| Magician | Transformative, mysterious, powerful | Tesla |
| Outlaw | Rebellious, disruptive, provocative | Red Bull |

Decision rules for shortlisting: trust-critical B2B or expertise-led → Sage or Ruler; challenger attacking an incumbent category → Outlaw or Magician; care/health/support products → Caregiver or Innocent; consumer brands built on relatability → Everyman; premium/design-led → Creator or Lover; performance and ambition → Hero. The archetype must match what the brand can *sustain*, not what sounds coolest.

### 3. Set the eight voice dimensions
Place the brand on each spectrum (1–5) with a one-line justification tied to the audience or positioning:

| Dimension | 1 ←→ 5 |
|---|---|
| Formality | Formal ↔ Casual |
| Optimism | Sober ↔ Optimistic |
| Humor | Serious ↔ Humorous |
| Confidence | Hedged ↔ Confident |
| Sophistication | Simple ↔ Complex |
| Warmth | Cold ↔ Warm |
| Energy | Calm ↔ Energetic |
| Directness | Indirect ↔ Direct |

**Rule: push 2–3 dimensions to an extreme (1 or 5); leave the rest moderate.** All-moderate settings produce a generic voice; all-extreme settings produce a caricature. The extremes are where distinctiveness lives — choose the ones the competition can't or won't match.

### 4. Write the enforcement rules
- **Do's / Don'ts** — 5 each, all testable against a sentence ("Do open with the reader's problem, not our product"; not "Do be authentic").
- **Word choices** — words/phrases the brand uses, and banned words (including the category's clichés).
- **Sentence structure** — length tendency, active/passive, contractions, punctuation habits (em-dashes, exclamation marks), person (we/you/I).

### 5. Build the tone matrix
Voice is constant; tone flexes by context. For each context, state which dimensions shift and by how much — never the archetype:

Educational content · Sales/promotional · Customer support · Social media · Crisis communication

Example rule format: "Support: Warmth 4→5, Humor 3→1, everything else unchanged."

### 6. Prove it with rewrites
Take 3 real passages from the user's content (or draft realistic ones if pre-launch) and show **before → after** in the new voice, each with one line naming which rules drove the change. This is the acceptance test: if the rewrite isn't visibly different and better, the guide's rules are too vague — tighten them and redo.

## Required output format

```
# Voice Guide — [Brand]

**Archetype:** [name] — [one-line why]
**Voice in one sentence:** [e.g., "A sharp, warm expert who talks like a person, not a deck."]

## Dimensions
| Dimension | Setting (1–5) | Why |
|---|---|---|
| Formality | ... | ... |
(all eight; mark the 2–3 extremes in bold)

## Rules
**Do:** 1–5 (testable)
**Don't:** 1–5 (testable)
**Say:** [preferred words/phrases] · **Never say:** [banned words]
**Sentences:** [structure rules]

## Tone matrix
| Context | Dimension shifts | Note |
|---|---|---|
| Educational | ... | ... |
| Sales | ... | ... |
| Support | ... | ... |
| Social | ... | ... |
| Crisis | ... | ... |

## Before / After
1. Before: "..." → After: "..." — [rule applied]
2. ...
3. ...
```

In audit mode, append: a scorecard of sampled content (pass/fail per rule) and the top 3 drift patterns to fix.

## Quality bar (check before delivering)

- [ ] 2–3 dimensions at an extreme, justified; not all-moderate, not all-extreme.
- [ ] Every do/don't is checkable against a single sentence of copy — no "be authentic"-grade rules.
- [ ] At least 3 before/after rewrites, using the user's real content when any exists.
- [ ] **Swap test:** replace the brand name with its nearest competitor's — if the guide still fits them, it's too generic; sharpen the extremes and word choices.
- [ ] Tone matrix changes dimensions only, never the archetype.
- [ ] No claims about the brand's audience invented — inferences labeled as assumptions.

## Integration

- **Upstream:** `skills/marketing/positioning-angles` supplies the positioning statement — the claim the voice must carry. `skills/marketing/orchestrator` routes here as a foundation step.
- **Downstream:** the voice guide is a required input to `skills/marketing/direct-response-copy`, `skills/marketing/seo-content`, `skills/marketing/email-sequences`, `skills/marketing/newsletter`, `skills/marketing/content-atomizer`, and `skills/marketing/tweet-writer`. What crosses the boundary is this document — paste or reference it whenever any of those skills write copy.
