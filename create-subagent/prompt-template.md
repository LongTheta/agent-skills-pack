# Create Subagent — Invocation Template

Copy and fill in the placeholders.

```
Create a subagent with the following:

**Name:** [lowercase-with-hyphens]
**Description:** [When to delegate; include "use proactively" if desired]
**Scope:** [project | user]
**Behavior when invoked:** [What the agent should do]
**Workflow:** [Steps to follow]
**Output format:** [Structure of feedback or output]

**Optional:**
- Checklist or constraints: [list]
- Domain focus: [e.g., security, performance, readability]
```

## Example

```
Create a subagent with the following:

**Name:** code-reviewer
**Description:** Expert code review specialist. Use proactively when code is written or modified.
**Scope:** project
**Behavior when invoked:** Run git diff, focus on modified files, begin review immediately
**Workflow:** Check correctness, security, readability; provide feedback by priority
**Output format:** Critical / Warnings / Suggestions with specific fix examples
```
