# Engineering Intelligence Framework

A unified measurement and operating model for AI-enabled, DevSecOps-aligned engineering. This framework combines **DORA** (delivery performance), **DORA AI Capabilities** (organizational readiness), **DX** (developer experience), and **HEART** (user/product impact) into a single, auditable system.

---

## Overview

The Engineering Intelligence Framework answers: *How do we measure and improve engineering success across speed, stability, experience, product impact, and AI effectiveness?*

| Dimension | Framework | What It Measures |
|-----------|-----------|------------------|
| **Delivery Performance** | DORA | Lead time, deployment frequency, change failure rate, MTTR |
| **Organizational Readiness** | DORA AI Capabilities | AI stance, data ecosystem, version control, platforms, learning culture |
| **Developer Experience** | DX + AI Measurement | Friction, cognitive load, bottlenecks, real vs perceived AI value |
| **Product/User Impact** | HEART | Happiness, engagement, adoption, retention, task success |
| **Risk & Governance** | AI Dependency Model | Over-reliance, hidden defects, review bottlenecks, traceability |

**Core principle:** Metrics are indicators, not targets. Combine quantitative data with qualitative feedback. Avoid metric fixation; focus on outcomes.

---

## 1. DORA: Delivery Performance

### Core Metrics

| Metric | Description | Optimization Direction |
|--------|-------------|------------------------|
| **Lead Time for Changes** | Time from commit to production | Reduce; favor small batches |
| **Deployment Frequency** | How often you release | Increase; with safety |
| **Change Failure Rate** | % of releases causing incidents | Reduce; quality gates |
| **Mean Time to Recovery (MTTR)** | Time to restore from failure | Reduce; observability, runbooks |

### Extended Metrics

| Metric | Description |
|--------|-------------|
| **Recovery Time** | Time to full recovery (beyond initial restore) |
| **Rework Rate** | % of work that must be redone |
| **Deployment Stability** | Consistency of successful deployments |

### Guiding Principles

- **Small batch changes** — Smaller changes reduce blast radius and failure rate
- **Reduce failure rate** — Quality gates, tests, code review
- **Improve rollback capability** — Immutable artifacts, versioned deploys, feature flags
- **Increase deployment confidence** — Automated testing, observability, safe rollout

### Goodhart's Law

Use DORA metrics as **indicators**, not targets. See [dora-alignment.md](dora-alignment.md#goodharts-law-use-metrics-as-indicators-not-targets).

---

## 2. DORA AI Capabilities Model

Seven foundational capabilities that amplify AI success ([DORA AI Capabilities Report](https://dora.dev/guides/)):

| Capability | Description | This Pack Supports |
|------------|-------------|-------------------|
| **Clear AI usage stance** | Communicated expectations; approved vs shadow AI | `ai-security-enforcement`, `ai-code-review-guardrails`, rules |
| **Healthy internal data ecosystem** | Quality, accessibility, governance of data | `dependency-governance`, `ai-devsecops-policy-enforcement` |
| **AI-accessible internal data** | Context, docs, APIs available to AI tools | `repo-docs-writer`, `create-rule`, `create-skill` |
| **Strong version control and rollback** | Git practices, rollback readiness | `release-pipeline-designer`, `zero-trust-gitops-enforcement` |
| **User-centered development** | Focus on user outcomes, not just output | HEART integration; `repo-docs-writer` |
| **High-quality internal platforms** | Platforms that enable teams | `release-pipeline-designer`, `observability-bootstrap`, `tool-evaluator` |
| **Continuous learning and feedback** | Feedback loops, retrospectives | Rules, `create-rule`, `create-skill` |

### Documentation and Rules Must

- Define AI usage expectations clearly
- Prevent shadow AI usage (unapproved tools)
- Ensure safe experimentation (sandbox, review)
- Connect AI tools to internal context (docs, rules, skills)
- Support versioning and rollback for AI-generated code

---

## 3. DX + AI Measurement: Developer Experience

### What to Measure

| Dimension | Description |
|-----------|-------------|
| **Developer friction** | Pain points in build, deploy, review, tooling |
| **Cognitive load** | Mental effort to understand and change systems |
| **Code review bottlenecks** | Time in review, review queue depth |
| **Real vs perceived AI usage** | Actual productivity gains vs assumed |
| **Time savings vs outcomes** | Did AI save time? Did it improve quality? |

### Guiding Principles

- **Metrics alone are insufficient** — Combine with qualitative feedback (surveys, retrospectives)
- **Qualitative feedback from engineers** — Regular pulse checks, DX surveys
- **Identify AI-introduced bottlenecks** — Especially code review (more code, same reviewers)
- **Distinguish AI activity from productivity** — More output ≠ better outcomes

### Skills That Support DX

- `ai-code-review-guardrails` — Reduces review friction, defines expectations
- `release-pipeline-designer` — Reduces deployment friction
- `observability-bootstrap` — Visibility into bottlenecks
- `create-rule`, `create-skill` — Codify practices; reduce cognitive load

---

## 4. HEART Framework: User and Product Impact

Extend beyond DevOps to product success. HEART dimensions:

| Dimension | Description | Engineering Connection |
|-----------|-------------|------------------------|
| **Happiness** | Developer + user satisfaction | DX surveys; NPS; sentiment |
| **Engagement** | Usage of tools and systems | Adoption of platforms, AI tools |
| **Adoption** | AI + platform adoption | % using approved AI; platform usage |
| **Retention** | Continued usage over time | Churn of tools, platforms |
| **Task Success** | Completion, quality, correctness | Deployment success; defect escape |

### Guiding Principles

- **Connect engineering output to user outcomes** — Features shipped → user value
- **Measure real value, not output volume** — Story points ≠ value; deployments ≠ impact
- **Align engineering work with product success** — Roadmap alignment; outcome-based goals

---

## 5. AI Dependency and Risk Management

### Risks Introduced by AI

| Risk | Mitigation |
|------|------------|
| **Over-reliance on AI-generated code** | Human validation; code review; test coverage |
| **Hidden defects in generated code** | Strong test strategy; security scanning |
| **Increased code volume without quality controls** | Review guardrails; maintainability standards |
| **Review bottlenecks** | AI-assisted review; parallel review; smaller batches |
| **Security and compliance risks** | Trust boundaries; output validation; audit trail |

### Guidance

- **Enforce human validation** — No auto-apply of AI outputs for high-risk changes
- **Strengthen code review** — `ai-code-review-guardrails`; severity levels; boundaries
- **Detect and manage AI-generated code** — Traceability; attribution; review focus
- **Prevent unsafe AI usage** | Approved tools; data boundaries; no shadow AI
- **Ensure traceability** | Commit messages; PR descriptions; audit logs

### Skills That Support AI Risk Management

- `ai-security-enforcement` — Trust boundaries, output validation
- `ai-code-review-guardrails` — Review standards for AI-assisted code
- `ai-devsecops-policy-enforcement` — Pipeline and config review
- `security-evaluator` — Security assessment of AI integrations

---

## 6. Metrics That Matter vs Vanity Metrics

| Metrics That Matter | Vanity Metrics |
|---------------------|----------------|
| Lead time (commit → prod) | Lines of code |
| Change failure rate | Deployment count (without quality) |
| MTTR | Story points completed |
| Developer satisfaction (DX) | PR count |
| User task success | Feature count |
| AI effectiveness (outcomes) | AI usage hours |

**Rule:** Prefer metrics that reflect outcomes and quality over volume and activity.

---

## 7. How to Measure Success

| Dimension | What to Measure |
|-----------|-----------------|
| **Speed** | Lead time, deployment frequency (with stability) |
| **Stability** | Change failure rate, MTTR, rollback success |
| **Experience** | DX surveys, friction points, cognitive load |
| **Product Impact** | HEART dimensions; user outcomes |
| **AI Effectiveness** | Time to value; quality of AI-assisted output; reduction in rework |

### Balanced Scorecard

Do not rely only on metrics dashboards. Include:

- **Human feedback loops** — Retrospectives, pulse surveys, 1:1s
- **Hidden bottleneck identification** — Value stream mapping; flow analysis
- **Balance speed with quality and experience** — No trade-off at the expense of sustainability

---

## 8. Integration with This Pack

| Component | Role |
|-----------|------|
| **Skills** | Support measurement, evaluation, bottleneck detection, AI risk mitigation |
| **Rules** | Enforce small batches, safe deployments, rollback readiness, secure AI usage |
| **Documentation** | Engineering Measurement Model; AI strategy; governance |
| **Workflows** | CI/CD gates; validation; certification score |

See [dora-alignment.md](dora-alignment.md) for skill-to-metric mapping.

---

## References

- [DORA Guides](https://dora.dev/guides/)
- [DORA AI Capabilities Model](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)
- [Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law)
- Muller, Jerry Z. *The Tyranny of Metrics*. Princeton University Press, 2018.
