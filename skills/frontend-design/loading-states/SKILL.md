---
name: loading-states
description: "Audit an app's async surfaces and implement the right loading, progress, and empty states — skeleton screens, spinners, progress bars, first-use/no-results/error-empty views — chosen by expected latency and layout knowledge. Use when the user says 'add loading states', 'the page just goes blank while fetching', 'add a skeleton screen', 'users think it's frozen', 'spinner or skeleton?', 'design the empty state', 'zero state', or when reviewing an app whose fetches show nothing. Produces a loading/empty-state audit of every async surface plus the implemented components."
---

# Loading & Empty States

Make sure no user ever stares at a blank or frozen-looking screen: inventory every place the app waits or can be empty, choose the correct state for each by expected latency, and implement it. **The prime directive: the indicator is chosen by how long the wait is and whether the layout is known — not by taste.** Deliver an audit table covering every async surface plus the implemented states, never a lone spinner component.

## When to use / when not to

Use for: loading indicators, skeleton screens, progress bars, empty states (first-use, no-results, error-empty, success-empty), "app looks frozen" complaints.

Hand off instead when the real need is:
- Making waits shorter or invisible (optimistic UI, preloading, caching) → `skills/frontend-design/performance-optimization` — always consider that first; the best loading state is none
- Error messages and recovery flows beyond a simple retry-empty-state → `skills/frontend-design/error-handling-recovery`
- Shimmer/spinner motion polish, timing tokens → `skills/frontend-design/interaction-physics`

## Step 0 — Inspect the codebase, then ask only what's left

1. Inventory async surfaces: grep for `fetch(`, `axios`, `useQuery`/`useSWR`/`createResource`, `isLoading`/`isPending`/`loading` flags, `Suspense` boundaries, and route-level data loaders. List every view/component that waits on data or mutation.
2. For each, note what currently shows while waiting: nothing (blank), layout jump, spinner, skeleton, or a disabled control. "Nothing" and "layout jump" are the defects to fix first.
3. Check for existing skeleton/spinner/empty-state components — reuse and extend them rather than duplicating.
4. Estimate expected latency per surface from evidence: cached client state (~instant), same-region API reads (usually sub-second), search/aggregation endpoints (seconds), uploads/exports/report generation (long, often measurable). Look for existing timeout configs or telemetry. Where you can't estimate, say so and pick the 1s-class treatment as the safe default.
5. Enumerate empty-capable views: every list, table, grid, search result, and inbox can be empty. Check which ones currently render a bare nothing.

Ask the user (one batch, only if not inferable): whether any operations are known to be long-running (uploads, exports, batch jobs), and whether there's a design language for illustrations/empty states. Otherwise state assumptions and proceed — never block an audit on questions the code answers.

## Workflow

### 1. Choose each loading state by the latency ladder

| Expected wait | Treatment |
|---|---|
| < 100ms | Nothing — an indicator that flashes in and out is worse than none |
| 100ms – 1s | Subtle inline cue: button spinner/opacity, `cursor: wait`; no layout change |
| 1s – 10s | **Skeleton** if the incoming layout is known; **spinner** if not |
| > 10s | Progress bar — determinate with count/percent if measurable, indeterminate + explanatory text if not |

Fork rules:
- **Skeleton vs spinner:** known content structure (cards, lists, tables, profiles) → skeleton mirroring that exact layout. Unknown/variable structure, or a small area like a button → spinner. Never skeleton modals, toasts, or dropdowns — those must feel instant.
- **Mutations vs reads:** button-level loading (spinner in the button, label hidden, width preserved) for submits; page/section-level states for reads. Don't block the whole page for a local mutation.
- **Flash prevention:** if a wait *might* be short, delay the indicator ~150–200ms so fast responses show nothing; once shown, keep it ≥300–500ms so it doesn't blink.
- **Determinate beats indeterminate** whenever total size/count is knowable (uploads: bytes; batches: items done).

### 2. Design each empty state by type

Every empty view gets one of four treatments — classify, then apply:

| Type | Trigger | Must include |
|---|---|---|
| First use | User has no data yet | What this area is for + primary CTA to create the first item |
| No results | Search/filter matched nothing | Echo of what was searched + escape hatch ("Clear filters") |
| Error-empty | Load failed | Plain-language failure + Retry action (hand complex recovery to `skills/frontend-design/error-handling-recovery`) |
| Success-empty | All items done (inbox zero) | Positive confirmation; no CTA needed |

Rule: an empty state without an action is a dead end — only success-empty may omit the CTA.

### 3. Implement with the structural rules

- Skeleton dimensions match the real content's dimensions — the swap must not shift layout (this is also a CLS fix). Reserve space; vary text-line widths.
- Show loading state immediately on action (or after the flash-prevention delay) — never wait for the first byte.
- Accessibility: loading regions get `aria-busy="true"` and a polite live region announcing "Loading"; skeletons are `aria-hidden="true"`; progress bars use `role="progressbar"` with `aria-valuenow/min/max`; shimmer stops under `prefers-reduced-motion`.
- Canonical implementations (skeleton shimmer, button spinner, determinate/indeterminate progress, all four empty states, a11y blocks): `references/patterns.md` — read it when writing the code.

### 4. Verify

Simulate slow network (devtools throttling or an artificial delay) and confirm: no blank frames, no layout shift at content swap, indicators don't flash on fast responses, empty states render with their actions.

## Required output format

Deliver both artifacts:

**1. The code** — implemented skeleton/spinner/progress/empty-state components and their wiring into each async surface, reusing existing project components and tokens.

**2. Loading & Empty State Audit** (markdown):

```
## Async surface inventory
| Surface | Wait class | Current | Correct state | Status |
| Product grid | 1–10s (search API) | blank screen | card skeleton ×8 | implemented |
| Save button | 100ms–1s | none | inline button spinner | implemented |
| CSV export | >10s | spinner | determinate progress + count | implemented |
| Comments | unknown → assume 1s class | layout jump | skeleton, space reserved | implemented |

## Empty state coverage
| View | First use | No results | Error-empty | Success-empty |
| Projects list | ✓ CTA "Create project" | n/a | ✓ Retry | n/a |
| Search page | n/a | ✓ "Clear filters" | ✓ Retry | n/a |

## Assumptions
[Latency estimates you could not verify, flagged for the user]
```

## Quality bar (check before delivering)

- [ ] Every async surface in the inventory has an assigned state — no blanks left
- [ ] Every state choice is justified by the latency ladder, not preference
- [ ] Skeletons mirror real content layout; content swap causes zero layout shift
- [ ] No skeleton on modals/toasts/dropdowns; no full-page block for local mutations
- [ ] Indicators are flash-proofed (delayed show, minimum display time) where waits may be short
- [ ] Every empty state except success-empty has an action
- [ ] `aria-busy`, live-region announcement, `role="progressbar"` values, `aria-hidden` skeletons, reduced-motion handling all present
- [ ] Operations > 10s show progress or explanatory text, never a bare spinner

Hard don'ts: no spinner-for-everything; no invented time estimates shown to users ("about 2 minutes") unless derived from real data; no loading state on operations that complete instantly.

## Integration

- `skills/frontend-design/performance-optimization` → run first or alongside; optimistic UI removes the need for many loading states, and skeleton space-reservation is shared CLS work.
- `skills/frontend-design/error-handling-recovery` ← consumes your error-empty placements and expands them into full recovery flows.
- `skills/frontend-design/interaction-physics` → supplies shimmer/spinner motion timing and the reduced-motion baseline.
- `skills/frontend-design/component-architecture` → provides the component inventory your skeletons must mirror; add Skeleton/EmptyState as shared components there.

## References

- `references/patterns.md` — full implementation gallery: skeleton building blocks and card example, spinner and button-loading CSS, determinate/indeterminate progress bars, all four empty-state markups, and the accessibility blocks. Read it when writing the code.
