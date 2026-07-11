# Model / Sub-Agent Selection Guide

Assign models by **task properties**, not habit. The two properties that matter most:

- **Ambiguity** — how many decisions remain open inside the task?
- **Blast radius** — how expensive is a wrong answer (schema damage, security, public contracts)?

Plus one modifier: **Volume** — is it a lot of mechanical work?

## Capability tiers

Model names drift; tiers don't. Map the tiers to whatever models are currently available. Default mapping (update if the user or repo config specifies otherwise):

| Tier | Default model | Character |
|------|---------------|-----------|
| **Reasoning tier** | Opus 4.8 | Deep architecture reasoning, hard debugging, algorithm design, gnarly refactors, security-sensitive decisions |
| **Implementation tier** | Sonnet 5 | Fast, reliable execution of well-specified work: feature code within a decided design, refactoring, repo navigation, boilerplate |
| **Generation/verification tier** | GPT-5.5 (Codex) | High-volume code generation, test-suite generation, API integrations against clear docs, large-scale mechanical edits, cross-checking another agent's output |

If a listed model isn't available in the execution environment, substitute the nearest available tier-mate and say so in the matrix.

A user-level or repo `CLAUDE.md` that ranks, prices, or constrains models **overrides this default mapping** — read it before assigning. Standing escalation rule: if a cheaper tier's output misses the bar, re-run the task on a higher tier rather than shipping mediocre work, and note the escalation in the matrix.

## Routing rules

| Task looks like | Route to | Because |
|---|---|---|
| Design decision still open inside the task | Reasoning | Shouldn't happen — split the task; if truly unavoidable, only the reasoning tier should hold an open decision |
| High blast radius (migration, auth, public API) regardless of difficulty | Reasoning | Cost of error dominates cost of compute |
| Well-specified multi-file feature work | Implementation | The plan already made the decisions; speed and reliability win |
| Boilerplate, wiring, config, renames | Implementation | Cheapest competent option |
| Generating a large test suite from acceptance criteria | Generation/verification | Volume + pattern-following strength |
| Integrating a documented third-party API | Generation/verification | Doc-following at volume |
| Verifying/cross-reviewing completed tasks | Generation/verification (different model than the author) | Independent-eyes principle: the verifier should not be the model that wrote the code |
| Debugging a failure the implementation tier couldn't fix in 2 attempts | Escalate to Reasoning | Two failed attempts = the problem is harder than classified |

## Matrix entry format

Every task's matrix row must contain:

| Field | Content |
|---|---|
| Recommended model | Tier + current default name |
| Why | One line tied to a routing rule above |
| Expected inputs | The SPEC sections, files, and prior-task outputs the agent needs (assume no other context) |
| Expected outputs | Concrete artifacts: files changed, tests added, migration scripts |
| Success criteria | The task's validation condition, verbatim from the task table |

## Cost sanity check

After assigning, review the distribution: if >40% of tasks landed in the Reasoning tier, the plan's tasks are under-specified — go back and make more decisions in the SPEC so cheaper tiers can execute them.
