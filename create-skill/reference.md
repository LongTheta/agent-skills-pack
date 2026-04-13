# Create Skill — Reference

## Skill Directory Structure

```
skill-name/
├── SKILL.md              # Required
├── reference.md          # Optional — detailed docs
├── examples.md           # Optional — usage examples
├── prompt-template.md    # Optional — invocation templates
└── scripts/             # Optional — utility scripts
```

## Storage Locations

| Type | Path | Scope |
|------|------|-------|
| Personal | `~/.agent/skills/skill-name/` | All projects |
| Project | `.agent/skills/skill-name/` | Shared with team |

Use the directory your AI tooling documents for custom skills; align with vendor guidance for reserved or built-in paths.

## SKILL.md Frontmatter

| Field | Requirements |
|-------|--------------|
| `name` | Max 64 chars; lowercase, hyphens only |
| `description` | Max 1024 chars; third person; include trigger terms |

## Description Best Practices

- **Third person:** "Processes Excel files" not "I can help you"
- **WHAT + WHEN:** Capability + trigger scenarios
- **Trigger terms:** Include keywords for discovery
