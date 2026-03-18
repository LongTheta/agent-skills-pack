---
name: observability-bootstrap
risk_tier: 2
description: >-
  Bootstraps observability for a repository: logging, metrics, tracing config,
  dashboards, and alerting. Produces config proposals for Prometheus, Grafana,
  OpenTelemetry, or similar. Use when adding observability to a new or existing
  repo. Complements security-evaluator for security assessment of observability
  setup.
---

# Observability Bootstrap

Bootstraps observability for a repository. Produces config proposals for logging, metrics, tracing, dashboards, and alerting. Output is config for user to review and apply. Use for new or existing repos; security-evaluator can assess the observability setup for security and compliance.

## When to Use

- User wants to add observability to a repository
- User asks for logging, metrics, or tracing setup
- User needs Prometheus, Grafana, OpenTelemetry, or similar config
- User wants dashboards or alerting bootstrap

## Inputs

- **Stack:** Prometheus, Grafana, Loki, OpenTelemetry, Datadog, etc.
- **Project type:** Application, API, worker, batch
- **Existing observability:** Any current setup to extend
- **Environment:** Local, Kubernetes, cloud (affects config)
- **Key metrics:** What to measure (latency, errors, throughput)

## Outputs

- **Metrics config** — Prometheus scrape, OpenTelemetry exporter
- **Logging config** — Structured log format, levels, aggregation
- **Tracing config** — Trace sampling, propagation (if applicable)
- **Dashboard proposals** — Grafana JSON or panel definitions
- **Alert rules** — Thresholds for critical metrics
- **Documentation** — How to run, interpret, extend

## Workflow

1. **Gather context** — Stack, project type, environment
2. **Define metrics** — RED (rate, errors, duration) or USE; custom
3. **Create metrics config** — Scrape targets, exporters
4. **Create logging config** — Format, levels, correlation IDs
5. **Create tracing config** — If applicable; sampling
6. **Propose dashboards** — Key panels; JSON or description
7. **Define alerts** — Critical thresholds; avoid alert fatigue
8. **Output** — Config files; user applies

## Limitations

- Proposes config only; does not deploy or run
- Dashboard JSON may need adjustment for specific data
- Alert thresholds are starting points; tune for environment
- Does not assess security of observability; use security-evaluator

## Safety Guardrails

- **Tier 2:** Proposes config; user reviews before applying. Validation Checklist required.
- **No secrets in config** — Use env vars or secrets manager for credentials
- **PII in logs** — Warn against logging PII; recommend redaction
- **Sampling** — For tracing, recommend sampling to avoid volume/cost issues

## Validation Checklist

- [ ] Metrics config is valid for chosen stack
- [ ] No credentials or secrets in config
- [ ] Log format supports correlation (trace ID, request ID)
- [ ] Alert thresholds are documented as starting points
- [ ] Compatible with security-evaluator review

## Portability Notes

Config format varies by stack (Prometheus, OpenTelemetry, Datadog). Structure (metrics, logs, traces) is universal. Adapt for cloud-native (GCP, AWS, Azure) managed services.
