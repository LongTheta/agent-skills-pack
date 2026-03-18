# Tool Evaluator – Full Criteria Reference

Use when building the evaluation scorecard. Include only criteria relevant to the tool and context.

## Core Categories (Score 1–10)

| Category | What to Assess |
|----------|----------------|
| **Problem Fit** | Does it solve the actual problem? Point solution vs platform? Match to intended use case? |
| **Capability Fit** | Core features, required functionality, extensibility, API/CLI/MCP support, automation friendliness |
| **Integration Fit** | Ease of connecting to existing systems; native integrations vs custom glue; compatibility with GitLab, ArgoCD, Kubernetes, Grafana, Prometheus, cloud providers, IdP, secrets tools, policy engines |
| **Data Hydration & Readiness** | See Data Hydration section below |
| **Security & Compliance** | Identity/access, RBAC, secrets, audit logging, encryption, supply chain, trust boundaries, SaaS vs self-hosted tradeoffs, NIST/FedRAMP/FISMA, policy-as-code, audit evidence |
| **Operational Fit** | Maintenance burden, upgrade complexity, deployment model, documentation, day-2 ops, observability, ownership, learning curve |
| **Cost & Risk** | Licensing/pricing risk, lock-in, migration effort, support maturity, community health, hidden costs, sustainability |

## Data Hydration & Readiness

Evaluate whether the tool can operate effectively on real-world data in the target environment.

| Criterion | What to Assess |
|-----------|----------------|
| Data availability | Does the required data exist? Where? |
| Data accessibility | Can the tool ingest it without excessive custom engineering? |
| Data quality | Will quality issues reduce tool effectiveness? |
| Data completeness | Gaps that block core workflows? |
| Transformation effort | Normalization, enrichment, or correlation needed? |
| Correlation complexity | Cross-system correlation difficulty |
| Schema consistency | Consistency across sources |
| Freshness / latency | Real-time vs batch; acceptable delay? |
| Pipeline observability | Can you observe and debug data flows? |
| AI / automation readiness | Is data structured enough for AI-assisted workflows? |

**Key questions:**

- Does the required data exist?
- Can the tool ingest it without excessive custom engineering?
- Does the data need normalization, enrichment, or correlation?
- Will data quality issues reduce tool effectiveness?
- Is the data structured enough for AI-assisted workflows?

## Regulated / Federal Additions

| Criterion | What to Assess |
|-----------|----------------|
| NIST/FedRAMP/FISMA | Alignment with controls; ATO implications |
| Auditability | Audit logs, retention, export |
| RBAC and secrets handling | Least privilege, secret management |
| Policy-as-code compatibility | Declarative config, GitOps-friendly |
| Change control/promotion | Approval workflows, promotion paths |
| Supply chain security | SBOM, provenance, dependency hygiene |
