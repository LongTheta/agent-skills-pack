# Release Pipeline Designer — Reference

## Typical Stages

1. **Lint** — Fast; fail early
2. **Test** — Unit, integration per test-strategy-designer
3. **Build** — Compile, bundle, or build image
4. **Security scan** — SBOM, dependency scan; policy review via ai-devsecops
5. **Artifact** — Publish to registry or package repo
6. **Deploy** — Per environment; manual gate for prod

## Zero Trust Alignment

- Identity-based access (OIDC, workload identity)
- No long-lived secrets in pipeline
- Immutable artifacts (SHA tags)
- Manual approval for production

See zero-trust-gitops-enforcement for full review.
