# DoD Zero Trust Architect — Reference

Detailed pillar evaluation criteria, scoring, and maturity mapping.

---

## 1. User Pillar

**Goal:** Right access, to the right entity, for the right reason.

| Criterion | Traditional (0–3) | Target ZT (4–7) | Advanced ZT (8–10) |
|-----------|-------------------|-----------------|---------------------|
| Identity | Local accounts, shared creds | Central IdP (CAC/PIV, OIDC/SAML) | Continuous verification, risk-based |
| Authentication | Password only | MFA, strong auth | Adaptive MFA, step-up |
| Authorization | Coarse roles, implicit trust | RBAC, least privilege | Attribute-based, policy-driven |
| Session | Long-lived, no re-auth | Token expiry, refresh | Continuous validation, anomaly detection |

**Required controls:** MFA, RBAC, session limits, audit of auth events.

**NIST 800-53:** AC-2, AC-3, IA-2, IA-4, IA-5, AU-2.

---

## 2. Device Pillar

**Goal:** Reduce risk from any single device.

| Criterion | Traditional (0–3) | Target ZT (4–7) | Advanced ZT (8–10) |
|-----------|-------------------|-----------------|---------------------|
| Enrollment | Unmanaged, BYOD | MDM/EMM, compliance check | Automated posture, attestation |
| Trust | Implicit | Device compliance before access | Continuous posture, revocation |
| Workload identity | None | Service accounts | Workload identity federation |

**Required controls:** Device compliance, attestation, workload identity (K8s SA, OIDC).

**NIST 800-53:** AC-17, AC-19, CM-8, SC-28.

---

## 3. Application & Workload Pillar

**Goal:** Application-level visibility and control.

| Criterion | Traditional (0–3) | Target ZT (4–7) | Advanced ZT (8–10) |
|-----------|-------------------|-----------------|---------------------|
| Auth at app | None or basic | Auth on all endpoints | Per-resource auth, mTLS |
| Workload isolation | Shared, flat | Namespace/network policies | Micro-segmentation, service mesh |
| Supply chain | No SBOM | SBOM, provenance | Signed artifacts, policy gates |

**Required controls:** Auth on all APIs, workload identity, SBOM, image scanning.

**NIST 800-53:** AC-17, SC-7, SA-11, SA-15.

---

## 4. Data Pillar

**Goal:** Data as the new perimeter.

| Criterion | Traditional (0–3) | Target ZT (4–7) | Advanced ZT (8–10) |
|-----------|-------------------|-----------------|---------------------|
| Classification | None or manual | Labels, CUI handling | Automated classification |
| Encryption at rest | None | DB/file encryption | Per-field, key rotation |
| Encryption in transit | Optional | TLS 1.2+ everywhere | mTLS, certificate pinning |
| Access control | Coarse | Per-resource, user-scoped | DLP, attribute-based |

**Required controls:** Encryption in transit and at rest, classification, least-privilege data access.

**NIST 800-53:** SC-8, SC-13, SC-28, MP-5, MP-6.

---

## 5. Network & Environment Pillar

**Goal:** Limit lateral movement; segment by trust.

| Criterion | Traditional (0–3) | Target ZT (4–7) | Advanced ZT (8–10) |
|-----------|-------------------|-----------------|---------------------|
| Segmentation | Flat, perimeter only | Network policies, zones | Micro-segmentation, zero-trust network |
| Access | VPN, implicit trust | Explicit allow, deny-by-default | Identity-based, continuous |
| Egress | Open | Allowlist, proxy | Per-workload egress control |

**Required controls:** Network policies, deny-by-default, micro-segmentation.

**NIST 800-53:** AC-4, AC-17, SC-7.

---

## 6. Automation & Orchestration Pillar

**Goal:** Automated security responses from policy.

| Criterion | Traditional (0–3) | Target ZT (4–7) | Advanced ZT (8–10) |
|-----------|-------------------|-----------------|---------------------|
| Policy | Manual, ad hoc | Policy-as-code, GitOps | Automated enforcement, drift detection |
| Response | Manual | Automated blocking, alerts | Self-healing, auto-remediation |
| CI/CD | Manual deploy | Promotion gates, approvals | Full automation with policy gates |

**Required controls:** Policy-as-code, automated checks, promotion controls.

**NIST 800-53:** CM-3, SA-11, SI-3, SI-4.

---

## 7. Visibility & Analytics Pillar

**Goal:** Detect and react; centralized telemetry.

| Criterion | Traditional (0–3) | Target ZT (4–7) | Advanced ZT (8–10) |
|-----------|-------------------|-----------------|---------------------|
| Logging | Minimal, local | Centralized, structured | Full correlation, retention |
| Metrics | None or basic | Prometheus, health | SLOs, anomaly detection |
| Correlation | None | Request ID, trace | End-to-end trace, SIEM |
| Alerting | Manual | Automated alerts | ML-driven, automated response |

**Required controls:** Centralized logs, metrics, request correlation, audit trails.

**NIST 800-53:** AU-2, AU-3, AU-6, AU-9, SI-4.

---

## Maturity Level Determination

**Traditional:** Any pillar < 4; perimeter-based; implicit trust.

**Target ZT:** All pillars ≥ 5; explicit verification; least privilege; encryption; centralized logging.

**Advanced ZT:** All pillars ≥ 7; adaptive; automated; continuous verification; ML-driven analytics.

---

## NIST 800-53 Control Families (Quick Reference)

| Family | Focus |
|--------|-------|
| AC | Access Control |
| AU | Audit and Accountability |
| IA | Identification and Authentication |
| SC | System and Communications Protection |
| SI | System and Information Integrity |
| CM | Configuration Management |
| SA | System and Services Acquisition |
| MP | Media Protection |

---

## FedRAMP Moderate Alignment

For FedRAMP Moderate, ensure:

- All Target ZT controls met
- Encryption (SC-8, SC-28)
- Audit logging (AU-2, AU-3, AU-6)
- Access control (AC-2, AC-3, AC-17)
- Incident response (IR-4, IR-5)
- Continuous monitoring (CA-7)

---

## DoD ZT Compliance Score (Optional)

Compute as: `(Sum of pillar scores) / 70 * 100` → percentage.

- **≥ 70%:** Target ZT compliant
- **≥ 90%:** Advanced ZT compliant

Map findings to NIST 800-53 controls for ATO evidence.
