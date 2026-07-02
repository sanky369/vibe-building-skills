---
name: direct-response-copy
description: "Write copy engineered to drive one specific action — landing pages, sales pages, opt-in pages, ads, promotional emails — using an eight-part direct-response architecture (hook, problem, mechanism, solution, proof, objections, CTA, urgency). Use when the user says 'write my landing page / sales page / ad', 'this page isn't converting', 'rewrite my homepage copy', 'write copy for my lead magnet page', or any request for persuasive copy with a measurable action at the end. Produces the full copy draft, section-labeled against the architecture, plus hook alternatives and a conversion checklist."
---

# Direct Response Copy

Write copy whose only job is to cause **one specific action** — click, signup, purchase, reply. Governing principle: **one page, one reader, one action.** Every section either moves the reader toward that action or gets cut; persuasion comes from a named mechanism and real proof, never from volume or hype.

## When to use / when not to

- Use for any asset with a conversion goal: landing/sales/opt-in pages, ads, promotional emails, upgrade prompts.
- Requires a positioning claim and a voice. If the positioning is missing or mushy, run `skills/marketing/positioning-angles` first — copy cannot rescue an undifferentiated claim. If a voice guide exists from `skills/marketing/brand-voice`, write within it; if not, sketch voice from intake and proceed.
- Multi-email automated flows → `skills/marketing/email-sequences` (it reuses this architecture per email). Content meant to rank → `skills/marketing/seo-content`. Recurring relationship email → `skills/marketing/newsletter`.

## Intake

One batch; pull answers from existing artifacts (positioning statement, voice guide, lead magnet spec) before asking:

1. What asset, and what is the ONE action a successful reader takes?
2. What's the offer, and what does it cost the reader (money, time, email address)?
3. Who is the reader, and what's the #1 reason they'd hesitate? (If unknown, name the likely objection yourself and flag it.)
4. What proof exists — testimonials, case studies, numbers, credentials, recognizable customers?
5. Any *real* deadline, capacity limit, or price change?

**Don't stall:** with an offer and audience in hand, draft with stated assumptions rather than blocking on Q3–Q5 — but never fill Q4/Q5 gaps with invented material.

## Workflow — build the eight components in order

### 1. Hook
Draft **3–5 hooks using different formulas**, present them with one-line rationales, and have the user pick (default to your top pick if they defer):

| Formula | Template |
|---|---|
| Curiosity | "The one thing [person] gets wrong about [topic]" |
| Specificity | "How I [specific result] in [specific timeframe]" |
| Benefit | "[Specific benefit] without [specific drawback]" |
| Question | "Are you [specific situation]?" |
| Bold statement | "[Controversial claim about the industry]" |

Decision rules: cold traffic → curiosity or bold; warm traffic that knows the problem → benefit or specificity; jaded market → specificity with proof baked in. A specificity hook may only use results that actually happened.

### 2. Problem validation
Show the reader you understand their situation before selling anything.
Formula: *"You're [specific situation], and it's frustrating because [specific consequence]."*
Rule: use the reader's own words (support tickets, reviews, sales calls) when available — felt understanding is what keeps them reading.

### 3. Mechanism
Explain *how* the result happens, using the named mechanism from the positioning statement.
Formula: *"Most people try [common approach]. But here's what works: [named mechanism]."*
Rule: the mechanism must be named ("The Micro-Launch Method"), never "our approach". No mechanism in the positioning → stop and get one from `skills/marketing/positioning-angles`.

### 4. Solution presentation
Present the offer as the mechanism made available — inevitable, not salesy.
Formula: *"That's why we created [offer]. It [specific benefit] by [mechanism]."*

### 5. Social proof
Deploy the strongest proof from intake Q4: testimonials → results-bearing case studies → customer counts → awards → metrics.
**Hard rule: never fabricate testimonials, customer counts, or statistics.** If proof is thin, substitute mechanism logic + a risk reversal (guarantee, free tier, no-card trial) and tell the user proof collection is their highest-leverage next task.

### 6. Objection handling
Take the #1 objection (intake Q3) plus the standard four — *no time, too expensive, tried it before, won't work for me* — and answer the 2–3 that fit this reader.
Formula: *"You might be thinking [objection]. Here's the truth: [answer]."*
Rule: answer honestly or reframe; never deny a true cost ("it does take 30 minutes a day — here's why that's the point").

### 7. Call-to-action
One action, stated identically everywhere it appears (long pages: after solution, after proof, at the end).
Formulas: simple ("Start your free trial"), benefit-focused ("Get the checklist now"), curiosity ("See how it works"), low-friction ("Reply and I'll send it over").
Decision rules: high-commitment offers → low-friction or curiosity CTA; free offers → benefit-focused. Never two competing actions on one page.

### 8. Urgency
Use only urgency that is true: a real deadline, real capacity limit, real price change, or the honest cost of waiting ("every week without X costs you Y").
**Hard rule: no fake countdowns, fake scarcity, or evergreen 'closing soon'.** If nothing real exists, end on the cost of inaction and skip the section.

### Then: voice pass and pressure test
Rewrite the draft through the voice guide (or stated voice assumptions), then run the persuasion checklist: specific beats vague ("increase revenue 23%" > "increase revenue" — only with a real number); proof quantified where honest; reciprocity — the page gives value before asking; authority shown, not claimed; consistency — the argument aligns with what the reader already believes about their problem.

## Required output format

```
# [Asset type] — [Offer]
**Goal action:** [the one action] · **Reader:** [who] · **Voice:** [guide reference or stated assumption]

---
[HOOK]
...
[PROBLEM]
...
[MECHANISM]
...
[SOLUTION]
...
[PROOF]
...
[OBJECTIONS]
...
[CTA]
...
[URGENCY]
...
---

## Hook alternates
2. "..." — [formula, when to prefer it]
3. "..." — ...

## Gaps flagged
- [missing proof, unverified claims, urgency omitted because nothing real exists]

## Conversion checklist
[the quality bar below, each item marked PASS/FAIL for this draft]
```

Deliver the copy clean (section labels are for the user's review; note they're removable). For ads or short emails, compress: hook, problem/mechanism fused, CTA — same rules, fewer sections.

## Quality bar (check before delivering)

- [ ] One CTA action; every CTA instance asks for exactly the same thing.
- [ ] Hook works out of context (would stop a scroll with zero surrounding info).
- [ ] Mechanism is named; the word "approach" or "process" never stands in for it.
- [ ] Every number, testimonial, and customer count came from the user — zero invented proof.
- [ ] Urgency is real or absent — never manufactured.
- [ ] Each objection answered, not dodged; true costs acknowledged.
- [ ] Voice matches the voice guide (or stated assumption); no generic "marketing voice" drift.
- [ ] Nothing on the page could be pasted onto a competitor's site unchanged.

## Integration

- **Upstream:** `skills/marketing/positioning-angles` supplies the claim and named mechanism (the page's spine); `skills/marketing/brand-voice` supplies the voice guide; `skills/marketing/lead-magnet` supplies the offer spec when the page sells a magnet.
- **Downstream:** `skills/marketing/email-sequences` reuses the page's hook/mechanism/objection answers across its emails; `skills/marketing/content-atomizer` can atomize a strong sales page into ad variants and social posts. What crosses the boundary is the finished copy plus the flagged-gaps list.
