# Observability Bootstrap — Examples

## Example 1: Node.js API

**Input:** "Bootstrap observability for a Node.js Express API"

**Output:** OpenTelemetry SDK config, Prometheus metrics endpoint, structured logging (pino), basic Grafana dashboard (latency, errors, throughput).

## Example 2: Python Worker

**Input:** "Observability for a Python Celery worker"

**Output:** Prometheus metrics (task count, duration), structured logs (JSON), optional tracing. Alert: task failure rate > 5%.

## Example 3: Kubernetes

**Input:** "Observability for a Kubernetes deployment"

**Output:** ServiceMonitor for Prometheus, OpenTelemetry sidecar or instrumentation, Grafana dashboard for pod metrics, alert on restarts.
