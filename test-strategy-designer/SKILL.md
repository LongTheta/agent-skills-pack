---
name: test-strategy-designer
risk_tier: 1
description: >-
  Designs a test strategy document for a repository: unit, integration, e2e,
  coverage targets, CI integration, and test pyramid. Use when establishing
  testing approach, defining test tiers, or documenting test requirements.
  Complements release-pipeline-designer and security skills.
---

# Test Strategy Designer

## Purpose

Produces a structured test strategy document for a repository. Defines test tiers, coverage targets, CI integration, and the test pyramid. Output is a proposal document; user applies it. Use before or alongside release-pipeline-designer for CI test steps. Tier 1: proposals only; no file writes unless explicitly requested.

## When to Use

- User wants to establish a testing approach for a repo
- User asks to define test tiers, coverage targets, or test pyramid
- User needs a test strategy document for documentation or review
- User is setting up CI and needs test step guidance

## Inputs

| Input | Description |
|-------|-------------|
| Project type | Application, library, API, CLI |
| Language/runtime | Affects tooling (pytest, Jest, Go test, etc.) |
| Existing tests | Any current test structure to align with |
| Constraints | Coverage targets, CI platform, time/resource limits |

## Outputs

- **Test strategy document** — Markdown with test tiers, pyramid, coverage, CI notes
- **Test pyramid** — Unit / integration / e2e ratio and rationale
- **Coverage targets** — Per-tier or overall
- **CI integration notes** — Where tests run, fail-fast behavior
- **Tool recommendations** — Frameworks, runners, mocking

## Steps / Behavior

1. **Gather context** — Project type, language, existing tests
2. **Define test tiers** — Unit, integration, e2e; what belongs where
3. **Set coverage targets** — Realistic per tier; call out exclusions
4. **Describe test pyramid** — Ratio and rationale
5. **CI integration** — When each tier runs; blocking vs non-blocking
6. **Tool recommendations** — pytest, Jest, Playwright, etc.
7. **Output document** — Structured Markdown for docs/ or README

## Constraints

- **Trust Boundaries:** User input untrusted; validate project type and paths. Output is proposal only; user applies. No file writes unless explicitly requested.
- **Output Validation:** Label output as "Proposal" or "Draft"; user applies manually. Mark assumptions and exclusions explicitly.
- **Limitations:** Proposes strategy only; does not write tests or CI config. Coverage targets are guidance; actual coverage depends on implementation. Does not run tests or measure coverage.
- **Safety Guardrails (Tier 1):** Proposals only; user applies. Realistic targets—avoid 100% coverage mandates; focus on high-value areas. Call out assumptions—testability of legacy code, flaky test risk.

## Examples

See [examples.md](examples.md) for example strategy documents. Use [prompt-template.md](prompt-template.md) for structured invocation.

## Validation Checklist

- [ ] All test tiers defined with clear scope
- [ ] Coverage targets are achievable
- [ ] CI integration notes align with release-pipeline-designer
- [ ] Tool recommendations match project language

## Portability Notes

Strategy structure is language-agnostic. Tool recommendations (pytest, Jest, etc.) are ecosystem-specific. Adapt for other languages and frameworks. Complements release-pipeline-designer for CI integration.
