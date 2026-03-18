# DoD Zero Trust Architect — Example Assessment

Example output for **taskforge-backend** (FastAPI task/notes API with JWT auth, PostgreSQL, GitHub Actions CI, Kustomize, ArgoCD, Prometheus).

---

# Zero Trust Assessment

**System:** taskforge-backend  
**Scope:** Backend API, CI/CD, GitOps, observability  
**Assumptions:** Development/production deployment; CUI not explicitly handled; PostgreSQL; Kubernetes target.

---

## Overall Score

**5.1 / 10** — Approaching Target ZT in User, Application, and Visibility; significant gaps in Device, Data, Network, and Automation.

---

## Maturity Level

| Level | Status |
|-------|--------|
| Traditional | Partial — perimeter assumptions, no device trust |
| Target ZT | In progress — User, App, Visibility partially met |
| Advanced ZT | Not started |

---

## Pillar Breakdown

### 1. User

- **Score:** 6/10
- **Current State:** JWT auth with bcrypt passwords; RBAC via `require_role`; user-scoped data; token expiry (30 min). No MFA, no CAC/PIV, no continuous re-auth.
- **Gaps:**
  - No MFA
  - No central IdP (CAC/PIV, OIDC/SAML)
  - No adaptive or step-up auth
  - Session validation is token-based only; no anomaly detection
- **Required Controls:** MFA, central IdP integration, session limits, auth audit logging
- **Recommended Fixes:**
  1. Integrate OIDC/SAML IdP (e.g., Keycloak, Okta) with MFA
  2. Add auth event logging (login, logout, failures) to centralized logs
  3. Implement refresh token rotation and shorter access token lifetime for sensitive ops

---

### 2. Device

- **Score:** 2/10
- **Current State:** No device posture or attestation. API accepts requests from any client. No workload identity federation.
- **Gaps:**
  - No device compliance check
  - No MDM/EMM integration
  - No workload identity (K8s ServiceAccount, OIDC) for CI or runtime
- **Required Controls:** Device compliance before access; workload identity for runners and pods
- **Recommended Fixes:**
  1. Use OIDC for GitHub Actions (no long-lived secrets)
  2. Configure workload identity for Kubernetes (IRSA, Workload Identity)
  3. For user-facing: require device attestation via IdP or ZTNA

---

### 3. Application & Workload

- **Score:** 6/10
- **Current State:** Auth on all protected endpoints; user-scoped access; SBOM (CycloneDX); provenance attestation; Bandit, pip-audit in CI.
- **Gaps:**
  - No mTLS between services
  - No service mesh or micro-segmentation
  - No container image scanning (Trivy) in CI
  - No image signing (cosign)
- **Required Controls:** Auth on all APIs (met); SBOM (met); add image scanning, signing
- **Recommended Fixes:**
  1. Add Trivy (or similar) container scan in CI; fail on high/critical
  2. Add cosign signing for prod images
  3. Plan mTLS or service mesh for multi-service deployments

---

### 4. Data

- **Score:** 4/10
- **Current State:** User-scoped data; TLS in transit (assumed for prod); no explicit encryption-at-rest for DB; secrets via env (no vault).
- **Gaps:**
  - No data classification or CUI handling
  - DB encryption at rest not documented
  - Secrets in env vars; no Vault or rotation
- **Required Controls:** Encryption in transit and at rest; classification; secrets management
- **Recommended Fixes:**
  1. Enable PostgreSQL encryption at rest (e.g., cloud-managed or LUKS)
  2. Integrate Vault (or equivalent) for SECRET_KEY, DATABASE_URL
  3. Document data classification and CUI handling if applicable

---

### 5. Network & Environment

- **Score:** 3/10
- **Current State:** Kustomize overlays (dev/prod); no NetworkPolicy in base; ArgoCD for GitOps.
- **Gaps:**
  - No NetworkPolicy for workload isolation
  - No explicit deny-by-default micro-segmentation
  - No egress allowlisting
- **Required Controls:** Network policies, deny-by-default, micro-segmentation
- **Recommended Fixes:**
  1. Add NetworkPolicy to base: deny all ingress except from ingress controller; restrict egress
  2. Segment by namespace (dev vs prod)
  3. Use a policy engine (e.g., OPA, Kyverno) for admission control

---

### 6. Automation & Orchestration

- **Score:** 5/10
- **Current State:** GitHub Actions CI; manual promotion gate (`production` environment); GitOps with ArgoCD; Kustomize; immutable image tags.
- **Gaps:**
  - No policy-as-code for K8s (OPA/Kyverno)
  - No automated drift detection
  - Promote job is placeholder; no registry push or overlay update
- **Required Controls:** Policy-as-code, promotion controls, automated checks
- **Recommended Fixes:**
  1. Add Kyverno or OPA policies for K8s (resource limits, no latest tag)
  2. Implement full promote flow: push image, update overlay, ArgoCD sync
  3. Add drift detection (e.g., Argo CD diff, config audit)

---

### 7. Visibility & Analytics

- **Score:** 7/10
- **Current State:** Structured JSON logging; request IDs; Prometheus metrics; health/ready/info; Grafana dashboard; Loki-ready logs.
- **Gaps:**
  - No distributed tracing (OpenTelemetry)
  - No SIEM integration
  - No auth event correlation in logs
- **Required Controls:** Centralized logs (met), metrics (met), correlation
- **Recommended Fixes:**
  1. Add OpenTelemetry tracing; propagate trace IDs
  2. Ensure auth events (login, logout, failures) are logged with request ID
  3. Define log retention and SIEM export for audit

---

## Cross-Pillar Risks

1. **Secrets in env** — Affects User (credential exposure), Data (key management), Application (supply chain). Mitigation: Vault integration.
2. **No device/workload identity** — Affects User, Device, Application. Mitigation: OIDC for CI; workload identity for K8s.
3. **No NetworkPolicy** — Affects Network, Application (lateral movement). Mitigation: Add NetworkPolicy base.

---

## Priority Fixes (Top 5)

1. **Integrate secrets management (Vault)** — Effort: Medium — Impact: High (Data, User, Application)
2. **Add NetworkPolicy to K8s base** — Effort: Low — Impact: High (Network, Application)
3. **Add OIDC for GitHub Actions** — Effort: Low — Impact: Medium (Device, Automation)
4. **Add MFA and IdP integration** — Effort: High — Impact: High (User)
5. **Add Trivy container scan in CI** — Effort: Low — Impact: Medium (Application, supply chain)

---

## Roadmap to Target ZT

**Phase 1 (0–3 months)**  
- Vault for secrets; NetworkPolicy base; OIDC for CI; Trivy in CI.

**Phase 2 (3–6 months)**  
- IdP + MFA; DB encryption at rest; auth event logging.

**Phase 3 (6–12 months)**  
- Workload identity for K8s; Kyverno/OPA policies; full promote flow.

---

## Roadmap to Advanced ZT

**Phase 1 (12–18 months)**  
- mTLS or service mesh; OpenTelemetry; SIEM integration; image signing.

**Phase 2 (18–24 months)**  
- Adaptive MFA; automated drift detection; ML-driven anomaly detection.

---

## DoD ZT Compliance Score

**36%** (5.1 × 7 / 10 ≈ 36% of 70% Target ZT threshold)

**NIST 800-53 gaps:** AC-17 (remote access), IA-2 (MFA), SC-28 (encryption at rest), SC-7 (boundary protection).  
**FedRAMP Moderate:** Not yet; complete Target ZT roadmap first.
