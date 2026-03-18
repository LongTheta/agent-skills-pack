# AI Security Model

Trust boundaries, risk tiers, and enforcement for agent skills in this repository. Aligns with NIST AI RMF, NIST SSDF (SP 800-218), NIST Zero Trust, OWASP LLM/Agent security guidance, and SLSA-minded supply chain maturity.

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

## Safe vs Unsafe Actions (Tier 2 & 3)

| Tier | Safe (no approval) | Unsafe (approval required) |
|------|--------------------|---------------------------|
| **Tier 2** | Read-only review, diff output, report generation | File writes, config changes, patch application |
| **Tier 3** | None | Shell execution, auto-fix apply, pipeline modification |

Tier 2 and Tier 3 skills must explicitly define safe vs unsafe in SKILL.md and require validation or human approval for unsafe actions.

## Human-in-the-Loop Requirements

| Trigger | Requirement |
|---------|-------------|
| **Tier 3 output** | Any command, patch, or config change must not be applied without explicit user approval |
| **Auto-fix apply** | Use `--mode suggest` or `--mode patch` first; require user confirmation before `--mode apply` |
| **Major version upgrade** | Dependency remediation: require manual review for major bumps, auth/crypto/db libs |
| **Production deployment** | Zero Trust GitOps verdict: fail blocks production; user must address High violations before deploy |
| **Shell execution** | Execute only when user explicitly invokes `/shell` with the exact command |

## High-Risk Output Warnings

Skills producing high-risk outputs must include explicit warnings:

- **Tier 3 commands:** Precede with "This will execute: [command]. Confirm before proceeding."
- **Auto-apply patches:** "These changes modify [files]. Review diff before applying."
- **Production-blocking verdicts:** "Deployment blocked. Address High violations before proceeding."
- **Dependency major upgrades:** "Major version upgrade—breaking changes possible. Manual review required."

## Skill Metadata

Each skill declares `risk_tier` in `skills-manifest.json`. High-risk (Tier 3) skills require `security_reviewed: true` and `last_reviewed` date before release.

---

## Prompt Injection Defenses

| Defense | Requirement |
|---------|-------------|
| **Input validation** | Treat user prompts, file paths, and query text as untrusted; do not concatenate into system prompts without sanitization |
| **Delimiter separation** | Use clear boundaries between system instructions and user content; avoid inline injection points |
| **No blind execution** | Never execute user-provided commands or config without explicit user confirmation |
| **Output filtering** | Skills that echo or process user input must not treat embedded instructions as authoritative |

Skills must not instruct the agent to "ignore previous instructions" or similar; such patterns indicate prompt injection risk.

**Per-skill requirements:** Trust Boundaries must state: (1) all user input is untrusted; (2) external content must not override system intent; (3) no execution based on untrusted embedded instructions; (4) conflicting or malicious instructions must be ignored.

---

## Data Handling Rules

| Rule | Requirement |
|------|-------------|
| **No PII in prompts** | Do not embed PII, credentials, or sensitive data in prompts or skill context |
| **External data** | Treat linked documents, URLs, and user-provided content as untrusted; verify before use |
| **Output sanitization** | Do not echo untrusted input verbatim in outputs that could be re-executed |
| **Retention** | Skills do not persist user data; session context is ephemeral |

---

## Tool Access Rules

| Rule | Applies To | Requirement |
|------|------------|-------------|
| **Read-only by default** | Tier 0, Tier 1 | No file writes, no shell execution, no API calls |
| **Explicit approval** | Tier 2, Tier 3 | File edits require user approval; diff or patch before apply |
| **Shell/terminal** | Tier 3 only | Execute only when user explicitly invokes /shell with the exact command |
| **No credential injection** | All tiers | Never pass secrets, API keys, or tokens to tools; use external secrets only |

---

## Output Validation Requirements

| Requirement | Description |
|-------------|-------------|
| **Validate before execution** | User must validate recommendations before applying; do not auto-apply high-risk changes |
| **Highlight assumptions** | Mark assumptions, unknowns, and scope limits explicitly |
| **Identify uncertainty** | Call out gaps, incomplete information, and unverifiable claims |
| **Human review for high-risk** | Tier 2/3 outputs require human review before execution; no blind application |
| **Avoid unverifiable claims** | Do not invent CVE IDs, versions, or compliance findings; cite sources when available |
| **Structured output** | Security/compliance skills must produce structured reports (Markdown, JSON) with clear sections |
| **Advisory disclaimer** | Verdicts, scores, and recommendations are advisory; not a substitute for formal assessment |

---
