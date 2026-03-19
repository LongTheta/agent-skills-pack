# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.1] - 2025-03-19

### Changed

- **Jade project focus** — Renamed and updated all documentation to reflect the Jade CI/CD Agent Skills Pack
- **README** — Title, description, and clone URL updated for Jade project
- **package.json** — Name set to `jade-cicd-agent-skills-pack`
- **skills-manifest.json** — Repo, description, and repository URL updated
- **docs/** — ai-governance-model, authoring-guide, release-readiness, skill-authoring-standard, supply-chain-security
- **.cursor/rules** — ai-security-enforcement, skill-authoring, project-conventions
- **scripts** — generate-manifest.js, generate_manifest.py, certification-score.js
- **sbom.json** — Package name and description
- **SKILL_ASSESSMENT_REPORT.md** — Repository references
- **.github/ISSUE_TEMPLATE** — Security URL

---

## [1.0.0] - 2025-03-18

### Added

**Repository Lifecycle Skills (7 new):**

- **create-repo-foundation** — Scaffold repo: .gitignore, README, LICENSE, CONTRIBUTING, directory layout
- **test-strategy-designer** — Design test strategy: unit, integration, e2e, coverage targets
- **repo-docs-writer** — Write or improve README, CONTRIBUTING, API docs, architecture, runbooks
- **release-pipeline-designer** — Design CI/CD pipelines: build, test, lint, scan, deploy
- **ai-code-review-guardrails** — Define guardrails for AI-assisted code review
- **dependency-governance** — Define dependency policy: licenses, pinning, blocklist
- **observability-bootstrap** — Bootstrap logging, metrics, tracing, dashboards, alerting

**Security & Compliance (7 skills):** ai-agent-architecture, ai-devsecops-policy-enforcement, cve-detect-and-remediate, dod-zero-trust-architect, security-evaluator, tool-evaluator, zero-trust-gitops-enforcement

**IDE & Authoring (6 skills):** create-rule, create-skill, create-subagent, migrate-to-skills, shell, update-cursor-settings

**Governance & Documentation:**

- **docs/ai-governance-model.md** — Skill approval process, security review requirements, release versioning
- **docs/ai-security-model.md** — Trust boundaries, risk tiers (0–3), prompt injection defenses, tool access rules
- **docs/release-readiness.md** — V1.0.0 release criteria
- **docs/review-model.md** — Author, security, release review tiers
- **docs/supply-chain-security.md** — SBOM, provenance, artifact integrity
- **docs/versioning.md** — Semantic versioning, branch strategy
- **docs/skill-authoring-standard.md** — Required sections, structure
- **SECURITY.md** — Vulnerability reporting, security review process
- **CODEOWNERS** — Default and security-skill owners
- **Issue templates** — Bug, feature, security
- **PR template** — Checklist for contributions

**Validation & CI:**

- **scripts/validate-skills.js** — Node validation: manifest, frontmatter, required files
- **scripts/validate_skills.py** — Python validation: YAML frontmatter, sections, links, Tier 2/3 enforcement
- **requirements.txt** — PyYAML for validation
- **GitHub Actions** — Validate, Lint, Link Check (all block merge on failure)
- **SBOM** — CycloneDX in sbom.json; generated in CI

**Manifest:**

- **skills-manifest.json** — Full metadata: version, category, risk_tier, triggers, tags, maintainer, last_reviewed, security_reviewed
- **risk_tiers** — 0 (read-only) through 3 (infra/pipeline impact)
- **enforcement** — Tier 2 Validation Checklist; Tier 3 human review

### Changed

- **README** — End-to-end pack for repo creation, hardening, testing, release, maintenance
- **All skills** — Standardized: Inputs, Outputs, Limitations, Safety Guardrails, Validation Checklist, Portability Notes
- **Lint workflow** — Fail on markdown violations (no `|| true`)
- **Link workflow** — Fail on broken links (no `continue-on-error`)

### Preserved

- All existing skill content and intent
- No skills removed; refactored and extended only

---

## Versioning

- **MAJOR** — Breaking changes (skill format, required files)
- **MINOR** — New skills, new features, backward-compatible
- **PATCH** — Fixes, docs, minor improvements
