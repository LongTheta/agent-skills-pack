# AI Governance Model

Governance for agent-skills-pack: skill approval, security review, and release versioning.

---

## Skill Approval Process

### Overview

All skills must pass a staged approval process before merge and release.

| Stage | Gate | Owner |
|-------|------|-------|
| **1. Author** | PR opened; validation passes | Contributor |
| **2. Review** | Maintainer approval; CI green | Maintainer |
| **3. Security** | Tier 3 / security-impacting only | Maintainer |
| **4. Release** | Tag; CHANGELOG; manifest version | Maintainer |

### Stage 1: Author Submission

1. Create skill directory with required files: `SKILL.md`, `examples.md`, `prompt-template.md`, `reference.md`
2. Add YAML frontmatter: `name`, `description`, `risk_tier`
3. Include required sections: When to Use, Safety Guardrails (or Validation Checklist / Enforcement)
4. Update `skills-manifest.json` with full metadata
5. Run `npm run validate:full` — must pass
6. Open PR with description of use cases and risk tier rationale

### Stage 2: Maintainer Review

- [ ] Content correctness and style per [skill-style-guide.md](skill-style-guide.md)
- [ ] Manifest entry complete: category, triggers, tags, maintainer, risk_tier
- [ ] No broken links; markdown lint passes
- [ ] CODEOWNERS satisfied for security skills

### Stage 3: Security Review (Conditional)

Required when:

- **New Tier 3 skill** — Must have `security_reviewed: true` and `last_reviewed` before merge
- **Changes to security/compliance skills** — security-evaluator, cve-detect-and-remediate, ai-devsecops-policy-enforcement, dod-zero-trust-architect, zero-trust-gitops-enforcement
- **Auto-apply or execution** — Any change that adds automatic application of commands or config

See [Security Review Requirements](#security-review-requirements) below.

### Stage 4: Release

- [ ] All skills pass validation
- [ ] CHANGELOG updated
- [ ] Version bumped per [Release Versioning](#release-versioning)
- [ ] Tag created; GitHub Release published

See [release-checklist.md](release-checklist.md) for steps.

---

## Security Review Requirements

### When Required

| Condition | Requirement |
|-----------|-------------|
| New Tier 3 skill | Security review before merge |
| Tier 3 skill changes | Re-review if behavior changes |
| Security/compliance skills | CODEOWNERS approval; security checklist |
| Auto-apply or execution | Explicit approval; document in skill |

### Security Review Checklist

- [ ] **Trust boundaries** — No untrusted input used for execution; see [ai-security-model.md](ai-security-model.md)
- [ ] **No unsafe defaults** — Commands and config require explicit user approval
- [ ] **Guardrails documented** — Limitations, Safety Guardrails, Validation Checklist, or Enforcement section present
- [ ] **Manifest metadata** — `security_reviewed: true`, `last_reviewed` (YYYY-MM-DD)
- [ ] **No secrets** — No hardcoded credentials, API keys, or tokens

### Tier 3 Specifics

Tier 3 skills modify CI/CD, infra, or execute commands. Before merge:

1. Maintainer performs security review
2. Set `security_reviewed: true` in manifest
3. Set `last_reviewed` to review date
4. Ensure skill documents human-review requirement

---

## Release Versioning

### Semantic Versioning

We follow [Semantic Versioning 2.0](https://semver.org/):

| Bump | When | Examples |
|------|------|----------|
| **MAJOR** | Breaking changes | Manifest schema change, skill format change, required sections added |
| **MINOR** | New features, backward-compatible | New skill, new category, new optional manifest field |
| **PATCH** | Fixes, docs, minor improvements | Bug fixes, typo fixes, doc updates |

### Version Locations

| File | Field | Purpose |
|------|-------|---------|
| `skills-manifest.json` | `version` | Pack version (source of truth) |
| `package.json` | `version` | Tooling version (keep in sync) |
| `CHANGELOG.md` | Section headers | Human-readable history |

### Release Cadence

- **Patch** — As needed for fixes
- **Minor** — When new skills or features land
- **Major** — When schema or format changes require migration

### Pre-Release Steps

1. Run `npm run validate:full`
2. Update CHANGELOG with new version section
3. Bump `version` in `skills-manifest.json` and `package.json`
4. Run `npm run sbom` if dependencies changed
5. Tag: `git tag v1.2.0`
6. Push tags; create GitHub Release

See [release-checklist.md](release-checklist.md) for the full checklist.

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [review-model.md](review-model.md) | Author, security, release review tiers |
| [ai-security-model.md](ai-security-model.md) | Trust boundaries, risk tiers |
| [supply-chain-security.md](supply-chain-security.md) | SBOM, provenance, artifact integrity |
| [versioning.md](versioning.md) | Semantic versioning, branch strategy |
| [release-checklist.md](release-checklist.md) | Pre-release steps |
