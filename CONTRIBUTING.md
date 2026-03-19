# Contributing to Jade CI/CD Agent Skills Pack

Thank you for your interest in contributing to the Jade project's CI/CD agent skills. This document covers how to propose changes and add new skills.

**Governance:** Skill approval process, security review requirements, and release versioning are defined in [docs/ai-governance-model.md](docs/ai-governance-model.md).

---

## How to Contribute

### Reporting Issues

- Use GitHub Issues for bugs, feature requests, or documentation improvements
- Search existing issues before creating a new one
- Include steps to reproduce, expected vs actual behavior, and environment details

### Proposing Changes

1. **Fork** the repository
2. **Create a branch** from `master`: `git checkout -b feature/my-skill`
3. **Make changes** following the [Authoring Guide](docs/authoring-guide.md) and [Skill Style Guide](docs/skill-style-guide.md)
4. **Validate**: Run `npm run validate` (Node); `npm run validate:full` for full checks (Node + Python)
5. **Commit** with clear messages: `feat(skill): add observability-evaluator`
6. **Push** and open a Pull Request

---

## Adding a New Skill

1. Create a directory: `skill-name/`
2. Add required and recommended files:
   - `SKILL.md` (required)
   - `examples.md` (recommended)
   - `prompt-template.md` (recommended)
   - `reference.md` (optional)
3. Update `skills-manifest.json` with the new skill entry
4. Run validation: `npm run validate`
5. Submit a PR with a description of the skill and its use cases

See [docs/authoring-guide.md](docs/authoring-guide.md) for detailed authoring guidance.

---

## Skill Requirements

- **SKILL.md**: YAML frontmatter with `name` and `description`; required sections per [skill-authoring-standard](docs/skill-authoring-standard.md); body under 500 lines
- **name**: Lowercase, hyphens only, max 64 chars; must match directory name
- **description**: Third person; include trigger terms; max 1024 chars
- **Content**: Direct, technical, enterprise-friendly; no marketing language

---

## Adding Dependencies

If you add npm or pip dependencies:

1. Run `npm run sbom` (or `npm install && npm run sbom`) to regenerate the SBOM
2. Commit updated `sbom.json` and `package-lock.json`

---

## Branch Protection and PR Requirements

**Recommended repository settings:**

- **Branch protection** on `master`/`main`: Require PR before merge; require status checks (Validate, Lint, Link Check)
- **Required reviewers:** At least one approval for security/compliance skills (see CODEOWNERS)
- **Status checks:** All CI workflows must pass; no merge on failure

## Pull Request Process

1. Ensure all CI checks pass (lint, validate, links)
2. Request review from maintainers
3. Address feedback
4. **Skill approval**: New skills and Tier 3 changes require security review per [docs/ai-governance-model.md](docs/ai-governance-model.md)
5. Maintainers will merge when approved

---

## Code of Conduct

- Be respectful and constructive
- Focus on technical merit
- Assume good intent

---

## Questions

Open an issue with the `question` label or start a discussion.
