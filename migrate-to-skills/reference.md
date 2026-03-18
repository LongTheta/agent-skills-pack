# Migrate to Skills — Reference

## Migration Rules

| Source | Condition | Destination |
|--------|-----------|-------------|
| `.cursor/rules/*.mdc` | Has `description`, no `globs`, no `alwaysApply: true` | `.cursor/skills/{name}/SKILL.md` |
| `.cursor/commands/*.md` | All | `.cursor/skills/{name}/SKILL.md` |
| `~/.cursor/commands/*.md` | All | `~/.cursor/skills/{name}/SKILL.md` |

## Conversion Summary

### Rule → Skill

- Add `name` (from filename)
- Keep `description`
- Remove `globs`, `alwaysApply`
- Copy body verbatim

### Command → Skill

- Add `name` (from filename)
- Add `description` (infer from first heading)
- Add `disable-model-invocation: true`
- Copy body verbatim

## Exclusions

- `~/.cursor/worktrees`
- `~/.cursor/skills-cursor`
