# Supply Chain Security

Provenance, integrity, and artifact security for the Jade CI/CD Agent Skills Pack.

**Governance:** Skill approval and release versioning are defined in [ai-governance-model.md](ai-governance-model.md).

## Current Practices

| Practice | Status |
|----------|--------|
| **SBOM** | CycloneDX in `sbom.json`; generated in CI |
| **Dependency pinning** | package-lock.json; pinned CI tools (markdownlint-cli, linkinator) |
| **Manifest validation** | `npm run validate`; CI checks |
| **Signed commits** | Recommended; not enforced |

## Artifact Integrity

- **Skills**: Markdown content; no executable code in skills
- **Scripts**: Node.js (stdlib) and Python (stdlib); no third-party runtime deps
- **CI**: GitHub Actions; pinned action versions (`@v4`)

## Future SLSA Alignment

| Level | Requirements | Status |
|-------|--------------|--------|
| **Level 1** | Build provenance (GitHub OIDC, attestations) | Roadmap: v1.3; document build steps and provenance generation |
| **Level 2** | Signed artifacts, two-person review | Planned |
| **Level 3** | Isolated build, hermetic | Future |

## Recommendations

1. **Verify before use**: Clone from official repo; check commit signatures
2. **Review skill content**: Especially Tier 2/3 skills before applying outputs
3. **Regenerate SBOM**: Run `npm run sbom` when adding dependencies
4. **Pin dependencies**: Use exact versions in package.json for reproducibility
