---
name: original-design
description: "Facilitates an interactive session that turns a product or subject into an original, internally consistent visual design language for any artifact — infographics, video storyboards, websites, or mobile app UI/UX. Use when the user wants an original design language, identity, or art direction, or when a design feels generic, derivative, 'AI-default,' or inconsistent and needs one unifying idea. Triggers on 'design language', 'art direction', 'make it original', 'visual identity', 'looks generic', 'design a world'. Produces a completed Design Language Brief (core metaphor, visual vocabulary, design DNA, signature constraint, Originality Test verdicts) saved to the project and handed off to the production skill for the chosen medium."
---

# Original Design

Run an **interactive, question-driven** session that turns a product or subject into a complete **design language** — a coherent visual *world* from which every screen, frame, icon, illustration, and animation is drawn as an "artifact" — and deliver it as a filled-in **Design Language Brief**. It works for any visual deliverable: an infographic, a video storyboard, a website, or a mobile app UI/UX. The governing principle: **originality is not about being unique — it is about being internally consistent around one core idea.** Don't ask "how do I make this look unique?"; ask "what is the visual manifestation of the core idea?" The biggest shift this skill enforces: **don't design screens — design a world.** Everything else is an element of that world.

## When to use / when not to

- Use when the user needs an original visual identity or art direction, or an existing design reads generic/AI-default and needs one unifying idea.
- If the user needs a practical brand *style guide* (palette, fonts, mood for asset generation) rather than an original world → `skills/creative/creative-strategist`; this skill's brief can feed that one.
- If the design language already exists and the user just needs assets → go straight to the production skill for the medium (see Phase 9).
- If the problem is UI structure/usability rather than visual identity → `skills/frontend-design/frontend-orchestrator`.

## How to run this skill (read first)

This is a **facilitated conversation, not a form dump.** Follow these rules:

1. **One phase at a time.** Ask the focused question(s) for the current phase, *wait for the answer*, reflect it back in one or two sentences, then move on. Never paste all seven phases at once.
2. **Always offer a recommendation.** For every question, propose 2–4 concrete options (with a "(recommended)" first) so the user can react instead of inventing from scratch. They can always answer freely.
3. **Use structured questions when the host supports them.** In Claude Code, prefer the `AskUserQuestion` tool for option-based phases. In other agents, ask in plain text with a short labeled option list.
4. **Gather live visual inspiration from the web** at Phase 1.5 and Phase 6 (see [references/inspiration-browsing.md](references/inspiration-browsing.md)). Pick the browsing method that matches the host agent.
5. **Capture decisions as you go** into a running Design Language Brief (template at [assets/design-language-brief-template.md](assets/design-language-brief-template.md)).
6. **Gate on the Originality Test** before producing final output. Don't skip it.
7. **Hand off to a production skill** for the chosen medium (see [references/medium-playbooks.md](references/medium-playbooks.md)).

Copy this checklist into your working notes and check items off:

```
Design Language Progress:
- [ ] Phase 0: Frame the world (medium, subject, audience)
- [ ] Phase 1: Core metaphor (one sentence)
- [ ] Phase 1.5: Inspiration sweep (web)
- [ ] Phase 2: Visual universe (vocabulary)
- [ ] Phase 3: Design DNA (shapes / colors / motion / texture)
- [ ] Phase 4: Mascot system (if applicable)
- [ ] Phase 5: The signature constraint
- [ ] Phase 6: Cross-domain inspiration (web)
- [ ] Phase 7: Generate many concepts → pick the world
- [ ] Phase 8: Originality Test (5 questions) — GATE
- [ ] Phase 9: Write the brief + medium handoff
```

---

## Phase 0 — Frame the world

Establish what you're actually making before anything visual. Ask:

- **What are we creating?** → infographic · video storyboard · website · mobile app UI/UX · other
- **What is the product/subject, in one line?**
- **Who is it for, and what should they *feel*?**

Then say the mindset shift out loud to the user: *"We're not going to design screens. We're going to design a world, and your "+ medium +" will be made of artifacts from that world."*

**Don't stall:** if the request already answers these (e.g. "an original look for my kids' math app"), reflect the answers back as assumptions in one line and move straight to Phase 1 — the interactive rule applies to the *design* questions, not to re-asking what the user already said.

## Phase 1 — Define the core metaphor

> Everything flows from the core metaphor.

Ask the unlocking question: **"If this product were a physical object or place, what would it be?"**

Offer seeds based on the domain (these are from the source method):

| Product type | Possible metaphor |
|---|---|
| Math / learning app | Toy Blocks |
| AI tutor / assistant | Wise Mentor |
| Finance / trading app | Command Center |
| Travel app | Explorer's Journal |
| Knowledge / docs app | Living Library |

Push for **one** metaphor, not three. Then write the **one-sentence design language**:
*"This is a [metaphor] — so it looks like [feeling/world]."*

If they can't say it in one sentence, the metaphor isn't sharp enough yet — keep refining.

## Phase 1.5 — Inspiration sweep (web)

Before defining vocabulary, gather real references for the chosen metaphor and mood. Follow [references/inspiration-browsing.md](references/inspiration-browsing.md): browse cosmos.so, Pinterest, Savee, Dribbble, Behance, Are.na for the metaphor + mood, collect 8–15 references, and note recurring patterns (lighting, color temperature, composition, texture, shapes). Summarize the patterns back to the user before continuing.

## Phase 2 — Build a visual universe

> List everything that exists in that world. Those become your visual vocabulary.

With the metaphor fixed, brainstorm *with the user* every object, surface, character, and texture that lives in that world. Example for **Living Library**: Books, Shelves, Notes, Ink, Stamps, Bookmarks, Paper texture.

Then explicitly map the vocabulary onto the design layers:

| World object | Becomes |
|---|---|
| (e.g. Books, Stamps) | Icons |
| (e.g. Margin sketches) | Illustrations |
| (e.g. Page turn, ink bleed) | Animations / motion |
| (e.g. Shelves, cards) | UI elements / layout |
| (e.g. Ink, paper, leather) | Colors |
| (e.g. Hand-lettered headers) | Typography |

Aim for a vocabulary of 6–10 concrete elements. This list is the source of truth for everything later.

## Phase 3 — Create your design DNA

> Define the system rules everything will follow.

Lock four dimensions. Keep each tight — constraints here are what make it feel designed:

- **Shapes** — 2–3 shape families (e.g. rounded rectangles, circles, cubes)
- **Colors** — 3–5 core colors with names tied to the world (e.g. Deep Navy, Electric Blue, Warm Yellow, Soft Gray)
- **Motion** — *one* philosophy in a phrase (e.g. "springy & playful, with purpose")
- **Texture** — *one* language (e.g. "paper, hand-drawn, sketch-like")

Record exact hex values for colors and concrete easing/timing intent for motion so the brief is build-ready.

## Phase 4 — Design a mascot system (when it fits)

> A mascot gives your product a face and personality, and becomes the heart of the world.

Ask whether a mascot serves this project. It's powerful for learning, consumer, kids', and brand-led products; often skipped for enterprise/finance or minimalist tools. If yes, define:

- **Who/what it is** (e.g. Curious Robot, Wise Fox, Tiny Scientist, Living Constellation)
- **Personality** in 3 adjectives
- **How it shows up** across the medium (empty states, loading, onboarding, narrator in a video, guide in an infographic)

Why it matters: emotional connection, memorability, and it unifies the whole experience.

## Phase 5 — Create the signature constraint

> Constraints don't limit creativity. They create identity.

Define **one** rule the design will never break. This single decision is often what makes a language recognizable:

| Constraint | Resulting style |
|---|---|
| No photos allowed | clean, illustrated (Zenn-like) |
| Everything is geometric blocks | structured (math-app-like) |
| Only black, white + one accent | sharp, linear (Linear-like) |
| Every illustration must look hand-drawn | warm, human (Excalidraw-like) |

Write the constraint as an enforceable sentence: *"In this world, we never ___ / we always ___."*

## Phase 6 — Get inspired from unrelated domains (web)

> Don't copy competitors. Borrow from other worlds.

Pull inspiration from domains *outside* the product's category to stay fresh: Architecture, Nature, Toys, Ancient manuscripts, Science diagrams, Space missions, Industrial machinery. Use [references/inspiration-browsing.md](references/inspiration-browsing.md) to browse 2–3 unrelated domains and extract transferable ideas (a grid system from architecture, a color story from nature, a labeling style from science diagrams). Bring back 3–5 concrete "steals."

## Phase 7 — Generate many concepts, then pick the world

> One core idea. Many worlds. Quantity creates the chance for brilliance.

Generate a **large batch of short concept directions** — each a different "world" expressing the *same* core idea (e.g. Museum, Spaceship, Magical Academy, Detective Board, Living Brain… aim for 20–50 one-line concepts). Most will be average; you're hunting for the one that's extraordinary.

Present them grouped, let the user react, then **narrow to 1 primary direction** (optionally 1–2 backups). For a big batch, you may dispatch a subagent or workflow to expand concepts, but keep the user in the selection loop.

## Phase 8 — The Originality Test (GATE)

Before producing anything, run all five questions. **Every answer should be "yes."** If any is "no," return to the relevant phase.

1. **Can I explain the visual language in one sentence?** (→ Phase 1)
2. **Does every element come from the same metaphor?** (→ Phase 2)
3. **Can I remove the logo and still identify the product?** (→ Phase 3/5)
4. **Would a child draw the same design language?** (is it simple and clear? → Phase 3)
5. **Does it look like a *world* rather than a UI?** (→ overall)

State each question and its verdict back to the user explicitly.

## Phase 9 — Write the brief and hand off

Fill in [assets/design-language-brief-template.md](assets/design-language-brief-template.md) with every locked decision and save it to the user's project (suggest `design-language.md`). Then translate the language into the chosen medium using [references/medium-playbooks.md](references/medium-playbooks.md) (read it at this phase for the per-medium translation tables), and offer to invoke the matching production skill:

- **Infographic / social graphic** → `skills/creative/social-graphics`, `skills/creative/image-generation`, or `skills/creative/brand-asset`
- **Video storyboard** → `skills/creative/remotion-script-writer`, `skills/creative/product-video`, or `skills/creative/creative-strategist`
- **Website** → `skills/frontend-design/frontend-orchestrator`, `skills/frontend-design/design-foundation`, `skills/frontend-design/color-system`, `skills/frontend-design/typography-system`
- **Mobile app UI/UX** → `skills/frontend-design/frontend-orchestrator`, `skills/frontend-design/component-architecture`, `skills/frontend-design/layout-system`

The brief is the contract: every downstream asset must be an artifact of the world it describes.

## Required output format

The deliverable is the completed brief — always the exact structure of [assets/design-language-brief-template.md](assets/design-language-brief-template.md), every section filled, none skipped:

```markdown
# Design Language Brief — [Product / Subject]
## 1. Core metaphor            (the one-sentence design language)
## 2. Visual universe          (6–10 vocabulary elements mapped to icons/illustrations/motion/UI/colors/type)
## 3. Design DNA               (shapes · colors with hex · one motion philosophy · one texture language)
## 4. Mascot system            (who/personality/where it appears — or "none" with reason)
## 5. Signature constraint     ("In this world, we never ___ / we always ___")
## 6. Cross-domain inspiration (3–5 concrete steals with sources)
## 7. Chosen direction         (the winning world + 1–2 backups)
## 8. Originality Test         (all five questions with explicit YES verdicts)
## 9. Production notes         (medium handoff: which skill, what it must obey)
```

Two sessions run on the same product must produce briefs with these same nine sections in this order; only the creative content differs.

## Common mistakes

| Mistake | Fix |
|---|---|
| Dumping all 7 phases as one questionnaire | One phase at a time; reflect each answer back |
| Picking 3 metaphors "to be safe" | Force exactly one — mixed metaphors kill consistency |
| Skipping the web inspiration sweep | Real references prevent generic, AI-default output |
| No signature constraint | Without a constraint there's no identity (Phase 5 is not optional) |
| Designing screens/frames before the world | Define the world first; artifacts come last |
| Shipping without the Originality Test | The 5-question gate is mandatory |

## Integration

- `skills/creative/creative-strategist` → consumes: the brief's Design DNA (colors, texture, motion) as raw material for a practical asset-generation style guide.
- `skills/creative/social-graphics`, `skills/creative/image-generation`, `skills/creative/brand-asset` → consume: the brief; every generated asset must be an artifact of the world (repo image pipeline: `docs/creative_cli.py`, model `fal-ai/nano-banana-pro`).
- `skills/creative/product-video`, `skills/creative/talking-head`, `skills/creative/remotion-script-writer` → consume: the brief as the visual world their beats, settings, and scenes are drawn from.
- `skills/frontend-design/frontend-orchestrator` → consumes: the brief as the identity layer over its design-system skills (`design-foundation`, `color-system`, `typography-system`, `layout-system`, `component-architecture`).

## The bottom line

**Design a world. Everything else is just an element of that world.** Every screen, thumbnail, image, icon, and animation should feel like an artifact from the same universe.
