# Foundation Sprint — Worked Examples & Calibration

Patterns to imitate. The first three are documented in *Click* / the authors' material. The Slack and Blue Bottle entries are **illustrative reconstructions** (the book shows the real versions) — use them for shape, not as quotable fact. The final section is a complete sample run in the exact output format the skill should produce.

## Documented anchors

### Gmail (reverse-engineered)
Plain-English promise from the book: *"We'll solve your overflowing inbox problems better than Outlook, Hotmail, and Yahoo because we offer more storage and great search."*

> If we help **people drowning in email** solve **an overflowing, unsearchable inbox** with **a free web-based email app**, they will choose it over **Outlook, Hotmail, and Yahoo** because our solution is **more storage + great search**.

Why it clicked: the promise is *simple* (two differentiators), the customer is everyone with email, and the differentiation was real and deliverable. People tried it, it delivered, they told friends.

### Google Meet — the good vs. bad hypothesis (the book's central illustration)
**Bad (stayed hidden for ~2 years, nearly killed the project):**
> If we help **"3D aficionados"** solve **boring meetings** with **a 3D virtual conference room + interactive docs/agendas/whiteboards**, they'll choose it over **existing tools** because our solution is **immersive and feature-rich**.

The moment you write it down, it's absurd — "3D aficionados" isn't a real target, and the promise isn't simple. **Lesson: dragging the hidden hypothesis into the spotlight exposes the flaw.**

**Good (formed under deadline in Stockholm → became Google Meet):**
> If we help **people who need to meet remotely** solve **the hassle of multi-way video calls** with **video calling that runs in the browser**, they'll choose it over **existing conferencing software** because our solution is **the fastest + easiest way to make a video call**.

Simple promise, real customer, deliverable differentiation. They built a bare prototype of exactly that — nothing more — and it spread.

### Latchit (case study in the book)
> If we help **artisans** solve **growing their online sales** with **a social sales app**, they'll choose it over **Shopify and Etsy** because our solution is **cooperative + easy to use**.

Differentiation 2x2 that drove it: X = *siloed ←→ cooperative*, Y = *hard ←→ easy*. Latchit sits alone top-right (cooperative + easy); Shopify (siloed, powerful-but-hard) and Etsy (commoditized) fall into Loserville.

## Illustrative reconstructions (shape only)

**Slack** — reconstruction: *If we help teams at work solve scattered, buried internal communication with a searchable group-chat app, they'll choose it over email and IRC because it's fun + organized (everything searchable).*

**Blue Bottle Coffee** — reconstruction: *If we help coffee lovers solve the problem of stale, mediocre coffee with freshly roasted beans and carefully made drinks, they'll choose it over Starbucks and grocery beans because it's fresher + higher craft.*

Note the recurring shape: a **specific customer**, a **painful everyday problem**, an **approach simple enough to prototype**, the **obvious incumbent** as the competitor, and **exactly two** differentiators that form a 2x2 corner you can own.

---

## Full sample run (use as the output template)

**User's idea:** "An AI tool that drafts grant applications for small nonprofits."

> Assumptions I'm making (correct me): the "small nonprofit" is a 1–5 person org with no dedicated grants staff; today they write grants by hand or hire a freelance grant writer. Proceeding on those.

## Founding Hypothesis
> If we help **tiny nonprofits with no grants staff** solve **the slow, intimidating work of writing fundable grant applications** with **an AI drafter trained on winning grants + the funder's own rubric**,
> they will choose it over **freelance grant writers and generic AI chatbots** because our solution is **funder-tailored + radically faster (first draft in an hour, not weeks)**.

## Basics
| Element | Decision | Why this one |
|---|---|---|
| Customer | Program leads at 1–5 person nonprofits | They feel the pain personally and have no grants team to delegate to. Narrower than "nonprofits." |
| Problem | Grants are slow, blank-page-intimidating, and easy to get wrong vs. each funder's rubric | Painful enough to pay for; the cost of a missed deadline is real money. |
| Advantage | *Insight:* funders score against a specific, often-public rubric most applicants ignore. *Capability:* a corpus of funded grants + rubric mapping. *Motivation:* mission fit. | Insight is the strongest leg and seeds the differentiation. |
| 800-lb gorilla | Freelance grant writers ($1–5k/grant) | Trusted and effective, but slow and expensive — beatable on speed and cost for this customer. |

(Competitors also include generic ChatGPT and "do nothing / write it themselves.")

## Differentiation 2x2
- Axes: **X = generic ←→ funder-tailored** · **Y = slow ←→ fast (time to a fundable first draft)**
- Win quadrant (top-right): **us** — funder-tailored *and* fast; an hour to a rubric-aligned draft.
- Loserville: freelance writer → *funder-tailored but slow* (top-left); generic AI chatbot → *fast but generic* (bottom-right); DIY → *slow + generic* (bottom-left).
- Principles: 1) "Score to the rubric, not to taste." 2) "An hour, not a week." 3) "Never invent facts about the nonprofit."

## Magic Lenses
Scores: **win** = lands top-right · **mid** = middling · **weak** = bottom/left.

| Approach | Customer | Pragmatic | Growth | Money | Unique-to-us | Pattern |
|---|---|---|---|---|---|---|
| A. Rubric-aware drafter (paste a call, get a tailored draft) | win | win | mid | win | win | **wins 4/5** |
| B. Full grant-management suite (search + track + draft) | mid | weak (slow to build) | mid | win | mid | strong money, heavy build |
| C. Marketplace matching nonprofits to grants | mid | weak | win | mid | weak | growthy, not differentiated |

- **Top Bet:** A — lands top-right on customer value, feasibility, money, and *uniqueness*, and directly delivers the "funder-tailored + fast" differentiation.
- **Backup:** B — if drafting alone doesn't retain users, expand into the workflow.

## Prove-it Scorecard
| Prediction | "Prove it!" test | Risk |
|---|---|---|
| Right customer? | 5 convos with 1–5 person nonprofits: do they write grants themselves and hate it? | M |
| Right problem? | Will they name "writing the draft" (not "finding grants") as the worst part? | **H** |
| Right approach? | Fake-door: "Paste a grant call, get a tailored draft" landing page — measure sign-ups | M |
| Real differentiation? | Blind-rate AI-rubric draft vs. generic AI draft with 3 real funders/reviewers | **H** |
| Does it click? | Do testers say "I'd pay for this" *and* submit the draft for a real grant? | H |

## First move
The single riskiest assumption is **that the painful part is *drafting*, not *finding* grants** — if it's discovery, approach C wins and the whole hypothesis shifts. Test it next with **5 customer conversations + a fake-door landing page**, before building anything.
