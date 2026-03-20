# Jade CI/CD Agent Skills Pack

**Production-ready Agent Skills for the Jade project—AI-assisted CI/CD, repository creation, security, DevSecOps, Zero Trust, testing, release, and IDE workflows.** End-to-end pack for repo creation, hardening, testing, release, and maintenance. Designed for Cursor and other AI agent IDEs.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Compliance alignment:** NIST AI RMF, NIST SSDF (SP 800-218), NIST Zero Trust, OWASP LLM/Agent security, SLSA-minded supply chain. See [docs/ai-security-model.md](docs/ai-security-model.md) and [docs/supply-chain-security.md](docs/supply-chain-security.md).

---

## Target Audience

- **Platform engineers** — GitOps, CI/CD, Kubernetes, DevSecOps
- **Security teams** — Compliance, vulnerability remediation, Zero Trust
- **Federal / regulated** — DoD Zero Trust, FedRAMP, NIST 800-53
- **AI agents** — Architecture design, evaluation, production readiness
- **Developers** — Rules, skills, IDE configuration, shell workflows

---

## Value Proposition

Jade CI/CD Agent Skills Pack delivers 20+ curated skills for the Jade CI/CD agent and teams building secure, compliant, production-grade systems. Use them for GitOps, vulnerability remediation, Zero Trust architecture, test strategy, release pipelines, and IDE configuration. Each skill is self-contained, versioned, and enterprise-ready. Target: platform engineers, security teams, federal/regulated environments.

---

## Architecture Overview

| Layer | Purpose |
|-------|---------|
| **Skills** | Domain instructions in `SKILL.md` + `examples.md` + `prompt-template.md` + `reference.md`. Loaded from `~/.cursor/skills/` or `.cursor/skills/`. |
| **Rules** | Project-level Cursor rules in `.cursor/rules/`. Enforce Jade conventions, security, and validation prompts. |
| **CI/CD** | GitHub Actions: manifest validation, Python structure checks, markdown lint, link check, certification score (threshold 7.5), SBOM generation. |

Skills and rules work together: skills provide task-specific behavior for Jade workflows; rules enforce governance and safety across the repo.

---

## Features

- **20+ skills** across Security & Compliance, Repository Lifecycle, and IDE & Authoring
- **Risk-tiered** (0–3): read-only guidance to pipeline-impacting; each tier has defined guardrails
- **Trust Boundaries & Output Validation** in every SKILL.md per [docs/ai-security-model.md](docs/ai-security-model.md)
- **Machine-readable manifest** (`skills-manifest.json`) for automation and discovery
- **Certification scoring** (0–10) with CI gate at 7.5
- **SBOM** (CycloneDX) generated in CI
- **Git hooks** (Husky): pre-commit validate, pre-push validate + lint
- **Portability** to GitHub Copilot, Windsurf, Zed, Continue via [docs/portability-guide.md](docs/portability-guide.md)

---

## Quick Start

**1. Clone**

```bash
git clone https://github.com/ai-devsecops-packs/jade-cicd-agent-skills-pack.git
cd jade-cicd-agent-skills-pack
```

**2. Install dependencies**

```bash
npm install
```

**3. Link skills to Cursor**

**Option A — Copy (one-time):**

```bash
# Linux/macOS
cp -r ai-agent-architecture security-evaluator ~/.cursor/skills/

# Windows (PowerShell)
Copy-Item -Recurse ai-agent-architecture, security-evaluator $env:APPDATA\Cursor\skills\
```

**Option B — Symlink (live updates):**

```bash
# Linux/macOS
ln -s "$(pwd)/ai-agent-architecture" ~/.cursor/skills/ai-agent-architecture
ln -s "$(pwd)/security-evaluator" ~/.cursor/skills/security-evaluator

# Windows (Admin PowerShell)
New-Item -ItemType SymbolicLink -Path "$env:APPDATA\Cursor\skills\ai-agent-architecture" -Target "$(Get-Location)\ai-agent-architecture"
```

**4. Validate**

```bash
npm run validate
npm run score
```

---

## Installation Modes

| Mode | What to Install | Use Case |
|------|-----------------|----------|
| **Skills only** | Copy/symlink selected skill folders into `~/.cursor/skills/` | Use skills in any project; no repo rules |
| **Rules only** | Copy `.cursor/rules/*.mdc` into your repo's `.cursor/rules/` | Enforce Jade conventions without skills |
| **Skills + Rules** | Skills in `~/.cursor/skills/` + rules in `.cursor/rules/` | Full Jade AI guidance; rules apply when working in this repo |
| **Full DevSecOps** | Clone repo, `npm install`, symlink skills, use rules in repo | Development, contribution, CI validation |

**Project-level skills:** Copy skill folders into `.cursor/skills/` at repo root to share with your team.

---

## Example Workflows

**Security review of a CI pipeline**

```
User: Review my .github/workflows/deploy.yml for security and Zero Trust compliance.
Agent: [Uses security-evaluator + zero-trust-gitops-enforcement] Produces findings, severity, remediation.
```

**Scaffold a new repo**

```
User: Create a new repo foundation with .gitignore, README, LICENSE, CONTRIBUTING.
Agent: [Uses create-repo-foundation] Generates files; user reviews and applies.
```

**CVE remediation**

```
User: Scan for CVEs in package.json and propose fixes.
Agent: [Uses cve-detect-and-remediate] Queries OSV/NVD; proposes patches; user approves before apply.
```

**Design a release pipeline**

```
User: Design a CI/CD pipeline for a Node.js app with build, test, scan, and deploy.
Agent: [Uses release-pipeline-designer] Produces GitHub Actions or GitLab CI config.
```

---

## Repository Structure

```
jade-cicd-agent-skills-pack/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── CHANGELOG.md
├── CODEOWNERS
├── skills-manifest.json      # Machine-readable catalog
├── sbom.json                 # CycloneDX SBOM (CI-generated)
├── .husky/                   # pre-commit, pre-push
├── .cursor/rules/            # Jade project rules (skill-authoring, ai-security-enforcement, etc.)
├── .github/workflows/        # validate.yml, lint.yml, links.yml
├── docs/
│   ├── README.md              # Documentation index
│   ├── ai-security-model.md
│   ├── skill-authoring-standard.md
│   ├── authoring-guide.md
│   ├── portability-guide.md
│   └── ...
├── scripts/
│   ├── validate-skills.js
│   ├── validate_skills.py
│   ├── certification-score.js
│   └── generate-manifest.js
├── tests/golden/
└── <skill-name>/
    ├── SKILL.md
    ├── examples.md
    ├── prompt-template.md
    └── reference.md
```

---

## Skill System Overview

Each skill is a self-contained unit:

| File | Purpose |
|------|---------|
| `SKILL.md` | Core instructions; YAML frontmatter (`name`, `description`); required sections: Purpose, When to Use, Inputs, Outputs, Steps/Behavior, Constraints (Trust Boundaries + Output Validation) |
| `examples.md` | Example prompts and expected behavior |
| `prompt-template.md` | Invocation templates |
| `reference.md` | Reference material, criteria, tables |

**Categories:** Security & Compliance | Repository Lifecycle | IDE & Authoring

**Risk tiers:** 0 (read-only) | 1 (content generation) | 2 (code/config proposal) | 3 (infra/pipeline impact). Tier 2+ require Validation Checklist; Tier 3 requires human review before applying outputs.

**Skill catalog:** See [skills-manifest.json](skills-manifest.json) for the full catalog.

| Category | Skills |
|----------|--------|
| **Security & Compliance** | [ai-agent-architecture](ai-agent-architecture/), [ai-devsecops-policy-enforcement](ai-devsecops-policy-enforcement/), [cve-detect-and-remediate](cve-detect-and-remediate/), [dod-zero-trust-architect](dod-zero-trust-architect/), [security-evaluator](security-evaluator/), [tool-evaluator](tool-evaluator/), [zero-trust-gitops-enforcement](zero-trust-gitops-enforcement/) |
| **Repository Lifecycle** | [create-repo-foundation](create-repo-foundation/), [test-strategy-designer](test-strategy-designer/), [repo-docs-writer](repo-docs-writer/), [release-pipeline-designer](release-pipeline-designer/), [ai-code-review-guardrails](ai-code-review-guardrails/), [dependency-governance](dependency-governance/), [observability-bootstrap](observability-bootstrap/) |
| **IDE & Authoring** | [create-rule](create-rule/), [create-skill](create-skill/), [create-subagent](create-subagent/), [migrate-to-skills](migrate-to-skills/), [shell](shell/), [update-cursor-settings](update-cursor-settings/) |

---

## Rules System Overview

Rules in `.cursor/rules/` apply when working in this repo:

| Rule | Purpose |
|------|---------|
| `project-conventions.mdc` | Validation prompts, commit reminders, skill authoring steps |
| `ai-security-enforcement.mdc` | Trust Boundaries, Output Validation, tier-specific guardrails |
| `skill-authoring.mdc` | Skill structure, required sections |
| `markdown-style.mdc` | Markdown formatting standards |

Rules are always-on for this repo; skills are invoked when the user's request matches the skill's trigger terms.

---

## DevSecOps Alignment

- **NIST SSDF (SP 800-218):** Secure development practices, supply chain integrity
- **NIST AI RMF:** Trustworthy AI; risk tiers and guardrails
- **NIST Zero Trust:** Zero Trust principles in pipelines (zero-trust-gitops-enforcement, dod-zero-trust-architect)
- **OWASP LLM/Agent:** Prompt injection defenses, output validation
- **SLSA-minded:** SBOM, attestation path (see [docs/supply-chain-security.md](docs/supply-chain-security.md))

---

## Validation & Scoring

| Check | Command | CI |
|-------|---------|-----|
| Manifest validation | `node scripts/validate-skills.js` | ✅ |
| Skill structure | `python scripts/validate_skills.py` | ✅ |
| Markdown lint | `npm run lint:md` | ✅ |
| Link check | `linkinator .` | ✅ |
| Certification score | `npm run score` | ✅ (threshold 7.5) |
| SBOM | `npm run sbom` | ✅ |

**Before committing:** `npm run validate` and `npm run lint:md`. Pre-commit runs validate; pre-push runs validate + lint.

**Score levels:** 10 = federal-grade; 8–9.9 = production-ready; 6–7.9 = acceptable; &lt;6 = not release-ready. See [docs/certification-model.md](docs/certification-model.md).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide. Summary:

1. Fork; create branch from `master`/`main`
2. Add/update skill per [docs/skill-authoring-standard.md](docs/skill-authoring-standard.md)
3. Update `skills-manifest.json` if adding a skill
4. Run `npm run validate` and `npm run lint:md`
5. Open PR; ensure CI passes

New skills and Tier 3 changes require security review per [docs/ai-governance-model.md](docs/ai-governance-model.md).

---

## Roadmap

- [ ] **v1.1** — Node.js / npm CVE support in cve-detect-and-remediate
- [ ] **v1.2** — MCP server evaluation skill
- [ ] **v1.3** — SLSA Level 1 provenance (build attestations)
- [ ] **v2.0** — Multi-IDE plugin / extension packaging

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## License

[MIT](LICENSE)
