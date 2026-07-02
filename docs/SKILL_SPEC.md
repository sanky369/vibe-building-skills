# Skill Authoring Spec

This is the quality bar every `SKILL.md` in this repo must meet. A skill is not
documentation a human reads — it is an **operating procedure an AI agent loads
and executes** when a user asks for the work. The reference implementation is
`skills/product-strategy/foundation-sprint/SKILL.md`; when in doubt, match its
register and structure.

## The test of an effective skill

Load the skill, give the agent a one-line user request ("write my welcome
emails", "my checkout page feels off"), and the agent should be able to run the
whole engagement — ask the right intake questions, make the right decisions at
forks, produce a concrete deliverable in a defined format, and check it against
a quality bar — without the user having to know the methodology.

If a skill only *explains* a topic, it fails the test. Explanation belongs in
`references/`; the SKILL.md is a procedure.

## Rules

### 1. The frontmatter description is a trigger contract

- Third person, describing what the skill does and **when to invoke it**.
- Include the situations and literal user phrases that should trigger it
  ("Use when the user says X, asks for Y, or is doing Z — even if they never
  name the method").
- Name the deliverable it produces.
- One paragraph, under ~1024 characters.

### 2. Write to the agent, in imperative voice

- "Ask the user for X. Then draft Y. Never Z." — not "This skill teaches you…"
  or "Your brand voice is…".
- The user is a character in the procedure ("have the user pick one"), not the
  audience of the document.

### 3. Every skill has this operational skeleton

1. **One-paragraph mission** — what the skill produces and the single most
   important principle governing it.
2. **When to use / when not to** — including handoffs: "if the user actually
   needs X, use `skills/<category>/<name>` instead."
3. **Intake** — the minimum questions to ask (one tight batch), what to infer
   from context instead of asking, and a don't-stall rule: if enough is known,
   state assumptions and proceed.
4. **Workflow** — numbered steps with real decision rules at forks ("if B2B →
   …; if consumer → …"), not menus of options. Where the method has a
   convergence point, the agent proposes 3–5 genuinely distinct candidates and
   the user decides.
5. **Required output format** — a concrete template (markdown block) for the
   deliverable. This is the heart of the skill: two agents running the same
   skill on the same input should produce structurally identical artifacts.
6. **Quality bar / guardrails** — checkable pass/fail rules the agent applies
   to its own draft before delivering ("no hook longer than 12 words", "every
   claim cited or labeled assumption"), plus hard don'ts.
7. **Integration** — which sibling skills feed this one and which consume its
   output, referenced by path, with one line on what crosses the boundary.

### 4. Progressive disclosure

- SKILL.md stays lean — target ≤ ~350 lines. It must earn its context window.
- Deep material (full framework taxonomies, long example galleries, extended
  code listings) moves to `references/*.md`, each with a one-line pointer in
  SKILL.md saying **when** to read it ("Read `references/archetypes.md` when
  the user wants to compare archetypes in depth").
- Never delete unique domain substance to hit the line target — relocate it.

### 5. Kill boilerplate on sight

Delete: "Keywords" sections (matching happens on the description), generic
"Overview" throat-clearing, motivational filler, restated tables of contents,
"Next Steps" that just name another skill, human-team project timelines
("Week 1–2: …") — an agent does the work in one session; sequence by
dependency, not calendar.

### 6. Be accurate and current

- Referenced files, scripts, and model IDs must exist and be correct (the
  creative automation lives in `docs/fal_api.py` / `docs/creative_cli.py` and
  uses the single FAL.ai model `fal-ai/nano-banana-pro`).
- Refer to sibling skills by directory path, never by ordinal ("Skill 02").
- No invented statistics or fake benchmark numbers; label heuristics as
  heuristics.

### 7. Orchestrators route, they don't lecture

A category orchestrator is a dispatcher: diagnose the situation with the
fewest questions, then route to concrete skill sequences by dependency,
stating what artifact each step passes to the next. It should read like a
routing table with decision rules, not a strategy essay.

## Definition of done (per skill)

- [ ] Description triggers on realistic user phrasings and names the deliverable
- [ ] Body is imperative, agent-addressed throughout
- [ ] Intake, workflow with decision rules, required output format, quality
      bar, and integration section all present
- [ ] SKILL.md ≤ ~350 lines; depth relocated to `references/` with
      when-to-read pointers
- [ ] No keywords sections, no calendar timelines, no ordinal skill references
- [ ] All file paths, tool names, and model IDs verified against the repo
