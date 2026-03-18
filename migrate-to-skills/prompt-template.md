# Migrate to Skills — Invocation Template

Copy and fill in the placeholders.

```
Migrate rules/commands to skills:

**Scope:** [project | user | both]
**Source patterns:**
- Rules: [e.g., **/.cursor/rules/*.mdc]
- Commands: [e.g., .cursor/commands/*.md, ~/.cursor/commands/*.md]

**Destination:** [.cursor/skills/ | ~/.cursor/skills/]

**Rules to migrate:** Applied intelligently only (has description, no globs, no alwaysApply: true)
**Commands to migrate:** All

**Preserve:** Body content exactly; no reformatting

**Optional:**
- Delete originals after migration: [yes | no]
- Undo available: [yes]
```
