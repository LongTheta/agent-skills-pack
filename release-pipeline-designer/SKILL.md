---
name: release-pipeline-designer
risk_tier: 2
description: >-
  Designs CI/CD release pipelines: build, test, lint, security scan, artifact
  build, and deployment stages. Produces pipeline config proposals (GitHub
  Actions, GitLab CI). Use when setting up CI/CD, defining release stages, or
  designing promotion flows. Complements zero-trust-gitops-enforcement and
  ai-devsecops-policy-enforcement for security hardening.
---

# Release Pipeline Designer

Designs CI/CD release pipelines. Produces pipeline config proposals (GitHub Actions, GitLab CI) with build, test, lint, security scan, and deployment stages. Output is config for user to review and apply. Use before or alongside zero-trust-gitops-enforcement and ai-devsecops-policy-enforcement for security review.

## When to Use

- User wants to set up CI/CD for a repository
- User asks to design release stages, build pipeline, or deployment flow
- User needs GitHub Actions or GitLab CI workflow proposals
- User wants to add security scanning, testing, or artifact build to CI

## Inputs

- **CI platform:** GitHub Actions, GitLab CI, or other
- **Project type:** Application, library, container image
- **Stages needed:** Build, test, lint, scan, deploy
- **Environment promotion:** dev → stage → prod (if applicable)
- **Existing pipeline:** Any current config to extend

## Outputs

- **Pipeline config** — YAML for GitHub Actions or GitLab CI
- **Stage definitions** — Build, test, lint, security scan, artifact, deploy
- **Job dependencies** — Order and fail-fast behavior
- **Secrets guidance** — What to configure (no actual secrets)
- **Promotion flow** — Manual gates, environment approvals (if applicable)

## Workflow

1. **Gather requirements** — Platform, project type, stages
2. **Define stages** — Build → Test → Lint → Scan → Artifact → Deploy
3. **Create config** — Valid YAML; use standard actions
4. **Add security scan placeholder** — SBOM, dependency scan; note ai-devsecops for policy
5. **Document secrets** — List required secrets; do not add values
6. **Promotion flow** — If multi-env, define manual gates
7. **Output** — Config file path; user applies

## Limitations

- Proposes config only; user applies. Does not run pipelines.
- Security policy enforcement is separate; use ai-devsecops-policy-enforcement for review
- Secrets must be configured in CI platform; skill only documents

## Safety Guardrails

- **Tier 2:** Proposes config; user reviews before applying. Validation Checklist required.
- **No secrets in config** — Use secrets/variables; never hardcode
- **Production gates** — Recommend manual approval for prod deploy
- **Immutable artifacts** — Recommend SHA tags or versioned artifacts

## Validation Checklist

- [ ] Pipeline stages are ordered correctly
- [ ] No secrets or credentials in config
- [ ] Production deployment has manual gate or equivalent
- [ ] Security scan step included (placeholder or concrete)
- [ ] Compatible with zero-trust-gitops-enforcement review

## Portability Notes

GitHub Actions and GitLab CI configs differ. Output is platform-specific. Adapt for other CI systems (Jenkins, Tekton, etc.) by mapping stages and jobs.
