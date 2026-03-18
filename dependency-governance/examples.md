# Dependency Governance — Examples

## Example 1: npm, Permissive Only

**Input:** "Dependency policy for npm; permissive licenses only"

**Output:** Allowed: MIT, Apache-2.0, BSD, ISC. Blocked: GPL, AGPL. Lockfile required. dependabot.yml for weekly updates.

## Example 2: Python, FedRAMP

**Input:** "Dependency governance for a FedRAMP Python project"

**Output:** License: permissive + Apache-2.0. Pinning: requirements.txt with exact versions. Blocklist: packages with known issues. Review: security team approval for new deps. Reference cve-detect-and-remediate for scanning.

## Example 3: Blocklist

**Input:** "Add a blocklist for known vulnerable packages"

**Output:** Policy section: Blocklist with package names, CVE or advisory refs, alternatives. Config: dependabot ignore or renovate config.
