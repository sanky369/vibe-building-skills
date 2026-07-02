---
name: performance-optimization
description: "Diagnose and fix how slow a frontend feels and measures: optimistic UI for mutations, latency masking (skeletons, blur-up, preloading, staggering), request batching/deduplication, and Core Web Vitals (LCP/INP/CLS) remediation. Use when the user says 'the app feels slow', 'clicks feel laggy', 'improve performance', 'my Lighthouse score is bad', 'fix my Core Web Vitals / LCP / CLS', 'make saves feel instant', or when interactions visibly wait on the network. Produces a performance audit (findings ranked by user impact, with measured or user-reported evidence) plus the implemented fixes — optimistic mutation code, masking treatments, and network-layer improvements."
---

# Performance Optimization

Make the interface feel instant and measure honestly: find where users wait, decide per wait whether to eliminate it (optimistic UI, preloading, batching) or mask it (skeletons, progressive loading), and implement the fix. **The prime directive: perceived latency outranks actual latency — a 3-second operation that responds instantly to the click beats a 1-second one that freezes — but never fake what you can't deliver (no invented progress numbers, no optimistic UI where rollback would burn the user).** Deliver an audit ranked by user impact plus working code.

## When to use / when not to

Use for: sluggish-feeling interactions, optimistic UI, Core Web Vitals remediation, preloading/anticipatory loading, request batching/dedup, layout-shift fixes, perceived-performance strategy.

Hand off instead when the real need is:
- Choosing/designing the loading indicators themselves → `skills/frontend-design/loading-states`
- Animation jank from non-compositor properties → `skills/frontend-design/interaction-physics` (motion spec) or `skills/frontend-design/design-engineer-mindset` (rendering pipeline, layout thrashing)
- The failure/rollback messaging your optimistic UI needs → `skills/frontend-design/error-handling-recovery`
- Backend/query latency itself — flag it, but that's outside this skill's frontend scope

## Step 0 — Inspect the codebase, then ask only what's left

1. Find the data layer: raw `fetch`/`axios` vs a data library (TanStack Query, SWR, Apollo, RTK Query). This decides implementation strategy — libraries get optimistic updates and dedup through their APIs; hand-rolled fetching may need those primitives added.
2. Find waiting patterns: mutations that disable the UI until the server responds, serial `await` chains that could parallelize, duplicate fetches of the same resource, effects re-fetching on every render.
3. Find layout-shift sources: images without dimensions/`aspect-ratio`, content injected above existing content, fonts swapping without fallback metrics, ad/embed slots without reserved space.
4. Look for existing measurement: `web-vitals` package, Lighthouse CI, RUM/analytics. If the project runs in this environment, get real numbers (Lighthouse or a profile) before and after — never quote scores you didn't measure.
5. Check bundle signals when load speed is the complaint: build output sizes, missing route-level code splitting, heavyweight dependencies imported globally.

Ask the user (one batch, only what inspection didn't answer): **which flows feel slow** (or is it a Lighthouse/CWV score problem?), and **any field data available** (CrUX, analytics). If the complaint is already specific ("saving a task feels laggy"), don't ask — profile that flow and proceed.

## Workflow

### 1. Classify every wait on the latency spectrum

| Perceived wait | Treatment |
|---|---|
| < 100ms | Nothing needed — feels instant |
| 100ms – 1s | Instant local feedback (button state) — no spinner |
| 1s – 10s | Eliminate if possible; else mask with skeleton/spinner (per `skills/frontend-design/loading-states`) |
| > 10s | Progress with real numbers + background the work if the stack allows |

### 2. Decide optimistic vs pessimistic per mutation — by failure cost

- **Optimistic** (update UI immediately, sync in background, roll back on failure): low failure cost + high likelihood of success + easy reversal. Likes, toggles, reorderings, adding items to a personal list, renames.
- **Pessimistic** (wait for server confirmation, show inline pending state): irreversible or high-stakes outcomes — payments, sends (email/message that actually dispatches), deletes without undo, anything with server-side validation likely to reject.
- Middle path: pessimistic commit with **undo** (delete now, offer "Undo" for 5–10s before the server call) gives instant feel with safety.
- Every optimistic update requires: a state snapshot before mutating, exact rollback on failure, and a user-visible failure notice (wire via `skills/frontend-design/error-handling-recovery`). Optimistic UI without rollback is a data-integrity bug, not a performance win.

### 3. Eliminate waits before masking them

In priority order:
1. **Parallelize/batch requests** — replace serial `await` chains with `Promise.all` or batched endpoints; deduplicate in-flight requests (data libraries do this free).
2. **Preload anticipatorily** — prefetch route/data on hover or near-viewport (use the framework's built-in prefetch when it exists).
3. **Cache and reuse** — don't refetch unchanged data on navigation.
4. Then mask what remains: skeletons for known layouts, blur-up for images, progressive enhancement for secondary content, staggered entrances for lists (cap total stagger ~300–400ms). Implementations: `references/patterns.md`.

### 4. Fix measured vitals against the real thresholds

Core Web Vitals "good" thresholds (75th percentile of field data):
- **LCP ≤ 2.5s** — largest content render. Fixes: prioritize/preload the LCP image, server-render critical content, cut render-blocking resources, code-split.
- **INP ≤ 200ms** — interaction responsiveness (replaced FID in March 2024). Fixes: break up long main-thread tasks, defer non-urgent work, avoid synchronous layout reads in handlers.
- **CLS ≤ 0.1** — layout stability. Fixes: dimension all media, reserve space for async content (skeletons double here), `font-display` strategy with fallback metrics.

Do not invent numbers: report only measured values, label lab vs field, and if you can't measure in this environment, deliver the fixes plus instructions for the user to verify.

### 5. Verify

Re-measure the same way you measured before (same tool, same page, throttling noted). For optimistic flows, force a failure and confirm exact rollback + notice. For CLS fixes, reload with network throttling and watch for shift.

## Required output format

Deliver both artifacts:

**1. The code** — implemented optimistic mutations (via the project's data library when present), parallelized/batched/deduplicated requests, masking treatments, and vitals fixes.

**2. Performance Audit** (markdown):

```
## Summary
One paragraph: what felt/measured slow, root causes, what changed.

## Measurements
| Metric | Before | After | Threshold | Source (lab/field, tool) |
| LCP | 4.1s | 2.2s | ≤2.5s | Lighthouse, throttled |
| INP | — | — | ≤200ms | not measurable here — verify via [tool] |
| CLS | 0.34 | 0.05 | ≤0.1 | Lighthouse |
(only rows you actually measured; never invented)

## Findings & fixes (ranked by user impact)
| # | Finding | Evidence | Fix | Status |
| 1 | Task save blocks UI ~800ms | network tab | optimistic update + rollback | implemented |
| 2 | 4 serial awaits on dashboard load | code | Promise.all | implemented |
| 3 | Hero image no dimensions → CLS | measured 0.34 | aspect-ratio + preload | implemented |

## Mutation strategy table
| Mutation | Strategy | Why | Rollback/undo |
| Like toggle | optimistic | trivial reversal | snapshot restore |
| Checkout | pessimistic | irreversible charge | n/a — inline pending |

## Not done / recommended next
[Backend latency, infra, CDN items outside frontend scope]
```

## Quality bar (check before delivering)

- [ ] Every claimed number was actually measured; lab vs field labeled; unmeasurable metrics marked as such
- [ ] Every optimistic update has snapshot, exact rollback, and user-visible failure notice
- [ ] No optimistic treatment on payments, dispatched sends, or undo-less destructive actions
- [ ] No serial `await` chains left where requests are independent
- [ ] All images/embeds in touched code have reserved dimensions
- [ ] No fabricated progress percentages or time estimates shown to users
- [ ] Masking respects `prefers-reduced-motion`; staggering capped
- [ ] Fixes ranked by user impact, not by ease of implementation

Hard don'ts: don't add a data-fetching library solely for one optimization without flagging the tradeoff; don't chase a Lighthouse score with tricks that hurt real UX (lazy-loading the LCP image, skeleton-flashing instant content); don't remove existing loading feedback just to "feel faster".

## Integration

- `skills/frontend-design/loading-states` → owns which indicator shows for waits this skill can't eliminate; run them together — space reservation is shared CLS work.
- `skills/frontend-design/error-handling-recovery` → supplies the rollback failure messaging every optimistic mutation needs.
- `skills/frontend-design/design-engineer-mindset` → owns rendering-pipeline depth (layout thrashing, frame budget) when INP/jank fixes need main-thread work.
- `skills/frontend-design/interaction-physics` → its compositor-only animation rule prevents the jank this skill would otherwise have to fix.

## References

- `references/patterns.md` — optimistic create/delete/toggle with rollback, data-library notes, skeleton/blur-up/progressive/staggered masking, anticipatory preloading, request batching and dedup code, and CWV measurement guidance. Read it when implementing the fixes.
