---
name: ai-code-review-guardrails
risk_tier: 1
description: >-
  Defines guardrails and rules for AI-assisted code review: what to check,
  severity levels, feedback format, and boundaries. Use when establishing code
  review standards, configuring review automation, or defining what AI reviewers
  should and should not do. Complements security-evaluator for security-focused
  review.
---

# AI Code Review Guardrails

## Purpose

Defines guardrails and rules for AI-assisted code review. Produces a structured document specifying what to check, severity levels, feedback format, and boundaries. Supports DORA metrics: lead time for changes, change failure rate. Addresses AI risk: review bottlenecks from AI-generated code, human validation requirements, traceability. Use to establish consistent review standards; security-evaluator handles security-specific assessments. Tier 1: proposals only; human must approve merge.

## When to Use

- User wants to define code review standards for AI-assisted review
- User asks what an AI reviewer should check or avoid
- User needs severity levels, feedback format, or review boundaries
- User is configuring a code review bot or PR automation
- User wants to address AI-generated code review bottlenecks or AI risk in review

## Inputs

| Input | Description |
|-------|-------------|
| Project context | Language, framework, conventions |
| Review scope | Security, quality, style, performance |
| Severity model | Critical / High / Medium / Low (or custom) |
| Feedback format | Inline comments, summary, checklist |
| Boundaries | What AI should not do (e.g., approve merge, bypass human) |

## Outputs

- **Guardrails document** — What to check, severity, format
- **Severity definitions** — Per-category (security, quality, style)
- **Feedback format** — Structure for comments and summary
- **Boundaries** — No auto-approve, no merge; human must decide
- **Example rules** — Concrete check examples

## Steps / Behavior

1. **Gather context** — Language, framework, existing conventions
2. **Define categories** — Security, correctness, style, performance, maintainability
3. **Set severity levels** — Per category; when to block vs suggest
4. **Define feedback format** — Inline vs summary; emoji or labels
5. **Set boundaries** — AI proposes; human approves. No auto-merge.
6. **Output document** — For .agent/rules, CONTRIBUTING, or review config

## Constraints

- **Trust Boundaries:** User input untrusted; validate project context. Output is proposal only; user applies. No auto-approve or merge.
- **Output Validation:** Label as proposal; user applies. Boundaries must state: human approves; no auto-merge.
- **Limitations:** Proposes guardrails only; does not implement review automation. Does not run or execute reviews. Security findings should align with security-evaluator; this skill defines process.
- **Safety Guardrails (Tier 1):** Proposals only; user applies. Human in the loop—guardrails must state: AI proposes; human approves merge. No auto-approve—explicit boundary: AI never approves or merges. Security handoff—for security findings, recommend security-evaluator or manual review.

## Examples

See [examples.md](examples.md) for example guardrails. Use [prompt-template.md](prompt-template.md) for structured invocation.

## Validation Checklist

- [ ] Severity levels defined for each category
- [ ] Feedback format is clear and actionable
- [ ] Boundaries explicitly state no auto-approve/merge
- [ ] Complements (does not duplicate) security-evaluator

## Portability Notes

Guardrails structure is platform-agnostic. Feedback format may need adaptation for GitHub PR comments, GitLab MR, or other review UIs. Severity mapping to blocking vs non-blocking is platform-specific. Complements security-evaluator for security-focused review.
