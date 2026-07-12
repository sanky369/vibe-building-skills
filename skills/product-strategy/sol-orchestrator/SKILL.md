---
name: sol-orchestrator
description: Orchestrates non-trivial software implementation with GPT-5.6 Sol as the decision-making root and bounded Sol Light/Medium, Terra, Luna, GPT-5.5, and Claude Sonnet 5 executors. Use when the user asks to build, implement, integrate, migrate, refactor, or fix work spanning multiple files or systems; requests parallel agents or an implementation plan; or needs evidence-backed execution with specialist routing, review gates, and end-to-end validation. Produces a grounded specification, dependency-aware task graph, implemented changes when authorized, and a verified completion report. Skip trivial one-file changes and explanation-only requests.
---

# Sol Orchestrator

Turn a non-trivial engineering request into a grounded plan and a verified implementation. Keep GPT-5.6 Sol responsible for decisions, task boundaries, synthesis, conflict resolution, and final validation; delegate bounded execution to the cheapest capable specialist without surrendering architectural depth.

Read `references/operating-manual.md` before starting. Read `references/model-selection.md` before assigning agents. Read `references/executor-contract.md` before the first delegation. For UI work, also read `references/sonnet-ui-runbook.md`.

## Use and handoff rules

Apply this skill when the work has meaningful ambiguity, touches three or more files, crosses a contract or subsystem boundary, introduces a dependency, changes data or API shape, needs rollback planning, or benefits from independent agents.

Skip it for a low-risk edit that one agent can implement and verify immediately. State that choice in one sentence and proceed directly.

Prefer GPT-5.6 Sol (`gpt-5.6` or `gpt-5.6-sol`) as the root. If the runtime exposes an explicitly different root and cannot switch, do not impersonate Sol. Continue with the current root only when completion is already authorized, and disclose the substitution in the final report.

## Autonomy boundary

Interpret the user's verb before acting:

- For **plan, spec, review, explain, or diagnose**, inspect and produce the requested artifact. Do not implement production changes.
- For **build, implement, change, migrate, refactor, or fix**, make the in-scope local changes and run non-destructive validation without asking for routine approval.
- Ask before destructive actions, external writes, purchases, production deploys, irreversible migrations, or material scope expansion.

Keep this policy in one place. Do not add approval pauses between ordinary implementation waves.

## Intake

Derive from the request and repository:

- objective and user-visible outcome;
- deliverables and acceptance criteria;
- constraints, explicit choices, and non-goals;
- authority layer: plan-only or implementation-authorized;
- completion bar and stopping conditions.

Ask one batched clarification only when a wrong assumption would invalidate most work or create irreversible harm. Otherwise log assumptions with confidence and proceed.

## Workflow

### 1. Establish ground truth

Read `AGENTS.md`, `CLAUDE.md`, and nested equivalents that govern the target files. Inspect the README, manifests, lockfiles, entry points, neighboring modules, similar implementations, tests, CI, and current git status.

Run a small verification baseline when practical. Record exact commands and whether failures predate the work. Cite load-bearing code claims with real paths and lines or symbols.

Use read-only Luna or Terra agents in parallel for independent scans such as architecture, analogous features, tests, and impact surface. Their summaries locate evidence; Sol must personally inspect every file that drives a design decision.

### 2. Close only material knowledge gaps

Research version-specific behavior from official documentation first. Record each material finding as question, answer, source, and plan impact. Do not browse again merely to add examples or improve phrasing.

When tools return empty or suspiciously narrow results, try one or two meaningful fallbacks before calling the evidence absent. Label inference separately from retrieved fact.

### 3. Choose and specify the solution

For materially ambiguous architecture, compare two or three viable approaches after verifying that each required extension point exists. Reject infeasible options with evidence; do not include strawmen.

Write the chosen design with the structure in `references/spec-template.md`. Scale depth to risk. Name real files, contracts, state transitions, failure behavior, security/privacy concerns, rollout, rollback, and validation.

### 4. Build the execution graph

Use `references/plan-template.md`. Cut work into one-session tasks with independently checkable done conditions. Order contracts before consumers and the highest-risk unknown early.

For every task define:

- objective and acceptance criteria;
- owned files and prohibited overlap;
- dependencies and whether it can run in parallel;
- required inputs and expected artifacts;
- assigned executor and reasoning level;
- validation command and failure handoff.

Parallelize independent reads freely. Parallelize writes only when file ownership is disjoint and interfaces are already fixed. Otherwise run sequential waves. Keep nesting depth at one unless the environment explicitly requires deeper delegation.

### 5. Delegate bounded tasks

Keep Sol on the main thread. Use the routing matrix in `references/model-selection.md`:

- Luna for low-risk scans, mechanical edits, fixtures, and high-volume pattern work.
- Terra for standard feature implementation, integrations, and balanced coding work.
- Sol Light (`gpt-5.6-sol` with low effort) for fast bounded implementation that benefits from Sol's coding and tool judgment.
- Sol Medium (`gpt-5.6-sol` with medium effort) for demanding, well-specified cross-cutting work that does not need root-level architectural control.
- GPT-5.5 for high-blast-radius implementation, hard debugging, and independent adversarial review.
- Claude Sonnet 5 through `claude -p` for UI implementation and visual refinement.

Pass each executor the contract from `references/executor-contract.md`, not the entire conversation. Include the task, owned files, verified context, constraints, exact validation, and required return schema. Do not leak the expected answer to reviewers.

If a named model or custom agent is unavailable, use the nearest capable executor, preserve the requested reasoning posture, and record the substitution. Do not block the whole implementation on one unavailable worker.

### 6. Integrate by dependency wave

Wait for all tasks in a wave, then synthesize before starting dependent work. Inspect each returned diff and artifact; never treat an executor summary as proof.

Resolve overlaps centrally. If an executor failed, classify the failure:

- incomplete context: repair the contract and retry once;
- implementation defect: send one focused correction;
- repeated or architectural failure: escalate to GPT-5.5 high/xhigh or Sol;
- unavailable tool/model: substitute and disclose.

Do not allow executors to silently broaden scope or overwrite unrelated user changes.

### 7. Verify independently

Run targeted tests for changed behavior, then relevant type, lint, build, integration, or smoke checks. Compare failures with the baseline.

Use a different model from the author for high-risk review. Ask the reviewer to attack correctness, security, migrations, concurrency, regressions, and missing tests with concrete file evidence. Fix confirmed findings and log disputed ones with a reason.

For visual work, render and inspect the result for layout, clipping, responsive behavior, states, accessibility, and consistency with the existing design system. Sonnet's completion claim is insufficient without a render or the best available substitute.

### 8. Stop at the completion bar

Finish when:

- every accepted requirement maps to implemented and verified work, or is explicitly blocked;
- every task's done condition has evidence;
- integration checks pass or baseline failures are distinguished;
- unrelated user changes remain intact;
- no agent is still running and no unresolved overlap remains;
- risks, substitutions, and unrun checks are plainly reported.

Do not continue tool loops once the core request has enough evidence. If required evidence is still missing, name the missing fact and use the smallest useful fallback.

## Required output

For plan-only requests, write one repository-appropriate plan artifact, normally `docs/plans/<feature-slug>-plan.md`, containing:

1. executive summary and chosen design;
2. technical specification;
3. evidence and assumptions;
4. dependency graph and task table;
5. model assignment matrix;
6. testing, rollout, rollback, risks, and open questions;
7. readiness checklist.

For implementation-authorized requests, end with:

```markdown
Outcome: <what now works>

Implemented:
- <behavior and key files>

Agent execution:
- <task -> executor/reasoning -> result or substitution>

Verification:
- <command/check -> result>

Risks or gaps:
- <remaining risk, blocked check, or None>
```

Lead with the outcome. Preserve required facts, decisions, caveats, and next actions; remove narration and repeated process detail first.

## Quality bar

- Sol owns architecture, task seams, synthesis, and the final truth claim.
- Every executor has exclusive file ownership or runs in a sequential wave.
- Every load-bearing claim is verified, assumed with confidence, or unknown.
- Every task has a binary validation condition and a failure handoff.
- The author and high-risk verifier are different agents.
- UI changes preserve existing tokens and patterns and are rendered before completion.
- Reasoning effort rises only after checking for missing criteria, dependencies, routing, or validation instructions.
- No production action, destructive mutation, or scope expansion occurs without authorization.

Run the five-question self-test in `references/operating-manual.md` before every user-facing plan and final report.

## Integration

- Use `skills/product-strategy/fable-like-implementation` when the user wants the original Opus-gated, plan-only workflow.
- Use relevant framework, security, database, testing, and design skills to inform bounded tasks; repository conventions win conflicts.
- Feed an approved plan from this skill directly into its implementation waves without rebuilding the plan from scratch.
