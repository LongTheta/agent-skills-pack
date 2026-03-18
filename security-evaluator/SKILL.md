---
name: security-evaluator
description: Evaluates tools, architectures, code changes, CI/CD workflows, GitOps platforms, dashboards, integrations, AI agents, MCP servers, and cloud-native systems from a security and compliance perspective. Use when the user asks to review something for security risk, assess a design for security concerns, evaluate a tool for enterprise or government use, identify compliance gaps, or create a security scorecard or mitigation plan.
---

# Security Evaluator

Evaluates tools, architectures, and systems from a security and compliance perspective. Produces structured assessments with scorecards, risks, mitigations, and practical recommendations. Call out assumptions and unknowns explicitly.

## When to Use

- Review something for security risk
- Assess a design for security concerns
- Evaluate a tool for enterprise or government use
- Identify compliance gaps
- Create a security scorecard or mitigation plan

## Evaluation Workflow

1. **Identify what is being evaluated** — tool, architecture, workflow, integration, etc.
2. **Determine relevant security domains** — from the list below; focus on what applies.
3. **Identify risks and unknowns** — gaps, assumptions, missing information.
4. **Recommend mitigations or compensating controls** — prioritized, actionable.
5. **Provide a practical recommendation** — using the output format categories.

## Security Domains to Evaluate

| Domain | What to Assess |
|--------|----------------|
| **Identity and access management** | IdP integration, MFA, session management |
| **RBAC / least privilege** | Role design, permission granularity, default access |
| **Authentication / authorization** | Auth flows, token handling, OAuth/SAML support |
| **Secrets handling** | Storage, rotation, exposure risk, vault integration |
| **Audit logging and accountability** | Log coverage, retention, tamper resistance, export |
| **Encryption in transit and at rest** | TLS, key management, data-at-rest encryption |
| **API / network exposure** | Surface area, auth on endpoints, rate limiting |
| **Supply chain security** | SBOM, provenance, signed artifacts |
| **Dependency/image scanning** | CVE coverage, scan frequency, remediation path |
| **Configuration management and drift risk** | IaC, drift detection, config validation |
| **Policy enforcement** | Policy-as-code, guardrails, automated checks |
| **Incident response visibility** | Logging, alerting, forensics capability |
| **Data exposure risk** | Data flows, PII/CUI handling, residency |
| **Third-party / vendor risk** | Subprocessors, certifications, data sharing |
| **SaaS vs self-hosted tradeoffs** | Control vs. operational burden, data location |
| **Operational security burden** | Patching, hardening, monitoring requirements |
| **Secure-by-default posture** | Default config safety, opt-in vs. opt-out |

## Regulated / Federal Additions

When the environment is regulated, federal, or compliance-sensitive, also evaluate:

| Area | What to Assess |
|------|----------------|
| **FedRAMP alignment concerns** | FedRAMP readiness, ATO impact |
| **NIST 800-53 family implications** | Control mapping (AC, AU, IA, SC, SI, etc.) |
| **FISMA-related expectations** | FISMA alignment, continuous monitoring |
| **Audit evidence** | Audit trails, retention, export for assessors |
| **Separation of duties** | Approval workflows, dual control |
| **Policy-as-code compatibility** | Declarative config, GitOps-friendly |
| **Change control / promotion governance** | Promotion paths, approval gates |

## Output Structure

Use this template. Be concise; avoid filler.

```markdown
## 1. Security Summary
[2–4 sentence overview of security posture and bottom-line risk level]

## 2. Threat / Risk Areas
[Key threat vectors and risk areas relevant to this evaluation]

## 3. Security Scorecard
| Domain | Score (1–5) | Notes |
|--------|-------------|-------|
| [Include domains from evaluation list that apply] | | |

## 4. Key Strengths
[Bullet list of security positives]

## 5. Key Risks / Gaps
[Bullet list; call out unknowns and assumptions]

## 6. Compliance / Control Considerations
[Relevant for regulated environments: NIST, FedRAMP, FISMA, etc.]

## 7. Required Mitigations
[Prioritized list with effort and ownership where applicable]

## 8. Operational Security Considerations
[Day-2 security ops, monitoring, maintenance]

## 9. Final Recommendation
[One of: Low risk | Moderate risk with controls | High risk | Pilot only | Not recommended | Need more information]

## 10. Next Validation Steps
[Concrete actions: tests to run, docs to review, questions to answer]
```

## Recommendation Types

| Type | When to Use |
|------|-------------|
| **Low risk** | Strong security posture; proceed with standard due diligence |
| **Moderate risk with controls** | Acceptable with specific mitigations; document controls |
| **High risk** | Significant gaps; require substantial mitigations before use |
| **Pilot only** | Validate in isolated environment before broader adoption |
| **Not recommended** | Unacceptable risk or better alternatives exist |
| **Need more information** | Gaps prevent a decision; list what to gather |

## Guidelines

- **No fluff**: Focus on evidence, tradeoffs, and actionable findings.
- **State assumptions**: Explicitly list what you assumed (versions, environment, data classification).
- **Highlight unknowns**: Mark areas where information was missing or uncertain.
- **Be practical**: Recommend a clear path forward, not vague “consider” statements.

---

## Invocation Prompt Template

When the user wants to run a security evaluation, use the template in [prompt-template.md](prompt-template.md). It includes placeholders for: tool/architecture name, category, intended use case, environment, data sensitivity, hosting model, integrations, constraints, and must-have controls. Fill in the placeholders; omit sections that do not apply.
