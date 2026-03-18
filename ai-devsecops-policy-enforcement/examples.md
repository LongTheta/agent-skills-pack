# AI DevSecOps Policy Enforcement — Examples

## Example 1: Local Pipeline Review

Review the CI/CD pipeline and GitOps manifests in this repo for policy compliance.

```
Use the ai-devsecops-policy-enforcement skill to review:
- .github/workflows/ci.yml
- k8s/argo-application.yaml

Generate a policy report and list any critical or high findings.
```

---

## Example 2: Auto-Fix Suggest

After a review, get suggested patches without modifying files.

```
Use the ai-devsecops-policy-enforcement skill. I ran a review and have artifacts/review-result.json. Run auto-fix in suggest mode and show me the proposed changes.
```

---

## Example 3: GitHub PR Review

Review a pull request for policy violations.

```
Use the ai-devsecops-policy-enforcement skill to review PR #42 in org/repo. Fetch the pipeline and GitOps configs from the PR branch and generate policy findings. Output comments.json for PR integration.
```

---

## Example 4: FedRAMP Policy

Run a review with FedRAMP Moderate policy.

```
Use the ai-devsecops-policy-enforcement skill to review our pipeline with policies/fedramp-moderate.yaml. Focus on supply chain and secrets controls.
```
