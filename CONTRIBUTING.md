# Contributing to Jade CI/CD Agent Skills Pack

Thank you for contributing to the Jade project's CI/CD agent skills. This guide covers how to propose changes, add skills, and meet quality standards.

**Governance:** Skill approval, security review, and release versioning are defined in [docs/ai-governance-model.md](docs/ai-governance-model.md).

---

## How to Contribute

### Reporting Issues

- Use GitHub Issues for bugs, feature requests, or documentation improvements
- Search existing issues before creating a new one
- Include: steps to reproduce, expected vs actual behavior, environment (OS, Node version, Cursor version)

### Proposing Changes

1. **Fork** the repository
2. **Create a branch** from `master` or `main`:
   ```bash
   git checkout -b feature/my-skill
   ```
3. **Make changes** following [docs/authoring-guide.md](docs/authoring-guide.md) and [docs/skill-style-guide.md](docs/skill-style-guide.md)
4. **Validate:**
   ```bash
   npm run validate
   npm run validate:full   # Node + Python
   npm run lint:md
   npm run score
   ```
5. **Commit** with conventional messages:
   ```bash
   git commit -m "feat(skill): add observability-evaluator"
   git commit -m "fix(security-evaluator): correct Trust Boundaries section"
   ```
6. **Push** and open a Pull Request

---

## Adding a New Skill

1. **Create directory:** `skill-name/` (lowercase, hyphens only)

2. **Add required and recommended files:**

   | File | Required | Purpose |
   |------|----------|---------|
   | `SKILL.md` | Yes | Core instructions; YAML frontmatter; required sections per [skill-authoring-standard](docs/skill-authoring-standard.md) |
   | `examples.md` | Recommended | Example prompts and expected behavior |
   | `prompt-template.md` | Recommended | Invocation templates |
   | `reference.md` | Optional | Reference material, criteria, tables |

3. **Update `skills-manifest.json`** with the new skill entry:
   - `name`, `version`, `category`, `risk_tier`
   - `triggers`, `tags`, `summary`
   - `required_files`, `maintainer`, `last_reviewed`, `security_reviewed` (for Tier 3)

4. **Run validation:**
   ```bash
   npm run validate
   npm run validate:full
   ```

5. **Submit PR** with description of the skill, use cases, and risk tier justification

See [docs/authoring-guide.md](docs/authoring-guide.md) for detailed authoring guidance.

### Pre-merge checklist (new skills)

Before requesting review, ensure:

- [ ] `SKILL.md` has all required sections: Purpose, When to Use, Inputs, Outputs, Steps/Behavior, Constraints
- [ ] Trust Boundaries and Output Validation present (or consolidated in Constraints)
- [ ] `examples.md` has at least 3 example prompts
- [ ] `skills-manifest.json` entry is complete: `name`, `category`, `risk_tier`, `triggers`, `summary`
- [ ] `npm run validate` passes
- [ ] `npm run validate:full` passes
- [ ] `npm run score` shows no new blockers

---

## Skill Requirements

- **SKILL.md:** YAML frontmatter with `name` and `description`; required sections per [docs/skill-authoring-standard.md](docs/skill-authoring-standard.md); body under 500 lines
- **name:** Lowercase, hyphens only, max 64 chars; must match directory name
- **description:** Third person; include trigger terms; max 1024 chars
- **Content:** Direct, technical, enterprise-friendly; no marketing language
- **Trust Boundaries & Output Validation:** Every skill must include these (or consolidated in Constraints per [docs/ai-security-model.md](docs/ai-security-model.md))
- **Tier 2:** Must include Validation Checklist; define safe vs unsafe; require approval for unsafe
- **Tier 3:** Requires human review; high-risk outputs must include explicit warnings

---

## Adding Dependencies

If you add npm or pip dependencies:

1. Run `npm install` (if npm)
2. Run `npm run sbom` to regenerate the SBOM
3. Commit updated `sbom.json` and `package-lock.json`

---

## Branch Protection and PR Requirements

**Recommended repository settings:**

- **Branch protection** on `master`/`main`: Require PR before merge; require status checks (Validate, Lint, Link Check)
- **Required reviewers:** At least one approval for security/compliance skills (see CODEOWNERS)
- **Status checks:** All CI workflows must pass; no merge on failure

### Pull Request Process

1. Ensure all CI checks pass (validate, lint, links, certification score)
2. Request review from maintainers
3. Address feedback
4. **Skill approval:** New skills and Tier 3 changes require security review per [docs/ai-governance-model.md](docs/ai-governance-model.md)
5. Maintainers merge when approved

---

## Code of Conduct

- Be respectful and constructive
- Focus on technical merit
- Assume good intent

---

## Questions

Open an issue with the `question` label or start a discussion.
