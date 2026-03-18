---
name: dependency-governance
risk_tier: 1
description: >-
  Defines dependency governance policies: allowed/blocked packages, version
  pinning, license requirements, and update cadence. Produces policy documents
  and config proposals. Use when establishing dependency rules, license
  compliance, or supply chain policy. Complements cve-detect-and-remediate which
  executes remediation.
---

# Dependency Governance

Defines dependency governance policies for a repository. Produces policy documents covering allowed/blocked packages, version pinning, license requirements, and update cadence. Output is policy for user to apply. cve-detect-and-remediate handles detection and remediation; this skill defines the rules.

## When to Use

- User wants to establish dependency governance for a repo
- User asks about allowed/blocked packages, license policy, or pinning
- User needs a dependency policy document or config
- User is defining supply chain or license compliance rules

## Inputs

- **Ecosystem:** npm, pip, Go modules, etc.
- **License requirements:** Allowed licenses (MIT, Apache-2.0); blocked (GPL, AGPL)
- **Pinning policy:** Exact versions, ranges, or lockfile-only
- **Update cadence:** How often to review and update
- **Blocklist:** Known vulnerable or unwanted packages

## Outputs

- **Policy document** — Allowed licenses, pinning, update cadence
- **Blocklist** — Packages to avoid (with rationale)
- **Config proposals** — .npmrc, pip config, dependabot.yml, renovate.json
- **Review process** — Who approves dependency changes; when to run cve-detect

## Workflow

1. **Gather requirements** — Ecosystem, license constraints, compliance needs
2. **Define license policy** — Allowed list; blocked list
3. **Define pinning** — Lockfile required; exact vs range
4. **Define blocklist** — Known bad packages; alternatives
5. **Update cadence** — Weekly, monthly; automated PRs
6. **Config proposals** — dependabot, renovate, or manual process
7. **Output** — Policy doc; config snippets for user to apply

## Limitations

- Proposes policy only; does not scan or remediate. Use cve-detect-and-remediate for that.
- License detection accuracy depends on package metadata
- Blocklist maintenance is ongoing; user must update

## Safety Guardrails

- **Tier 1:** Proposals only; user applies.
- **No fabricated data** — Do not invent CVE IDs or package issues
- **Cite sources** — For blocklist entries; link to advisory or policy
- **License clarity** — Distinguish copyleft vs permissive; user decides

## Validation Checklist

- [ ] License policy is clear (allowed/blocked)
- [ ] Pinning policy matches ecosystem (lockfile, etc.)
- [ ] Blocklist has rationale or source
- [ ] Complements cve-detect-and-remediate (policy vs execution)

## Portability Notes

Policy structure is ecosystem-agnostic. Config format (dependabot.yml, renovate.json, .npmrc) varies. Adapt for pip, Go, Rust, etc.
