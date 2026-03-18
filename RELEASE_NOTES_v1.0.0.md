# Agent Skills Pack v1.0.0

**Release Date:** 2025-03-18

Production-ready Agent Skills for AI-assisted repository creation, security, DevSecOps, Zero Trust, testing, release, and IDE workflows. End-to-end pack for repo creation, hardening, testing, release, and maintenance. Designed for Cursor and other AI agent IDEs.

---

## What's Included

### 20 Skills Across 3 Categories

**Security & Compliance (7)** — Architecture review, policy enforcement, CVE remediation, Zero Trust, security evaluation

| Skill | Risk | Description |
|-------|------|-------------|
| ai-agent-architecture | 0 | Design and evaluate AI agent systems across 7 layers |
| ai-devsecops-policy-enforcement | 3 | Policy enforcement for CI/CD and GitOps pipelines |
| cve-detect-and-remediate | 2 | Detect vulnerable dependencies and propose remediations |
| dod-zero-trust-architect | 0 | DoD Zero Trust Architecture evaluation and design |
| security-evaluator | 0 | Security and compliance evaluation for systems |
| tool-evaluator | 0 | Evaluate tools for enterprise adoption |
| zero-trust-gitops-enforcement | 2 | Zero Trust principles in CI/CD and GitOps |

**Repository Lifecycle (7)** — Repo creation, testing, docs, release, review, dependencies, observability

| Skill | Risk | Description |
|-------|------|-------------|
| create-repo-foundation | 2 | Scaffold repo: .gitignore, README, LICENSE, CONTRIBUTING |
| test-strategy-designer | 1 | Design test strategy: unit, integration, e2e, coverage |
| repo-docs-writer | 1 | Write or improve README, CONTRIBUTING, API docs |
| release-pipeline-designer | 2 | Design CI/CD pipelines: build, test, scan, deploy |
| ai-code-review-guardrails | 1 | Define guardrails for AI-assisted code review |
| dependency-governance | 1 | Define dependency policy: licenses, pinning, blocklist |
| observability-bootstrap | 2 | Bootstrap logging, metrics, tracing, dashboards |

**IDE & Authoring (6)** — Rules, skills, subagents, migration, shell, settings

| Skill | Risk | Description |
|-------|------|-------------|
| create-rule | 1 | Create rules for persistent AI guidance |
| create-skill | 1 | Create new Agent Skills |
| create-subagent | 2 | Create subagents for complex tasks |
| migrate-to-skills | 2 | Migrate rules and commands to skills format |
| shell | 3 | Shell and terminal operations |
| update-cursor-settings | 2 | Modify Cursor/VSCode user settings |

---

## Quick Start

1. **Clone** the repository
2. **Copy** or symlink skill folders into `~/.cursor/skills/` (or `.cursor/skills/` for project-level)
3. **Validate** (optional): `npm run validate:full`

---

## Risk Tiers

| Tier | Description |
|------|-------------|
| 0 | Read-only guidance; no execution |
| 1 | Content generation; user applies manually |
| 2 | Code/config proposals; Validation Checklist required |
| 3 | Pipeline/infra impact; human review required |

---

## Documentation

- [README](README.md) — Overview, install, skill list
- [CONTRIBUTING](CONTRIBUTING.md) — How to contribute
- [SECURITY](SECURITY.md) — Vulnerability reporting
- [docs/](docs/) — Authoring guide, governance, release checklist

---

## Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for the complete v1.0.0 changelog.
