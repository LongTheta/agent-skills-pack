---
name: create-skill
risk_tier: 1
description: >-
  Guides users through creating effective Agent Skills for Cursor. Use when you
  want to create, write, or author a new skill, or asks about skill structure,
  best practices, or SKILL.md format.
---

# Create Agent Skills

## Purpose

Guides users through creating effective Agent Skills for Cursor. Skills are markdown files that teach the agent how to perform specific tasks. Produces skill directory with SKILL.md, examples.md, prompt-template.md, reference.md. Tier 1: proposals only; user reviews before applying.

## When to Use

- User wants to create, write, or author a new skill
- User asks about skill structure, best practices, or SKILL.md format
- User needs guidance on Agent Skills for Cursor
- User wants to add a specialized workflow or domain knowledge to the agent

## Inputs

| Input | Description |
|-------|-------------|
| Skill purpose | Primary use case and task |
| Target location | Personal (~/.cursor/skills/) or project (.cursor/skills/) |
| Trigger scenarios | When the agent should apply this skill |
| Output format preferences | Templates, formats, styles |
| Existing patterns | Examples or conventions to follow |

## Outputs

- **Skill directory** — SKILL.md, examples.md, prompt-template.md, reference.md
- **YAML frontmatter** — `name`, `description`, optional `risk_tier`
- **Body sections** — When to Use, Steps/Behavior, Constraints, Validation Checklist

## Steps / Behavior

1. **Discovery** — Gather purpose, storage location, trigger scenarios, requirements, existing patterns.
2. **Design** — Draft skill name (lowercase, hyphens, max 64 chars); write specific third-person description; outline sections; identify supporting files.
3. **Implementation** — Create directory structure; write SKILL.md with frontmatter; create reference, examples, prompt-template; add utility scripts if needed.
4. **Verification** — Verify SKILL.md under 500 lines; check description includes trigger terms; ensure consistent terminology; verify file references one level deep.

### Skill File Structure

```
skill-name/
├── SKILL.md              # Required - main instructions
├── reference.md          # Optional - detailed documentation
├── examples.md           # Optional - usage examples
└── scripts/              # Optional - utility scripts
```

### Description Best Practices

- **Third person** — "Processes Excel files and generates reports" (not "I can help you")
- **Specific and include trigger terms** — What + when
- **Both WHAT and WHEN** — Capabilities and trigger scenarios

### Core Authoring Principles

- **Concise** — Challenge each piece: does the agent really need this?
- **Under 500 lines** — Use progressive disclosure; put details in reference.md
- **Progressive disclosure** — Essential in SKILL.md; detailed in reference files
- **Appropriate degrees of freedom** — Match specificity to task fragility (high/medium/low)

### Anti-Patterns to Avoid

- Windows-style paths (use `/` not `\`)
- Too many options (provide default with escape hatch)
- Time-sensitive information (use "old patterns" section for deprecated)
- Inconsistent terminology
- Vague skill names (use `processing-pdfs` not `helper`)

## Constraints

- **Trust Boundaries:** User input untrusted; validate paths and skill purpose. Output proposes skill files; user reviews before applying.
- **Output Validation:** Label as proposal; user applies. No overwrite without confirmation.
- **Limitations:** Cursor-specific paths and formats; adapt for other IDEs per portability guide. Cannot execute scripts; guides user to run them. Skill discovery depends on description quality.
- **Safety Guardrails (Tier 1):** Proposals only; user applies. No secrets in skills. Keep SKILL.md under 500 lines.

## Examples

See [examples.md](examples.md) for complete skill example (code-review). See [reference.md](reference.md) for detailed authoring patterns (template, examples, workflow, conditional workflow, feedback loop, utility scripts).

## Validation Checklist

- [ ] Description includes trigger terms
- [ ] SKILL.md under 500 lines
- [ ] Examples and prompt-template present
- [ ] File references one level deep

## Portability Notes

Skill structure (SKILL.md, examples, reference) is IDE-agnostic. Cursor paths (`~/.cursor/skills/`) differ for other IDEs; see portability guide.
