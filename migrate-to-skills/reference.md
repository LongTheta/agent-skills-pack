# Migrate to Skills — Reference

## Source → Destination

| Source pattern | Migrate when | Destination |
|----------------|--------------|-------------|
| `.agent/rules/*.mdc` | Has `description`, no `globs`, no `alwaysApply: true` | `.agent/skills/{name}/SKILL.md` |
| `.agent/commands/*.md` | All | `.agent/skills/{name}/SKILL.md` |
| `~/.agent/commands/*.md` | All | `~/.agent/skills/{name}/SKILL.md` |

## Frontmatter Mapping

**Rules (.mdc → SKILL.md):**

- Keep `description`
- Add `name` from filename (lowercase, hyphens)
- Remove `globs`, `alwaysApply` if present
- Body: verbatim

**Commands (.md → SKILL.md):**

- Add `name`, `description` (infer from content)
- Add `disable-model-invocation: true` when appropriate
- Body: verbatim

## Ignore

- Vendor cache, worktrees, and built-in skill dirs per your environment’s documentation.
