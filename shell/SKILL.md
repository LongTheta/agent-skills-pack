---
name: shell
risk_tier: 3
description: >-
  Runs the rest of a /shell request as a literal shell command. Use only when
  the user explicitly invokes /shell and wants the following text executed
  directly in the terminal.
disable-model-invocation: true
---
# Run Shell Commands

Use this skill only when the user explicitly invokes `/shell`.

## When to Use

- User explicitly invokes `/shell` and provides the command to run
- User wants to execute a literal shell command in the terminal
- Do **not** use for general terminal assistance—only when `/shell` is explicitly invoked

## Behavior

1. Treat all user text after the `/shell` invocation as the literal shell command to run.
2. Execute that command immediately with the terminal tool.
3. Do not rewrite, explain, or "improve" the command before running it.
4. Do not inspect the repository first unless the command itself requires repository context.
5. If the user invokes `/shell` without any following text, ask them which command to run.

## Inputs

- Literal shell command provided by user after `/shell` invocation
- No other inputs; user must supply the exact command text

## Outputs

- Command execution result (exit code, stdout, stderr)
- Brief report of outcome

## Limitations

- Executes only what the user types; no interpretation or improvement
- User is responsible for command correctness and safety
- No built-in sandboxing; environment-dependent

## Response

- Run the command first.
- Then briefly report the exit status and any important stdout or stderr.

## Validation Checklist

- [ ] User explicitly invoked `/shell`
- [ ] Command was provided by user (not inferred or suggested)
- [ ] Do not execute commands that were not explicitly provided

## Portability Notes

Shell execution is environment-specific. Paths, commands, and behavior depend on OS and shell (bash, zsh, PowerShell, etc.).

## Enforcement (Tier 3)

**Human review required.** The user explicitly invokes `/shell` and provides the command—this constitutes approval. Do not execute commands that were not explicitly provided by the user after `/shell`.
