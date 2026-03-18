# Certification Model

Automated scoring for federal-grade AI, DevSecOps, and security best practices. Run with `npm run score`.

## Scoring Breakdown

| Category | Weight | What It Measures |
|----------|--------|------------------|
| **Structure & Governance** | 10% | README, LICENSE, CONTRIBUTING, SECURITY, CHANGELOG, CODEOWNERS |
| **Validation & Enforcement** | 15% | validate-skills script, Git hooks, CI workflows, validation in CI |
| **Skill Standardization** | 20% | SKILL.md, YAML frontmatter, required sections per skill |
| **AI Security Model** | 20% | docs/ai-security-model.md with trust boundaries, prompt injection, tool access, output validation |
| **Trust Boundaries** | 10% | Every SKILL.md contains Trust Boundaries section |
| **Output Validation** | 10% | Every SKILL.md contains Output Validation section |
| **Risk Tier Enforcement** | 10% | risk_tier metadata; Tier 3 requires security_reviewed and last_reviewed |
| **Auditability** | 3% | last_reviewed and security_reviewed populated in manifest |
| **Release Readiness** | 2% | docs/release-readiness.md, CHANGELOG v1.0.0, CI workflows |

## Score Levels

| Score | Meaning |
|-------|---------|
| **10** | Federal-grade, enterprise-ready. All checks pass. |
| **8–9.9** | Production-ready. Minor gaps (e.g., some last_reviewed null). |
| **6–7.9** | Acceptable. Address blockers before release. |
| **&lt; 6** | Not release-ready. Significant gaps in governance or security. |

## How to Improve

### To reach 8+

- Resolve all **BLOCKERS**
- Populate `last_reviewed` for skills with null
- Ensure every skill has Trust Boundaries and Output Validation
- Verify docs/ai-security-model.md contains all required terms

### To reach 10

- Resolve all **WARNINGS**
- Populate `security_reviewed` where appropriate
- Ensure Tier 3 skills have `security_reviewed: true` and `last_reviewed`
- Add docs/release-readiness.md if missing
- Ensure CHANGELOG includes v1.0.0

## Usage

```bash
npm run score
```

**CI:** Fails if score &lt; 7.5 (configurable via `--threshold=7.5` or `CERT_THRESHOLD` env).

```bash
node scripts/certification-score.js --threshold=8.0
```

**JSON output:**

```bash
node scripts/certification-score.js --json
```
