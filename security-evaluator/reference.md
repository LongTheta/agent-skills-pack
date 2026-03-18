# Security Evaluator — Reference

## Security Domains Quick Reference

| Domain | Key Questions |
|--------|---------------|
| **Identity and access** | IdP integration, MFA, session management, RBAC |
| **Secrets handling** | Storage, rotation, exposure risk, vault integration |
| **Audit logging** | Log coverage, retention, tamper resistance, export |
| **Encryption** | TLS, key management, data-at-rest |
| **API / network** | Surface area, auth on endpoints, rate limiting |
| **Supply chain** | SBOM, provenance, signed artifacts |
| **Configuration** | IaC, drift detection, config validation |
| **Policy enforcement** | Policy-as-code, guardrails, automated checks |

## Regulated Environment Additions

| Framework | Focus Areas |
|-----------|-------------|
| **FedRAMP** | ATO readiness, control mapping, continuous monitoring |
| **NIST 800-53** | AC, AU, IA, SC, SI families |
| **FISMA** | Continuous monitoring, audit trails |
| **SOC 2** | Trust criteria, evidence, access controls |

## Recommendation Mapping

| Recommendation | Implication |
|----------------|-------------|
| Low risk | Proceed with standard due diligence |
| Moderate risk with controls | Document and implement mitigations |
| High risk | Substantial mitigations before use |
| Pilot only | Validate in isolated environment first |
| Not recommended | Unacceptable risk or better alternatives |
| Need more information | Gather listed items before deciding |
