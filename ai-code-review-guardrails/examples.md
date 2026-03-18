# AI Code Review Guardrails — Examples

## Example 1: Python Project

**Input:** "Define AI code review guardrails for a Python API"

**Output:** Categories: security (secrets, injection), correctness (error handling), style (black, ruff). Severity: Critical blocks; High suggests. Format: Inline + summary. Boundary: No approve/merge.

## Example 2: React Frontend

**Input:** "Guardrails for AI reviewing React PRs"

**Output:** Categories: accessibility, performance, security (XSS), hooks rules. Severity: a11y High; style Low. Format: Checklist + inline. Boundary: Human approves.

## Example 3: Generic

**Input:** "Generic AI code review guardrails"

**Output:** Categories: security, correctness, style, tests. Severity: Critical/High/Medium/Low. Format: Markdown summary with file:line refs. Boundary: Propose only.
