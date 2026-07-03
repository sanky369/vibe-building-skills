---
name: product-design-review
description: "Run an evidence-based product design and UI/UX review of a digital product (web, mobile, desktop) — heuristic evaluation, task walkthroughs, visual and interaction critique, and WCAG 2.2 AA accessibility checks. Use when the user says 'review my app/page/site', 'critique this UI', 'something feels off', 'why are users dropping off', 'audit our onboarding/checkout/dashboard', 'is this usable/accessible', or shares a URL, screenshot, Figma link, or codebase and asks what to improve — even if they never say 'design review'. Produces a Design Review Report: executive summary, prioritized findings table with evidence and severity, flow walkthroughs, accessibility blockers, and next steps routed to the skill that fixes each category."
---

# Product Design Review

Review a product the way a strong design lead would: walk its real tasks, judge it against explicit heuristics, and deliver findings a team can act on tomorrow. **Prime directive: evidence over opinion.** Every finding names where it occurs, what the user suffers, and the concrete fix — and never claims to have seen something you didn't actually render. A review that says "improve the hierarchy" has failed; one that says "the destructive Clear action sits one unconfirmed click from the primary CTA (checkout.html:18) — gate it behind a confirm" has done its job.

## When to use / when not

- Use for critique of an existing product surface: a page, flow, app, prototype, or design system in use.
- If the user wants the fixes *implemented*, deliver the review, then route each fix per the table in step 5 — don't rebuild the UI inside this skill.
- If the product's problem is the promise, not the pixels (nobody wants the thing), hand off to `skills/product-strategy/foundation-sprint`.
- If the user wants a broad "make it better" engagement rather than a review artifact, hand off to `skills/frontend-design/frontend-orchestrator`.

## Step 1 — Establish evidence mode

Before any judgment, determine what you can actually inspect. Pick the strongest mode available; state which one you're in at the top of the report.

| Artifact | Procedure | Evidence tier |
|---|---|---|
| Live URL + browser automation available (claude-in-chrome, agent-browser, Playwright) | Render it. Screenshot at ~375px and ~1440px. Tab through the primary flow checking focus visibility. Trigger reachable error, empty, and loading states. | **Observed** |
| Live URL, no browser | Fetch the HTML and CSS. You can verify markup semantics, labels, real color/type values, and compute contrast ratios. You cannot see layout, motion, or states — say so. | **Computed** |
| Codebase | Read the flow's components, styles, and copy. If the project documents a way to run the app, run it and review rendered output (upgrades findings to observed). | **Computed** |
| Screenshots / mockups | Visual, copy, and hierarchy critique of what's shown. Keyboard behavior, states, and motion are unverifiable — list them under "needs live check", don't guess. | **Observed** (static only) |
| Figma link | Use Figma MCP tools (`get_screenshot`, `get_design_context`) if connected; otherwise ask for exported frames. | **Observed** (static only) |

**Tier discipline:** tag each finding observed, computed, or inferred. Severity-3 findings require observed or computed evidence. Never present an inferred visual claim ("the spacing feels cramped") as something you saw — either render it or label the inference.

## Step 2 — Intake (one batch, then move)

Ask only what's missing, in a single batch: **who the primary user is, the one flow that matters most, and what "better" means** (conversion, activation, task speed, trust). Infer platform and product type from the artifact itself. Default the accessibility target to **WCAG 2.2 AA** without asking. If the user is unavailable or the request is self-evident ("review my checkout page"), state your assumptions in the report and proceed — never stall the review on missing context.

## Step 3 — Walk the tasks

Define 3–5 representative tasks for the surface under review (for a checkout: find the field, complete payment, recover from an error, back out safely; for a dashboard: orient, find today's anomaly, drill in, act). Attempt each task in your evidence mode as the target user would, and evaluate against the lenses in `references/heuristics-and-checklists.md` (read it now — it holds the heuristics, the first-use and trust lenses, the WCAG 2.2 quick checks with real thresholds, and the severity rubric).

Scope by request: a single screen gets all lenses on one surface; a flow gets task walkthroughs end-to-end including error paths; a full product audit gets the top 3 revenue- or activation-critical flows — tell the user what you scoped out.

For every issue capture three things at the moment you find it: **location** (file:line, selector, screen, or timestamp), **what the user experiences**, and **which lens it violates**. An issue without a location doesn't go in the report.

## Step 4 — Score and synthesize

Severity scores **impact if the issue is real** — never discount severity because you're unsure; that's what confidence is for.

- **3 Critical** — blocks task completion or destroys trust/data for many users (unrecoverable destructive action, broken primary CTA, checkout that can't be completed by keyboard).
- **2 Major** — significant friction or drop-off on a core task; WCAG failures on core-task content.
- **1 Minor** — noticeable friction; task completes.
- **0 Cosmetic** — polish; no task impact.

Confidence (High/Med/Low) scores the evidence: High = observed or computed; Med = strong inference from source; Low = pattern-matched guess (severity ≤ 1 only). Then group findings by task, and split recommendations into **quick wins** (S effort, high confidence) vs **strategic work**.

## Step 5 — Recommend and route

Every finding gets a concrete fix — the changed value, copy, or pattern, not "improve X". When a cluster of fixes falls into one category, name the sibling skill that implements it:

| Fix category | Route to |
|---|---|
| Hierarchy, clutter, "nothing stands out" | `skills/frontend-design/visual-hierarchy-refactoring` |
| Contrast, palette drift, dark mode | `skills/frontend-design/color-system` |
| Type scale, readability | `skills/frontend-design/typography-system` |
| Spacing, grid, alignment | `skills/frontend-design/layout-system` |
| Accessibility remediation | `skills/frontend-design/accessibility-excellence` |
| Error messages, validation, recovery | `skills/frontend-design/error-handling-recovery` |
| Loading, empty, progress states | `skills/frontend-design/loading-states` |
| Dead-feeling interactions, janky motion | `skills/frontend-design/interaction-physics` |
| Component/state architecture debt | `skills/frontend-design/component-architecture` |
| Slow or slow-feeling surfaces | `skills/frontend-design/performance-optimization` |

Propose an experiment only when a recommendation is genuinely contested or risks the product's identity (e.g., adding onboarding copy to a deliberately minimal product) — state hypothesis, test, and metric. Don't append boilerplate A/B tests to obvious fixes.

## Required output format

```
# Design Review: [product/surface]
**Evidence mode:** [observed via rendered browser | computed from source | static screenshots] — [what this could and could not verify]
**Scope & assumptions:** [flows covered; assumptions made in place of missing context]

## Executive summary
[2–3 sentences: overall verdict + the single most likely cause of the user's complaint]
**Top 3 issues:** [one line each, worst first]
**Quick wins:** [1–3 S-effort/high-confidence fixes]
**Strategic:** [1–2 larger moves]

## Findings
| # | Issue | Evidence (location) | Tier | Sev | Fix | Effort | Conf |
[worst first; every row has a location and a concrete fix]

## Task walkthroughs
### [Task name]
[What happens when the target user attempts it; where it breaks; the fix]

## Accessibility (WCAG 2.2 AA)
[Blockers with criterion numbers and computed values, e.g. "#999 on #fff = 2.8:1, fails 1.4.3"]

## Needs live check
[Claims that require rendering/interaction you couldn't perform — omit section if none]

## Next steps
1–3 immediate actions, then fix clusters routed to skills per the table above.
```

## Quality bar — check before delivering

- Every finding has a location; every severity ≥ 2 finding is observed or computed, not inferred.
- Every contrast claim states the computed ratio; every accessibility blocker cites its WCAG 2.2 criterion.
- Every finding's fix is concrete enough to implement without asking what you meant.
- The executive summary answers the user's actual complaint ("something feels off" → name the thing).
- Nothing in "Findings" contradicts the evidence-mode disclosure; anything unverifiable sits in "Needs live check".
- No recommendation introduces a dark pattern (fake urgency, confirm-shaming, forced continuity), even if it would lift the stated metric.

## Integration

- Consumes: a Founding Hypothesis or positioning from `skills/product-strategy/foundation-sprint` when one exists — review against the promise the product makes.
- Produces: the findings report that `skills/frontend-design/frontend-orchestrator` or any routed sibling skill uses as its work queue; accessibility blockers feed `skills/frontend-design/accessibility-excellence` directly.

## References

- `references/heuristics-and-checklists.md` — severity rubric, Nielsen heuristics, first-use and trust lenses, usability/visual/content checklists, WCAG 2.2 AA quick checks with thresholds, platform checks. Read during step 3.
