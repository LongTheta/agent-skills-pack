# Create Rule — Reference

## Rule File Format

- **Location:** `.cursor/rules/`
- **Extension:** `.mdc`
- **Frontmatter:** YAML between `---` delimiters

## Frontmatter Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Shown in rule picker; be specific |
| `globs` | string | File pattern; rule applies when matching files are open |
| `alwaysApply` | boolean | If true, applies to every conversation |

## Glob Examples

| Pattern | Applies To |
|---------|------------|
| `**/*.ts` | All TypeScript files |
| `**/*.tsx` | All TSX files |
| `backend/**/*.py` | Python files in backend |
| `**/api/**/*.ts` | API-related TypeScript |
| `*.md` | Markdown files in root |

## Best Practices

- Keep rules under 50 lines when possible
- One concern per rule
- Include concrete examples
- Use actionable language
