# Dependency Governance — Reference

## License Categories

- **Permissive:** MIT, Apache-2.0, BSD, ISC
- **Weak copyleft:** LGPL
- **Strong copyleft:** GPL, AGPL

## Relation to cve-detect-and-remediate

- **dependency-governance:** Defines policy (what's allowed, pinning, blocklist)
- **cve-detect-and-remediate:** Executes scanning and remediation per policy

Use both: governance sets rules; cve-detect enforces and fixes.
