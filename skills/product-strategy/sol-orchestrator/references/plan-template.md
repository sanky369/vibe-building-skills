# Orchestration plan template

```markdown
# Implementation Plan: <Feature>

## Outcome and authority
- User-visible outcome:
- Authority: plan-only | local implementation authorized
- Completion bar:
- External/destructive actions requiring approval:

## Evidence and assumptions
| Claim | Status: Verified/Assumed/Unknown | Evidence or resolving question | Impact |
|---|---|---|---|

## Chosen design
<decision, why it wins, rejected alternatives, revisit trigger>

## Task graph
| ID | Outcome | Owned files | Depends on | Parallel wave | Executor/effort | Validation | Failure handoff |
|---|---|---|---|---|---|---|---|

## Wave checkpoints
| Wave | Milestone | Required checks | Review gate |
|---|---|---|---|

## Risks and rollback
| Risk | Likelihood | Impact | Detection | Mitigation/rollback | Owner task |
|---|---|---|---|---|---|

## Requirement traceability
| Requirement | Task(s) | Validation evidence |
|---|---|---|

## Open questions
<Only questions that materially affect implementation.>
```

Each task must fit one focused agent session, own an exclusive file set, and end in a binary check. Contracts precede consumers. Put the riskiest unknown in the earliest safe wave.
