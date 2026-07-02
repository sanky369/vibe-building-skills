---
name: accessibility-excellence
description: "Audit a frontend against WCAG and fix what fails: semantic HTML, keyboard navigation, focus management, screen-reader support (ARIA), color contrast, forms, and media alternatives. Use when the user asks 'is this accessible', 'make this WCAG/AA compliant', 'add keyboard navigation', 'fix screen reader support', 'a11y audit', 'we got an accessibility complaint/legal notice', or whenever building/reviewing UI components with interactive behavior — even if accessibility isn't mentioned. Produces a prioritized accessibility audit (issue × WCAG criterion × severity × fix) plus the implemented fixes in code."
---

# Accessibility Excellence

Make the product usable by everyone — keyboard-only users, screen-reader users, low-vision users — by auditing real code against WCAG checkpoints and fixing the failures in priority order. **The prime directive: semantic HTML first; ARIA only fills gaps native elements can't. Most accessibility bugs are the wrong element doing the right job.** Deliver a prioritized audit plus implemented fixes — never a compliance lecture.

## When to use / when not to

Use for: accessibility audits, WCAG conformance work, keyboard/focus behavior, ARIA and screen-reader support, contrast failures, accessible forms/modals/menus, alt text and captions.

Hand off instead when the real need is:
- Designing the color palette itself (accessible-by-construction tokens) → `skills/frontend-design/color-system`
- Reduced-motion and animation safety in depth → `skills/frontend-design/interaction-physics` (this skill audits it; that one implements the motion layer)
- Error-message UX beyond ARIA wiring → `skills/frontend-design/error-handling-recovery`
- Restructuring messy components before making them accessible → `skills/frontend-design/component-architecture`

## Step 0 — Inspect the codebase, then ask only what's left

1. Measure current ARIA/semantics usage: grep for `aria-`, `role=`, `alt=`, `tabIndex`, `<main`, `<nav`, `<button`, `onClick` on `div`/`span`, `outline: none`, `label`/`htmlFor`. The ratio of clickable divs to real buttons is a fast health signal.
2. Inventory the interactive surface: forms, modals/dialogs, menus/dropdowns, tabs, tooltips, custom widgets (drag-drop, sliders, comboboxes) — these carry most keyboard/ARIA risk.
3. Check heading structure (one `h1`, no skipped levels), landmark usage, `<html lang>`, skip link, image alt coverage, video captions.
4. If a runnable environment exists, run an automated scan (axe-core / Lighthouse a11y) for a baseline — but treat it as ~a third to half of real issues, never the whole audit.
5. Note the component stack: headless a11y libraries already present (Radix, React Aria, Headless UI, native `<dialog>`) mean fix-by-adoption beats hand-rolling.

**Choose the WCAG target by context — don't ask unless genuinely ambiguous:** default to **WCAG 2.2 AA** (the norm for legal/regulatory contexts — ADA, EAA, Section 508 references AA). Government/public-sector/education → AA mandatory, consider select AAA criteria. AAA as a blanket target is impractical — apply specific AAA criteria (e.g. 7:1 contrast) only when the user serves a low-vision-heavy audience or asks. Ask the user only: whether there's a compliance deadline/driver, and which flows are most critical if the app is large. Otherwise state "auditing to WCAG 2.2 AA" and proceed.

## Workflow

### 1. Audit against the POUR checkpoints

Work through the four principles using the checkpoint tables in `references/checkpoints.md` (read it when running the audit). Key AA thresholds to apply — these are the real numbers, don't approximate:

- **Contrast:** normal text ≥ 4.5:1; large text (≥24px, or ≥18.66px bold) ≥ 3:1; non-text UI components and focus indicators ≥ 3:1. (AAA: 7:1 / 4.5:1.)
- **Target size (WCAG 2.2 AA):** pointer targets ≥ 24×24 CSS px; 44×44 is the AAA/mobile-HIG bar.
- **Keyboard:** every action operable via keyboard; visible focus everywhere; no `tabindex` > 0; no traps (except intentional, escapable modal traps).
- **Flashing:** nothing flashes more than 3×/second.

### 2. Severity-rank every finding

- **Blocker** — a user population cannot complete a core task (unreachable control, focus trap, unlabeled form in checkout, missing keyboard path).
- **Serious** — task completable but badly degraded (missing announcements, contrast failures on primary text, wrong reading order).
- **Moderate** — friction (vague link text, redundant announcements, minor contrast on secondary text).
- **Minor** — polish (decorative images with verbose alt, missing `aria-current`).

Fix order: blockers → serious → moderate. Present the ranked list; for large codebases have the user confirm scope before mass fixes, otherwise proceed.

### 3. Fix with these decision rules

- **Native element vs ARIA retrofit:** if a `<div onClick>` behaves like a button/link/checkbox, replace it with the native element — that one change fixes role, keyboard, and focus at once. Only add `role`/`tabIndex`/key handlers when a native element genuinely can't work.
- **Custom widget vs library:** for modals, menus, comboboxes, tabs — adopt the project's existing headless library or native `<dialog>` before hand-rolling focus traps and arrow-key logic. Hand-roll only when no library is present and adding one is unwelcome.
- **Contrast fixes:** adjust the token, not one instance — find where the failing color is defined and fix it at the source (coordinate with `skills/frontend-design/color-system` if a palette redesign is implied).
- **Announcements:** task-blocking errors → `role="alert"`; background status → `aria-live="polite"` (region must pre-exist in the DOM); moving focus is for navigation-sized context changes only.
- **Labels:** visible `<label for>` beats `aria-label` beats `aria-labelledby` chains; placeholder is never a label.

Canonical patterns (focus trap, skip link, live regions, field-error wiring, expected keys per widget): `references/checkpoints.md`.

### 4. Verify

Minimum verification pass on touched flows: full keyboard walk-through (reach, operate, see focus, escape), automated re-scan if available, zoom to 200%, and confirm announcements/names by inspecting the accessibility tree. State plainly what you could not verify (e.g. real screen-reader testing on VoiceOver/NVDA) and tell the user to do it — never claim conformance beyond what was checked.

## Required output format

Deliver both artifacts:

**1. The code** — implemented fixes (semantic swaps, labels, focus management, ARIA wiring, contrast token changes), respecting existing component conventions.

**2. Accessibility Audit** (markdown):

```
## Scope & target
Pages/flows audited; target: WCAG 2.2 AA; tools used (axe/Lighthouse/manual keyboard).

## Findings
| # | Severity | Issue | WCAG criterion | Location | Fix | Status |
| 1 | Blocker | Checkout "Pay" is a div, keyboard-unreachable | 2.1.1 | Checkout.tsx | native <button> | fixed |
| 2 | Serious | Placeholder-only labels on signup | 3.3.2 | SignupForm.tsx | <label for> added | fixed |
| 3 | Serious | Body text #9CA3AF on #F9FAFB ≈ 2.5:1 | 1.4.3 | tokens.css | darkened token to pass 4.5:1 | fixed |
| 4 | Moderate | No skip link | 2.4.1 | layout | added | fixed |

## Verified
- Keyboard walk-through: [flows] ✓
- Automated scan: [before → after issue count]

## Not verified — user action required
- Screen reader pass (VoiceOver/NVDA) on [flows]
- [anything environment prevented]

## Recurring root causes
[e.g. "clickable divs pattern-wide — adopt lint rule jsx-a11y"]
```

## Quality bar (check before delivering)

- [ ] Every finding cites a WCAG criterion and a severity — no vibes-based flags
- [ ] All blockers fixed or explicitly declined by the user
- [ ] No new `<div onClick>`, `outline: none` without replacement, positive `tabindex`, or placeholder-as-label introduced anywhere in delivered code
- [ ] Contrast fixes made at the token/source level and verified with computed values against 4.5:1 / 3:1
- [ ] Every modal/menu in scope: focus moves in, traps correctly, Escape works, focus returns to trigger
- [ ] Every form control has a programmatic label; every error is associated via `aria-describedby` and announced
- [ ] Heading hierarchy valid; landmarks present; `lang` set; skip link first-focusable
- [ ] "Not verified" section honestly lists untested surface — no conformance overclaim

Hard don'ts: don't sprinkle ARIA on native elements that already work; don't claim "WCAG compliant" from an automated scan; don't fix contrast by inventing new one-off colors; don't remove focus outlines, ever, without an equal-or-better visible replacement.

## Integration

- `skills/frontend-design/component-architecture` → provides the component inventory; fixes land in shared components so they propagate. Feed recurring issues back as component-level conventions.
- `skills/frontend-design/color-system` → owns palette redesign when contrast failures are systemic rather than one token.
- `skills/frontend-design/error-handling-recovery` → owns error copy and recovery UX; this skill supplies the `role="alert"`/`aria-invalid`/focus rules it must follow.
- `skills/frontend-design/interaction-physics` → owns implementing reduced-motion and flash-safety; this skill audits them.

## References

- `references/checkpoints.md` — full POUR checkpoint tables with WCAG criterion numbers, semantic HTML reference, keyboard patterns (focus trap, skip link, per-widget key expectations), ARIA pattern gallery and common ARIA mistakes, media/content rules, and testing tooling guidance. Read it when running the audit and when writing fixes.
