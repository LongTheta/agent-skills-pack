# AI Security Model

Trust boundaries and risk tiers for agent skills in this repository.

## Trust Boundaries

| Boundary | What It Is | Trust Level |
|----------|------------|-------------|
| **User input** | Prompts, queries, file paths | Untrusted; validate and sanitize |
| **Repo content** | Skills, examples, reference docs | Curated; assume good intent |
| **Linked documents** | External URLs, docs outside repo | Untrusted; verify before use |
| **Generated commands** | Shell, API calls, config changes | Untrusted; require explicit user approval |
| **Security/compliance claims** | Verdicts, recommendations, scores | Advisory only; no legal guarantee |

## Risk Tiers

| Tier | Description | Guardrails |
|------|--------------|------------|
| **Tier 0** | Read-only guidance | No execution; no file writes |
| **Tier 1** | Content generation | Proposals only; user applies |
| **Tier 2** | Code/config proposal | Diffs; review before apply |
| **Tier 3** | Pipeline/infra/security-impacting | Mandatory review; explicit approval |

### Tier 0: Read-Only Guidance

- Architecture reviews, evaluations, assessments
- No commands, no file writes, no API calls
- Examples: security-evaluator, tool-evaluator, ai-agent-architecture

### Tier 1: Content Generation

- Generates text, docs, templates
- User copies and applies manually
- Examples: create-rule, create-skill, prompt-template outputs

### Tier 2: Code/Config Proposal

- Proposes diffs, patches, config changes
- User must review and apply
- Examples: cve-detect-and-remediate (auto-fix suggest), create-subagent

### Tier 3: Pipeline/Infra/Security-Impacting

- Can modify CI/CD, infra, security controls
- Requires explicit user approval
- Examples: ai-devsecops-policy-enforcement (auto-fix apply), zero-trust-gitops-enforcement (blocking verdicts)

## Guardrails by Tier

| Tier | Required |
|------|----------|
| 0 | State assumptions; call out unknowns |
| 1 | Clear "proposal" labeling; no auto-apply |
| 2 | **Validation Checklist** — Must include Validation Checklist section in SKILL.md |
| 3 | **Human review** — Outputs require human review before applying |

## Enforcement Rules

| Rule | Applies To | Requirement |
|------|------------|-------------|
| **Validation Checklist** | Tier 2 | SKILL.md must include a "Validation Checklist" section with pre-apply verification steps |
| **Human review** | Tier 3 | Outputs (commands, patches, config changes) must not be applied without explicit user approval |

## Skill Metadata

Each skill declares `risk_tier` in `skills-manifest.json`. High-risk (Tier 3) skills require `security_reviewed: true` and `last_reviewed` date before release.
