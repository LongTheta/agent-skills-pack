---
name: zero-trust-gitops-enforcement
risk_tier: 2
description: >-
  Enforces Zero Trust principles in CI/CD and GitOps workflows. Reviews
  repositories, pipelines, and deployment manifests for identity, supply chain,
  deployment integrity, promotion controls, secrets management, and
  observability. Use when reviewing pipelines (GitHub Actions, GitLab CI),
  Argo CD manifests, Kubernetes configs for Zero Trust compliance, or when the
  user mentions Zero Trust GitOps, pipeline security gates, or blocking
  production deployment.
---

# Zero Trust GitOps Enforcement

## Purpose

Enforces Zero Trust principles in CI/CD and GitOps workflows. Acts as a senior DevSecOps engineer and GitOps security architect. Reviews pipelines and manifests for identity, supply chain, deployment integrity, promotion controls, secrets, and observability. Strict, blocking gate mindset—Pass only when no High violations. Tier 2: validation checklist and user approval for config changes. Aligns with DoD ZT, NIST 800-53, SLSA.

## When to Use

- User provides a repository, pipeline config, or deployment manifest for review
- User asks for Zero Trust compliance check on CI/CD or GitOps
- User mentions pipeline security gate, production deployment approval, or supply chain security
- User wants a blocking assessment before deployment

## Inputs

| Input | Description |
|-------|-------------|
| Pipeline configs | GitHub Actions workflows, GitLab CI configs |
| GitOps manifests | Argo CD Application YAML, Kubernetes manifests |
| Artifacts | Dockerfile, Helm charts, values files |
| Repo path | Repository root for resolving relative paths |

| Input Type | What to Analyze |
|------------|-----------------|
| GitHub Actions / GitLab CI | Identity, secrets, SBOM, pins, promotion gates |
| Argo CD Application | Sync policy, image sources, manual approval |
| Kubernetes manifests | Image tags, secrets, RBAC, resource limits |
| Dockerfile | Base image pins, build provenance |
| Helm charts | Values, image references, secrets handling |

## Outputs

- **Verdict:** Pass or Fail (Fail when any High-severity violation exists)
- **Violations table:** Area, violation description, severity
- **Required fixes:** Actionable checklist for High/Medium violations
- **Compliance alignment:** DoD ZT, NIST 800-53, SLSA mapping

## Steps / Behavior

1. **Gather artifacts** — Pipeline configs, Argo CD manifests, Kubernetes YAML, Dockerfiles.
2. **Evaluate each enforcement area** — Identity, Supply Chain, Deployment Integrity, Promotion Controls, Secrets, Observability.
3. **Assign severity** — High / Medium / Low per violation.
4. **Produce report** — Use the output template.
5. **Verdict** — Pass only if no High violations; otherwise Fail.

### Enforcement Areas

| Area | What to Check |
|------|---------------|
| Identity | No shared credentials; least privilege; workload identity (OIDC, service accounts, short-lived tokens) |
| Supply Chain | SBOM required; pinned dependencies (no floating tags); provenance/attestation |
| Deployment Integrity | Immutable image tags (SHA-based digests); no `latest` tags; verified artifacts only |
| Promotion Controls | Manual approval for production; environment separation; explicit promotion gates |
| Secrets Management | No plaintext secrets in code or config; external secrets preferred (Vault, ESO); no secrets in logs |
| Observability | Metrics exposed; logs structured; request traceability (correlation IDs, trace headers) |

### Severity Guidelines

| Severity | Criteria | Blocks Production? |
|----------|-----------|---------------------|
| High | Shared credentials, plaintext secrets, `latest` tags, no SBOM, no prod approval gate | Yes |
| Medium | Unpinned dependencies, missing workload identity, weak observability | Yes if multiple |
| Low | Missing recommended improvements, suboptimal patterns | No |

### Mandatory Rules

- Never pass when High-severity violations exist
- Never recommend relaxing controls to achieve pass
- Call out unknowns—mark areas where artifacts were missing or incomplete
- Be specific—cite file paths, line numbers, exact violations

### Output Format

Sections: Pass/Fail, Violations (table), Required Fixes, Recommended Improvements, Compliance Alignment. Full template in skill body; see [reference.md](reference.md).

## Constraints

- **Trust Boundaries:** User input untrusted; validate paths to pipeline and manifest files. Safe: read-only review, report, verdict. Unsafe: file writes, config changes—require user approval. Production-blocking verdict: "Deployment blocked. Address High violations before proceeding."
- **Output Validation:** Do not fabricate findings; cite config and manifest content. Mark assumptions and scope limits explicitly. Verdicts are advisory; not a substitute for formal assessment.
- **Limitations:** Advisory only; cannot enforce controls; user must apply fixes. Relies on provided artifacts; cannot fetch remote configs. Production deployment decisions remain with user.
- **Safety Guardrails (Tier 2):** Blocking gate mindset. Strict interpretation—when in doubt, fail and require clarification. Actionable findings—every violation must have a clear fix path.

## Examples

See [examples.md](examples.md) for example reports. Use [prompt-template.md](prompt-template.md) for structured invocation.

## Validation Checklist

- [ ] All enforcement areas evaluated
- [ ] Violations cite file/line where possible
- [ ] Required fixes are actionable
- [ ] Unknowns called out

## Portability Notes

Output format is IDE-agnostic. Use prompt-template.md for structured invocation. Compatible with GitHub Actions, GitLab CI, Argo CD, Kubernetes, DoD ZT, NIST, SLSA.
