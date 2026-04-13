# Account-Level Validation Prompts

Use these rules so the agent proactively prompts you to run validation when coding in any project.

## Option 1: Editor user rules (recommended for global)

1. Open your AI-assisted editor → **Settings** → **Rules for AI** (or equivalent; name varies by product).
2. Add this text to your **User Rules**:

```
When I'm working in a project with validation scripts, proactively prompt me in chat when relevant:
- After editing key files (schemas, configs, SKILL.md, architecture docs): "Run validation before committing, or I can run it for you."
- When I mention commit, push, or "ready to ship": "Before committing, run validation and tests. I can run them for you."
- When I ask about project health: "I can run validation and score for you. Say 'run validation' or 'run score'."
- When starting a session involving skills/architecture/review: "Want me to run validation or score?"
Do not be repetitive; prompt once per context. If I decline or already ran checks, don't prompt again in the same thread.
```

## Option 2: Global rules folder

If your environment loads rules from a user directory, place `.mdc` files in a path your tool documents, for example:

```
%USERPROFILE%\.agent\rules\
```

A pre-built file is in this repo at `docs/validation-prompts-global.mdc` — copy it into your user rules directory per your editor’s documentation.

## Option 3: Project-specific rules

Each project can have its own `.agent/rules/` (or equivalent) with project-specific commands:

| Project | Validation Commands |
|---------|---------------------|
| agent-skills-pack | `npm run validate`, `npm run lint:md`, `npm run score` |
| aws-repo-well-architected-advisor | `npm run validate`, `npm run validate:schemas`, `npm run test`, `npm run score` |

The AWS Well-Architected repo may ship `validation-prompts.mdc` under its project rules directory.

## Summary

- **Account-level (all projects):** Use Option 1 (user rules in settings) or Option 2 (global rules folder)
- **AWS Well-Architected repo:** May include `validation-prompts.mdc` with repo-specific commands
- **agent-skills-pack:** May include `project-conventions.mdc` with validation prompts when using project rules
