# Zero Trust GitOps Enforcement — Invocation Template

Copy and fill in the placeholders. Omit sections that do not apply.

```
Perform a Zero Trust GitOps enforcement review:

**Artifacts to analyze:**
- Pipeline: [path, e.g., .github/workflows/ci.yml]
- GitOps: [path, e.g., argocd/apps/*.yaml]
- Kubernetes: [path, e.g., k8s/]
- Dockerfile: [path, if applicable]

**Context:**
- Target environment: [dev | staging | production]
- Compliance requirements: [DoD ZT | NIST | SLSA | none]

**Return:**
1. Pass / Fail verdict
2. Violations table (Area, Violation, Severity)
3. Required fixes (must address before production)
4. Recommended improvements
5. Compliance alignment (DoD ZT, NIST 800-53, SLSA)
```

## Example

```
Perform a Zero Trust GitOps enforcement review:

**Artifacts to analyze:**
- Pipeline: .github/workflows/deploy.yml
- GitOps: argocd/applications/
- Kubernetes: k8s/base/

**Context:**
- Target environment: production
- Compliance requirements: DoD ZT

**Return:**
1. Pass / Fail verdict
2. Violations table
3. Required fixes
4. Recommended improvements
5. Compliance alignment
```
