# Technical Specification Template

Use this exact section order. Never omit a section — write "None" or "N/A (reason)" instead, so downstream agents can rely on the structure. Keep each section as short as honesty allows; the SPEC's value is precision, not length.

```markdown
# SPEC: <Feature Name>

## 1. Problem Statement
What is broken/missing, for whom, and why it matters now. 2–5 sentences. No solutions here.

## 2. Goals
Numbered, testable outcomes. Each goal should be verifiable by the Acceptance Criteria (§21).

## 3. Non-Goals
Explicitly out of scope. This is the section that prevents scope creep — include the things a reader might *assume* are included but aren't.

## 4. Assumptions
Table: | # | Assumption | Confidence (H/M/L) | Resolving question | Impact if wrong |

## 5. Constraints
Technical (versions, platforms, resource limits), organizational (deadlines, review requirements), and repo-convention constraints (from CLAUDE.md).

## 6. Existing Architecture Summary
Condensed from the Stage 2 Architecture Snapshot: stack + versions, relevant patterns, the components this feature will build on. Name real files/modules.

## 7. Proposed Architecture
The chosen approach (from the Stage 5 Decision Record). Include a diagram (Mermaid or ASCII) when there are 3+ interacting components. Reference the rejected alternatives in one line each with the rejection reason.

## 8. Component Responsibilities
Table: | Component (new/modified) | Responsibility | Owns | Must NOT do |
The "Must NOT do" column prevents responsibility bleed between agents implementing different tasks.

## 9. Data Flow
Step-by-step trace of the primary flow(s), from trigger to persisted result. Include the failure path, not just the happy path.

## 10. API Changes
New/modified endpoints or interfaces: method, path/signature, request/response shape, auth, versioning strategy, backward-compatibility notes. "None" if not applicable.

## 11. Database Changes
Schema diffs, new tables/columns/indexes, migration direction AND rollback migration, data backfill plan, estimated row impact. "None" if not applicable.

## 12. UI/UX Changes
Screens/components affected, states (loading/empty/error), accessibility notes. "None" if not applicable.

## 13. File-Level Modifications
Table: | Path | New/Modified/Deleted | Intent (one line) |
Paths must be real paths verified in Stage 2, or explicitly marked (new).

## 14. Edge Cases
Enumerated list. For each: the case, expected behavior, which task handles it.

## 15. Error Handling
Error taxonomy for this feature, propagation strategy (matching repo conventions), user-facing messages, retry/timeout policy.

## 16. Security Considerations
Input validation, authn/authz changes, secrets handling, injection surfaces, new dependency audit result (from Stage 3). "No new surface" must be justified, not asserted.

## 17. Performance Considerations
Expected load, hot paths, complexity of new algorithms, caching, N+1 risks, budget (latency/memory) if one exists.

## 18. Observability & Logging
New logs (level + what), metrics, traces, and the specific dashboards/alerts that would detect this feature failing in production.

## 19. Testing Strategy
Unit/integration/e2e split, what gets mocked, fixtures needed, which existing test patterns to follow (name a real test file as the exemplar), coverage expectations for the new code.

## 20. Risks
Table: | Risk | Likelihood | Impact | Mitigation | Detection signal |

## 21. Open Questions
Only questions that do NOT block the plan. Blocking questions must be resolved (or assumed with High-visibility logging) before the SPEC is complete.

## 22. Acceptance Criteria
Numbered, binary (pass/fail) statements. Every Goal in §2 is covered by at least one criterion.

## 23. Definition of Done
The full gate: all acceptance criteria pass + tests green + lint/typecheck clean + docs updated + migration tested both directions + review checkpoints passed + rollout plan actionable.
```
