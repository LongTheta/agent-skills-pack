# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
