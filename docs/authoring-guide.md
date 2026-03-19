# Authoring Guide

How to create and maintain Agent Skills for the Jade CI/CD Agent Skills Pack repository.

---

## Skill Structure

Each skill lives in its own directory. Required and optional files:

| File | Required | Purpose |
|------|----------|---------|
| `SKILL.md` | Yes | Main skill definition; frontmatter + instructions |
| `examples.md` | Recommended | Example prompts and usage scenarios |
| `prompt-template.md` | Recommended | Invocation templates with placeholders |
| `reference.md` | Optional | Detailed reference material |

---

## SKILL.md Format

### Frontmatter

```yaml
---
name: skill-name
description: Brief description. Use when [trigger scenarios]. Include trigger terms for discovery.
---
```

**Required fields:**

- `name` — Lowercase, hyphens only, max 64 chars. Must match directory name.
- `description` — Max 1024 chars. Third person. Include WHAT and WHEN.

**Optional fields:**

- `disable-model-invocation: true` — For skills that must be explicitly invoked (e.g., shell, migrate-to-skills)

### Body

- Clear sections: When to Use, Workflow, Output Format, Guidelines
- Link to `reference.md`, `examples.md`, `prompt-template.md` where relevant
- Keep under 500 lines; use progressive disclosure for detail

---

## Description Best Practices

1. **Third person:** "Evaluates tools for enterprise adoption" not "I can evaluate tools"
2. **Trigger terms:** Include keywords: "Use when reviewing pipelines, GitOps, Argo CD..."
3. **WHAT + WHEN:** Capability + when the agent should apply the skill

---

## Progressive Disclosure

Put essential instructions in `SKILL.md`. Move detailed criteria, API references, and extended examples to:

- `reference.md` — Criteria, decision trees, API details
- `examples.md` — Example prompts and sample outputs
- `prompt-template.md` — Copy-paste templates with placeholders

---

## Adding a New Skill

1. Create directory: `skill-name/`
2. Add `SKILL.md` with frontmatter and body
3. Add `examples.md` with 3–5 example prompts
4. Add `prompt-template.md` if the skill benefits from structured invocation
5. Add `reference.md` if detailed criteria or APIs are needed
6. Update `skills-manifest.json` with the new skill entry
7. Run `npm run validate` to verify

---

## Validation

Before submitting:

```bash
npm run validate
# Optional: regenerate manifest from folders
npm run generate-manifest
```

---

## See Also

- [Skill Style Guide](skill-style-guide.md) — Writing conventions
- [Portability Guide](portability-guide.md) — Adapting for other IDEs
