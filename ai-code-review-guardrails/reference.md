# AI Code Review Guardrails — Reference

## Severity Levels

| Level | Action |
|-------|--------|
| Critical | Block merge; must fix |
| High | Strongly recommend fix |
| Medium | Suggest improvement |
| Low | Optional; nice to have |

## Boundary Rules

- AI proposes feedback; never approves or merges
- Human must review and decide
- Security findings: escalate to security-evaluator or manual review

## Relation to security-evaluator

security-evaluator: Security and compliance assessment of tools, architectures, workflows.
ai-code-review-guardrails: Process and rules for AI-assisted PR/code review. Use both: guardrails define process; security-evaluator for deep security assessment.
