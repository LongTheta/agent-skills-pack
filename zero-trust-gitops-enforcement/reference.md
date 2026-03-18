# Zero Trust GitOps Enforcement — Reference

## Enforcement Areas Summary

| Area | Required Controls |
|------|-------------------|
| **Identity** | No shared credentials; workload identity (OIDC, SA); least privilege |
| **Supply Chain** | SBOM; pinned dependencies; provenance/attestation |
| **Deployment Integrity** | Immutable image tags (SHA); no `latest`; verified artifacts |
| **Promotion Controls** | Manual approval for prod; environment separation; explicit gates |
| **Secrets** | No plaintext in code/config; external secrets (Vault, ESO) |
| **Observability** | Metrics; structured logs; request traceability |

## Severity Criteria

| Severity | Examples | Blocks Production? |
|----------|----------|---------------------|
| **High** | Shared creds, plaintext secrets, `latest` tags, no SBOM, no prod gate | Yes |
| **Medium** | Unpinned deps, missing workload identity, weak observability | Yes if multiple |
| **Low** | Suboptimal patterns, missing recommendations | No |

## DoD ZT Pillar Mapping

| Enforcement Area | DoD Pillar |
|------------------|------------|
| Identity | User |
| Supply Chain | Application & Workload |
| Deployment Integrity | Application & Workload |
| Promotion Controls | Automation & Orchestration |
| Secrets | Data |
| Observability | Visibility & Analytics |

## SLSA Alignment

- **Level 1:** Build provenance
- **Level 2:** Signed artifacts, two-person review
- **Level 3:** Isolated build, hermetic
