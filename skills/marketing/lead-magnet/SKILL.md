---
name: lead-magnet
description: "Design a lead magnet — the free offer that trades real value for an email address — by picking the right problem slice, hook, and format, validating it, and drafting the asset. Use when the user says 'grow my email list', 'I need a lead magnet / freebie / opt-in', 'create a free download', 'how do I capture leads', 'nobody signs up', or when a funnel needs an entry offer before the paid ask. Produces a Lead Magnet Spec (title, hook, format, contents outline, delivery, follow-up path) plus a draft of the asset itself when the format allows."
---

# Lead Magnet

Design and draft the **free offer** that turns strangers into subscribers. Governing principle: **a lead magnet solves one specific problem fast, and the problem it solves must be the first step of the problem the paid offer solves** — so consuming the magnet naturally creates demand for the product, instead of attracting freebie-hunters who will never buy.

## When to use / when not to

- Use when building or fixing the top of an email funnel, or when list growth has stalled.
- If there's no clear positioning yet, run `skills/marketing/positioning-angles` first — the magnet's problem slice comes from the positioning claim.
- The landing page that sells the magnet is `skills/marketing/direct-response-copy`'s job; the emails that deliver it and convert to paid are `skills/marketing/email-sequences`' job. Produce the spec + asset here, then hand off.
- If the user wants a recurring free email (not a one-time asset), that's `skills/marketing/newsletter`.

## Intake

One batch; reuse artifacts from `skills/marketing/orchestrator` and `skills/marketing/positioning-angles` instead of re-asking:

1. What paid offer should this magnet ultimately sell, and what problem does that offer solve?
2. Who exactly is the ideal subscriber, and what's the most painful *first step* of that problem for them?
3. What do you already have that could be repurposed (talks, docs, spreadsheets, processes, data)?
4. Any delivery constraints — email platform, ability to host PDFs/video, willingness to maintain a tool?

**Don't stall:** with a known offer and audience, choose the problem slice yourself, state it as an assumption, and proceed.

## Workflow

### 1. Pick the problem slice
Choose one narrow, urgent sub-problem of the paid offer's problem.
Decision rules:
- Must be solvable in one sitting (the magnet's consumption, not a course of study).
- Must be *upstream* of the paid offer: solving it should surface the need the product fills ("audit reveals gaps → product fixes gaps").
- **Reject** slices that fully substitute for the paid offer (cannibalizes sales) and slices so broad any audience would want them (attracts the wrong list).

### 2. Choose the hook
Propose the 2 best-fitting hooks with example titles; the user picks one.

| Hook | Move | Example title | Works because |
|---|---|---|---|
| **Quick win** | Immediate result | "The 5-Minute Positioning Audit" | People want results fast |
| **Forbidden knowledge** | Insider/secret frame | "The Positioning Secrets Top Agencies Don't Want You to Know" | Curiosity drives action |
| **Shortcut** | Faster path | "The 30-Day Positioning Framework (Instead of 90)" | Time-saving is valued |
| **Social proof** | Others' results | "How 500+ Founders Found Their Positioning in 30 Days" | Proof builds trust |
| **Diagnosis** | Reveal their blind spot | "The Positioning Diagnostic: Discover Your Blind Spots" | Self-awareness drives action |

Decision rules: skeptical/jaded audience → social proof or diagnosis; impatient/busy audience → quick win or shortcut; sophisticated audience that's "seen everything" → diagnosis; forbidden knowledge only when there's a genuine insider angle. Social-proof hooks require *real* numbers — never invent them; if none exist, pick another hook.

### 3. Choose the format
Match format to the problem slice, not to fashion:

| Format | Best for | Rule of thumb |
|---|---|---|
| **Checklist** | Process the reader already roughly knows | Consumable in minutes |
| **Template** | "Blank page" problems — they know what, not how to structure it | Fill-in-the-blanks, usable immediately |
| **Guide/workbook** | Problems needing explanation before action | 5–20 pages, never more |
| **Audit/assessment** | "I don't know what's wrong" problems | Scored questions → verdict |
| **Video course** | Show-don't-tell topics | 3–5 short videos |
| **Spreadsheet/calculator** | Numeric decisions | One clear output number |

Decision rules: diagnosis hook → audit/assessment format; quick win → checklist or template; shortcut → template or calculator. Prefer the format the user can build from existing assets (intake Q3). When two formats tie, pick the faster-to-consume one.

### 4. Validate before building
All five must pass, or return to the failing step:
1. Solves exactly one problem (else → Step 1).
2. The *ideal* customer wants it — not just anyone (else → Step 1).
3. Deliverable immediately and automatically on signup (else → Step 3).
4. Better than the competing free offers a search would surface (else sharpen the hook or slice).
5. Consuming it makes the paid offer the obvious next step (else → Step 1).

### 5. Title and draft
Draft **3–5 title candidates** varying the hook intensity; the user picks one. Titles must name the outcome and pass the specificity test ("The 10-Point Positioning Checklist", not "Free Marketing Guide").
Then draft the asset itself: checklists, templates, guides, and audits are drafted in full here; for video courses produce the script outline; for calculators produce the model logic and labels.

### 6. Hand off
Package the spec (format below) and route: landing page copy → `skills/marketing/direct-response-copy`; delivery + nurture emails → `skills/marketing/email-sequences`.

## Required output format

```
# Lead Magnet Spec — [Title]

**Title:** [chosen] (runners-up: [2])
**Hook:** [type] — [why it fits this audience]
**Format:** [type] — [why it fits this problem]
**Problem it solves:** [one sentence]
**Paid offer it leads to:** [offer] — bridge: [why solving this creates demand for that]
**Ideal subscriber:** [who] · **Deliberately excludes:** [who it shouldn't attract]

## Contents outline
1. ...
2. ...

## Delivery
- Mechanism: [instant email / hosted page / tool link]
- Consumption time: [minutes]

## Validation record
1. One problem: PASS/FAIL — [note]  2. Ideal customer wants it: ...  3. Instant delivery: ...
4. Beats competing freebies: ...    5. Sells the next step: ...

## Handoffs
- Landing page → skills/marketing/direct-response-copy (pass this spec + positioning statement)
- Delivery & nurture emails → skills/marketing/email-sequences (pass the promise the emails must keep)

[Draft of the asset follows / is attached]
```

## Quality bar (check before delivering)

- [ ] One problem, one audience — the "deliberately excludes" line is filled in and real.
- [ ] Consumable in one sitting (guide ≤ 20 pages; checklist/template in minutes).
- [ ] The bridge sentence to the paid offer is causal, not "and then buy our stuff".
- [ ] Title names a concrete outcome; no invented numbers or fake social proof anywhere.
- [ ] All five validation checks recorded PASS.
- [ ] Doesn't give away the paid offer's core deliverable.

## Integration

- **Upstream:** `skills/marketing/positioning-angles` supplies the claim the magnet's slice derives from; `skills/marketing/orchestrator` routes here on conversion paths; `skills/marketing/keyword-research` can suggest magnet topics from high-intent clusters.
- **Downstream:** `skills/marketing/direct-response-copy` consumes the spec to write the opt-in page; `skills/marketing/email-sequences` consumes the promise + paid-offer bridge to build the welcome sequence. What crosses the boundary is this spec document.
