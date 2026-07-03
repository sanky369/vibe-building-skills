# Heuristics and Checklists

Working reference for step 3 of the review. Apply every lens that the evidence mode can support; skip a lens only when the artifact genuinely can't show it (e.g., motion on a static screenshot) and note the skip under "Needs live check".

## Severity rubric

Severity = impact **if the issue is real**. Uncertainty lowers the Confidence column, never the severity.

- **3 Critical** — blocks task completion or destroys trust/data for many users: unrecoverable destructive actions, primary CTA broken or effectively invisible, core task impossible by keyboard, payment/security signals that read as unsafe.
- **2 Major** — significant friction or drop-off on a core task: failed contrast on task-critical text, missing/blocking error recovery, inverted action hierarchy, unlabeled form fields on a conversion path.
- **1 Minor** — noticeable friction; the task still completes: ambiguous labels, missing currency/units, weak affordances on secondary controls.
- **0 Cosmetic** — polish with no task impact: typos off the money path, minor alignment drift.

Escalate one level when the issue sits on the product's single most important flow; de-escalate one when it's on an admin/edge surface.

## Heuristic evaluation (Nielsen)

- **Visibility of system status** — every action gets feedback; loading, progress, and success are visible within ~1s.
- **Match to the real world** — familiar language and mental models; no internal jargon or error codes surfaced to users.
- **User control and freedom** — undo, cancel, and safe exits; destructive actions confirmed or reversible.
- **Consistency and standards** — same pattern means the same thing everywhere; platform conventions respected.
- **Error prevention** — constraints and validation before submission, not after failure.
- **Recognition over recall** — options visible; nothing depends on remembering an earlier screen.
- **Flexibility and efficiency** — shortcuts and defaults for repeat users without burying the novice path.
- **Aesthetic and minimalist design** — every element earns its place; noise removed rather than decorated.
- **Error recovery** — errors say what happened, why, and the next step, adjacent to where they occurred.
- **Help and documentation** — discoverable help at the point of complexity, not only in a help center.

## First-use lens (onboarding, activation, "first-time visitor")

Apply whenever the review concerns new users, signups, landing surfaces, or "why aren't people activating".

- Can a first-time visitor answer "what is this and why should I care" from the first screen alone, without scrolling or clicking?
- Is the first meaningful action obvious, low-risk, and rewarding (time-to-first-value measured in seconds)?
- Does the product use vocabulary a newcomer can't yet know (internal nouns, unlabeled icons, community jargon)? Every such term is a finding.
- What happens when a logged-out or empty-state user touches a members-only control — a helpful nudge, or a silent bounce to login?
- Is account creation sold (what it unlocks) or merely demanded?
- Do empty states teach and offer the first step, or just say "no data"?

## Trust and dark-patterns lens

Apply on any surface handling money, personal data, or consent.

- Urgency and scarcity claims are real and verifiable; no manufactured countdowns or "ACT NOW" pressure.
- Consent copy says what is agreed to and links the actual terms — "you agree to stuff" is a finding.
- Prices show currency, totals include fees before the final step, and the cheapest option isn't visually buried.
- No confirm-shaming ("No thanks, I hate saving money"), forced continuity, or pre-checked upsells.
- Security signals (badges, locks) are genuine and labeled; a decorative unlabeled trust badge is worse than none.
- Cancel/downgrade paths are as findable as upgrade paths.

## Core usability checklist

- **Task clarity** — the next step is obvious and unambiguous on every screen of the flow.
- **Information scent** — labels and links predict what's behind them.
- **Navigation** — predictable, shallow, resilient to back-button and deep-link entry.
- **Forms** — minimum fields, grouped logically, visible labels (placeholders are not labels), correct `type`/`inputmode`/`autocomplete`, inline validation near the field.
- **Error handling** — human language, cause + fix, placed at the problem; never a bare code or blocking `alert()`.
- **State inventory** — for each key component, verify all of: default, hover, focus, active, loading, empty, error, disabled. Missing states are findings.
- **Search and filters** — findable, forgiving, easy to reset; leaving the domain or losing state is a finding.
- **Progress honesty** — step counts and progress indicators are accurate ("Step 4 of 3" is a trust-destroying bug, not a typo).

## Visual and UI checklist

- **Hierarchy** — the primary action is the most visually dominant control; visual weight matches importance (a huge "Go Back" next to a faint "Continue" is an inverted hierarchy, severity 2+ on a conversion path).
- **Layout** — consistent spacing scale, alignment to a grid, sensible max line length (~45–75 characters).
- **Typography** — readable sizes (body ≥ 16px on web), consistent scale, weight used for meaning.
- **Color** — computed contrast passes (thresholds below); color never the only carrier of meaning.
- **Affordances** — interactive things look interactive; non-interactive things don't.
- **Motion** — animation explains state change; nothing flashes, loops distractingly, or blocks input.

## Content and IA checklist

- Labels and groupings match user intent, not org chart or database schema.
- Microcopy is concise, action-oriented, and consistent in tone.
- Content is scannable: front-loaded headings, bullets over walls of text.
- Units, dates, currency, and pluralization are explicit and localizable.

## Accessibility quick checks (WCAG 2.2 AA)

Use real numbers; compute, don't eyeball. Contrast ratio = (L1 + 0.05) / (L2 + 0.05) with relative luminance from the hex values — when reviewing source you have the exact hex pairs, so state the ratio in the finding.

- **Contrast (1.4.3, 1.4.11)** — normal text ≥ 4.5:1; large text (≥ 24px, or ≥ 18.66px bold) ≥ 3:1; non-text UI components and focus indicators ≥ 3:1.
- **Keyboard (2.1.1)** — every action operable via keyboard; `<span onclick>` controls are automatic failures.
- **Focus (2.4.7, 2.4.11)** — visible focus indicator on everything interactive (`outline: none` with no replacement is a finding); focused element never fully obscured by sticky UI.
- **Target size (2.5.8)** — pointer targets ≥ 24×24 CSS px (44×44 is the mobile-HIG/AAA bar).
- **Labels (1.3.1, 3.3.2, 4.1.2)** — every input has a programmatic label; every icon-only control an accessible name; every image meaningful `alt` or explicit `alt=""`.
- **Motion (2.3.1, 2.2.2)** — nothing flashes > 3×/second; auto-moving content pausable; `prefers-reduced-motion` respected.
- **Media (1.2.x)** — captions for video, transcripts for audio.
- **Redundant entry / accessible auth (3.3.7, 3.3.8)** — flows don't re-ask for info already given; login doesn't require transcription or memorization puzzles.

Deep remediation belongs to `skills/frontend-design/accessibility-excellence`; this list is for flagging blockers with correct criteria numbers.

## Platform-specific checks

- **Web** — responsive at ~375px and ~1440px; usable at 200% zoom; no horizontal body scroll; perceived performance on the first meaningful screen.
- **iOS/Android** — safe-area insets respected; system back behaves; gestures don't conflict with system edges; touch targets per the 24/44px bars above.
- **Desktop** — keyboard shortcuts for repeat actions; large-screen layouts use the space (no phone layout stretched to 27").
