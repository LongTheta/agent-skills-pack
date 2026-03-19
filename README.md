# Jade CI/CD Agent Skills Pack

A production-ready collection of **Agent Skills** for the **Jade** project—AI-assisted CI/CD, repository creation, security, DevSecOps, Zero Trust, testing, release, and IDE workflows. End-to-end pack for repo creation, hardening, testing, release, and maintenance. Designed for Cursor and other AI agent IDEs.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Compliance alignment:** NIST AI RMF, NIST SSDF (SP 800-218), NIST Zero Trust, OWASP LLM/Agent security, SLSA-minded supply chain. See [docs/ai-security-model.md](docs/ai-security-model.md) and [docs/supply-chain-security.md](docs/supply-chain-security.md).

---

## Overview

Agent Skills are specialized instructions that teach AI agents how to perform domain-specific tasks. This repository provides a curated, reusable set of skills for the **Jade** CI/CD agent and teams building secure, compliant, and production-grade systems.

Each skill is self-contained, versioned independently, and can be used across Jade workflows or adapted for other AI coding assistants.

---

## Target Audience

- **Platform engineers** — GitOps, CI/CD, Kubernetes, DevSecOps
- **Security teams** — Compliance, vulnerability remediation, Zero Trust
- **Federal / regulated** — DoD Zero Trust, FedRAMP, NIST 800-53
- **AI agents** — Architecture design, evaluation, production readiness
- **Developers** — Rules, skills, IDE configuration, shell workflows

---

## Skill Categories

### Security & Compliance

| Skill | Description | Risk Tier |
|-------|-------------|-----------|
| [ai-agent-architecture](ai-agent-architecture/) | Design and evaluate AI agent systems across 7 layers | 0 |
| [ai-devsecops-policy-enforcement](ai-devsecops-policy-enforcement/) | Policy enforcement for CI/CD and GitOps pipelines | 3 |
| [cve-detect-and-remediate](cve-detect-and-remediate/) | Detect vulnerable dependencies and propose remediations | 2 |
| [dod-zero-trust-architect](dod-zero-trust-architect/) | DoD Zero Trust Architecture evaluation and design | 0 |
| [security-evaluator](security-evaluator/) | Security and compliance evaluation for systems | 0 |
| [tool-evaluator](tool-evaluator/) | Evaluate tools for enterprise adoption | 0 |
| [zero-trust-gitops-enforcement](zero-trust-gitops-enforcement/) | Zero Trust principles in CI/CD and GitOps | 2 |

### Repository Lifecycle

| Skill | Description | Risk Tier |
|-------|-------------|-----------|
| [create-repo-foundation](create-repo-foundation/) | Scaffold repo: .gitignore, README, LICENSE, CONTRIBUTING | 2 |
| [test-strategy-designer](test-strategy-designer/) | Design test strategy: unit, integration, e2e, coverage | 1 |
| [repo-docs-writer](repo-docs-writer/) | Write or improve README, CONTRIBUTING, API docs | 1 |
| [release-pipeline-designer](release-pipeline-designer/) | Design CI/CD pipelines: build, test, scan, deploy | 2 |
| [ai-code-review-guardrails](ai-code-review-guardrails/) | Define guardrails for AI-assisted code review | 1 |
| [dependency-governance](dependency-governance/) | Define dependency policy: licenses, pinning, blocklist | 1 |
| [observability-bootstrap](observability-bootstrap/) | Bootstrap logging, metrics, tracing, dashboards | 2 |

### IDE & Authoring

| Skill | Description | Risk Tier |
|-------|-------------|-----------|
| [create-rule](create-rule/) | Create rules for persistent AI guidance | 1 |
| [create-skill](create-skill/) | Create new Agent Skills | 1 |
| [create-subagent](create-subagent/) | Create subagents for complex tasks | 2 |
| [migrate-to-skills](migrate-to-skills/) | Migrate rules and commands to skills format | 2 |
| [shell](shell/) | Shell and terminal operations | 3 |
| [update-cursor-settings](update-cursor-settings/) | Modify Cursor/VSCode user settings | 2 |

---

## Quick Start

1. **Clone** the repository:
   ```bash
   git clone https://github.com/ai-devsecops-packs/jade-cicd-agent-skills-pack.git
   ```

2. **Link skills** to Cursor:
   - Copy desired skill folders into `~/.cursor/skills/` (or `%APPDATA%\Cursor\skills\` on Windows)
   - Or use symlinks for live updates

3. **Validate** (optional): `npm run validate`

---

## Installation

### Cursor

1. **Copy** or **symlink** skill folders into `~/.cursor/skills/`
2. **Project-level**: Copy into `.cursor/skills/` to share with your team
3. **Managed install**: Cursor Settings → Skills (if supported)

### Other AI IDEs

Skills use a standard structure (`SKILL.md`, `examples.md`, `prompt-template.md`, `reference.md`). See [docs/portability-guide.md](docs/portability-guide.md) for adapting to GitHub Copilot, Windsurf, Zed, Continue.

---

## Local Development Setup

Git hooks (via [Husky](https://typicode.github.io/husky/)) enforce validation locally so invalid skills are caught before push. CI remains the final gate.

### Install hooks

```bash
npm run setup
```

Or, after cloning:

```bash
npm install
```

The `prepare` script runs automatically after `npm install` and configures Husky.

### Hooks

| Hook | Runs | Purpose |
|------|------|---------|
| **pre-commit** | `npm run validate` | Fast check: manifest, SKILL.md structure, required files |
| **pre-push** | `npm run validate` + `npm run lint:md` | Full check matching CI (skills + markdown lint) |

### Bypass (emergency only)

```bash
git push --no-verify
```

Use sparingly; CI will still block invalid pushes.

---

## Contribution Model

| Step | Action |
|------|--------|
| 1 | Fork; create branch |
| 2 | Add/update skill per [docs/skill-authoring-standard.md](docs/skill-authoring-standard.md) |
| 3 | Run `npm run validate` (or rely on pre-commit hook) |
| 4 | Update manifest if new skill |
| 5 | Open PR with checklist |

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

---

## Validation Pipeline

| Check | Command / CI |
|-------|--------------|
| Manifest validation | `node scripts/validate-skills.js` (pre-commit, pre-push) |
| Certification score | `npm run score` (0–10; CI threshold 7.5; see [docs/certification-model.md](docs/certification-model.md)) |
| Skill structure & sections | `python scripts/validate_skills.py` |
| Markdown lint | `npm run lint:md` (pre-push), CI |
| Link check | `linkinator` in CI |
| SBOM generation | `npm run sbom` in CI |

---

## Repository Structure

```
jade-cicd-agent-skills-pack/
├── README.md
├── .husky/                   # Git hooks (pre-commit, pre-push)
├── skills-manifest.json      # Machine-readable catalog (rich schema)
├── sbom.json                 # Software Bill of Materials (CycloneDX)
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── CODEOWNERS
├── CHANGELOG.md
├── docs/
│   ├── ai-security-model.md
│   ├── authoring-guide.md
│   ├── skill-authoring-standard.md
│   ├── skill-style-guide.md
│   ├── portability-guide.md
│   ├── supply-chain-security.md
│   ├── review-model.md
│   ├── versioning.md
│   └── release-checklist.md
├── scripts/
│   ├── validate-skills.js
│   ├── validate_skills.py
│   ├── generate-manifest.js
│   └── generate_manifest.py
├── tests/golden/             # Golden test cases for flagship skills
└── <skill-name>/
    ├── SKILL.md
    ├── examples.md
    ├── prompt-template.md
    └── reference.md
```

---

## Roadmap

- [ ] **v1.1** — Node.js / npm CVE support in cve-detect-and-remediate
- [ ] **v1.2** — MCP server evaluation skill
- [ ] **v1.3** — SLSA Level 1 provenance (build attestations; see [docs/supply-chain-security.md](docs/supply-chain-security.md))
- [ ] **v2.0** — Multi-IDE plugin / extension packaging

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## License

[MIT](LICENSE)
