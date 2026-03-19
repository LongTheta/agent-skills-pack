# Skill Assessment Report — Jade CI/CD Agent Skills Pack

Assessment of the Jade CI/CD Agent Skills Pack repository using Security Evaluator, Zero Trust GitOps Enforcement, and CVE Detect skills.

---

# Zero Trust GitOps Enforcement Report

**Repository:** jade-cicd-agent-skills-pack  
**Artifacts analyzed:** `.github/workflows/lint.yml`, `validate.yml`, `links.yml`

## Pass / Fail

**FAIL**

## Violations

| # | Area | Violation | Severity |
|---|------|-----------|----------|
| 1 | Supply Chain | ~~No SBOM generation step~~ — Added in validate workflow; sbom.json committed | Resolved |
| 2 | Supply Chain | GitHub Actions use `@v4` (pinned) but markdownlint-cli, linkinator use `npm install -g` without version pin | Medium |
| 3 | Identity | Workflows use default GITHUB_TOKEN; no OIDC or workload identity | Medium |
| 4 | Promotion Controls | No environment separation (dev/stage/prod); all workflows run on push/PR | Low |
| 5 | Observability | No structured logging or artifact upload for audit | Low |

## Required Fixes

- [x] Add SBOM generation step — **DONE**: `@cyclonedx/cyclonedx-npm` in validate workflow; `sbom.json` in repo; `npm run sbom` script
- [x] Pin markdownlint-cli and linkinator versions (markdownlint-cli@0.48.0, linkinator@7.6.1) — **DONE**
- [ ] Document OIDC/workload identity for future deployment workflows (N/A for current CI-only scope)

## Recommended Improvements

- Add `actions/checkout` with explicit ref for reproducibility
- Consider Dependabot or Renovate for dependency updates
- Add job summaries for easier audit

## Compliance Alignment

| Framework | Alignment Notes |
|-----------|-----------------|
| DoD Zero Trust | Automation pillar: improved — CI + SBOM; no promotion gates (N/A for content repo) |
| NIST 800-53 | SA-11 (supply chain): SBOM present |
| Supply Chain (SLSA) | Level 1: SBOM; no provenance/attestation yet |

---

# Security Evaluator Report

**Tool/architecture name:** Jade CI/CD Agent Skills Pack  
**Category:** Open-source skills repository / Markdown content platform  
**Intended use case:** Reusable Agent Skills for Cursor and other AI IDEs  
**Environment:** Public GitHub; consumed locally or via clone  
**Data sensitivity:** Low — Markdown, JSON, scripts; no PII/CUI  
**Hosting model:** GitHub-hosted; user copies/symlinks to local skills dir  

## 1. Security Summary

The Jade CI/CD Agent Skills Pack is a low-risk, content-only repository. It contains Markdown skills, JSON manifests, Node.js and Python scripts (stdlib only), and GitHub Actions for lint/validate. No secrets, no runtime services, no external API calls. Main risks are supply chain (unpinned npm global installs in CI) and dependency hygiene if future deps are added.

## 2. Threat / Risk Areas

- **Supply chain:** CI installs global npm packages without version pins
- **Content integrity:** Skills are consumed as-is; no signing or checksums
- **Script execution:** Users run `node scripts/validate-skills.js` and `python scripts/generate_manifest.py` locally — trust model is clone-and-run

## 3. Security Scorecard

| Domain | Score (1–5) | Notes |
|--------|-------------|-------|
| Identity and access | 5 | GitHub OAuth; repo public |
| Secrets handling | 5 | No secrets in repo |
| Audit logging | 4 | GitHub Actions logs; no custom audit |
| Supply chain | 3 | Unpinned global npm in CI; no SBOM |
| Configuration management | 5 | IaC (YAML); validation script |
| Policy enforcement | 4 | Lint, validate workflows |
| Secure-by-default | 5 | Minimal attack surface |

## 4. Key Strengths

- No secrets, API keys, or credentials
- Scripts use Node/Python stdlib only; no npm/pip deps in package.json
- LICENSE, CONTRIBUTING, CHANGELOG present
- Validation script enforces manifest consistency
- Markdown lint and link check in CI

## 5. Key Risks / Gaps

- Unpinned `markdownlint-cli` and `linkinator` in CI
- No SBOM for future dependencies
- No content signing or integrity checks for skills

## 6. Compliance / Control Considerations

- N/A for regulated data — content-only, no PII
- FedRAMP/NIST: Not applicable for this use case

## 7. Required Mitigations

1. **Pin CI tool versions** — Add `@version` to `npm install -g` commands
2. **Add SBOM step** — When dependencies are added, include `cyclonedx-npm` or similar in validate workflow

## 8. Operational Security Considerations

- Monitor Dependabot/Renovate if deps added
- Keep Node/Python versions in CI updated

## 9. Final Recommendation

**Low risk** — Proceed with standard due diligence. Suitable for public reuse.

## 10. Next Validation Steps

- Run `npm run validate` to confirm manifest consistency
- Add version pins to CI workflows
- Consider SBOM when adding npm/pip dependencies

---

# CVE Detect and Remediate — Summary

**Scope:** Jade CI/CD Agent Skills Pack dependencies

**Findings:** No lockfiles or dependency manifests with third-party packages. `package.json` has no `dependencies` or `devDependencies`. Python scripts use only stdlib (`json`, `re`, `sys`, `pathlib`). Node scripts use only `fs` and `path`.

**Conclusion:** No dependency CVEs to remediate. If dependencies are added later, run CVE scan per cve-detect-and-remediate skill (OSV, NVD, CISA KEV).

---

# Summary

| Skill | Verdict | Key Finding |
|-------|---------|-------------|
| Zero Trust GitOps | FAIL | No SBOM; unpinned npm tools in CI |
| Security Evaluator | Low risk | Content-only; pin CI tools |
| CVE Detect | N/A | No third-party dependencies |

**Priority fix:** ~~Pin `markdownlint-cli` and `linkinator` versions~~ — **Applied** (markdownlint-cli@0.48.0, linkinator@7.6.1).
