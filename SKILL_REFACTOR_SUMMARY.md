# SKILL.md Refactor Summary

## Overview

All 20 SKILL.md files in **Jade CI/CD Agent Skills Pack** were refactored to follow a strict, consistent structure. Security-evaluator was already in the target format and served as the reference template.

## Files Changed

### Skills Refactored (19)

| Skill | Category | Risk Tier |
|-------|----------|-----------|
| ai-agent-architecture | security-compliance | 0 |
| ai-devsecops-policy-enforcement | security-compliance | 3 |
| cve-detect-and-remediate | security-compliance | 2 |
| dod-zero-trust-architect | security-compliance | 0 |
| tool-evaluator | security-compliance | 0 |
| zero-trust-gitops-enforcement | security-compliance | 2 |
| create-repo-foundation | repo-lifecycle | 2 |
| test-strategy-designer | repo-lifecycle | 1 |
| repo-docs-writer | repo-lifecycle | 1 |
| release-pipeline-designer | repo-lifecycle | 2 |
| ai-code-review-guardrails | repo-lifecycle | 1 |
| dependency-governance | repo-lifecycle | 1 |
| observability-bootstrap | repo-lifecycle | 2 |
| create-rule | ide-authoring | 1 |
| create-skill | ide-authoring | 1 |
| create-subagent | ide-authoring | 2 |
| migrate-to-skills | ide-authoring | 2 |
| shell | ide-authoring | 3 |
| update-cursor-settings | ide-authoring | 2 |

### Unchanged (1)

- **security-evaluator** — Already conformed to the target structure; used as reference.

### Scripts Updated

- `scripts/validate_skills.py` — Updated RECOMMENDED_SECTIONS to align with new structure; Constraints, Purpose, Steps, Behavior, Examples.
- `scripts/certification-score.js` — Updated REQUIRED_SECTIONS and SECTION_ALTERNATIVES; Trust Boundaries and Output Validation now accept content within Constraints section (bold subheadings or phrase match).

## Summary of Changes

### Structure Applied (Order)

1. **Title (H1)** — Skill name as main heading
2. **Purpose** — 1–2 sentences: scope, what it does, when to invoke
3. **When to Use** — Explicit trigger conditions, bullet list
4. **Inputs** — Table or list
5. **Outputs** — What the skill produces
6. **Steps / Behavior** — Workflow, process, numbered steps
7. **Constraints** — Consolidated: Trust Boundaries + Output Validation + Limitations + Safety Guardrails
8. **Examples** — Reference to examples.md or inline
9. **Validation Checklist** — Present for Tier 2/3; retained for Tier 0/1 where useful
10. **Portability Notes** — When applicable

### Normalization

- **Language:** Clear, direct, explicit triggers
- **Duplication removed:** Trust Boundaries, Output Validation, Limitations, Safety Guardrails merged into Constraints
- **Consistency:** Same section order across all skills
- **DevSecOps/GitOps/Federal:** Explicit compatibility notes added where relevant (NIST, FedRAMP, DoD ZT)

### Domain Content Preserved

- All tables, templates, criteria, and evaluation frameworks retained
- 7-layer model (ai-agent-architecture)
- DoD 7 pillars, maturity model, scoring (dod-zero-trust-architect)
- Tool evaluation categories, data hydration (tool-evaluator)
- Enforcement areas, severity guidelines (zero-trust-gitops-enforcement)
- Remediation rules, data sources (cve-detect-and-remediate)
- Policy selection, auto-fix modes (ai-devsecops-policy-enforcement)
- Rule format, frontmatter (create-rule)
- Skill structure, authoring principles (create-skill)
- Subagent locations, examples (create-subagent)
- Migration workflow, conversion format (migrate-to-skills)
- Settings mappings (update-cursor-settings)

## Gaps and Overlaps Detected

### Gaps

- **create-skill:** Reference to `portability-guide.md` in Portability Notes — Jade has `docs/portability-guide.md`; reference is valid.
- **Nested skills:** Some skills may have nested folders; only the top-level SKILL.md in each manifest skill was refactored.

### Overlaps

- **security-evaluator vs tool-evaluator:** Both evaluate tools/systems; security-evaluator focuses on security/compliance; tool-evaluator on adoption fit, data hydration, operational burden. Clear separation maintained.
- **ai-code-review-guardrails vs security-evaluator:** Guardrails define process; security-evaluator does security assessment. Complements, not duplicates.
- **cve-detect-and-remediate vs dependency-governance:** Governance defines policy; CVE skill executes detection/remediation. Complements, not duplicates.
- **zero-trust-gitops-enforcement vs ai-devsecops-policy-enforcement:** ZT GitOps focuses on Zero Trust principles in pipelines; DevSecOps policy is broader (SBOM, secrets, compliance). Overlap in pipeline review; different emphasis and verdict models.

## Validation Results

- **npm run validate:** Pass
- **python scripts/validate_skills.py:** Pass
- **node scripts/certification-score.js:** Pass (9.8/10, threshold 7.5)

## Recommendations

1. Run `npm run validate:full` and `npm run lint:md` before committing.
2. Consider adding Purpose to frontmatter `description` for skills where it would improve discovery.
