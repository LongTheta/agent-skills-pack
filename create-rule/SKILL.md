---
name: create-rule
risk_tier: 1
description: >-
  Create project AI rules for persistent guidance. Use when you want to create a
  rule, add coding standards, set up project conventions, configure
  file-specific patterns, create RULE.md files, or asks about .agent/rules/ or
  AGENTS.md.
---

# Create Project AI Rules

## Purpose

Creates project rules in `.agent/rules/` to provide persistent context for the AI agent. Produces `.mdc` rule files with frontmatter and actionable content. Tier 1: proposals only; user reviews before applying; no overwrite without confirmation.

## When to Use

- User wants to create a rule, add coding standards, or set up project conventions
- User asks about `.agent/rules/`, RULE.md, or AGENTS.md
- User wants file-specific patterns (e.g., TypeScript conventions when editing `.ts` files)
- User needs persistent AI guidance for a project

## Inputs

| Input | Description |
|-------|-------------|
| User's intent | What to enforce or teach |
| Scope | Always apply vs. file-specific |
| File patterns | If file-specific: e.g., `**/*.ts`, `backend/**/*.py` |

## Outputs

- **.mdc rule file** — In `.agent/rules/`
- **Frontmatter** — `description`, optional `globs`, `alwaysApply`
- **Rule body** — Clear, actionable content

## Steps / Behavior

1. **Gather requirements** — Purpose (what to enforce/teach), scope (always vs file-specific), file patterns (if file-specific).
2. **Infer from context** — If previous conversation provides answers, infer rules; create multiple rules if distinct topics.
3. **Create rule file** — `.mdc` in `.agent/rules/` with YAML frontmatter and body.
4. **Configure frontmatter** — `description` (required), `globs` (for file-specific), `alwaysApply` (for universal).
5. **Write body** — Concise, actionable; under 50 lines recommended; one concern per rule.

### Rule File Format

Rules are `.mdc` files in `.agent/rules/` with YAML frontmatter:

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | What the rule does (shown in rule picker) |
| `globs` | string | File pattern—rule applies when matching files are open |
| `alwaysApply` | boolean | If true, applies to every session |

### Best Practices

- **Under 50 lines** — Rules should be concise
- **One concern per rule** — Split large rules into focused pieces
- **Actionable** — Write like clear internal docs
- **Concrete examples** — Provide examples of how to fix issues

## Constraints

- **Trust Boundaries:** User input untrusted; validate paths and patterns. Output proposes .mdc files; user reviews before applying. No overwrite without confirmation.
- **Output Validation:** Label as proposal; user applies. No auto-overwrite of existing rules.
- **Limitations:** Rule filename and path conventions may differ by IDE; align with your environment’s docs. Max ~50 lines recommended; split large rules into focused pieces. Cannot execute code; rules are static guidance only.
- **Safety Guardrails (Tier 1):** Proposals only; user applies manually. No auto-apply of rules. Keep rules concise: under 50 lines; one concern per rule. No secrets: do not include API keys, credentials, or sensitive data in rules.

## Examples

See [examples.md](examples.md) for example rules (TypeScript standards, React patterns). Use [prompt-template.md](prompt-template.md) for structured invocation.

## Validation Checklist

- [ ] File is `.mdc` format in `.agent/rules/`
- [ ] Frontmatter configured correctly
- [ ] Content under 500 lines
- [ ] Includes concrete examples

## Portability Notes

Rules use `.mdc` with YAML frontmatter under `.agent/rules/` in this pack. Other tools use different rule systems (e.g., Copilot's `.github/copilot-instructions.md`).
