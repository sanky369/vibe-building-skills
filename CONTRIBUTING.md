# Contributing

Thanks for improving Vibe Building Skills. This repo is meant to stay practical, safe, and easy to install as a collection of standalone agent skills.

## What Makes a Good Contribution

- A new skill that solves a real builder workflow
- Improvements to an existing skill's clarity, examples, or sequencing
- Documentation that makes installation or usage easier
- Security improvements, especially around API keys and local credentials
- Validation scripts or tests that catch broken skill metadata

## Skill Guidelines

Every skill must meet the authoring standard in [`docs/SKILL_SPEC.md`](docs/SKILL_SPEC.md) — a skill is an operating procedure an AI agent executes, not documentation a human reads. In short, each skill should:

- Live in its own directory under `skills/<category>/<skill-name>/`
- Include a `SKILL.md` file with `name` and `description` frontmatter, where the description is a trigger contract (what it does, when to invoke it, what it produces)
- Be written to the agent in imperative voice, with intake questions, a workflow with decision rules, a required output format, and a quality bar
- Keep `SKILL.md` lean (≤ ~350 lines) and move deep material to `references/*.md` with when-to-read pointers
- Be usable on its own without requiring the reader to inspect unrelated skills
- Avoid hardcoded secrets, tokens, private URLs, or personal credentials

## Before Opening a Pull Request

Run these quick checks:

```bash
find skills -name SKILL.md | sort
rg -n "api[_-]?key|secret|token|password" .
```

Review any secret-like matches before committing. Placeholder examples are fine when clearly labeled, but real keys must never be committed.

## Maintainer Focus

The maintainer roadmap is to add automated validation for skill metadata, improve examples, and make contribution review faster without lowering quality.
