#!/usr/bin/env python3
"""
Generate skills-manifest.json from repository structure and SKILL.md files.

Outputs a rich manifest schema with:
- name, category, summary, tags, triggers
- compatibility, risk_tier, status
- required_files, maintainer, last_reviewed, security_reviewed

Usage:
  python scripts/generate_manifest.py           # Write to skills-manifest.json
  python scripts/generate_manifest.py --dry-run # Print to stdout only
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "skills-manifest.json"

CATEGORIES = [
    {"id": "security-compliance", "label": "Security & Compliance"},
    {"id": "ide-authoring", "label": "IDE & Authoring"},
]

SECURITY_SKILLS = {
    "ai-agent-architecture",
    "ai-devsecops-policy-enforcement",
    "cve-detect-and-remediate",
    "dod-zero-trust-architect",
    "security-evaluator",
    "tool-evaluator",
    "zero-trust-gitops-enforcement",
}

# Risk tiers: 0=read-only, 1=content gen, 2=code/config proposal, 3=pipeline/infra/security
RISK_TIERS = {
    "ai-agent-architecture": 0,
    "ai-devsecops-policy-enforcement": 3,
    "cve-detect-and-remediate": 2,
    "dod-zero-trust-architect": 0,
    "security-evaluator": 0,
    "tool-evaluator": 0,
    "zero-trust-gitops-enforcement": 2,
    "create-rule": 1,
    "create-skill": 1,
    "create-subagent": 2,
    "migrate-to-skills": 2,
    "shell": 3,
    "update-vscode-settings": 2,
}

# Skills requiring security review (Tier 3 or security-impacting)
SECURITY_REVIEWED_SKILLS = {
    "security-evaluator",
    "cve-detect-and-remediate",
    "ai-devsecops-policy-enforcement",
    "dod-zero-trust-architect",
    "zero-trust-gitops-enforcement",
    "shell",  # Tier 3: shell/command execution
}

# ISO date for manifest audit trail (update when governance re-reviews the pack)
MANIFEST_LAST_REVIEWED = "2026-04-13"

REQUIRED_FILES = ["SKILL.md"]
OPTIONAL_FILES = ["examples.md", "prompt-template.md", "reference.md"]


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from SKILL.md content."""
    match = re.match(r"^---\s*\n([\s\S]*?)\n---", content)
    if not match:
        return {}
    yaml_block = match.group(1)
    result = {}
    for line in yaml_block.split("\n"):
        colon = line.find(":")
        if colon == -1:
            continue
        key = line[:colon].strip()
        value = line[colon + 1 :].strip()
        if value.startswith(">-"):
            value = value[2:].replace("\n", " ").strip()
        elif value.startswith(('"', "'")):
            value = value[1:-1]
        result[key] = value
    return result


def extract_triggers(description: str) -> list[str]:
    """Infer trigger phrases from description."""
    triggers = []
    desc_lower = description.lower()
    patterns = [
        r"use when\s+([^.]+)",
        r"trigger on\s+([^.]+)",
        r"use for\s+([^.]+)",
    ]
    for pattern in patterns:
        for m in re.finditer(pattern, desc_lower, re.IGNORECASE):
            phrase = m.group(1).strip()
            for part in re.split(r"\s+or\s+|\s+and\s+|,\s*", phrase):
                part = part.strip()
                if part and len(part) > 3 and part not in triggers:
                    triggers.append(part[:80])
    if not triggers and "when" in desc_lower:
        idx = desc_lower.find("when")
        rest = description[idx + 5 :].strip()
        for part in re.split(r"[,;.]", rest)[:5]:
            part = part.strip()
            if part and len(part) > 4:
                triggers.append(part[:80])
    return triggers[:10]


def infer_summary(description: str, max_len: int = 200) -> str:
    """Create a short summary from the full description."""
    for pattern in ["Use when", "Trigger on", "Use for", "Use when you"]:
        if pattern in description:
            idx = description.find(pattern)
            description = description[:idx].strip()
    description = description.rstrip(".,; ")
    if len(description) > max_len:
        description = description[: max_len - 3] + "..."
    return description


def get_required_files(skill_dir: Path) -> dict:
    """Return required_files object: skill, examples, template, reference."""
    name = skill_dir.name
    return {
        "skill": f"{name}/SKILL.md" if (skill_dir / "SKILL.md").exists() else None,
        "examples": f"{name}/examples.md" if (skill_dir / "examples.md").exists() else None,
        "template": f"{name}/prompt-template.md" if (skill_dir / "prompt-template.md").exists() else None,
        "reference": f"{name}/reference.md" if (skill_dir / "reference.md").exists() else None,
    }


def get_tags(skill_name: str) -> list[str]:
    """Default tags per skill."""
    tag_map = {
        "ai-agent-architecture": ["ai", "architecture", "production-readiness", "evaluation"],
        "ai-devsecops-policy-enforcement": ["devsecops", "ci-cd", "gitops", "argo-cd", "compliance"],
        "cve-detect-and-remediate": ["cve", "supply-chain", "dependencies", "remediation", "osv"],
        "dod-zero-trust-architect": ["zero-trust", "dod", "federal", "nist", "fedramp"],
        "security-evaluator": ["security", "compliance", "evaluation", "scorecard", "fedramp", "nist"],
        "tool-evaluator": ["evaluation", "enterprise", "devops", "gitops"],
        "zero-trust-gitops-enforcement": ["zero-trust", "gitops", "ci-cd", "pipeline-security"],
        "create-rule": ["ai-ide", "rules", "conventions"],
        "create-skill": ["ai-ide", "skills", "authoring"],
        "create-subagent": ["ai-ide", "subagents", "agents"],
        "migrate-to-skills": ["ai-ide", "migration", "rules", "commands"],
        "shell": ["shell", "terminal", "cli"],
        "update-vscode-settings": ["vscode", "settings", "editor"],
    }
    return tag_map.get(skill_name, [])


def scan_skills() -> list[dict]:
    """Scan repo and build skill entries with full schema."""
    skills = []
    for item in sorted(ROOT.iterdir()):
        if not item.is_dir() or item.name.startswith(".") or item.name in ("docs", "scripts", "node_modules"):
            continue
        skill_md = item / "SKILL.md"
        if not skill_md.exists():
            continue

        content = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        name = fm.get("name") or item.name

        description = fm.get("description", "")
        if isinstance(description, str) and ">-" in content:
            desc_match = re.search(r"description:\s*>-?\s*\n\s*(.+?)(?=\n\w|\n---|\Z)", content, re.DOTALL)
            if desc_match:
                description = desc_match.group(1).replace("\n", " ").strip()

        category = "security-compliance" if name in SECURITY_SKILLS else "ide-authoring"
        triggers = extract_triggers(description) if description else [name.replace("-", " ")]
        risk_tier = RISK_TIERS.get(name, 0)
        security_reviewed = name in SECURITY_REVIEWED_SKILLS
        last_reviewed = MANIFEST_LAST_REVIEWED

        skills.append({
            "name": name,
            "category": category,
            "summary": infer_summary(description) if description else "",
            "triggers": triggers,
            "tags": get_tags(name),
            "compatibility": ["vscode"],
            "risk_tier": risk_tier,
            "status": "active",
            "required_files": get_required_files(item),
            "maintainer": "LongTheta",
            "last_reviewed": last_reviewed,
            "security_reviewed": security_reviewed,
        })
    return skills


def main():
    dry_run = "--dry-run" in sys.argv
    skills = scan_skills()

    manifest = {
        "repo": "jade-cicd-agent-skills-pack",
        "description": "Jade CI/CD Agent Skills for security, DevSecOps, Zero Trust, and IDE workflows. Designed for VS Code–based editors and other AI-assisted development environments.",
        "version": "1.0.0",
        "repository": "https://github.com/ai-devsecops-packs/jade-cicd-agent-skills-pack",
        "license": "MIT",
        "categories": CATEGORIES,
        "skills": skills,
    }

    out = json.dumps(manifest, indent=2, ensure_ascii=False)

    if dry_run:
        print(out)
        return

    MANIFEST_PATH.write_text(out + "\n", encoding="utf-8")
    print(f"Generated {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
