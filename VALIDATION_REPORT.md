# Validation Report

**Date:** 2025-03-18  
**Validator:** `scripts/validate_skills.py`  
**Status:** Standard validation **PASSED**

---

## Summary

All skills pass standard validation. Defects identified by the validator have been repaired.

---

## Defects Repaired

### 1. Malformed Frontmatter

| Skill | Issue | Fix |
|-------|-------|-----|
| **ai-agent-architecture** | `risk_tier` merged with `description` (YAML parse error) | Split into separate `risk_tier: 0` and multi-line `description` |

### 2. Missing Required Sections

| Skill | Missing | Fix |
|-------|---------|-----|
| **ai-agent-architecture** | Safety Guardrails / Validation Checklist / Enforcement | Added Safety Guardrails section |
| **create-rule** | When to Use, Safety Guardrails | Added When to Use, Safety Guardrails, Validation Checklist |
| **create-skill** | When to Use | Added When to Use (had Validation Checklist, Portability Notes) |
| **migrate-to-skills** | When to Use | Added When to Use |
| **shell** | When to Use | Added When to Use |
| **tool-evaluator** | Safety Guardrails | Added Safety Guardrails |
| **update-cursor-settings** | When to Use | Added When to Use |

### 3. Broken Links

| Skill | Link | Fix |
|-------|------|-----|
| **create-skill** | `../../docs/portability-guide.md` | Corrected to `../docs/portability-guide.md` |
| **create-skill** | `STANDARDS.md` (in example) | Changed to `reference.md` (standard skill structure) |

### 4. Inconsistent Structure (Recommended Sections Added)

To align with full SKILL.md standards, the following sections were added where missing:

| Skill | Sections Added |
|-------|----------------|
| **ai-agent-architecture** | Inputs, Outputs, Limitations, Validation Checklist, Portability Notes |
| **create-rule** | Inputs, Outputs, Limitations, Portability Notes |
| **create-skill** | Inputs, Outputs |
| **migrate-to-skills** | Inputs, Outputs, Limitations, Portability Notes |
| **shell** | Inputs, Outputs, Limitations, Validation Checklist, Portability Notes |
| **tool-evaluator** | Inputs, Outputs, Limitations, Validation Checklist, Portability Notes |
| **update-cursor-settings** | Inputs, Outputs, Limitations, Portability Notes |

---

## Validation Results

### Standard Validation (Required Checks)

```
All skills valid.
```

**Checks:** Required files, YAML frontmatter, When to Use, Safety Guardrails (or Validation Checklist / Enforcement), risk_tier, links, manifest alignment, Tier 2/3 enforcement.

### Strict Validation (Recommended Sections)

Some skills still lack recommended sections when run with `--strict`:

| Skill | Missing Recommended Sections |
|-------|------------------------------|
| ai-devsecops-policy-enforcement | Inputs, Outputs |
| create-subagent | Inputs, Outputs, Limitations, Portability Notes |
| cve-detect-and-remediate | Inputs, Outputs |
| dod-zero-trust-architect | Inputs, Outputs |
| zero-trust-gitops-enforcement | Inputs, Outputs |

---

## Skills Needing Manual Editorial Judgment

The following skills pass standard validation but may benefit from manual review to add recommended sections (Inputs, Outputs, Limitations, Portability Notes) for consistency:

1. **ai-devsecops-policy-enforcement** — Add Inputs, Outputs
2. **create-subagent** — Add Inputs, Outputs, Limitations, Portability Notes
3. **cve-detect-and-remediate** — Add Inputs, Outputs
4. **dod-zero-trust-architect** — Add Inputs, Outputs
5. **zero-trust-gitops-enforcement** — Add Inputs, Outputs

These skills have strong content; the additions would improve discoverability and consistency with the full SKILL.md standard.

---

## Linked Docs Updated

- **create-skill/SKILL.md** — Portability Notes link corrected to `../docs/portability-guide.md` (file exists at `docs/portability-guide.md`)
- **create-skill/SKILL.md** — Example updated to use `reference.md` instead of `STANDARDS.md` (no new file created; example now matches standard skill structure)

---

## Standards Enforced

Every repaired SKILL.md now includes:

- Valid YAML frontmatter
- Clear title/summary metadata (`name`, `description`, `risk_tier`)
- When to Use
- Inputs
- Outputs
- Workflow or steps
- Limitations
- Safety Guardrails (or Validation Checklist / Enforcement)
- Validation Checklist (for Tier 2)
- Portability Notes (where applicable)
