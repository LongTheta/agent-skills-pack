# Shell — Reference

## Behavior

1. User invokes `/shell` with optional command text
2. All text after `/shell` is treated as literal shell command
3. Execute immediately; do not rewrite or "improve"
4. Report exit status and important stdout/stderr

## When Not to Use

- Do not use for general terminal tasks—only when user explicitly invokes `/shell`
- Do not inspect repo first unless the command requires it
