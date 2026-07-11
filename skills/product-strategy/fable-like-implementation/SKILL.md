---
name: fable-like-implementation
description: Use when the session model is Opus 4.8 (claude-opus-4-8) and the user asks to build, add, implement, refactor, migrate, or integrate something non-trivial — 3+ files, a new dependency or subsystem, an API contract or database schema change, or meaningful ambiguity or risk — or says "plan this out", "spec this", "how should we build", "create an implementation plan". Also use when the user says "just implement it" but the work is non-trivial. Do NOT use on Claude Fable 5 or any other model, nor for one-line fixes, typo corrections, single-function changes, or questions that require no code change.
---

# Fable-Like Implementation Planning

Transform an initial request into an implementation-ready engineering plan. **No production code is written by this skill.** The output is a plan package another agent (or human) can execute with minimal clarification.

## When this skill applies — and when it must not

**Model gate (check first):** this skill runs ONLY when the current session model is **Opus 4.8** (`claude-opus-4-8`). Check your own model identity from the system prompt/environment. If you are Claude Fable 5 or any other model, do not execute this skill — handle the request normally without it. Do not switch models or claim to be Opus 4.8 to satisfy the gate; the gate reflects the user's routing preference, not a capability requirement to work around.

If the model gate passes, apply when ANY of these are true:
- Change spans 3+ files or introduces a new module/subsystem
- API contract, database schema, or public interface changes
- New dependency, framework, or external service integration
- Migration, large refactor, or anything with rollback concerns
- The request is ambiguous enough that two engineers would build different things

Skip (answer directly, no plan) when ALL of these are true:
- Single-file, low-risk, obvious change
- No new dependencies, no contract changes
- A competent engineer would just do it without a design doc

If skipped, say so in one line ("This is trivial — implementing directly") so the choice is visible.

## Hard rules (apply throughout)

1. **Never start implementation** until the plan is complete AND the user explicitly approves. The plan is the deliverable.
2. **Read `CLAUDE.md`** (repo root and any nested ones) before anything else. Its conventions override this skill's defaults.
3. **Reuse over rebuild** — every proposed new component must state why an existing one can't serve.
4. **Assumptions are first-class** — never silently assume. Every assumption gets logged with confidence (High/Med/Low) and the question that would resolve it.
5. **Cite sources** for load-bearing technical decisions (official docs URL + the specific claim relied on).

## Operating posture (governs how every stage executes)

**Read `references/operating-manual.md` now.** It is the full way of working this posture summarizes: eight practices in fixed order — reading the request beneath its literal words, cutting work into independently checkable pieces, spending effort where the risk lives, re-deriving claims instead of trusting recall, labeling known vs. guessed out loud, attacking your own conclusion, communicating answer→reasoning→risk, and the mistakes that look like competence — each with its procedure, a worked example, and the failure it prevents. It ends with a five-question self-test: run that self-test on **every** user-facing output before sending it — clarifying questions, summaries, and the final plan alike.

- **Facts by acting.** Never assert what a command can verify. Pin versions from lockfiles, run the build/lint/test commands to learn whether the baseline passes today, grep for real usage before claiming how something works.
- **Evidence discipline.** Every load-bearing claim about the codebase carries a `file:line` (or file + symbol) reference you gathered by actually reading it. No invented paths, no "probably".
- **Delegate width, keep depth.** If a subagent tool (Agent/Task/Explore) is available, dispatch parallel read-only subagents for wide scans and documentation research, and personally read only the files the plan will rely on. With or without subagents, batch independent tool calls into one message instead of running them serially.
- **User decisions are constraints, not alternatives.** If the user already chose a stack, approach, or naming, do not reopen it in the comparison.
- **Lead with conclusions.** In everything you present, the first sentence states the decision or finding; detail follows. State confidence honestly — neither hedge everything nor overclaim.

---

## Workflow

Execute the 10 stages in order. Stages 2 and 3 may interleave (research gaps discovered during the scan). Track stages in your todo list if available.

### Stage 1 — Understand the Request

Restate the request as: **Objective** (the outcome, not the mechanism), **Deliverables**, **Constraints** (stated + inferred), **Out of scope** (inferred — confirm in the plan's Non-Goals).

Ask clarifying questions ONLY if a wrong guess would invalidate most of the plan or cause irreversible harm (data deletion, breaking a public API, security posture). Everything else: make the most reasonable assumption, log it in the Assumptions register, and proceed. Batch any questions into one message — never drip-feed.

### Stage 2 — Scan the Codebase

If subagents are available, fan the scan out: dispatch 2–4 parallel read-only explorers with distinct missions — (a) architecture, layering, and conventions; (b) existing implementations of similar features; (c) the impact surface this feature touches; (d) tests, CI, and how verification runs. Each explorer returns a structured summary citing `file:line` evidence. Subagent summaries *locate* code; they don't verify it — personally read every file whose contents the plan will rely on.

Scan in this priority order, stopping when new files stop changing your mental model:

1. `CLAUDE.md`, `README`, `CONTRIBUTING`, ADRs / `docs/`
2. Manifests & configs: `package.json` / `pyproject.toml` / `go.mod`, lockfiles, `.env.example`, CI configs, Dockerfiles — this pins the **actual versions** in use
3. Entry points & routing (main, app bootstrap, route/handler registries)
4. The modules the feature will touch, plus their direct neighbors
5. Existing implementations of *similar* features — the strongest signal for conventions
6. Schema/migrations, shared utilities, and the tests covering the touched areas

Produce an **Architecture Snapshot**: stack + pinned versions, layering/patterns observed, naming and error-handling conventions, test framework and how tests are organized, and a list of reusable components relevant to this feature. Also list **Impact Areas**: every file/module likely to change or be at risk. Also record the **Verification Baseline**: the exact commands that build/lint/test this repo and whether each passes right now (run them) — a phase checkpoint that says "tests pass" is meaningless without today's status.

Do not read the whole repo. Depth where the feature lives, breadth elsewhere.

### Stage 3 — Gather Missing Knowledge

List knowledge gaps the plan actually depends on — not nice-to-knows. For each gap, research with this source hierarchy:

1. Official documentation / API references / RFCs
2. Source code or changelogs of the library itself
3. Issue trackers (known pitfalls, open bugs)
4. Reputable engineering blogs (last resort, verify against #1)

**Critical**: research the documentation for the version the repo actually pins (from Stage 2), not the latest version. Note any relevant breaking changes between the pinned and current versions.

Record findings as: *Question → Answer → Source → How it affects the plan.* Cover security advisories and performance characteristics for any new dependency. Gaps are usually independent of each other — if subagents are available, research them in parallel (one dispatch per gap), not serially.

### Stage 4 — Apply Relevant Skills

Check the available skills list for skills that address parts of this problem (e.g. framework-specific skills, testing-strategy, architecture/ADR, database, security-review skills). For each relevant one: read it, apply its guidance to the affected plan sections, and note in the plan which skill informed which decision. If skills conflict, repo conventions win, then the more specific skill.

### Stage 5 — Reason About the Solution

Identify **2–3 genuinely viable approaches** (not strawmen). For each: one-paragraph sketch, key trade-offs, and a rough cost (effort/risk).

**Feasibility gate — before the comparison table:** verify each candidate's load-bearing mechanism against the actual code. The extension point, hook, or data shape it depends on must be confirmed to exist, cited at `file:line`. The gate covers requirements too: an approach that cannot satisfy a stated requirement (with evidence of why) fails just as one whose mechanism doesn't exist. Either failure is recorded as rejected-with-evidence and never enters the comparison. Feasibility checks routinely send you back to Stages 2–3; that loop is normal, not a failure.

Compare the survivors in a table against the criteria that matter *for this feature* — typically a subset of: scalability, maintainability, performance, security, DX, testability, backward compatibility, migration cost, rollout complexity, failure modes.

Select one and write a short **Decision Record**: chosen approach, why it beats the alternatives (citing the feasibility evidence), what would make you revisit it. Then stress-test the chosen approach only against the full criteria list plus failure scenarios (what breaks, how it's detected, how it recovers).

### Stage 6 — Produce the Technical Specification

Write the SPEC using the exact template in `references/spec-template.md` (read it now). Every section is mandatory; write "None" rather than omitting a section, so downstream agents can rely on the structure. Depth follows blast radius: sections covering schema, auth, security rules, or public contracts get full treatment; inapplicable sections are one line ("None — <reason>"). Never pad a section to look thorough. File-level modifications must name real paths from Stage 2 with a one-line intent per file.

### Stage 7 — Generate the Implementation Plan

Use the structure in `references/plan-template.md` (read it now). Rules for the task breakdown:

- **Task sizing**: each task is completable by a coding agent in one focused session — roughly "one PR-sized coherent change": named files, a verifiable done-condition, and no hidden context. If you can't write the done-condition in one sentence, split the task.
- Every task lists: ID, description, files touched, dependencies (task IDs), parallelizable (Y/N), complexity (S/M/L), validation step.
- Phases end in a **checkpoint**: what must build/pass/be reviewed before the next phase starts.
- Front-load the riskiest/most-unknown task (fail fast); schema and contract changes come before their consumers.

### Stage 8 — Recommend a Sub-Agent per Task

Assign every task a model using `references/model-selection.md` (read it now). Route by task properties (ambiguity × blast radius × volume), not by habit. For each task record: recommended model, one-line justification, expected inputs, expected outputs, success criteria. Present this as the **Model Assignment Matrix**.

### Stage 9 — Validate, Then Attack the Plan

Run this checklist explicitly; fix failures before output:

- [ ] Every SPEC requirement maps to at least one task (build a quick traceability check)
- [ ] Every file in Impact Areas appears in some task, or its exclusion is justified
- [ ] No task depends on an undocumented decision
- [ ] Reuse: no proposed component duplicates something found in Stage 2
- [ ] All Low-confidence assumptions appear in Open Questions or Risks
- [ ] Rollback/rollout path exists for every irreversible change
- [ ] A stranger (agent or human) could execute this plan without asking you anything major

The checklist catches omissions; an **adversarial pass** catches wrongness. After the checklist passes:

- If subagents are available, dispatch a fresh-context critic with the draft plan file and repo access: "Attack this plan: what breaks in production, what's missing, what duplicates existing code, what's over-engineered? Concrete findings with `file:line` evidence only."
- If not, re-read only the draft plan (not your working notes) and attack it yourself from a hostile reviewer's stance.

Fix confirmed findings in the plan. Findings you dispute go into the Risk Register with your rebuttal — not into the void.

### Stage 10 — Output the Plan Package

Write the package as a single markdown file `docs/plans/<feature-slug>-plan.md` (create the directory if absent; follow repo conventions if a plans/RFC location already exists). Single file: downstream agents load one artifact into context. Section order is fixed:

1. Executive Summary (≤1 page; the first sentence states the chosen approach and recommendation, then what, why, effort, top 3 risks — complete sentences, unresolved risks stated plainly)
2. Technical Specification (Stage 6)
3. Architecture Notes (Stage 2 snapshot + how the feature fits)
4. Research Findings (Stage 3 table)
5. Implementation Plan (phases + milestones)
6. Task Breakdown (full task table)
7. Model Assignment Matrix (Stage 8)
8. Risk Register (risk, likelihood, impact, mitigation, owner-task)
9. Testing Strategy
10. Rollout Plan (flags, migration order, monitoring, rollback triggers)
11. Final Readiness Checklist (Stage 9 results)
12. Assumptions Register & Open Questions

Before presenting anything, run the **five-question self-test** from `references/operating-manual.md` against the package; any "no" gets fixed first, never shipped as a "mostly."

Then present to the user: the Executive Summary inline, the file location, and this exact closing move — **ask whether to (a) proceed to implementation, (b) revise the plan, or (c) stop here.** Do not begin coding without an explicit (a).
