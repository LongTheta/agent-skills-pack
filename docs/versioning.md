# Versioning

Release versioning and pre-release steps are defined in [ai-governance-model.md](ai-governance-model.md). Summary below.

## Semantic Versioning

We follow [Semantic Versioning 2.0](https://semver.org/):

- **MAJOR** — Breaking changes (manifest schema, skill format, required sections)
- **MINOR** — New skills, new features, backward-compatible
- **PATCH** — Fixes, docs, minor improvements

## Version Locations

| Location | Purpose |
|----------|---------|
| `skills-manifest.json` → `version` | Pack version |
| `package.json` → `version` | Tooling version |
| `CHANGELOG.md` | Human-readable history |

## Release Cadence

- **Patch**: As needed for fixes
- **Minor**: When new skills or features land
- **Major**: When schema or format changes require migration

## Branch Strategy

- `master` / `main` — Default branch; protected
- `release/v*` — Release branches (optional)
- Feature branches: `feature/`, `fix/`, `docs/`

See [release-checklist.md](release-checklist.md) for pre-release steps.
