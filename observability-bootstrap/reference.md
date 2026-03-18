# Observability Bootstrap — Reference

## RED Metrics (Services)

- **Rate** — Requests per second
- **Errors** — Error rate
- **Duration** — Latency (p50, p95, p99)

## USE Metrics (Resources)

- **Utilization** — % used
- **Saturation** — Queue depth, wait time
- **Errors** — Error count

## Log Best Practices

- Structured (JSON)
- Correlation ID / trace ID in each log
- No PII in logs
- Levels: DEBUG, INFO, WARN, ERROR

## Relation to security-evaluator

security-evaluator assesses observability setup for: log retention, audit trails, access control, PII exposure. Use observability-bootstrap for setup; security-evaluator for security review.
