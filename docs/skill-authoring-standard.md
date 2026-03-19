# Skill Authoring Standard

Required structure and sections for skills in the Jade CI/CD Agent Skills Pack.

## SKILL.md Structure

Every SKILL.md must include:

| Section | Required | Purpose |
|---------|----------|---------|
| **YAML frontmatter** | Yes | `name`, `description`; optional `disable-model-invocation` |
| **When to Use** | Yes | Trigger scenarios; when agent should apply |
| **Inputs** | Yes | What the skill expects (table or list) |
| **Outputs** | Yes | What the skill produces |
| **Workflow** | Yes | Steps or process |
| **Limitations** | Yes | What the skill cannot do; advisory scope |
| **Safety Guardrails** | Yes | Risk tier; constraints; no auto-apply where inappropriate |
| **Validation Checklist** | Yes | Pre-output verification |
| **Portability Notes** | Recommended | IDE compatibility; adaptation guidance |

## Frontmatter

```yaml
---
name: skill-name
description: [Third person; WHAT + WHEN; trigger terms]
---
```

## Risk Tiers

Declare in manifest; enforce in skill:

- **Tier 0**: Read-only; no execution
- **Tier 1**: Content generation; user applies
- **Tier 2**: Code/config proposal; review before apply
- **Tier 3**: Pipeline/infra; explicit approval required

## Supporting Files

| File | When |
|------|------|
| `examples.md` | 3+ example prompts |
| `prompt-template.md` | Structured invocation with placeholders |
| `reference.md` | Detailed criteria, APIs, decision trees |

## See Also

- [Authoring Guide](authoring-guide.md)
- [AI Security Model](ai-security-model.md)
- [Skill Style Guide](skill-style-guide.md)
