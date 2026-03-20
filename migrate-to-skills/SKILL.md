---
name: migrate-to-skills
risk_tier: 2
description: >-
  Convert 'Applied intelligently' Cursor rules (.cursor/rules/*.mdc) and slash
  commands (.cursor/commands/*.md) to Agent Skills format (.cursor/skills/). Use
  when you want to migrate rules or commands to skills, convert .mdc rules to
  SKILL.md format, or consolidate commands into the skills directory.
disable-model-invocation: true
---
# Migrate Rules and Slash Commands to Skills

## Purpose

Converts Cursor rules ("Applied intelligently") and slash commands to Agent Skills format. Preserves body content verbatim—do not modify, reformat, or "improve" it. Tier 2: user approval required for file writes and deletions.

## When to Use

- User wants to migrate rules or commands to skills format
- User asks to convert `.mdc` rules to SKILL.md format
- User wants to consolidate commands into the skills directory
- User has "Applied intelligently" rules or slash commands to migrate

## Inputs

| Input | Description |
|-------|-------------|
| Source files | `.cursor/rules/*.mdc`, `.cursor/commands/*.md` (project or user) |
| Rules criteria | Has `description`; no `globs`; no `alwaysApply: true` |
| Commands | All slash commands (plain markdown) |

## Outputs

- **Migrated skills** — `.cursor/skills/{skill-name}/SKILL.md` for each rule or command
- **Original files** — Optionally deleted after verification

## Steps / Behavior

1. **Create skills directories** — `.cursor/skills/` (project), `~/.cursor/skills/` (user) if they don't exist.
2. **Find files to migrate** — Project: `{workspaceFolder}/**/.cursor/rules/*.mdc`, `{workspaceFolder}/**/.cursor/commands/*.md`; User: `~/.cursor/commands/*.md`. Ignore `~/.cursor/worktrees`, `~/.cursor/skills-cursor`.
3. **Filter rules** — Migrate only "Applied intelligently" rules: has `description`, no `globs`, no `alwaysApply: true`. Commands: migrate all.
4. **Convert each file** — Read source; create SKILL.md with new frontmatter + EXACT body content (character-for-character). Use read/edit/delete tools; do not use terminal.
5. **Delete originals** — After writing migrated file.
6. **Summarize** — List migrated files; inform user they can ask to undo.

### Rules: .mdc → SKILL.md

- Add `name` (from filename); keep `description`; remove `globs` and `alwaysApply`
- Preserve body content exactly

### Commands: .md → SKILL.md

- Add frontmatter: `name` (from filename), `description` (infer from content), `disable-model-invocation: true`
- Preserve body content exactly

**CRITICAL:** Copy body content character-for-character. Do not reformat, fix typos, or "improve" anything.

## Constraints

- **Trust Boundaries:** User input untrusted; validate paths to rules and commands. Safe: propose migrated files. Unsafe: file writes, deletion—require user approval. Preserve content verbatim: do not modify or reformat body content.
- **Output Validation:** Label as proposal; user verifies before applying. "These changes modify [files]. Review diff before applying." for migrations.
- **Limitations:** Only migrates "Applied intelligently" rules; always-apply and glob rules are excluded. Preserves body content verbatim; does not improve or reformat. Cursor-specific paths; other IDEs have different structures.
- **Safety Guardrails (Tier 2):** User approval required. Preserve content exactly. Inform user how to undo (ask agent to restore).

## Examples

See [examples.md](examples.md) for before/after conversion examples. Use [prompt-template.md](prompt-template.md) for structured invocation.

## Validation Checklist

- [ ] Confirm files to migrate (rules: description, no globs, no alwaysApply; commands: all)
- [ ] Verify target `.cursor/skills/` or `~/.cursor/skills/` exists
- [ ] Spot-check one migrated SKILL.md for content fidelity
- [ ] Ensure user knows how to undo (ask agent to restore)

## Portability Notes

Migration targets Cursor's skills format. Other AI IDEs may use different skill/rule structures; adapt paths and frontmatter accordingly.
