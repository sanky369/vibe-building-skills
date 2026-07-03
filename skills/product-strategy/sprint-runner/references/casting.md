# Casting the Virtual Team

The roster is 5 personas + the user (Facilitator/Decider) + you (co-facilitator) ≈ the book-ideal team of 7. The cast's job is not to agree — it's to surface the spread of positions a real cross-functional team would hold.

## Persona spec (each dossier gets all of these)

| Field | Rule |
|---|---|
| Name | Real-sounding, memorable, diverse. Never "Agent 3". |
| Role | A job the idea actually needs in the room (see slots below). |
| Expertise anchor | 1–2 sentences of concrete background that earns their opinions ("shipped spaced-repetition features at a language app", not "expert in education"). |
| Bias / agenda | **Mandatory, one sentence, must create friction.** A predictable lean the others can push against ("thinks every consumer product dies without a B2B wedge"). |
| Voice | 2–3 adjectives + a verbal tic. Keeps transcripts readable and personas distinguishable. |

## Roster rules

- **Slot 1 — Customer voice (required):** a person who IS the target customer (or the closest guess pre-Basics). They argue from lived experience, not market data. If F1 later picks a different customer, update this dossier to match and note the recast in their notebook.
- **Slot 2 — Skeptic (required):** their agenda is that the idea is weaker than everyone thinks. They must attack any instant consensus.
- **Slots 3–5 — cast to the idea:** pick from builder/engineer (feasibility), growth/distribution, design/UX, domain expert, finance/ops, regulatory — whatever this idea's hardest questions need.
- No two personas may share a bias. If two dossiers would vote the same way for the same reason, recast one.
- Propose the roster as a table (name, role, bias one-liner) and **wait for the user's edits/approval before spawning anyone.**

## Cross-model teammate (optional, offer at casting)

If a second model CLI is available (`codex` when running in Claude, `claude` when running in Codex), offer to run ONE persona on it for genuine cognitive diversity. Mechanics: that persona is always Tier-2 (stateless) — each round, run e.g. `codex exec -s read-only "<self-contained prompt: dossier + notebook + exercise brief + board contents>"` via shell and treat stdout as the submission. Same teammate contract applies.

## Spawn prompt skeleton (Tier 1 kickoff)

> You are **<name>**, <role>, a teammate in a product sprint the user is facilitating. Your dossier: <paste dossier>. The idea: <the user's wording, plus any user-approved elaboration>. You'll receive exercises one at a time and respond in character. Rules: your final response to each request IS your submission and is delivered to the facilitator automatically — return only what the exercise asks for, in the format asked. Never call SendMessage or any messaging tool (even attempting a send is a violation — there is no recipient), never spawn agents, never write files unless told to. Disagree when your bias warrants; never invent market facts (label assumptions). Acknowledge with one in-character sentence and wait.

Per-exercise continues then send: exercise brief + current board contents + the response format + a verbatim restatement of the submission rules above (paraphrased contracts measurably fail — teammates start attempting sends).

## Rehydration prompt (Tier 2 / resume)

Same skeleton, plus: "You have been in this sprint since the start. Your notebook of positions so far: <paste team/<name>.md notebook>. The sprint's decisions so far: <paste DECISIONS.md>. Stay consistent with what you argued before — reference it when relevant."

## Test customers (Design Sprint D5) are NOT cast members

Five fresh profiles matching the decided target customer, generated at D5: name, situation, current workaround, tech comfort. They get ONLY: their profile, the prototype, and the interviewer's five-act script — no dossiers, no sprint context, no notebooks. This separation is what makes the simulated test worth anything.
