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
| Personal | `~/.cursor/skills/skill-name/` | All projects |
| Project | `.cursor/skills/skill-name/` | Shared with team |

**Do not use:** `~/.cursor/skills-cursor/` — reserved for Cursor built-in skills.

## SKILL.md Frontmatter

| Field | Requirements |
|-------|--------------|
| `name` | Max 64 chars; lowercase, hyphens only |
| `description` | Max 1024 chars; third person; include trigger terms |

## Description Best Practices

- **Third person:** "Processes Excel files" not "I can help you"
- **WHAT + WHEN:** Capability + trigger scenarios
- **Trigger terms:** Include keywords for discovery
