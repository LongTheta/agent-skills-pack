# Security Evaluator – Invocation Prompt Template

Copy and fill in the placeholders. Omit sections that do not apply.

```
Perform a security evaluation of the following:

**Tool or architecture name:** [name]
**Category:** [e.g., CI/CD platform, MCP server, AI agent, GitOps tool, security scanner, SaaS integration]
**Intended use case:** [what problem it solves; how it will be used]
**Environment:** [e.g., cloud, on-prem, hybrid; note if regulated/federal]
**Data sensitivity:** [e.g., public, internal, PII, CUI, PHI; classification level]
**Hosting model:** [e.g., SaaS, self-hosted, hybrid; FedRAMP-authorized cloud, GovCloud]
**Integrations:** [e.g., IdP, SIEM, vault, ticketing, other tools]
**Constraints:** [budget, timeline, team size, existing stack, compliance requirements]

**Must-have controls:**
- [control 1]
- [control 2]

Produce a structured security evaluation with:
1. Security Summary
2. Threat / Risk Areas
3. Security Scorecard
4. Key Strengths
5. Key Risks / Gaps
6. Compliance / Control Considerations
7. Required Mitigations
8. Operational Security Considerations
9. Final Recommendation (Low risk | Moderate risk with controls | High risk | Pilot only | Not recommended | Need more information)
10. Next Validation Steps
```

## Example

```
Perform a security evaluation of the following:

**Tool or architecture name:** Argo CD
**Category:** GitOps / continuous delivery
**Intended use case:** Sync Kubernetes manifests from Git to clusters; multi-cluster management
**Environment:** Cloud-native (EKS); FedRAMP Moderate target
**Data sensitivity:** CUI; deployment configs may contain secrets references
**Hosting model:** Self-hosted in customer VPC
**Integrations:** OIDC IdP, HashiCorp Vault, Prometheus
**Constraints:** Must support RBAC; audit logs required for ATO

**Must-have controls:**
- RBAC with least privilege
- Audit logging with retention
- Secrets not stored in Git
- SBOM available for container images

Produce a structured security evaluation with:
1. Security Summary
2. Threat / Risk Areas
3. Security Scorecard
4. Key Strengths
5. Key Risks / Gaps
6. Compliance / Control Considerations
7. Required Mitigations
8. Operational Security Considerations
9. Final Recommendation (Low risk | Moderate risk with controls | High risk | Pilot only | Not recommended | Need more information)
10. Next Validation Steps
```

## FedRAMP / NIST / FISMA Compliance Variant

Use when evaluating for federal compliance:

```
Perform a security evaluation of [TOOL/ARCHITECTURE] for FedRAMP/NIST/FISMA compliance.

**Context:**
- Tool/architecture name: [name]
- Category: [category]
- Intended use case: [use case]
- Environment: [e.g., FedRAMP Moderate, FISMA Moderate, IL4]
- Data sensitivity: [e.g., CUI, PII, PHI; classification]
- Hosting model: [e.g., FedRAMP-authorized cloud, GovCloud, on-prem]
- Integrations: [e.g., IdP (CAC/PIV), SIEM, CMDB]
- Must-have controls: [list]

**Return:**
1. Security Summary
2. Threat / Risk Areas (including FedRAMP/NIST implications)
3. Security Scorecard
4. Key Strengths
5. Key Risks / Gaps (including compliance gaps)
6. Compliance / Control Considerations (NIST 800-53 mapping, FedRAMP readiness)
7. Required Mitigations
8. Operational Security Considerations
9. Final Recommendation
10. Next Validation Steps
```
