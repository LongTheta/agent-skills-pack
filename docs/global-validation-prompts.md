# Account-Level Validation Prompts

Use these rules so the agent proactively prompts you to run validation when coding in any project.

## Option 1: Cursor Settings > Rules (Recommended for Global)

1. Open **Cursor** → **Settings** (Ctrl+,) → **Rules for AI**
2. Add this text to your **User Rules**:

```
When I'm working in a project with validation scripts, proactively prompt me in chat when relevant:
- After editing key files (schemas, configs, SKILL.md, architecture docs): "Run validation before committing, or I can run it for you."
- When I mention commit, push, or "ready to ship": "Before committing, run validation and tests. I can run them for you."
- When I ask about project health: "I can run validation and score for you. Say 'run validation' or 'run score'."
- When starting a session involving skills/architecture/review: "Want me to run validation or score?"
Do not be repetitive; prompt once per context. If I decline or already ran checks, don't prompt again in the same thread.
```

## Option 2: Global Rules Folder

If Cursor picks up rules from your user directory, place `.mdc` files in:

```
%USERPROFILE%\.cursor\rules\
```

Example: `C:\Users\Cathy\.cursor\rules\validation-prompts-global.mdc`

A pre-built file is in this repo at `docs/validation-prompts-global.mdc` — copy it to `%USERPROFILE%\.cursor\rules\` (Windows) or `~/.cursor/rules/` (macOS/Linux).

## Option 3: Project-Specific Rules

Each project can have its own `.cursor/rules/` with project-specific commands:

| Project | Validation Commands |
|---------|---------------------|
| agent-skills-pack | `npm run validate`, `npm run lint:md`, `npm run score` |
| aws-repo-well-architected-advisor | `npm run validate`, `npm run validate:schemas`, `npm run test`, `npm run score` |

The AWS Well-Architected repo already has `validation-prompts.mdc` in `.cursor/rules/`.

## Summary

- **Account-level (all projects):** Use Option 1 (Settings > Rules) or Option 2 (global rules folder)
- **AWS Well-Architected repo:** Already has `validation-prompts.mdc` with repo-specific commands
- **agent-skills-pack:** Has `project-conventions.mdc` with validation prompts
