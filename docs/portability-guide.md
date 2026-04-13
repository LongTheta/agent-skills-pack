# Portability Guide

How to adapt Agent Skills for use across AI-assisted IDEs and editors.

---

## Overview

Skills in this repository use a standard structure designed for portability:

- `SKILL.md` — Core instructions (markdown + YAML frontmatter)
- `examples.md` — Example prompts
- `prompt-template.md` — Invocation templates
- `reference.md` — Reference material

The format is IDE-agnostic. Adaptation is mainly about **discovery** and **invocation**.

---

## Default layout (this pack)

- **Discovery:** Skills in `~/.agent/skills/` or `.agent/skills/`; agent uses `description` for matching where supported
- **Invocation:** Automatic when user request matches; or explicit via slash/mention per product
- **Frontmatter:** `name`, `description`, optional `disable-model-invocation`

---

## Other AI IDEs

### GitHub Copilot / Copilot Workspace

- **Adaptation:** Convert SKILL.md to a custom instruction or rule
- **Location:** `.github/copilot-instructions.md` or repo-specific instructions
- **Format:** Extract body of SKILL.md; prepend to context when relevant

### Windsurf (Codeium)

- **Adaptation:** Use Rules or Custom Instructions
- **Format:** Markdown; may support YAML frontmatter in rules

### Zed

- **Adaptation:** Use project or user AI instructions
- **Format:** Plain markdown; structure similar to SKILL.md body

### Continue

- **Adaptation:** Use `.continuerc` or custom prompts
- **Format:** Markdown; reference skills as context files

### Generic / Custom

- **Adaptation:** Treat each skill as a **prompt template** or **context document**
- **Flow:** 1) User request → 2) Match to skill (by keywords or manual selection) → 3) Inject SKILL.md + relevant examples/reference into context → 4) Generate response

---

## Mapping Table

| Concept | This pack | Generic |
|---------|-----------|---------|
| Skill location | `~/.agent/skills/<name>/` | Any path |
| Discovery | `description` field | Keyword match, manual pick |
| Invocation | Automatic or explicit | Manual or custom routing |
| Frontmatter | `name`, `description` | Optional; use for metadata |

---

## Minimal Portable Format

For maximum portability, each skill can be reduced to:

1. **Instructions** — Body of SKILL.md (vendor-agnostic frontmatter where possible)
2. **Examples** — examples.md content
3. **Template** — prompt-template.md content

Package as:

- A single markdown file (instructions + examples + template)
- A directory with the four standard files
- A JSON object with `instructions`, `examples`, `template` keys

---

## Contributing Portable Skills

When adding skills:

- Avoid vendor-specific paths in the skill body; use placeholders like `{skills-dir}`
- Document product-specific behavior in SKILL.md only where necessary
- Keep `reference.md` and `examples.md` IDE-agnostic
