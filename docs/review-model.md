# Review Model

Three-tier review for skills: author, security, release.

**Governance:** Full approval process, security requirements, and release versioning are defined in [ai-governance-model.md](ai-governance-model.md).

## Review Tiers

| Tier | Who | When | Scope |
|------|-----|------|-------|
| **Author review** | Contributor | Every PR | Correctness, style, completeness |
| **Security review** | Maintainer | Tier 3 skills; security-impacting changes | Guardrails, trust boundaries, no unsafe guidance |
| **Release review** | Maintainer | Before tag | Manifest, CHANGELOG, validation |

## Author Review

- [ ] SKILL.md has required sections (When to Use, Inputs, Outputs, Workflow, Limitations, Safety Guardrails, Validation Checklist)
- [ ] Frontmatter correct; description includes triggers
- [ ] Examples and prompt-template present
- [ ] `npm run validate` passes
- [ ] Manifest updated

## Security Review

Required for:

- New Tier 3 skills
- Changes to security-evaluator, cve-detect-and-remediate, ai-devsecops-policy-enforcement, dod-zero-trust-architect, zero-trust-gitops-enforcement
- Any change that adds auto-apply or execution

Checklist:

- [ ] Trust boundaries respected (see [ai-security-model.md](ai-security-model.md))
- [ ] No unsafe commands or config without explicit user approval
- [ ] Limitations and guardrails documented
- [ ] `security_reviewed: true` and `last_reviewed` set in manifest

## Release Review

- [ ] All skills pass validation
- [ ] CHANGELOG.md updated
- [ ] Version bumped in manifest and package.json
- [ ] SBOM current
- [ ] No known security issues
