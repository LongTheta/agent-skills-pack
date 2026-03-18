# Golden Test Cases — security-evaluator

Representative prompts for validating security-evaluator skill behavior.

## Case 1: Tool Evaluation

```
Perform a security evaluation of Argo CD for use in our Kubernetes deployment pipeline. We're targeting FedRAMP Moderate. Include RBAC, audit logging, and secrets handling.
```

**Expected**: Structured output with Security Summary, Scorecard, Risks, Mitigations, Final Recommendation.

## Case 2: Architecture Review

```
Use the security-evaluator skill to review our proposed microservices architecture. We have 5 services, OIDC for auth, Vault for secrets. Data includes PII.
```

**Expected**: Security scorecard; compliance considerations; PII handling called out.

## Case 3: Compliance Gaps

```
Evaluate our CI/CD workflow for security and compliance. We need audit evidence for SOC 2.
```

**Expected**: Audit logging, retention, export assessed; SOC 2 relevant controls.
