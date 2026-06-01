# Contributing

Thanks for improving Vibe Building Skills. This repo is meant to stay practical, safe, and easy to install as a collection of standalone Claude Skills.

## What Makes a Good Contribution

- A new skill that solves a real builder workflow
- Improvements to an existing skill's clarity, examples, or sequencing
- Documentation that makes installation or usage easier
- Security improvements, especially around API keys and local credentials
- Validation scripts or tests that catch broken skill metadata

## Skill Guidelines

Each skill should:

- Live in its own directory under `skills/<category>/<skill-name>/`
- Include a `SKILL.md` file with `name` and `description` frontmatter
- Be usable on its own without requiring the reader to inspect unrelated skills
- Prefer concrete workflows, checklists, examples, and decision points
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
