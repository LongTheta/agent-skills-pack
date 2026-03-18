---
name: create-repo-foundation
risk_tier: 2
description: >-
  Creates the foundational structure for a new repository: .gitignore, README,
  LICENSE, CONTRIBUTING, basic directory layout, and initial config files. Use
  when starting a new repo, scaffolding a project, or establishing repo
  conventions. Complements security and DevSecOps skills applied later.
---

# Create Repository Foundation

Scaffolds the foundational structure for a new repository. Produces essential files and directory layout before security hardening, testing, or release pipelines are added. Use this first in the lifecycle; follow with test-strategy-designer, release-pipeline-designer, and security skills.

## When to Use

- User wants to create a new repository from scratch
- User asks to scaffold a project or establish repo structure
- User needs .gitignore, README, LICENSE, CONTRIBUTING for a new project
- User wants initial directory layout and config conventions

## Inputs

- **Project type:** Application, library, CLI, API, monorepo, etc.
- **Language/runtime:** Python, Node.js, Go, etc. (affects .gitignore, config)
- **License preference:** MIT, Apache-2.0, proprietary
- **Existing files:** Any files already present to preserve

## Outputs

- **.gitignore** — Language and tool-specific exclusions
- **README.md** — Project overview, install, usage, contribution pointer
- **LICENSE** — Selected license text
- **CONTRIBUTING.md** — How to contribute, PR process, code style
- **Directory layout** — e.g., `src/`, `tests/`, `docs/`, `.github/`
- **Initial config** — e.g., `package.json`, `pyproject.toml`, `.editorconfig`

## Workflow

1. **Gather requirements** — Project type, language, license, conventions
2. **Create .gitignore** — Use language-specific templates; add IDE, OS, build artifacts
3. **Create README.md** — Title, description, install steps, usage, link to CONTRIBUTING
4. **Add LICENSE** — Insert full license text; include year and copyright holder
5. **Create CONTRIBUTING.md** — PR process, branch strategy, style guide pointer
6. **Create directory structure** — `src/`, `tests/`, `docs/`, `.github/` as appropriate
7. **Add initial config** — Minimal package.json, pyproject.toml, or equivalent
8. **Summarize** — List created files; note next steps (tests, CI, security review)

## Limitations

- Does not add CI/CD, tests, or security tooling; use release-pipeline-designer and other skills
- License text must be exact; verify from official source
- Does not configure branch protection or repo settings (GitHub/GitLab UI)

## Safety Guardrails

- **Tier 2:** Proposes files; user reviews before applying. Do not overwrite without confirmation.
- **Preserve existing content** — Do not replace README or config if user has custom content unless explicitly asked.
- **No secrets** — Do not add API keys, tokens, or credentials.

## Validation Checklist

- [ ] .gitignore covers language, IDE, OS, build artifacts
- [ ] README has install and usage sections
- [ ] LICENSE matches user choice; year and holder correct
- [ ] CONTRIBUTING references PR process
- [ ] No overwrite of user-provided files without confirmation

## Portability Notes

Structure is platform-agnostic. `.github/` is GitHub-specific; use `.gitlab/` or equivalent for GitLab. Config formats (package.json, pyproject.toml) vary by ecosystem.
