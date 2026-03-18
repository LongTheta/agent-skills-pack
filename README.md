# Agent Skills Pack

A production-ready, security-focused collection of **Agent Skills** for AI-assisted development—security, compliance, DevSecOps, Zero Trust, and IDE workflows. Designed for Cursor and other AI agent IDEs.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Overview

Agent Skills are specialized instructions that teach AI agents how to perform domain-specific tasks. This repository provides a curated, reusable set of skills for teams building secure, compliant, and production-grade systems.

Each skill is self-contained, versioned independently, and can be used across projects or adapted for other AI coding assistants.

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
   git clone https://github.com/LongTheta/agent-skills-pack.git
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

## Contribution Model

| Step | Action |
|------|--------|
| 1 | Fork; create branch |
| 2 | Add/update skill per [docs/skill-authoring-standard.md](docs/skill-authoring-standard.md) |
| 3 | Run `npm run validate` |
| 4 | Update manifest if new skill |
| 5 | Open PR with checklist |

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

---

## Validation Pipeline

| Check | Command / CI |
|-------|--------------|
| Manifest validation | `node scripts/validate-skills.js` |
| Skill structure & sections | `python scripts/validate_skills.py` |
| Markdown lint | `markdownlint` in CI |
| Link check | `linkinator` in CI |
| SBOM generation | `npm run sbom` in CI |

---

## Repository Structure

```
agent-skills-pack/
├── README.md
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
- [ ] **v1.3** — SLSA Level 1 provenance
- [ ] **v2.0** — Multi-IDE plugin / extension packaging

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## License

[MIT](LICENSE)
