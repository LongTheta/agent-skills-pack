# Skill Style Guide

Writing conventions for Agent Skills in this repository.

---

## Tone and Voice

- **Direct and technical** — No marketing language or hype
- **Enterprise-friendly** — Assume regulated environments, compliance, audit
- **Actionable** — Clear steps, checklists, and outputs
- **Concise** — Every token competes for context; avoid redundancy

---

## Structure

### SKILL.md

1. **When to Use** — Trigger scenarios; when the agent should apply
2. **Workflow / Process** — Steps, decision points, checklists
3. **Output Format** — Template or structure for responses
4. **Guidelines** — Constraints, anti-patterns, preferences
5. **Additional Resources** — Links to reference, examples, templates

### examples.md

- 3–5 example prompts minimum
- Cover common and edge-case scenarios
- Include expected output structure where helpful

### prompt-template.md

- Copy-paste template with `[placeholders]`
- One or more variants (e.g., standard, FedRAMP)
- Example filled-in template

### reference.md

- Detailed criteria, decision trees, API references
- Tables for quick lookup
- One level deep from SKILL.md; avoid deep nesting

---

## Terminology

- **Skill** — A set of instructions that teach the agent a domain task
- **Invoke** — User or agent triggers the skill
- **Trigger** — Scenario that causes the agent to apply the skill
- **Frontmatter** — YAML metadata at top of SKILL.md

Use consistent terms throughout. Avoid mixing "rule," "command," "skill" when referring to skills.

---

## Formatting

- **Headers:** Sentence case for H1; title case for H2/H3
- **Lists:** Prefer bullet for unordered; numbered for sequential steps
- **Tables:** Use for criteria, mappings, quick reference
- **Code blocks:** Specify language for syntax highlighting

---

## Anti-Patterns

- **Vague descriptions** — "Helps with security" → "Evaluates tools for security and compliance; use when assessing adoption risk"
- **Too many options** — Provide a default with escape hatch, not a menu
- **Time-sensitive info** — Avoid "before August 2025"; use "Current" vs "Legacy" sections
- **Windows paths in examples** — Prefer `scripts/helper.py` over `scripts\helper.py`
- **Verbose explanations** — Assume the agent knows basics; add only domain-specific context

---

## Compliance and Security Skills

For security, compliance, and Zero Trust skills:

- State assumptions explicitly
- Call out unknowns and missing information
- Use structured output (scorecards, verdicts, checklists)
- Include NIST, FedRAMP, DoD references where relevant
- Be strict by default; do not relax controls to achieve pass
