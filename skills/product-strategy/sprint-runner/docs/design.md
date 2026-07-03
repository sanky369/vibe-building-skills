# sprint-runner — Design Spec

Date: 2026-07-03 · Status: approved by user (with day-free amendment)

## Purpose

A personal skill that lets the user facilitate a Foundation Sprint (from *Click*) and/or a
Design Sprint (from *Sprint*) with a **virtual team of persistent subagent personas**. The
user is Facilitator + Decider. Claude (main session) is co-facilitator running the room.
Five persona teammates do the exercises — note-and-vote, sketching, lens plotting,
prototyping, testing — writing to a shared file-based sprint room.

Distinct from the existing `foundation-sprint` skill (a solo thinking session where Claude
stands in for the whole team): sprint-runner produces a *cast* of independent agents with
memory, biases, and disagreements, and the user runs the actual workshop.

## Core decisions (user-approved)

1. **Scope**: Both sprint types, chainable. Kickoff picks Foundation / Design / Foundation→Design.
2. **Pace**: Full workshop. Every exercise pauses for the user's notes, votes, and Decider call.
3. **Artifacts**: `sprints/<date>-<slug>/` in the invoking repo.
4. **Casting**: Skill proposes 5 personas tailored to the idea; user edits/approves before start.
5. **Day-free** (amendment): Sprint "days" are **outcome-gated phases**. A phase completes when
   its output artifact exists and the Decider call is logged; the next phase unlocks
   immediately. The whole chain can run in one sitting. Never schedule, never mention
   calendar days as gates; "Day 1/Monday" survive only as method vocabulary in reference docs.
6. **Harness-portable** (amendment): The skill must work in Claude Code, Codex, and any
   Agent-Skills-compatible harness. Self-contained (no references into other skills'
   directories), no hard dependency on Claude-Code-only tools — the team engine adapts to
   whatever the harness provides (see Capability tiers).

## Architecture

### Team mechanics — files first, agents as performance layer

The sprint room files are the single source of truth. Live agents are an enhancement
chosen by capability tier, so the same sprint works on any harness:

- **Tier 1 — persistent live team** (Claude Code: Agent + SendMessage): each approved
  persona is spawned once as a named background agent; every exercise continues the
  **same agent**, so teammates retain sprint memory and carry opinions forward.
- **Tier 2 — stateless workers** (any harness with one-shot subagents, or a shell that can
  run `codex exec` / `claude -p` sub-processes): each exercise spawns fresh per-persona
  workers that rehydrate from dossier + notebook, contribute, and exit.
- **Tier 3 — inline cast** (no subagents at all): the orchestrator itself plays each
  persona in strictly separated, sequential in-character turns, writing to the same files.
  Anonymized posting still applies.

Detection rule in SKILL.md: use the highest tier the harness supports; never fail because
a tool is missing. Rehydration from files also covers session breaks at every tier.

- Optional cross-model teammate: one persona runs on a different model (e.g. gpt-5.5 via
  `codex exec`, or Claude via `claude -p` when running inside Codex) for genuine cognitive
  diversity. Offered at casting; default on when a second CLI is available.
- Model choice: teammates default to the session model; this is user-facing creative
  output, taste matters.

### Sprint room layout

```
sprints/<YYYY-MM-DD>-<slug>/
  STATE.md          — sprint type, phase pointer, roster, agent status, resume protocol
  CHECKLIST.md      — phase-by-phase checklist (adapted from official checklists), checked live
  team/<name>.md    — persona dossier (role, expertise, bias/agenda, voice) + running notebook
  whiteboards/      — one file per exercise (notes boards, 2x2s, HMW board, heat maps, storyboard)
  DECISIONS.md      — every Decider call with the user's one-line reason
  OUTPUTS.md        — Founding Hypothesis, Mini Manifesto, Magic Lenses table, prototype link, test results
```

### The exercise engine (uniform protocol for every activity)

1. **Brief** — co-facilitator announces the exercise, creates the worksheet from a template,
   gives user and team identical instructions.
2. **Work Alone Together** — all teammates work in parallel (one SendMessage each, batched),
   returning structured in-character contributions.
3. **Post anonymized** — contributions go on the whiteboard unattributed where the method
   demands (note-and-vote, heat map); the user's entries are mixed in unlabeled too.
4. **User turn** — user reads the whiteboard, adds notes, casts votes (AskUserQuestion or free text).
5. **Team votes** — teammates vote without seeing the running tally.
6. **Decider call** — user commits; logged to DECISIONS.md; checklist box ticked; STATE.md advanced.

First-class method moves: Note-and-Vote, straw poll, heat map, speed critique, supervote,
Lightning Demos, Crazy 8s, solution sketch (annotated markdown/ASCII), storyboard,
five-act interview.

### Sprint content

- **Foundation Sprint phases** (own `references/foundation-sprint-method.md`, distilled —
  self-contained for portability, no cross-skill path dependency): Basics →
  Differentiation (2x2 + principles + Mini Manifesto) → Approach (Magic Lenses) →
  Founding Hypothesis + prove-it scorecard.
- **Design Sprint phases** (new `references/design-sprint-method.md`, distilled from the
  book/official checklist): Map (expert asks, HMW, target) → Sketch (Lightning Demos,
  4-step sketch) → Decide (art museum, heat map, speed critique, straw poll, supervote,
  storyboard) → Prototype (the team **actually builds it** in the repo — Claude Code
  advantage) → Test (5 fresh customer agents, never exposed to sprint context, interviewed
  against the prototype with the five-act script; results honestly labeled SIMULATED, with
  a standing nudge to run 5 real interviews).
- Chained mode: Design Sprint inherits the Founding Hypothesis; the sprint question and
  target derive from the riskiest assumption in the scorecard.

### Skill file layout

```
~/.claude/skills/sprint-runner/
  SKILL.md                                  — facilitation engine, capability tiers, casting rules,
                                              exercise engine, phase tables, resume protocol, guardrails
  references/foundation-sprint-method.md    — Foundation Sprint mechanics distilled, phase-gated
  references/design-sprint-method.md        — Design Sprint mechanics distilled, phase-gated
  references/casting.md                     — persona design guide + roster rules + cross-model teammate
  references/templates/                     — STATE, CHECKLIST(foundation/design), dossier,
                                              whiteboard variants, DECISIONS, OUTPUTS, interview script
```

Portability constraints on SKILL.md: standard Agent Skills frontmatter only (name +
description); all instructions phrased capability-first ("if the harness can spawn
persistent agents...") rather than tool-name-first; user interaction falls back from
structured question tools to plain-text prompts.

Casting rules: always one **customer-voice** persona matching the target customer; always
one **skeptic**; remaining three tailored to the idea's domain (e.g., engineer, growth,
domain expert). Roster of 5 + user + co-facilitator ≈ book-ideal 7.

## Guardrails

- The Decider is the user, always. Teammates never converge on their own; ties and calls
  go to the user. Claude co-facilitates but does not vote unless invited.
- Anonymity where the method demands it — no authority bias.
- Personas must disagree when their bias warrants; no yes-man chorus. Bias is written into
  each dossier explicitly.
- Simulated test results are labeled simulated; the skill never claims real validation.
- Phase gates are artifacts + logged decision, never time.
- Files are the source of truth; agents are a performance layer over them.

## Out of scope (v1)

- Miro/visual board integration (whiteboards are markdown).
- Multi-human sprints.
- Automatic scheduling/cron.
