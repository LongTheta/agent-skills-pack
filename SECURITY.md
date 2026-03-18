# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

### Scope

We welcome reports for:

- **Skills content**: Incorrect security guidance, unsafe recommendations, or misleading compliance claims
- **Repository**: Supply chain issues, CI/CD misconfigurations, exposed secrets
- **Scripts**: Validation or manifest generation scripts

### How to Report

1. **Do not** open a public issue for security vulnerabilities
2. Email security concerns to the maintainers (see repository contacts)
3. Include:
   - Description of the vulnerability
   - Affected skill or file
   - Steps to reproduce
   - Expected vs actual behavior
   - Suggested fix (if any)

### Response

- We aim to acknowledge within 48 hours
- We will confirm receipt and provide remediation timeline
- We will credit reporters (with permission) after fix is released

### Security Review Requirements

Skills are reviewed per [docs/review-model.md](docs/review-model.md). Security review is required for:

- **Tier 3 skills** — Before merge; must have `security_reviewed: true` and `last_reviewed` in manifest
- **Security/compliance skills** — security-evaluator, cve-detect-and-remediate, ai-devsecops-policy-enforcement, dod-zero-trust-architect, zero-trust-gitops-enforcement
- **Auto-apply or execution** — Any change that adds automatic application of commands or config

See [docs/ai-governance-model.md](docs/ai-governance-model.md) for the full security review checklist and [docs/ai-security-model.md](docs/ai-security-model.md) for risk tiers.

## Security Best Practices

- Skills are **guidance only**; users must validate outputs before applying to production
- Do not paste secrets, API keys, or credentials
- Review generated commands or config changes before execution
- See [docs/supply-chain-security.md](docs/supply-chain-security.md) for artifact integrity
