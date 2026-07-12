# Executor and reasoning selection

Route by ambiguity, blast radius, volume, and visual responsibility. Sol keeps decisions; executors receive decided work.

## Default team

| Agent | Model and effort | Use for | Avoid for |
|---|---|---|---|
| Sol root | `gpt-5.6` / Sol, high or xhigh only when needed | architecture, decomposition, synthesis, conflict resolution, final validation | bulk mechanical edits that a worker can own |
| Sol Light executor | `gpt-5.6-sol`, low (ChatGPT Light equivalent) | fast bounded coding, focused fixes, tool-heavy tasks, and small integrations where Sol judgment helps | open architecture, irreversible changes, or cheap repetitive work Luna can handle |
| Sol Medium executor | `gpt-5.6-sol`, medium | demanding but decided multi-file implementation, cross-cutting integration, nuanced tests, and complex repository navigation | tasks whose decisions must remain with the root or high-volume mechanical edits |
| Terra executor | `gpt-5.6-terra`, medium | ordinary multi-file features, integrations, refactors, test-backed implementation | unresolved architecture or irreversible changes without a Sol decision |
| Luna executor | `gpt-5.6-luna`, low | read-heavy scans, fixtures, boilerplate, renames, repetitive tests, bounded low-risk edits | security, schema design, subtle concurrency, ambiguous debugging |
| GPT-5.5 executor | `gpt-5.5`, high | high-blast-radius tasks, difficult debugging, migrations, public contracts | cheap high-volume work |
| GPT-5.5 reviewer | `gpt-5.5`, xhigh | independent hostile review of risky completed work | authoring the same task it reviews |
| UI executor | Claude Sonnet 5 via `claude -p --model sonnet --effort high` | frontend implementation, visual hierarchy, responsive states, refinement after rendering | backend architecture or final integration ownership |

Model IDs and availability drift. Prefer the configured custom agents `sol_light_executor`, `sol_medium_executor`, `terra_executor`, `luna_executor`, `gpt55_executor`, and `gpt55_reviewer` when installed. Otherwise steer the runtime in the delegation prompt and disclose the nearest-tier substitution.

## Decision rules

1. If architecture is still open, keep the decision with Sol before delegation.
2. If the work is bounded and straightforward but benefits from strong coding or tool judgment, use Sol Light.
3. If the design is settled but implementation is cross-cutting, nuanced, or context-heavy, use Sol Medium.
4. If the task is well-specified standard implementation and cost balance matters, use Terra medium.
5. If the task is mechanical, read-heavy, or high-volume with cheap rollback, use Luna low.
6. If a wrong change can corrupt data, weaken auth, or break a public contract, use GPT-5.5 high and a different xhigh reviewer.
7. If the task changes user-facing layout or interaction, use Sonnet 5 high and require render evidence.
8. If an executor fails twice, do not increase effort blindly. First repair missing criteria, dependencies, tool routing, or validation; then escalate one tier.
9. If more than roughly one third of tasks require high/xhigh executors, re-cut the plan: Sol has likely left too many decisions inside worker tasks.

Use medium as the default reasoning baseline. In Codex agent configuration, map the ChatGPT **Light** intelligence label to `model_reasoning_effort = "low"` and **Medium** to `"medium"`. Use high for complex logic and edge cases, and xhigh only when the quality gain justifies it. Never recommend max globally.

## Sources

- [GPT-5.6 prompting guidance](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)
- [OpenAI model catalog](https://developers.openai.com/api/docs/models)
- [Codex subagents and custom agent configuration](https://developers.openai.com/codex/agent-configuration/subagents)
