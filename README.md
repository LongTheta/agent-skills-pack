# Agent Skills Pack

A production-ready collection of **Agent Skills** for AI-assisted development—security, compliance, DevSecOps, Zero Trust, and IDE workflows. Designed for Cursor and other AI agent IDEs.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Overview

Agent Skills are specialized instructions that teach AI agents how to perform domain-specific tasks. This repository provides a curated, reusable set of skills for teams building secure, compliant, and production-grade systems.

Each skill is self-contained, versioned independently, and can be used across projects or adapted for other AI coding assistants.

---

## Who This Is For

- **Platform engineers** — GitOps, CI/CD, Kubernetes, DevSecOps
- **Security teams** — Compliance, vulnerability remediation, Zero Trust
- **Federal / regulated** — DoD Zero Trust, FedRAMP, NIST 800-53
- **AI agents** — Architecture design, evaluation, production readiness
- **Developers** — Rules, skills, IDE configuration, shell workflows

---

## Supported Use Cases

| Use Case | Skills |
|----------|--------|
| **Security & compliance** | Security Evaluator, Policy Enforcement, CVE Remediation |
| **Zero Trust** | DoD Zero Trust Architect, Zero Trust GitOps Enforcement |
| **AI agent design** | AI Agent Architecture |
| **Tool adoption** | Tool Evaluator |
| **IDE & workflows** | Create Rule, Create Skill, Create Subagent, Update Settings |
| **Migration** | Migrate to Skills |

---

## Skill Categories

### Security & Compliance

| Skill | Description |
|-------|-------------|
| [ai-agent-architecture](ai-agent-architecture/) | Design and evaluate AI agent systems across 7 layers |
| [ai-devsecops-policy-enforcement](ai-devsecops-policy-enforcement/) | Policy enforcement for CI/CD and GitOps pipelines |
| [cve-detect-and-remediate](cve-detect-and-remediate/) | Detect vulnerable dependencies and propose remediations |
| [dod-zero-trust-architect](dod-zero-trust-architect/) | DoD Zero Trust Architecture evaluation and design |
| [security-evaluator](security-evaluator/) | Security and compliance evaluation for systems |
| [tool-evaluator](tool-evaluator/) | Evaluate tools for enterprise adoption |
| [zero-trust-gitops-enforcement](zero-trust-gitops-enforcement/) | Zero Trust principles in CI/CD and GitOps |

### IDE & Authoring

| Skill | Description |
|-------|-------------|
| [create-rule](create-rule/) | Create rules for persistent AI guidance |
| [create-skill](create-skill/) | Create new Agent Skills |
| [create-subagent](create-subagent/) | Create subagents for complex tasks |
| [migrate-to-skills](migrate-to-skills/) | Migrate rules and commands to skills format |
| [shell](shell/) | Shell and terminal operations |
| [update-cursor-settings](update-cursor-settings/) | Modify Cursor/VSCode user settings |

---

## Installation

### Cursor

1. **Clone or sync** this repository:
   ```bash
   git clone https://github.com/LongTheta/agent-skills-pack.git
   ```

2. **Link skills** to Cursor:
   - **Copy**: Copy desired skill folders into `~/.cursor/skills/` (or `%APPDATA%\Cursor\skills\` on Windows)
   - **Symlink** (recommended for updates):
     ```bash
     # macOS / Linux
     ln -s "$(pwd)/agent-skills-pack/security-evaluator" ~/.cursor/skills/security-evaluator

     # Windows (PowerShell, run as Administrator)
     New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.cursor\skills\security-evaluator" -Target "C:\path\to\agent-skills-pack\security-evaluator"
     ```

3. **Project-level** (optional): Copy skills into `.cursor/skills/` in your project to share with your team.

4. **Managed install**: If your Cursor setup supports managed skills, install via Cursor Settings → Skills.

### Other AI IDEs

Skills use a standard structure (`SKILL.md`, `examples.md`, `reference.md`, `prompt-template.md`). See [docs/portability-guide.md](docs/portability-guide.md) for adapting skills to other AI coding assistants (e.g., GitHub Copilot, Windsurf, Zed, Continue).

---

## Repository Structure

```
agent-skills-pack/
├── README.md                 # This file
├── skills-manifest.json      # Machine-readable skill catalog
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/                     # Authoring and portability guides
│   ├── authoring-guide.md
│   ├── skill-style-guide.md
│   ├── portability-guide.md
│   └── release-checklist.md
├── scripts/                  # Validation and tooling
│   ├── validate-skills.js
│   ├── generate-manifest.js
│   └── generate_manifest.py   # Rich manifest with triggers (npm run generate-manifest:py)
├── .github/workflows/        # CI: lint, manifest validation, link checks
└── <skill-name>/             # One directory per skill
    ├── SKILL.md              # Required — main skill definition
    ├── examples.md           # Example prompts
    ├── prompt-template.md    # Invocation templates
    └── reference.md          # Detailed reference material
```

---

## Contributing

We welcome contributions. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for:

- How to propose new skills
- Skill structure and style requirements
- Pull request workflow
- Code of conduct expectations

See [docs/authoring-guide.md](docs/authoring-guide.md) for detailed authoring guidance.

---

## Roadmap

- [ ] **v1.1** — Additional skills for observability, cost optimization
- [ ] **v1.2** — Node.js / npm CVE support in cve-detect-and-remediate
- [ ] **v1.3** — MCP server evaluation skill
- [ ] **v2.0** — Multi-IDE plugin / extension packaging

See [CHANGELOG.md](CHANGELOG.md) for version history and semantic versioning.

---

## License

[MIT](LICENSE)
