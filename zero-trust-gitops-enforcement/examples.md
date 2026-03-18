# Zero Trust GitOps Enforcement — Examples

## Example 1: Pipeline Review

Review a pipeline for Zero Trust compliance.

```
Use the zero-trust-gitops-enforcement skill to review our GitHub Actions workflow at .github/workflows/deploy.yml. Check for identity, supply chain, deployment integrity, promotion controls, secrets, and observability. Give a Pass/Fail verdict.
```

---

## Example 2: Argo CD Application

Assess an Argo CD application manifest.

```
Use the zero-trust-gitops-enforcement skill to evaluate our Argo CD Application at argocd/apps/production.yaml. Check for risky autosync, image pinning, and promotion controls.
```

---

## Example 3: Full Repo Assessment

Review an entire repository for Zero Trust GitOps.

```
Use the zero-trust-gitops-enforcement skill to review this repository. Analyze all CI/CD configs, Argo CD manifests, and Kubernetes deployments. Produce a blocking assessment before we deploy to production.
```

---

## Example 4: Dockerfile Review

Check a Dockerfile for supply chain controls.

```
Use the zero-trust-gitops-enforcement skill to review our Dockerfile. Verify base image pinning, no latest tags, and build provenance.
```
