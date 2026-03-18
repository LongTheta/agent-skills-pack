# Migrate to Skills — Examples

## Example 1: Migrate Project Rules

```
Migrate all "applied intelligently" rules from .cursor/rules/ to skills format. Preserve body content exactly. Create skills in .cursor/skills/.
```

---

## Example 2: Migrate User Commands

```
Migrate my slash commands from ~/.cursor/commands/ to skills. Add disable-model-invocation: true to each. Preserve content verbatim.
```

---

## Example 3: Migrate Specific Rule

```
Migrate .cursor/rules/api-conventions.mdc to a skill. It has description but no globs. Create .cursor/skills/api-conventions/SKILL.md.
```

---

## Example 4: Full Migration

```
Find all rules and commands in this project and in my user directory. Migrate eligible ones to skills. Report what was migrated and offer to undo if needed.
```
