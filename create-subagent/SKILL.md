---
name: create-subagent
risk_tier: 2
description: >-
  Create custom subagents for specialized AI tasks. Use when you want to create
  a new type of subagent, set up task-specific agents, configure code reviewers,
  debuggers, or domain-specific assistants with custom prompts.
disable-model-invocation: true
---
# Create Custom Subagents

## Purpose

Guides creation of custom subagents for AI-assisted development environments. Subagents are specialized AI assistants that run in isolated contexts with custom system prompts. Produces subagent files in `.agent/agents/` or `~/.agent/agents/`. Tier 2: user approval required for file writes; no credential injection in system prompts.

## When to Use

- User wants to create a new type of subagent
- User asks to set up task-specific agents (code reviewers, debuggers, domain-specific assistants)
- User wants to preserve context by isolating exploration from main conversation
- User wants to specialize behavior with focused system prompts

## Inputs

| Input | Description |
|-------|-------------|
| Task purpose | What the subagent should do when invoked |
| Scope | Project (`.agent/agents/`) or user (`~/.agent/agents/`) |
| System prompt content | Instructions, workflow, output format, constraints |

## Outputs

- **Subagent file** — `.md` in `.agent/agents/` or `~/.agent/agents/`
- **Frontmatter** — `name` (lowercase, hyphens), `description` (delegation trigger)
- **Body** — System prompt (markdown) that defines behavior when invoked

## Steps / Behavior

1. **Decide scope** — Project-level (`.agent/agents/`) for team-shared; user-level (`~/.agent/agents/`) for personal.
2. **Create file** — `mkdir -p .agent/agents` or `~/.agent/agents`; create `{name}.md`.
3. **Define frontmatter** — `name` (unique, lowercase, hyphens), `description` (specific; include "use proactively" for auto-delegation).
4. **Write system prompt** — What to do when invoked; workflow; output format; constraints.
5. **Test** — Ask AI to use the new subagent for a sample task.

### Subagent Locations

| Location | Scope | Priority |
|----------|-------|----------|
| `.agent/agents/` | Current project | Higher |
| `~/.agent/agents/` | All projects | Lower |

### Required Frontmatter Fields

| Field | Description |
|-------|-------------|
| `name` | Unique identifier (lowercase letters and hyphens only) |
| `description` | When to delegate to this subagent (be specific; include trigger terms) |

### Best Practices

- Design focused subagents—each excels at one specific task
- Write detailed descriptions—include trigger terms for delegation
- Check into version control—share project subagents with team
- Use proactive language—include "use proactively" in descriptions

## Constraints

- **Trust Boundaries:** User input untrusted; validate paths and system prompt content. Safe: propose subagent file. Unsafe: file writes to `.agent/agents/`—require user approval. No credential injection: never include secrets in system prompts.
- **Output Validation:** Label as proposal; user reviews before applying. Subagent runs with same access as main agent; no built-in sandboxing.
- **Limitations:** Paths and delegation vary by IDE; adapt per vendor docs. Subagent invocation is delegated by main agent; user cannot always invoke directly. No built-in sandboxing; subagent runs with same access as main agent.
- **Safety Guardrails (Tier 2):** Proposals only; user approves before applying. No secrets in system prompts. Subagent has same access as main agent—design prompts accordingly.

## Examples

See [examples.md](examples.md) for example subagents (code reviewer, debugger, data scientist). Use [prompt-template.md](prompt-template.md) for structured invocation.

## Validation Checklist

- [ ] Verify `name` and `description` in frontmatter are set
- [ ] Confirm agent file path (project vs user) matches intent
- [ ] Review system prompt for sensitive or project-specific content
- [ ] Test agent invocation before committing

## Portability Notes

Subagent format (`.md` with YAML frontmatter + body) is generic. Paths (`.agent/agents/`, `~/.agent/agents/`) follow this pack’s convention; other tools may use different locations and delegation mechanisms.
