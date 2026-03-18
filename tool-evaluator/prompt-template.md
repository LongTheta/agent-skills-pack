# Tool Evaluator – Invocation Prompt Template

Copy and fill in the placeholders. Omit sections that do not apply.

```
Evaluate [TOOL NAME] as a [CATEGORY] for [USE CASE].

Environment:
- Team/org: [size, structure, expertise]
- Stack: [existing tools, platforms, languages]
- Hosting model: [cloud, on-prem, hybrid; SaaS vs self-hosted]
- Security/compliance constraints: [regulated, FedRAMP, SOC2, etc.]
- Required integrations: [GitLab, ArgoCD, Kubernetes, Grafana, Prometheus, IdP, secrets, etc.]
- Available data sources: [what data exists; format, freshness, accessibility]
- Must-have requirements: [list]
- Nice-to-have requirements: [list]
- Comparison tools: [if comparing: tool A, tool B, ...]

Return:
- Summary (what the tool is, what problem it solves, high-level recommendation)
- Best fit use cases (where it works well; where it does not)
- Evaluation scorecard (Problem Fit, Capability Fit, Integration Fit, Data Hydration & Readiness, Security & Compliance, Operational Fit, Cost & Risk — each with score 1–10 and justification)
- Data hydration assessment (readiness score, key blockers, transformation effort, correlation difficulty, timeline risk)
- Strengths
- Weaknesses / risks
- Security / compliance considerations
- Integration / operational considerations
- Final recommendation (Strong fit | Fit with caveats | Pilot first | Not recommended | Need more information)
- Next steps (e.g., run PoC, validate integrations, confirm data availability, perform security review, map control ownership, test with production-like data)
```

## Example

```
Evaluate Argo CD as a GitOps platform for Kubernetes deployment automation.

Environment:
- Team/org: Platform team of 8; moderate Kubernetes experience
- Stack: EKS, GitLab, Prometheus, Grafana, HashiCorp Vault
- Hosting model: Self-hosted in AWS; targeting FedRAMP Moderate
- Security/compliance constraints: FedRAMP Moderate; RBAC, audit logs required
- Required integrations: GitLab, Vault, Prometheus, OIDC IdP
- Available data sources: Git repos (manifests, Helm); cluster metrics via Prometheus; audit logs from API server
- Must-have requirements: RBAC, audit logging, secrets externalization, multi-cluster
- Nice-to-have requirements: SSO, policy-as-code, UI dashboards
- Comparison tools: Flux CD, Rancher Fleet

Return:
- Summary
- Best fit use cases
- Evaluation scorecard (all 7 categories, 1–10)
- Data hydration assessment
- Strengths
- Weaknesses / risks
- Security / compliance considerations
- Integration / operational considerations
- Final recommendation
- Next steps
```

## FedRAMP / NIST / FISMA Compliance Variant

Use when evaluating for federal compliance:

```
Evaluate [TOOL/ARCHITECTURE] for FedRAMP/NIST/FISMA compliance.

**Context:**
- Environment: [e.g., FedRAMP Moderate, FISMA Moderate, IL4]
- Data sensitivity: [e.g., CUI, PII, PHI; classification]
- Hosting model: [e.g., FedRAMP-authorized cloud, GovCloud, on-prem]
- Users: [e.g., federal employees, contractors; scope]
- Integrations: [e.g., IdP, SIEM, CMDB]

**Return:**
- Compliance summary (FedRAMP readiness + ATO risk)
- NIST 800-53 control mapping
- Gaps
- Risks
- Required mitigations
- Final recommendation
```
