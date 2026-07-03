# Heuristics and Checklists

## Table of contents
1. Severity rubric
2. Heuristic evaluation (Nielsen-style)
3. Core usability checklist
4. Visual and UI checklist
5. Content and IA checklist
6. Accessibility quick checks
7. Platform-specific checks

## 1) Severity rubric
Use a 0-3 scale. Combine impact, frequency, and persistence.

- 0 Cosmetic: Visual polish issue; minimal impact on task success.
- 1 Minor: Noticeable friction; task still completes without major risk.
- 2 Major: Blocks or derails key tasks; significant drop-off or errors.
- 3 Critical: Prevents completion for many users or causes serious trust loss.

Tip: If unsure, default to lower severity and note uncertainty.

## 2) Heuristic evaluation (Nielsen-style)
- Visibility of system status: Provide clear feedback for actions, loading, and progress.
- Match to real world: Use familiar language, mental models, and conventions.
- User control and freedom: Offer undo, cancel, and easy recovery from mistakes.
- Consistency and standards: Keep patterns, labels, and interactions consistent.
- Error prevention: Design to avoid errors; validate before submission.
- Recognition over recall: Surface options; reduce memory burden.
- Flexibility and efficiency: Support shortcuts and power use when appropriate.
- Aesthetic and minimalist design: Remove unnecessary noise and distractions.
- Help users recover from errors: Explain, guide, and provide next steps.
- Help and documentation: Provide discoverable help for complex flows.

## 3) Core usability checklist
- Task clarity: Is the next step obvious and unambiguous?
- Information scent: Do labels and links match user expectations?
- Navigation: Is it predictable, shallow, and resilient to detours?
- Forms: Are fields minimized, grouped, and clearly validated?
- Error handling: Are errors actionable and placed near the problem?
- Empty states: Do they teach and offer next steps?
- Search and filters: Are they findable, relevant, and easy to reset?
- Trust cues: Are security, pricing, and data use transparent?

## 4) Visual and UI checklist
- Hierarchy: Is primary action visually dominant?
- Layout: Is spacing consistent and aligned?
- Typography: Is size/weight/line-length readable and consistent?
- Color: Is contrast sufficient; do colors encode meaning consistently?
- Affordances: Do controls look clickable and interactive?
- States: Are hover, focus, loading, disabled, and error states defined?
- Motion: Does animation clarify state changes without distracting?

## 5) Content and IA checklist
- IA: Are labels and groupings aligned to user intent?
- Microcopy: Is it concise, helpful, and action-oriented?
- Tone: Is it consistent with brand and context?
- Readability: Is content scannable with headings and bullets?
- Localization: Are units, dates, and language adaptable?

## 6) Accessibility quick checks
- Contrast: Text and UI meet WCAG 2.1 AA contrast ratios.
- Keyboard: All interactive elements are reachable and operable.
- Focus: Visible focus indicators and logical focus order.
- Labels: Inputs have labels; icons have accessible names.
- Touch targets: Adequate size and spacing on mobile.
- Motion: Respect reduced motion preferences.
- Media: Provide captions or transcripts when needed.

## 7) Platform-specific checks
- Web: Responsive breakpoints, zoom at 200%, performance perception.
- iOS/Android: Safe areas, back navigation, gesture conflicts.
- Desktop: Keyboard shortcuts, large-screen layout efficiency.
