#!/usr/bin/env python3
"""
Generate skills-manifest.json from repository structure and SKILL.md files.

Scans skill directories, extracts frontmatter (name, description), infers
triggers from description text, and builds a rich manifest schema.

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

# Categories inferred from repo structure
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
    """Infer trigger phrases from description (Use when, Trigger on, etc.)."""
    triggers = []
    desc_lower = description.lower()

    # Common patterns
    patterns = [
        r"use when\s+([^.]+)",
        r"trigger on\s+([^.]+)",
        r"use for\s+([^.]+)",
        r"use\s+(?:for|when)\s+([^.]+)",
    ]
    for pattern in patterns:
        for m in re.finditer(pattern, desc_lower, re.IGNORECASE):
            phrase = m.group(1).strip()
            # Split on commas, "or", "and"
            for part in re.split(r"\s+or\s+|\s+and\s+|,\s*", phrase):
                part = part.strip()
                if part and len(part) > 3 and part not in triggers:
                    triggers.append(part[:80])

    # Fallback: extract key phrases (words after "when")
    if not triggers and "when" in desc_lower:
        idx = desc_lower.find("when")
        rest = description[idx + 5 :].strip()
        for part in re.split(r"[,;.]", rest)[:5]:
            part = part.strip()
            if part and len(part) > 4:
                triggers.append(part[:80])

    return triggers[:10]  # Cap at 10


def infer_summary(description: str, max_len: int = 200) -> str:
    """Create a short summary from the full description."""
    # Remove "Use when" / "Trigger on" clauses
    for pattern in ["Use when", "Trigger on", "Use for", "Use when you"]:
        if pattern in description:
            idx = description.find(pattern)
            description = description[:idx].strip()
    # Clean trailing punctuation
    description = description.rstrip(".,; ")
    if len(description) > max_len:
        description = description[: max_len - 3] + "..."
    return description


def get_skill_files(skill_dir: Path) -> dict:
    """Return paths for skill, examples, template, reference. Use null if missing."""
    name = skill_dir.name
    return {
        "skill": f"{name}/SKILL.md" if (skill_dir / "SKILL.md").exists() else None,
        "examples": f"{name}/examples.md" if (skill_dir / "examples.md").exists() else None,
        "template": f"{name}/prompt-template.md" if (skill_dir / "prompt-template.md").exists() else None,
        "reference": f"{name}/reference.md" if (skill_dir / "reference.md").exists() else None,
    }


def get_tags(skill_name: str) -> list[str]:
    """Default tags per skill (can be overridden by parsing)."""
    tag_map = {
        "ai-agent-architecture": ["ai", "architecture", "production-readiness", "evaluation"],
        "ai-devsecops-policy-enforcement": ["devsecops", "ci-cd", "gitops", "argo-cd", "compliance"],
        "cve-detect-and-remediate": ["cve", "supply-chain", "dependencies", "remediation", "osv"],
        "dod-zero-trust-architect": ["zero-trust", "dod", "federal", "nist", "fedramp"],
        "security-evaluator": ["security", "compliance", "evaluation", "scorecard", "fedramp", "nist", "gitops"],
        "tool-evaluator": ["evaluation", "enterprise", "devops", "gitops"],
        "zero-trust-gitops-enforcement": ["zero-trust", "gitops", "ci-cd", "pipeline-security"],
        "create-rule": ["cursor", "rules", "conventions"],
        "create-skill": ["cursor", "skills", "authoring"],
        "create-subagent": ["cursor", "subagents", "agents"],
        "migrate-to-skills": ["cursor", "migration", "rules", "commands"],
        "shell": ["shell", "terminal", "cursor"],
        "update-cursor-settings": ["cursor", "vscode", "settings"],
    }
    return tag_map.get(skill_name, [])


def scan_skills() -> list[dict]:
    """Scan repo and build skill entries."""
    skills = []
    for item in sorted(ROOT.iterdir()):
        if not item.is_dir() or item.name.startswith(".") or item.name in ("docs", "scripts", "node_modules"):
            continue
        skill_md = item / "SKILL.md"
        if not skill_md.exists():
            continue

        content = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        name = fm.get("name")
        if not name:
            name = item.name

        description = fm.get("description", "")
        if isinstance(description, str) and ">-" in content:
            # Multiline YAML
            desc_match = re.search(r"description:\s*>-?\s*\n\s*(.+?)(?=\n\w|\n---|\Z)", content, re.DOTALL)
            if desc_match:
                description = desc_match.group(1).replace("\n", " ").strip()

        category = "security-compliance" if name in SECURITY_SKILLS else "ide-authoring"
        triggers = extract_triggers(description) if description else []
        if not triggers:
            triggers = [name.replace("-", " ")]

        skills.append({
            "name": name,
            "category": category,
            "summary": infer_summary(description) if description else "",
            "triggers": triggers,
            "files": get_skill_files(item),
            "tags": get_tags(name),
            "status": "active",
        })
    return skills


def main():
    dry_run = "--dry-run" in sys.argv
    skills = scan_skills()

    manifest = {
        "repo": "agent-skills-pack",
        "description": "Production-ready Agent Skills for security, DevSecOps, Zero Trust, and IDE workflows. Designed for Cursor and other AI agent IDEs.",
        "version": "0.1.0",
        "repository": "https://github.com/LongTheta/agent-skills-pack",
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
