---
name: repo-docs-writer
risk_tier: 1
description: >-
  Writes or improves repository documentation: README, CONTRIBUTING, API docs,
  architecture overview, runbooks. Use when creating docs, improving existing
  docs, or generating documentation from code structure. Complements
  create-repo-foundation for content quality and completeness.
---

# Repo Docs Writer

## Purpose

Produces or improves repository documentation. Writes README, CONTRIBUTING, API docs, architecture overviews, and runbooks. Output is content for user to apply. Complements create-repo-foundation (which scaffolds structure); this skill focuses on content quality and completeness. Tier 1: proposals only; no overwrite without confirmation.

## When to Use

- User wants to write or improve README, CONTRIBUTING, or other docs
- User asks for API documentation, architecture overview, or runbook
- User needs docs generated from code structure or comments
- User wants to improve existing documentation quality

## Inputs

| Input | Description |
|-------|-------------|
| Target doc | README, CONTRIBUTING, API docs, architecture, runbook |
| Repo context | Project type, language, key features |
| Existing content | What to preserve or improve |
| Audience | Developers, operators, contributors |

## Outputs

- **Document content** — Markdown ready to paste or apply
- **Sections** — Structured with headings; clear and scannable
- **Code examples** — Where applicable; tested patterns
- **Links** — To other docs, external resources

## Steps / Behavior

1. **Identify target** — Which doc(s) to create or improve
2. **Gather context** — Read existing README, package.json, key files
3. **Outline structure** — Sections appropriate for doc type
4. **Generate content** — Clear, technical, concise
5. **Add examples** — Where relevant; use real patterns from repo
6. **Review** — Ensure completeness; no placeholder text

## Constraints

- **Trust Boundaries:** User input untrusted; validate paths and repo context. Output is proposal only; user applies. No overwrite without confirmation.
- **Output Validation:** Label as proposal; user applies. No fabricated APIs or config; use actual repo structure.
- **Limitations:** Proposes content only; user applies. Does not run or validate code examples. API docs from code require docstrings; may be incomplete.
- **Safety Guardrails (Tier 1):** Proposals only; user applies. No file overwrites without confirmation. No fabricated data—use actual repo structure; do not invent APIs or config. Preserve intent—when improving, keep user's meaning; improve clarity.

## Examples

See [examples.md](examples.md) for example docs. Use [prompt-template.md](prompt-template.md) for structured invocation.

## Validation Checklist

- [ ] Sections match doc type (README: install, usage; CONTRIBUTING: process)
- [ ] Code examples are syntactically valid
- [ ] No placeholder text (TODO, TBD) unless explicitly marked
- [ ] Links are valid or relative

## Portability Notes

Document format is Markdown; platform-agnostic. README conventions (badges, structure) vary by repo host (GitHub, GitLab). Adapt for audience and platform.
