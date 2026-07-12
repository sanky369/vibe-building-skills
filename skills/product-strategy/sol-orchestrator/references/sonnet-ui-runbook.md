# Claude Sonnet 5 UI executor

Use this route only for a bounded UI task with decided product behavior and exclusive file ownership.

## Preconditions

- Confirm `claude` is installed and `claude --version` succeeds.
- Inspect the existing design tokens, components, responsive conventions, and relevant screenshots or running UI.
- Keep backend contracts and shared files out of the Sonnet task unless explicitly owned.
- Do not run Sonnet concurrently with another writer on overlapping files.

## Invocation

Write the executor contract to a temporary prompt file under the task workspace, then run from the repository root:

```bash
claude -p \
  --model sonnet \
  --effort high \
  --permission-mode auto \
  --output-format json \
  < "$PROMPT_FILE"
```

The `sonnet` alias intentionally tracks the installed Claude Code client's current Sonnet model; record the resolved client version and disclose if Sonnet 5 is unavailable. Do not use `--dangerously-skip-permissions`.

The prompt must require:

- preservation of the existing design system and product behavior;
- owned files and prohibited paths;
- loading, empty, error, disabled, and responsive states that matter;
- accessibility requirements;
- targeted tests or build checks;
- rendering and visual inspection before completion;
- the standard executor return schema.

## Parent verification

Treat JSON output as a report, not proof. Sol must inspect the diff, run the relevant checks, render the UI, and check layout, clipping, spacing, responsive behavior, interaction states, and visual consistency. Send one focused correction when needed; after repeated failure, reassign or finish the bounded integration centrally.
