# Create Subagent — Reference

## Subagent Locations

| Location | Scope | Priority |
|----------|-------|----------|
| `.cursor/agents/` | Current project | Higher |
| `~/.cursor/agents/` | All projects | Lower |

Project subagents override user subagents when names match.

## File Format

- **Extension:** `.md`
- **Structure:** YAML frontmatter + markdown body (system prompt)

## Required Frontmatter

| Field | Description |
|-------|-------------|
| `name` | Unique identifier; lowercase, hyphens |
| `description` | When to delegate; be specific; include trigger terms |

## Description Tips

- Include "use proactively" for automatic delegation
- Be specific: "Expert code review specialist" not "Helps with code"
- List trigger scenarios
