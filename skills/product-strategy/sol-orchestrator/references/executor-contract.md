# Executor contract

Use this compact contract for every delegated task. Fill only fields that change behavior.

```markdown
Role: Execute one bounded implementation task. Do not redesign the parent plan or spawn more agents.

Goal: <observable task outcome>

Success criteria:
- <binary behavior or artifact check>
- <exact validation command and expected result>

Owned files:
- <paths this agent may edit>

Do not touch:
- <overlapping, user-owned, generated, or out-of-scope paths>

Verified context:
- <file:line or symbol evidence>
- <decided interface or prior-task artifact>

Constraints:
- preserve existing conventions and unrelated changes
- do not change contracts outside the stated task
- stop and report if the task requires an undecided architecture change

Validation:
- run <commands>
- if a command cannot run, return the exact blocker and next-best check

Return exactly:
- status: complete | partial | blocked
- files_changed: paths
- checks: command and result
- findings: concise facts
- risks_or_handoffs: remaining work or None
```

For read-only exploration, replace `Owned files` with `Search scope` and require file-and-line evidence. For hostile review, omit the intended fix and expected conclusion; provide the artifact, requirements, and review categories only.

Keep prompts outcome-first. State invariants once, use decision rules for judgment calls, and include a stop condition. Do not paste the full parent conversation.
