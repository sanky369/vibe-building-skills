---
name: email-sequences
description: "Write a complete automated email sequence, every email fully drafted: welcome sequence for new subscribers, ongoing nurture rotation, conversion sequence for an offer, or launch sequence for something new. Use when the user says 'write my welcome emails', 'set up a drip campaign', 'I'm launching X and need emails', 'nurture my list', 'write a sales email sequence', or connects a lead magnet to follow-up — even if they don't know which sequence type they need. Produces a sequence map (per-email purpose and send-day) plus full drafts: subject line, preview text, body, and one CTA per email."
---

# Email Sequences

Write automated email sequences — fixed sets of emails sent on a schedule after a trigger (signup, purchase, launch date) — that build trust before they ask for anything. **Prime directive: every email must be worth opening on its own, and every email must move the sequence's single job forward.** A sequence with one job (deliver, nurture, convert, or launch) outperforms one trying to do everything; an email that only exists to "stay in touch" gets cut.

## When to use / when not to

- Use for any triggered/automated email series: welcome, nurture, conversion/sales, launch, or a custom variant of these.
- If the user wants a **recurring broadcast** written fresh each time, that's `skills/marketing/newsletter`, not an automation.
- If the user has no opt-in offer generating subscribers yet, run `skills/marketing/lead-magnet` first — a welcome sequence needs something to deliver.
- If the user needs one high-stakes standalone sales page or email, `skills/marketing/direct-response-copy` goes deeper on a single asset.

## Intake

Ask in one batch, only what's missing:

1. **Trigger and goal** — what event starts the sequence, and what should the subscriber do/believe by the end?
2. **The offer** (if any) — product, price point, main objections buyers raise.
3. **Audience temperature** — cold strangers from an ad, warm lead-magnet subscribers, or existing customers? (This sets how early you can pitch.)
4. **Proof assets** — testimonials, case studies, results, credentials available to use. Never invent these.
5. **Voice** — sample emails or a brand-voice guide (use `skills/marketing/brand-voice` output if it exists).

Infer the sequence type from the trigger (Step 1 decision rule) rather than asking. If enough is known, state assumptions and draft — don't stall.

## Workflow

### 1. Pick the sequence architecture

Decision rule — match on trigger:

| Trigger | Sequence | Emails / span | Job |
|---|---|---|---|
| New subscriber (lead magnet, signup) | **Welcome** | 5 over 7 days | Deliver promise, set expectations, earn trust, introduce offer softly |
| Subscriber finished welcome, no offer live | **Nurture** | rotating weekly pattern | Stay valuable and top-of-mind between campaigns |
| Existing offer, warm list | **Conversion** | 7 over 14 days | Persuade a considered purchase |
| Something new going live on a date | **Launch** | 7 over ~17 days | Build anticipation, then open and close the cart |

If the user's situation genuinely spans two (e.g., welcome that must sell a low-ticket offer), keep the primary architecture and borrow single emails from the other — never run two sequences at once to the same person.

### 2. Map the sequence

Lay out every email's day, job, and angle before writing a word. The canonical architectures (adjust days to the user's platform, keep the spacing logic — gaps grow as the sequence ages):

**Welcome** — Day 1: welcome + deliver the lead magnet + set expectations · Day 2: value + your story (why you do this) · Day 4: proof (case study or customer story) · Day 6: soft offer (introduce, no pressure) · Day 7: engagement ask (a genuine question that invites replies — replies also train inbox placement, a deliverability heuristic worth stating to the user).

**Nurture** — weekly, rotating pattern that repeats: story + lesson → framework or tool → case study/proof → soft offer → question/engagement. One value email between every ask, minimum.

**Conversion** — Day 1: name the problem + open a curiosity loop · Day 3: the mechanism (why common approaches fail, what's different about yours) · Day 5: the offer, plainly (what it is, who it's for, first CTA to buy) · Day 7: proof stack (testimonials, results) · Day 10: objection handling (take the top 2–3 objections from intake head-on) · Day 12: honest urgency (real deadline, real scarcity — see guardrail) · Day 14: final call (deadline restated, last CTA, no new arguments).

**Launch** — Day 1: announcement tease ("something's coming") · Day 3: the why + mechanism · Day 5: full reveal + benefits + early price/bonus · Day 7: early social proof · Day 10: objections · Day 14: urgency (closing soon / price rises) · Day 17: final call.

Propose the map as a table first if the situation is nonstandard; otherwise proceed straight to drafting.

### 3. Write every email

For each email in the map, in order:

- **Subject line**: ≤50 characters, 2 candidates per email. Rotate styles across the sequence — curiosity ("the one thing X gets wrong about Y"), specificity ("how I [result] in [timeframe]"), benefit ("[benefit] without [drawback]"), question, urgency (only when urgency is real). No two consecutive emails with the same style.
- **Preview text**: ≤90 characters extending, not repeating, the subject.
- **Hook** (first 1–2 sentences): drop into a story mid-scene, a question, or a curiosity gap. Never open with "Hope you're doing well" or a recap of who you are.
- **Body**: 100–200 words for value emails; sales emails (offer, objections, final call) may run to ~300 when the argument needs it. One idea per email. Short paragraphs. Written to one person.
- **CTA**: exactly one per email, matched to the email's job — value emails end in a reply prompt or a single link; sales emails end in one buy/signup link (repeating the same link twice in a long email is fine; two *different* asks is not).
- **P.S.**: optional; use for the soft-offer whisper in value emails or the deadline reminder in sales emails.

Thread the sequence: each email should reference or pay off something from the previous one (open loops close, stories continue) so the series reads as one narrative, not seven strangers.

### 4. Self-review and deliver

Run the quality bar per email and across the sequence. Deliver in the required output format with platform-agnostic setup notes (trigger, delays, exit conditions — e.g., "exit conversion sequence on purchase").

## Required output format

```
# [Type] Sequence — [offer/audience]

## Sequence map
| # | Day | Job | Angle | CTA |
| 1 | 1 | ... | ... | ... |
(one row per email)

## Emails

### Email 1 — Day 1 — [job]
Subject A: "…" (n chars)
Subject B: "…" (n chars)
Preview: "…" (n chars)

[Full body, greeting through sign-off, CTA link marked as [LINK: destination]]

P.S. [if used]

---
(repeat for every email)

## Setup notes
- Trigger: [event] · Exit condition: [e.g., purchase removes from sequence]
- Delays: [as mapped] · Assumed platform capabilities: [merge name, delays, exit rules]

## Measure
- Watch: open rate by email (subject problem), click rate on offer emails (offer/copy problem), unsubscribe spikes (pacing problem), replies (health signal).
- Rule: rewrite any email whose opens fall far below its neighbors — it's the subject, not the list. (Heuristic.)
```

## Quality bar

Per email — check, don't eyeball:

- [ ] Subject ≤50 chars (count), makes a promise the body cashes, no clickbait mismatch
- [ ] Preview ≤90 chars, not a subject repeat
- [ ] Hook lands in the first 2 sentences; no "hope you're well" openers
- [ ] One idea, one CTA; value emails 100–200 words, sales emails ≤~300
- [ ] Merge fields used where natural ([FIRST_NAME]), never faked personalization ("I was just thinking about you")

Across the sequence:

- [ ] Value-to-ask ratio: never two consecutive hard-sell emails except the final urgency → final call pair
- [ ] Every objection from intake is answered somewhere before the final call
- [ ] All proof (testimonials, numbers, results) supplied by the user or clearly marked `[PLACEHOLDER — insert real testimonial]`; never invented
- [ ] Urgency is real (actual deadline/scarcity) or absent — fake countdowns are forbidden
- [ ] Consecutive subjects use different styles; sequence reads as one continuing narrative
- [ ] Send-day gaps follow the architecture (no two sales emails on back-to-back days)

## Integration

- `skills/marketing/lead-magnet` — supplies the opt-in promise the welcome sequence's Email 1 must deliver; pull the magnet's exact promise into intake.
- `skills/marketing/brand-voice` — supplies the voice all emails match.
- `skills/marketing/direct-response-copy` — deepens the offer/objection/final-call emails when the sale is high-ticket; hand it the offer and objection list.
- `skills/marketing/newsletter` — subscribers exit the welcome/nurture sequence into the recurring newsletter; note the handoff in setup notes.
- `skills/marketing/content-atomizer` — strong sequence emails can be atomized into social content, and vice versa.
