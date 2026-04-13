# Migrate to Skills — Examples

## Example 1: Migrate applied-intelligently rules

```
Migrate all "applied intelligently" rules from .agent/rules/ to skills format. Preserve body content exactly. Create skills in .agent/skills/.
```

---

## Example 2: Migrate user slash commands

```
Migrate my slash commands from ~/.agent/commands/ to skills. Add disable-model-invocation: true to each. Preserve content verbatim.
```

---

## Example 3: Single rule file

```
Migrate .agent/rules/api-conventions.mdc to a skill. It has description but no globs. Create .agent/skills/api-conventions/SKILL.md.
```
