# Release Checklist

Use this checklist before tagging a release. For v1 release criteria, see [release-readiness.md](release-readiness.md).

---

## Pre-Release

- [ ] All skills pass `npm run validate:full`
- [ ] SBOM up to date: run `npm install && npm run sbom` and commit `sbom.json` if deps changed
- [ ] Manifest is valid: `npm run generate-manifest -- --dry-run`
- [ ] CHANGELOG.md updated with version and changes
- [ ] No broken links (CI link check passes)
- [ ] Markdown lint passes

---

## Version Bumping

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** — Breaking changes (e.g., skill format, required files)
- **MINOR** — New skills, new features, backward-compatible
- **PATCH** — Fixes, docs, minor improvements

Update:

- `skills-manifest.json` → `version`
- `CHANGELOG.md` → New section for version
- `README.md` → Roadmap if needed

---

## Release Steps

1. **Final validation**
   ```bash
   npm run validate
   ```

2. **Commit and tag**
   ```bash
   git add -A
   git commit -m "Release v1.0.0"
   git tag v1.0.0
   git push origin main --tags
   ```

3. **Create GitHub Release**
   - Use tag `v1.0.0`
   - Copy CHANGELOG section for release notes
   - Attach any artifacts if needed

---

## Post-Release

- [ ] Verify tag on GitHub
- [ ] Update any external docs or indexes
- [ ] Announce in community channels if applicable
