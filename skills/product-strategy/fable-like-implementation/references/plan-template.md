# Implementation Plan Template

## Structure

```markdown
# Implementation Plan: <Feature Name>

## Phases

Phases are ordered stages of coherent work. Each phase ends in a checkpoint that gates the next phase. Typical shape (adapt, don't force):

- **Phase 0 — Foundations**: scaffolding, config, schema/contract changes, feature flag creation. (Contracts first: everything downstream consumes them.)
- **Phase 1 — Core implementation**: the riskiest/most-unknown component FIRST (fail fast while the sunk cost is low), then remaining core logic.
- **Phase 2 — Integration**: wiring into existing flows, API surface, UI.
- **Phase 3 — Hardening**: edge cases, error handling, observability, performance passes.
- **Phase 4 — Verification & rollout**: full test suite, docs, migration rehearsal, staged rollout.

For each phase:
| Field | Content |
|---|---|
| Milestone | The observable state of the system when the phase is done |
| Checkpoint | What must build/pass/be reviewed before the next phase starts (be specific: "pytest tests/feature_x passes", "schema migration applied+rolled back on a copy of staging") |
| Review checkpoint | Human or agent review required? Of what? |

## Task Breakdown

One table, all tasks:

| ID | Task | Phase | Files | Depends on | Parallel? | Complexity | Validation |
|----|------|-------|-------|------------|-----------|------------|------------|
| T1 | ... | 0 | `src/...` | — | Y | S | ... |

### Task sizing rules
- One task ≈ one PR-sized coherent change an agent completes in a single focused session.
- The done-condition ("Validation") must fit in one sentence and be checkable without judgment calls. If it can't, split the task.
- A task must carry all context needed to execute it: exact files, the SPEC sections it implements, and the conventions to follow. Tasks are handed to agents that have NOT read this conversation.
- Mark tasks parallelizable only when they share no files and no undecided interfaces.
- Complexity: S (< ~1h agent work, mechanical), M (multi-file, some decisions within a decided design), L (novel logic or cross-cutting; consider splitting or assigning the strongest model).

### Ordering heuristics
1. Contracts (schema, API shapes, interfaces) before consumers.
2. Highest-uncertainty task as early as possible.
3. Test scaffolding alongside (not after) the code it tests.
4. Observability lands with the feature, not in a follow-up.
```

## Milestone quality bar

A milestone is a system state ("API returns paginated results behind flag X"), never an activity ("work on pagination"). If you can't demo or assert it, it's not a milestone.
