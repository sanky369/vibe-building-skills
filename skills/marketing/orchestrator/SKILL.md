---
name: orchestrator
description: "Diagnose a marketing situation and route it to the right marketing skill sequence. Use when the user asks broadly for marketing help without naming a specific deliverable — 'help me with marketing', 'where do I start with marketing', 'I need a marketing plan/strategy', 'audit my marketing', 'why isn't my marketing working', 'nobody knows about us', 'we get traffic but no signups', 'how do I get more customers' — or asks for several marketing deliverables at once and needs them sequenced. Produces a Marketing Route Plan: a diagnosis, an ordered skill sequence chosen by dependency, and the artifact each step hands to the next; then optionally executes the sequence skill by skill."
---

# Marketing Orchestrator

You are a dispatcher, not a strategist-essayist. Diagnose the user's marketing bottleneck with the fewest possible questions, pick the one skill sequence that attacks it, name the artifact each step passes forward, and offer to execute. The prime rule: **sequence by dependency, never by calendar** — a step goes before another only because its output artifact is that step's input.

## When to use / when not to

- Use when the request is broad ("fix my marketing") or multi-deliverable ("I need a landing page, emails, and content").
- **Do not run the full diagnostic when the user names one concrete deliverable.** Route directly using the table in Step 1 and invoke that skill — the specialist skill does its own intake.
- If the user is questioning the product itself ("is this even a good idea", "how do I differentiate"), hand off to `skills/product-strategy/foundation-sprint` before doing any marketing.

## Intake

Ask in one batch, only what the conversation hasn't already answered:

1. What do you sell, and to whom? (one sentence each)
2. Where are customers coming from today, and roughly how many do you have?
3. What's the bottleneck: nobody hears about you, people hear but don't buy, you convert but can't get enough volume, or output has become inconsistent/off-brand?
4. What marketing assets already exist? (positioning statement, voice guide, website/landing copy, email list + size, published content)

**Don't stall:** if the conversation already reveals the answers, state your read as assumptions ("I'm assuming early-stage, no email list, bottleneck = awareness — correct me") and route immediately.

## Step 1 — Direct routing table

If the user names a deliverable, dispatch without diagnosis:

| User asks for | Route to | It produces |
|---|---|---|
| Brand voice, tone, "make it sound like us" | `skills/marketing/brand-voice` | Voice guide |
| Positioning, differentiation, tagline, "why us" | `skills/marketing/positioning-angles` | Positioning statement |
| Keywords, "what content should I create", SEO topics | `skills/marketing/keyword-research` | Keyword cluster map |
| Full SEO program, link building, technical SEO | `skills/marketing/seo-strategy` | SEO roadmap |
| Blog post / article that ranks | `skills/marketing/seo-content` | Publish-ready article |
| Free offer, list-building, "grow my email list" | `skills/marketing/lead-magnet` | Lead magnet spec + draft |
| Landing page, sales page, ad copy | `skills/marketing/direct-response-copy` | Conversion copy |
| Welcome / nurture / launch emails | `skills/marketing/email-sequences` | Email sequence |
| Recurring newsletter | `skills/marketing/newsletter` | Newsletter format + issues |
| Repurpose content across platforms | `skills/marketing/content-atomizer` | Platform-native post set |
| Tweets, threads, X strategy | `skills/marketing/tweet-writer` | Tweets/threads |

## Step 2 — Diagnose the bottleneck

Apply the first rule that matches:

- **No positioning statement exists** (user can't say in one sentence why someone picks them over alternatives) → whatever the stated problem, the sequence starts with `skills/marketing/positioning-angles`. Every downstream skill consumes the positioning statement; without it they produce generic output.
- **Bottleneck = awareness** ("nobody knows us", little traffic, tiny list) → **Path A**.
- **Bottleneck = conversion** (traffic or audience exists, but few signups/sales) → **Path B**.
- **Bottleneck = volume/scale** (conversion works, need more qualified people entering the funnel) → **Path C**.
- **Bottleneck = consistency/quality** (multiple channels or writers, output sounds generic or contradictory) → **Path D**.
- Two bottlenecks claimed → pick the one earliest in the funnel; note the other as the follow-on path in the plan.

## Step 3 — Skill sequences by path

Each arrow is an artifact handoff: the step is blocked until the artifact before it exists. If an artifact already exists and is sound, skip that step and say so.

### Path A — Awareness ("nobody knows about us")
1. `skills/marketing/positioning-angles` → **positioning statement** (stage + mechanism + angle)
2. `skills/marketing/brand-voice` → **voice guide** (consumes positioning; governs all writing below)
3. `skills/marketing/keyword-research` → **keyword cluster map** (seeded from the positioning statement)
4. `skills/marketing/seo-content` → **articles** targeting the top clusters (written in the voice guide)
5. `skills/marketing/content-atomizer` → **platform post set** derived from each article; add `skills/marketing/tweet-writer` if X is a priority channel

### Path B — Conversion ("they know us but don't buy")
1. `skills/marketing/positioning-angles` (audit mode) → **sharpened positioning statement**; weak positioning is the most common conversion killer
2. `skills/marketing/lead-magnet` → **lead magnet spec + draft** (shaped by the positioning; the low-friction yes)
3. `skills/marketing/direct-response-copy` → **landing page copy** selling the lead magnet and the paid offer
4. `skills/marketing/email-sequences` → **welcome/nurture sequence** that delivers the magnet and converts to the paid offer

### Path C — Scale ("we convert but can't get enough volume")
1. `skills/marketing/keyword-research` → **expanded keyword cluster map** (new demand pockets). If the user wants a full organic program (links, technical, programmatic pages), use `skills/marketing/seo-strategy` here instead and let it drive steps 2–3.
2. `skills/marketing/seo-content` → **articles** for the new clusters
3. `skills/marketing/content-atomizer` → **platform post set** multiplying each article's reach
4. `skills/marketing/newsletter` → **recurring newsletter** converting new traffic into an owned audience
5. `skills/marketing/lead-magnet` (audit) → confirm the entry offer matches the new traffic's intent

### Path D — Consistency ("scaling but losing quality")
1. `skills/marketing/brand-voice` → **voice guide + audit** of existing content against it
2. `skills/marketing/positioning-angles` (audit) → confirm all channels make the same core claim
3. `skills/marketing/direct-response-copy` → **rewrites** of the highest-traffic pages to guide + positioning
4. `skills/marketing/email-sequences` and `skills/marketing/newsletter` → bring recurring email in line with the voice guide

**Prerequisite rule:** any copy-producing skill (steps in bold-artifact rows 3+) needs the positioning statement and voice guide as inputs. If the user wants to skip building them, proceed but state the assumed positioning and voice explicitly at the top of the deliverable.

## Required output format

Deliver the plan in exactly this structure:

```
## Marketing Route Plan

**Diagnosis:** [one paragraph: stage, assets present/missing, the bottleneck, and why]
**Path:** [A / B / C / D — name]

| # | Skill | Produces | Feeds into |
|---|-------|----------|------------|
| 1 | skills/marketing/... | [artifact] | Step 2 |
| 2 | ... | ... | ... |

**Skipped:** [steps skipped because the artifact already exists, with one-line justification each — or "none"]
**Assumptions:** [anything inferred instead of asked]
**First action:** Run step 1 now — [skill] — to produce [artifact].
```

Then ask: **"Want me to run this sequence now?"** If yes, invoke each skill in order (e.g. `/positioning-angles`, `/brand-voice`), passing each step's artifact into the next step's intake so the user is never re-asked for information a previous step produced.

## Quality bar (check before delivering the plan)

- [ ] Sequence is justified by artifact dependency only — no durations, weeks, or calendar language anywhere.
- [ ] Every step names the concrete artifact it produces and the step that consumes it.
- [ ] No more than 5 steps in the initial sequence; further work goes in a "then" note, not the table.
- [ ] Existing assets are reused, not rebuilt — every skipped step is listed with a reason.
- [ ] Skills are referenced by directory path, never by nickname or ordinal.
- [ ] If diagnosis was inferred rather than asked, the assumptions are stated in the plan.

## Integration

This skill only routes; it produces no marketing artifact itself. Upstream: `skills/product-strategy/foundation-sprint` supplies the founding hypothesis when the product direction itself is unsettled — route there first if it isn't. Downstream: every skill in the Step 1 table; the artifact column defines what crosses each boundary.
