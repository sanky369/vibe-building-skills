---
name: product-design-review
description: Expert product design and UI/UX review for digital products (web, mobile, desktop), including heuristic evaluation, usability audits, interaction/visual critique, accessibility checks, and prioritized recommendations. Use when asked to review a product, critique UI/UX, evaluate flows/onboarding, assess a design system, or propose improvements to product experience.
---

# Product Design Review

## Overview
Provide a rigorous, actionable product design review that yields prioritized findings and concrete recommendations grounded in user goals and business outcomes.

## Workflow

### 1) Intake and scope
- Ask for product type, platform, primary goals, success metrics, and scope (screens, flows, time period).
- Request artifacts: live URL, prototype link, screenshots, flow map, design system, analytics, research notes.
- Establish constraints: timeline, tech limitations, brand rules, compliance, accessibility target (default to WCAG 2.1 AA).
- If information is missing, state assumptions explicitly and proceed.

### 2) Context and tasks
- Identify key user segments or personas; if none are provided, infer likely segments and call them out.
- Define 3-5 representative tasks (onboarding, activation, purchase, retention, support) to evaluate.
- Clarify success criteria for each task (time to complete, error rate, drop-off, satisfaction).

### 3) Evaluate with heuristics and checklists
- Run a heuristic evaluation using `references/heuristics-and-checklists.md`.
- Review usability, IA, content, visual hierarchy, interaction patterns, error handling, and accessibility.
- Capture evidence for each issue (where it occurs, user impact, and business impact).

### 4) Synthesize findings
- Group issues by theme and user task.
- Assign severity using the 0-3 rubric (Cosmetic, Minor, Major, Critical).
- Map fixes by effort (S/M/L) and confidence; highlight quick wins vs. strategic work.

### 5) Recommend improvements
- Provide specific fixes or design alternatives, not just problem statements.
- Suggest experiments or usability tests when uncertain.
- Note dependencies across product, engineering, content, and analytics.

### 6) Deliverable
- Use the format in `references/review-output-template.md` unless the user asks for a different structure.
- Keep the tone constructive and focused on outcomes.

## Common request patterns
- Review onboarding or activation: focus on clarity, perceived value, friction, and error recovery.
- Critique a dashboard: emphasize hierarchy, scanability, data density, filtering, and states.
- Audit accessibility: run quick checks, list blockers, and provide fixes.

## Resources

### references/
- `references/heuristics-and-checklists.md` for heuristics, checklists, and severity rubric.
- `references/review-output-template.md` for the reporting format and wording patterns.
