# DORA Alignment

This document maps the Agent Skills Pack to **DORA** (DevOps Research and Assessment) principles, metrics, and framework pillars. DORA is a research program led by [Google Cloud](https://cloud.google.com/devops) that identifies practices and metrics that differentiate elite software delivery teams.

**Part of the Engineering Intelligence Framework.** DORA (delivery performance) is one dimension of the unified model. See [engineering-intelligence-framework.md](engineering-intelligence-framework.md) for the full integration with DORA AI Capabilities, DX, and HEART.

## References

- [DORA Guides](https://dora.dev/guides/) — Software delivery metrics, value stream mapping, organizational transformation
- [DORA Software Delivery Performance Metrics](https://dora.dev/guides/) — Essential measurements for continuous improvement
- [What Are DORA Principles and Why Do They Matter?](https://medium.com/@bahram.maravandi/what-are-dora-principles-and-why-do-they-matter-998bbef4a074) — Overview of DORA metrics
- [DORA Framework for Development Projects](https://www.metridev.com/en/metrics/dora-framework-for-your-development-projects/) — Five pillars and implementation

---

## The Four DORA Metrics

| Metric | Description | Skills That Support It |
|--------|-------------|------------------------|
| **Deployment Frequency** | How often you release to production | `release-pipeline-designer`, `ai-devsecops-policy-enforcement`, `zero-trust-gitops-enforcement` |
| **Lead Time for Changes** | Time from commit to production | `release-pipeline-designer`, `ai-code-review-guardrails`, `zero-trust-gitops-enforcement`, `ai-devsecops-policy-enforcement` |
| **Change Failure Rate** | % of releases that cause incidents or require fixes | `test-strategy-designer`, `ai-code-review-guardrails`, `cve-detect-and-remediate`, `ai-devsecops-policy-enforcement` |
| **Mean Time to Restore (MTTR)** | How quickly you recover from production failures | `observability-bootstrap`, `ai-devsecops-policy-enforcement` |

### Extended Metrics (Supporting)

| Metric | Description | Skills |
|--------|-------------|--------|
| **Recovery Time** | Time to full recovery beyond initial restore | `observability-bootstrap`, `repo-docs-writer` |
| **Rework Rate** | % of work that must be redone | `test-strategy-designer`, `ai-code-review-guardrails` |
| **Deployment Stability** | Consistency of successful deployments | `release-pipeline-designer`, `ai-devsecops-policy-enforcement` |

---

## The Five DORA Framework Pillars

| Pillar | Description | Skills That Support It |
|--------|-------------|------------------------|
| **Continuous Delivery** | Release software quickly, reliably, and frequently | `release-pipeline-designer`, `ai-devsecops-policy-enforcement`, `zero-trust-gitops-enforcement` |
| **Continuous Integration** | Merge code regularly; detect conflicts early | `release-pipeline-designer`, `ai-code-review-guardrails`, `test-strategy-designer` |
| **Deployment Automation** | Automate deployment to dev, test, prod | `release-pipeline-designer`, `ai-devsecops-policy-enforcement` |
| **Monitoring and Observability** | Insights into performance, health, behavior | `observability-bootstrap`, `security-evaluator` |
| **Leadership and Culture** | Collaboration, trust, continuous learning | `repo-docs-writer`, `create-rule`, `ai-agent-architecture` (team/org design) |

---

## DORA Guides Alignment

| DORA Guide | Skills That Support It |
|------------|------------------------|
| **Software delivery performance metrics** | All pipeline, test, and observability skills |
| **Value stream mapping** | `release-pipeline-designer`, `observability-bootstrap`, `test-strategy-designer` (flow visibility) |
| **How to transform your organization** | `ai-agent-architecture`, `create-rule`, `repo-docs-writer` |
| **Empowering software delivery teams** | `create-repo-foundation`, `create-rule`, `create-skill`, `release-pipeline-designer` |
| **Generative AI for software delivery** | `ai-code-review-guardrails`, `ai-devsecops-policy-enforcement`, `ai-agent-architecture` |

---

## Skill-to-DORA Mapping

### High DORA Alignment (Core Delivery)

| Skill | DORA Metrics | DORA Pillars |
|-------|--------------|--------------|
| **release-pipeline-designer** | Deployment Frequency, Lead Time | CD, CI, Deployment Automation |
| **observability-bootstrap** | MTTR | Monitoring and Observability |
| **test-strategy-designer** | Change Failure Rate | CI |
| **ai-code-review-guardrails** | Lead Time, Change Failure Rate | CI |
| **ai-devsecops-policy-enforcement** | All four | CD, CI, Deployment Automation |
| **zero-trust-gitops-enforcement** | Deployment Frequency, Lead Time | CD, Deployment Automation |

### Supporting DORA (Quality & Security)

| Skill | DORA Contribution |
|-------|--------------------|
| **cve-detect-and-remediate** | Reduces Change Failure Rate (vulnerable deps) |
| **dependency-governance** | Supply chain hygiene; supports stable deployments |
| **security-evaluator** | Assesses observability and pipeline security |
| **tool-evaluator** | Evaluates tools for DORA-friendly adoption |

### Enabling DORA (Foundation & Culture)

| Skill | DORA Contribution |
|-------|--------------------|
| **create-repo-foundation** | Establishes repo structure for CI/CD |
| **repo-docs-writer** | Runbooks, architecture docs for incident response (MTTR) |
| **ai-agent-architecture** | Team/org design; production-readiness |
| **create-rule**, **create-skill** | Codify practices; empower teams |

---

## Using This Pack for DORA Improvement

1. **Assess current state** — Use `release-pipeline-designer`, `observability-bootstrap`, `test-strategy-designer` to understand pipeline, monitoring, and test coverage.
2. **Reduce lead time** — Use `ai-code-review-guardrails`, `release-pipeline-designer`, `zero-trust-gitops-enforcement` to streamline reviews and deployments.
3. **Lower change failure rate** — Use `test-strategy-designer`, `cve-detect-and-remediate`, `ai-devsecops-policy-enforcement` for quality and security gates.
4. **Improve MTTR** — Use `observability-bootstrap` for metrics, dashboards, alerting; `repo-docs-writer` for runbooks.
5. **Increase deployment frequency** — Use `release-pipeline-designer`, `ai-devsecops-policy-enforcement` for automated, safe pipelines.

---

## Goodhart's Law: Use Metrics as Indicators, Not Targets

[Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) states: **"When a measure becomes a target, it ceases to be a good measure."** Once pressure is placed on a metric for control purposes, the statistical relationship it represents tends to break down—people optimize for the number instead of the outcome.

### DORA Metrics at Risk

| Metric | Goodhart risk |
|--------|---------------|
| **Deployment Frequency** | Trivial deployments, tiny commits, or splitting work into many small releases to hit targets |
| **Lead Time for Changes** | Shortcuts, weaker reviews, or bypassing quality gates to appear faster |
| **Change Failure Rate** | Under-reporting incidents, redefining "failure," or hiding problems |
| **MTTR** | "Resolving" by masking symptoms or restarting services instead of fixing root cause |

### Recommended Usage

- **Treat DORA metrics as indicators** — Use them to understand flow, spot bottlenecks, and guide improvement. Do not use them as performance targets or incentives.
- **Focus on outcomes** — The goal is better software delivery and reliability, not better numbers. Metrics should inform decisions, not replace judgment.
- **Avoid metric fixation** — Combine quantitative metrics with qualitative feedback. Use DORA to start conversations, not to judge teams.

### Further Reading

- [Goodhart's law (Wikipedia)](https://en.wikipedia.org/wiki/Goodhart%27s_law)
- Muller, Jerry Z. *The Tyranny of Metrics*. Princeton University Press, 2018.

---

## Triggers for DORA-Related Invocation

When users mention **DORA**, **DORA metrics**, **deployment frequency**, **lead time for changes**, **change failure rate**, **MTTR**, **DevOps Research and Assessment**, or **Accelerate metrics**, consider invoking:

- `release-pipeline-designer` — Pipeline design and CI/CD
- `observability-bootstrap` — MTTR and monitoring
- `test-strategy-designer` — Change failure rate
- `ai-code-review-guardrails` — Lead time and quality
- `ai-devsecops-policy-enforcement` — Pipeline and GitOps review

---

## Related Frameworks

| Framework | Purpose | Document |
|-----------|---------|----------|
| **DORA AI Capabilities** | Organizational readiness for AI | [engineering-intelligence-framework.md](engineering-intelligence-framework.md#2-dora-ai-capabilities-model) |
| **DX + AI Measurement** | Developer experience, bottlenecks | [engineering-intelligence-framework.md](engineering-intelligence-framework.md#3-dx--ai-measurement-developer-experience) |
| **HEART** | User and product impact | [engineering-intelligence-framework.md](engineering-intelligence-framework.md#4-heart-framework-user-and-product-impact) |
