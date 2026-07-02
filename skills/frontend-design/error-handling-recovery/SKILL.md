---
name: error-handling-recovery
description: "Audit and implement an app's error UX end-to-end: rewrite error messages, place them correctly, add recovery actions, and build error states for validation, network, permission, system, and 404 failures. Use when the user says 'improve my error handling', 'my error messages suck', 'users get stuck when something fails', 'add form validation errors', 'handle offline/network errors', 'design a 404 page', or when a review finds bare 'Something went wrong' strings, silent failures, or errors with no way forward. Produces an error-state matrix (every failure mode × message × recovery action) plus the implemented error components and copy."
---

# Error Handling & Recovery

Turn every failure into a guided path forward: find each way the app can fail, give it a specific human message, a correct placement, and at least one recovery action. **The prime directive: never blame the user, and never leave them at a dead end — every error state ships with a way out.** Deliver an error-state matrix covering the failure modes plus the implemented components and copy — not messaging guidelines alone.

## When to use / when not to

Use for: error message copy, validation UX, network/offline failure handling, permission-denied and 404 pages, recovery workflows, graceful degradation, error accessibility.

Hand off instead when the real need is:
- Preventing the wait/failure in the first place (retries as performance, optimistic rollback mechanics) → `skills/frontend-design/performance-optimization`
- The loading half of the async lifecycle (skeletons, spinners, empty states) → `skills/frontend-design/loading-states` — this skill owns what happens when loading *fails*
- Error animation timing → `skills/frontend-design/interaction-physics`
- Full accessibility audit beyond error surfaces → `skills/frontend-design/accessibility-excellence`

## Step 0 — Inspect the codebase, then ask only what's left

1. Harvest existing error surfaces: grep for `catch`, `.catch(`, `onError`, `error` state variables, `toast.error`, `alert(`, error boundary components, and string literals like "error", "failed", "wrong", "invalid". Collect the actual message strings — the current copy is your before-picture.
2. Map failure classes present in the app: forms (validation), API calls (network/server), auth'd resources (permission), routing (404), plus anything domain-specific (payment declines, quota limits, file-type rejections).
3. Find the gaps: catch blocks that swallow errors silently, fetches with no error branch, forms that only style the border red, missing error boundaries around independent sections, no offline handling.
4. Check a11y wiring: search for `role="alert"`, `aria-live`, `aria-invalid`, `aria-describedby`. Absence = automatic fix items.

Ask the user (one batch, only if not inferable): the support channel to point to (email/help center — needed for system-error copy), and whether any operations are high-stakes (payments, destructive actions) needing extra-careful recovery. If unanswerable, use a placeholder support link, flag it, and proceed.

## Workflow

### 1. Build the error-state matrix

For every failure mode found in Step 0, fill one row: **failure mode → what the user was doing → message (what happened / why / what to do) → placement → recovery action(s) → a11y wiring**. This matrix is the audit deliverable and the implementation checklist.

### 2. Write each message with the four-part anatomy

1. **What happened** — specific, plain language ("Email already in use", not "Invalid input")
2. **Why** — one line of context, no jargon (never surface "CORS policy violation" to a user)
3. **What to do** — the concrete next step(s)
4. **Where to get help** — support pointer for system errors, with an error/reference ID when the backend provides one

Copy rules: never blame ("you entered an invalid…" → "please enter a…"); state the fix, not just the rule; keep the user's data intact in the message's promises only if the app actually preserves it — never claim "we saved your work" unless it's true.

### 3. Decide placement and recovery per failure class

| Class | Placement | Timing | Recovery |
|---|---|---|---|
| Validation | Inline, adjacent to the field | On blur or submit — never on each keystroke of an incomplete entry; clear immediately once fixed | Fix guidance; shortcut when it exists ("Sign in instead") |
| Network | Section-level state or toast; full state if the whole view failed | On failure | Retry button; preserve entered data; offline continuation if supported |
| Permission | Full state replacing the blocked content | On load/action | Explain why + "Request access" or path to the owner |
| System/5xx | Section or page state | On failure | Retry + support contact + error ID |
| 404 | Dedicated page | On route | Search + links to key destinations |

Fork rules:
- **Inline vs modal vs page:** field-scoped → inline; a blocking, high-stakes failure mid-flow (payment declined) → modal recovery; the whole resource unavailable → full page/section state. Toasts only for failures unrelated to the user's current focus — never for form validation.
- **Auto-retry vs manual:** idempotent reads may retry automatically with backoff; mutations get an explicit user-triggered retry only (never silently resubmit a payment or post).
- **Degrade, don't break:** an unavailable feature is disabled with an explanation, not hidden and not a crash. Wrap independent UI regions in error boundaries so one failure can't blank the page.

### 4. Implement with accessibility built in

- Dynamic errors announce via `role="alert"` (task-blocking) or `aria-live="polite"` (background).
- Fields: `aria-invalid="true"` + `aria-describedby` pointing at the message element.
- On submit failure, move focus to the first invalid field or an error summary linking to each.
- Icon + text + color on every indicator — never color alone.
- Canonical markup/CSS for every class and the recovery patterns: `references/patterns.md` — read it when writing the code.

### 5. Verify

Force each failure (invalid input, network offline in devtools, a 500 via bad endpoint, an unknown route) and confirm: message renders in the right place, recovery action works, entered data survives, screen reader announcement fires (or the wiring is present), nothing fails silently.

## Required output format

Deliver both artifacts:

**1. The code** — implemented error components, copy strings, error boundaries, and a11y wiring, edited into the app's existing component and styling conventions.

**2. Error-State Matrix** (markdown):

```
## Error-state matrix
| # | Failure mode | Class | Message (final copy) | Placement | Recovery | A11y | Status |
| 1 | Signup email taken | validation | "Email already in use…" | inline under field | "Sign in instead" link | aria-invalid + describedby + role=alert | implemented |
| 2 | Feed fetch fails | network | "We couldn't load your feed…" | section state | Retry | polite live region | implemented |
| 3 | Card declined | system | "Your card was declined…" | modal | Try again / other method | alertdialog, focus trapped | implemented |

## Silent failures fixed
| Location | Was | Now |

## Copy changes
| Before | After |

## Assumptions
[Support contact used, failure modes you could not reproduce, etc.]
```

## Quality bar (check before delivering)

- [ ] Every row in the matrix has a recovery action — zero dead ends
- [ ] No message blames the user; no raw technical jargon (stack traces, status codes, CORS) shown to users
- [ ] Every message states what to do, not only what went wrong
- [ ] Validation fires on blur/submit and clears on fix; no keystroke-nagging
- [ ] Errors sit adjacent to their cause (no orphaned error summaries without field links)
- [ ] All indicators use icon/text + color, never color alone
- [ ] `role="alert"`/`aria-live`, `aria-invalid`, `aria-describedby`, and focus management implemented
- [ ] No `catch` block in touched code swallows an error without a user-facing or logged consequence
- [ ] Mutations never auto-retry; user data is preserved across failures in touched flows

Hard don'ts: don't promise recovery the app can't deliver ("your work is saved" without persistence); don't use humor for destructive or payment failures; don't add error UI that hides the actual error from developers — keep console/telemetry logging intact.

## Integration

- `skills/frontend-design/loading-states` → hands you its error-empty placements; you expand them into full messages + recovery. The loading→error transition should reuse the same layout slot.
- `skills/frontend-design/performance-optimization` → optimistic-UI rollbacks from that skill need your failure toasts/messages when a background sync fails.
- `skills/frontend-design/component-architecture` → provides the form/input components you add error variants to; add ErrorState as a shared component there.
- `skills/frontend-design/accessibility-excellence` ← audits your live-region and focus behavior; build to its standards up front.

## References

- `references/patterns.md` — bad→good message rewrites, complete markup for each failure class (validation, network, permission, system, 404), inline/modal/progressive recovery patterns, graceful-degradation snippets, error styling CSS, and the a11y wiring blocks. Read it when writing the components and copy.
