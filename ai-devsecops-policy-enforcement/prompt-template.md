# AI DevSecOps Policy Enforcement — Invocation Template

Copy and fill in the placeholders. Omit sections that do not apply.

```
Run a DevSecOps policy review with the following:

**Platform:** [github | gitlab]
**Pipeline path:** [e.g., .github/workflows/ci.yml]
**GitOps path:** [e.g., k8s/argo-application.yaml]
**Policy:** [default | fedramp-moderate | supply-chain-baseline | self-review]
**Artifact directory:** [e.g., artifacts]

**Optional:**
- PR/MR number for remote fetch: [number]
- Owner/repo or project: [org/repo or group/project]

Produce:
1. Verdict (pass | pass_with_warnings | fail)
2. Findings by severity
3. Required fixes
4. Auto-fix suggestions (if applicable)
```

## Example

```
Run a DevSecOps policy review with the following:

**Platform:** github
**Pipeline path:** .github/workflows/deploy.yml
**GitOps path:** argocd/applications/production.yaml
**Policy:** default
**Artifact directory:** artifacts

Produce:
1. Verdict
2. Findings by severity
3. Required fixes
4. Auto-fix suggestions
```
