# Release Readiness

Criteria for considering agent-skills-pack production-ready for public v1 release.

---

## V1.0.0 Readiness Checklist

### Governance & Security

- [x] All Tier 3 skills have `security_reviewed: true` and `last_reviewed` in manifest
- [x] Trust boundaries, prompt injection defenses, and tool access rules documented in [ai-security-model.md](ai-security-model.md)
- [x] Security review process defined in [ai-governance-model.md](ai-governance-model.md)
- [x] SECURITY.md present with vulnerability reporting process

### Validation & CI

- [x] `npm run validate:full` passes (Node + Python)
- [x] All CI workflows block merge on failure (validate, lint, links)
- [x] SBOM generated and committed
- [ ] No broken internal links (verify via CI Link Check)

### Skills & Manifest

- [x] All skills have required sections: When to Use, Inputs, Outputs, Limitations, Safety Guardrails (or Validation Checklist / Enforcement)
- [x] Tier 2 skills include Validation Checklist
- [x] Tier 3 skills document human-review requirement
- [x] Manifest aligned with all skill directories; risk_tier defined per skill

### Documentation

- [x] README clear for first-time users
- [x] CONTRIBUTING.md describes PR process and skill approval
- [x] CHANGELOG.md updated with v1.0.0 section
- [x] Release checklist and review model in place

### Pre-Release

- [ ] Run [release-checklist.md](release-checklist.md) end-to-end
- [ ] Tag `v1.0.0`; create GitHub Release
- [ ] Verify no known security issues

---

## Blocking Criteria

The following **must** be satisfied before v1.0.0:

1. **CI green** — Validate, lint, and link-check workflows pass
2. **Tier 3 reviewed** — shell, ai-devsecops-policy-enforcement have security_reviewed and last_reviewed
3. **No critical gaps** — All skills pass strict validation
4. **Governance complete** — Approval process, security review, and versioning documented

---

## Post-V1 Improvements

Not blocking for v1, but recommended for future releases:

- Branch protection rules (require PR review, status checks)
- SLSA Level 1 provenance
- Signed commits enforcement
- Additional golden tests for security skills
