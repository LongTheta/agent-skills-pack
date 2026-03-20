# AI DevSecOps Policy Enforcement Agent – Reference

## End-to-End Workflow

1. **Run review** – `review` (local) or `review-all` (with remote fetch)
2. **Inspect findings** – Verdict, risk score in `review-result.json`, `policy-summary.json`
3. **Run auto-fix suggest** – See proposed changes without modifying files
4. **Inspect diff** – Review generated patch output
5. **Patch or apply** – Write fixes to output dir or apply safe fixes with backups
6. **Re-run review** – Validate improvement

## Artifact Structure

### review-result.json

```json
{
  "verdict": "pass" | "pass_with_warnings" | "fail",
  "summary": "Human-readable summary",
  "findings": [
    {
      "id": "finding-id",
      "title": "...",
      "severity": "critical" | "high" | "medium" | "low",
      "category": "secrets" | "supply_chain" | "governance" | "...",
      "description": "...",
      "impacted_files": ["path/to/file"],
      "remediation_summary": "..."
    }
  ],
  "policy_results": [...],
  "compliance_considerations": [...],
  "recommended_remediations": [...],
  "context": {...},
  "metadata": {...}
}
```

### workflow-status.json

Used for CI integration: verdict, artifact paths, event context.

## CLI Commands Summary

| Command | Purpose |
|---------|---------|
| `review` | Full policy review; Markdown, JSON, SARIF, artifacts |
| `review-all` | Review with optional remote fetch from PR/MR |
| `comments` | Generate PR/MR comments; optional `--post` |
| `remediate` | Remediation suggestions with patches |
| `auto-fix` | Generate or apply config patches (suggest \| patch \| apply) |

## Fix Types and Safety

| Fix Type | Finding IDs | Can Auto-Apply |
|----------|-------------|----------------|
| `add_resource_limits` | gitops-003 | Yes |
| `disable_risky_argo_autosync` | gitops-001, argo-001 | Yes |
| `add_sbom_step` | pipeline-003, sbom-001, policy-require_sbom | Yes |
| `pin_container_image` | pipeline-002, github-005, gitops-005 | No (needs digest) |
| `pin_github_action` | github-001, pipeline-002 | No (needs SHA) |

## GitHub Actions Integration

Example workflow step:

```yaml
- name: Policy Review
  run: |
    pip install -e .
    python -m ai_devsecops_agent.cli review \
      --platform github \
      --pipeline .github/workflows/ci.yml \
      --gitops k8s/argo-app.yaml \
      --policy policies/default.yaml \
      --artifact-dir artifacts
```

## GitLab CI Integration

Use `--platform gitlab` and `.gitlab-ci.yml` path. Set `GITLAB_TOKEN` for remote fetch.

## Extending Policies

Add rules to policy YAML:

```yaml
rules:
  - id: rule_id
    name: Rule name
    description: Rule description
    severity: critical | high | medium | low
    category: secrets | supply_chain | governance
    enabled: true
```

## MITRE ATLAS Alignment

Supply chain and model artifact review aligns with MITRE ATLAS tactics:

- **Initial Access** — AI Supply Chain Compromise (model artifacts, datasets in pipelines)
- **Resource Development** — Poisoned datasets, malicious packages in dependencies
- **Defense Evasion** — Corrupt AI Model (AML.T0076): model scanners should handle models that cannot be fully deserialized

When reviewing pipelines that pull or scan AI models, ensure scanning does not assume successful deserialization. See [docs/mitre-atlas-reference.md](../docs/mitre-atlas-reference.md).

## Project Location

Default path: `C:\Users\Cathy\OneDrive\Documents\Coding Exercises\Learning_Path\New_Development\ai-devsecops-policy-enforcement-agent`
