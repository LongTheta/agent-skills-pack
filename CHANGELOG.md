# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2025-03-18

### Added

- **docs/ai-governance-model.md** — Skill approval process, security review requirements, release versioning
- **SECURITY.md** — Vulnerability reporting, security review process
- **CODEOWNERS** — Default and security-skill owners
- **Issue templates** — Bug, feature, security
- **PR template** — Checklist for contributions
- **docs/ai-security-model.md** — Trust boundaries, risk tiers (0–3)
- **docs/skill-authoring-standard.md** — Required sections, structure
- **docs/supply-chain-security.md** — SBOM, provenance, SLSA alignment
- **docs/review-model.md** — Author, security, release review
- **docs/versioning.md** — Semantic versioning, branch strategy
- **scripts/validate_skills.py** — Section validation, manifest checks
- **tests/golden/** — Golden prompts for security-evaluator, cve-detect-and-remediate
- **Manifest schema** — compatibility, risk_tier, required_files, maintainer, last_reviewed, security_reviewed

### Changed

- **skills-manifest.json** — Rich schema with risk_tier, compatibility, maintainer
- **security-evaluator** — Added Inputs, Outputs, Limitations, Safety Guardrails, Validation Checklist, Portability Notes
- **README** — Polished; target audience, validation pipeline, roadmap
- **Validate workflow** — Python validate_skills.py; Setup Python step

---

## [1.0.0] - 2025-03-18

### Added

- **Repository upgrade** — Production-quality skills platform for Cursor and other AI agent IDEs
- **README** — Professional open-source README with overview, install instructions, roadmap
- **skills-manifest.json** — Richer metadata: categories, tags, file manifests per skill
- **Standardized skills** — All 13 skills now have SKILL.md, examples.md, prompt-template.md, reference.md where appropriate
- **docs/** — Authoring guide, skill style guide, portability guide, release checklist
- **Validation tooling** — `scripts/validate-skills.js`, `scripts/generate-manifest.js`
- **GitHub Actions** — Markdown lint, manifest validation, link checks
- **LICENSE** — MIT
- **CONTRIBUTING.md** — Contribution workflow and skill requirements
- **CHANGELOG.md** — This file; semantic versioning guidance

### Changed

- Root README rewritten for public reuse
- Skill folders standardized with consistent file structure
- SKILL.md frontmatter normalized across skills

### Preserved

- All existing skill content and intent
- No skills removed; refactored and extended only

---

## Versioning

- **MAJOR** — Breaking changes (skill format, required files)
- **MINOR** — New skills, new features, backward-compatible
- **PATCH** — Fixes, docs, minor improvements
