#!/usr/bin/env python3
"""
Validate all skills in the repository.

Checks:
- Required files exist (per manifest)
- YAML frontmatter valid
- Required sections exist (When to Use, Safety Guardrails)
- Risk tier defined (frontmatter + manifest)
- Safety guardrails present
- Links not broken

Usage:
  python scripts/validate_skills.py
  python scripts/validate_skills.py --strict  # Fail on missing optional sections
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "skills-manifest.json"

REQUIRED_SECTIONS = ["When to Use", "Safety Guardrails"]
SECTION_ALTERNATIVES = {
    "Safety Guardrails": ["Safety Guardrails", "Validation Checklist", "Enforcement", "Constraints"],
}
RECOMMENDED_SECTIONS = [
    "Inputs", "Outputs", "Validation Checklist", "Portability Notes",
    "Purpose", "Steps", "Behavior", "Constraints", "Examples"
]

IGNORE_DIRS = {"docs", "scripts", "node_modules", ".github", ".git"}


def load_manifest() -> dict:
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


def parse_frontmatter_yaml(content: str) -> tuple[dict | None, str | None]:
    """Parse YAML frontmatter. Returns (parsed_dict, error_message)."""
    match = re.match(r"^---\s*\n([\s\S]*?)\n---", content)
    if not match:
        return None, "Missing or malformed frontmatter (expected --- ... ---)"

    yaml_block = match.group(1)
    try:
        import yaml
        data = yaml.safe_load(yaml_block)
        if data is None:
            return {}, None
        if not isinstance(data, dict):
            return None, "Frontmatter must be a YAML object"
        return data, None
    except ImportError:
        # Fallback: simple line-based parser when PyYAML not installed
        result = {}
        for line in yaml_block.split("\n"):
            colon = line.find(":")
            if colon == -1:
                continue
            key = line[:colon].strip()
            value = line[colon + 1 :].strip()
            if value.startswith(('"', "'")):
                value = value[1:-1]
            elif value.startswith(">-") or value.startswith("|"):
                value = value.lstrip(">-|").strip()
            result[key] = value
        return result, None
    except Exception as e:
        return None, f"Invalid YAML: {e}"


def get_required_files(manifest_skill: dict | None) -> list[Path]:
    """Return list of required file paths (relative to ROOT)."""
    if not manifest_skill:
        return [Path("SKILL.md")]  # Minimal default
    rf = manifest_skill.get("required_files")
    if not rf:
        return [Path("SKILL.md")]
    if isinstance(rf, list):
        return [Path(p) for p in rf]
    if isinstance(rf, dict):
        paths = []
        for v in rf.values():
            if v and isinstance(v, str):
                paths.append(Path(v))
        return paths if paths else [Path("SKILL.md")]
    return [Path("SKILL.md")]


def validate_skill(skill_dir: Path, manifest_skill: dict | None, strict: bool) -> list[str]:
    errors = []
    name = skill_dir.name

    # 1. Required files exist
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{name}: SKILL.md missing")
        return errors

    required_files = get_required_files(manifest_skill)
    for rel_path in required_files:
        abs_path = ROOT / rel_path
        if not abs_path.exists():
            errors.append(f"{name}: required file missing: {rel_path}")

    content = skill_md.read_text(encoding="utf-8")

    # 2. YAML frontmatter valid
    fm, fm_error = parse_frontmatter_yaml(content)
    if fm_error:
        errors.append(f"{name}: {fm_error}")
        return errors
    if fm is None:
        return errors

    if not fm.get("name"):
        errors.append(f"{name}: frontmatter missing 'name'")
    elif str(fm["name"]).strip() != name:
        errors.append(f"{name}: frontmatter 'name' ({fm['name']}) != directory")

    if not fm.get("description"):
        errors.append(f"{name}: frontmatter missing 'description'")
    elif len(str(fm.get("description", ""))) > 1024:
        errors.append(f"{name}: description exceeds 1024 chars")

    # 3. Risk tier defined (frontmatter)
    if "risk_tier" not in fm:
        errors.append(f"{name}: frontmatter missing 'risk_tier'")
    else:
        rt = fm["risk_tier"]
        try:
            rt_val = int(rt) if not isinstance(rt, int) else rt
            if rt_val not in (0, 1, 2, 3):
                errors.append(f"{name}: risk_tier must be 0, 1, 2, or 3 (got {rt})")
        except (ValueError, TypeError):
            errors.append(f"{name}: risk_tier must be integer 0-3 (got {rt})")

    # 4. Required sections exist
    content_lower = content.lower()
    for section in REQUIRED_SECTIONS:
        if section == "Safety Guardrails":
            alts = SECTION_ALTERNATIVES.get(section, [section])
            found = any(
                f"## {a}" in content or f"### {a}" in content
                for a in alts
            )
            if not found:
                errors.append(f"{name}: missing required section (one of: {', '.join(alts)})")
        else:
            if f"## {section}" not in content and f"### {section}" not in content:
                errors.append(f"{name}: missing required section '{section}'")

    # At least one workflow/output-like section
    has_workflow = any(
        p in content_lower for p in ["workflow", "process", "steps", "behavior", "gather"]
    )
    has_output = any(
        p in content_lower for p in ["output", "structure", "format", "template", "response"]
    )
    if not has_workflow:
        errors.append(f"{name}: missing workflow/process section")
    if not has_output:
        errors.append(f"{name}: missing output/format section")

    if strict:
        for section in RECOMMENDED_SECTIONS:
            if f"## {section}" not in content and f"### {section}" not in content:
                errors.append(f"{name}: missing recommended section '{section}' (strict)")

    # 6. Links not broken
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", content):
        link_target = m.group(2).strip()
        if link_target.startswith("http"):
            continue
        if "#" in link_target:
            link_target = link_target.split("#")[0]
        if not link_target:
            continue
        # Resolve relative to the SKILL.md file location
        base = skill_md.parent
        target_path = (base / link_target).resolve()
        if not target_path.exists():
            errors.append(f"{name}: broken link to {link_target}")

    # Manifest alignment and enforcement rules
    if manifest_skill:
        risk_tier = manifest_skill.get("risk_tier", 0)
        if "risk_tier" not in manifest_skill:
            errors.append(f"{name}: manifest missing risk_tier")
        # Tier 2: must include Validation Checklist
        if risk_tier == 2:
            if "## Validation Checklist" not in content and "### Validation Checklist" not in content:
                errors.append(f"{name}: Tier 2 skill must include Validation Checklist section")
        # Tier 3: requires security_reviewed and last_reviewed
        if risk_tier == 3:
            if not manifest_skill.get("security_reviewed"):
                errors.append(f"{name}: Tier 3 skill requires security_reviewed=true")
            if not manifest_skill.get("last_reviewed"):
                errors.append(f"{name}: Tier 3 skill requires last_reviewed date")
        if manifest_skill.get("security_reviewed") and not manifest_skill.get("last_reviewed"):
            errors.append(f"{name}: security_reviewed=true but last_reviewed missing")

    return errors


def main():
    strict = "--strict" in sys.argv
    manifest = load_manifest()
    manifest_skills = {s["name"]: s for s in manifest.get("skills", [])}

    all_errors = []

    for item in sorted(ROOT.iterdir()):
        if not item.is_dir() or item.name.startswith(".") or item.name in IGNORE_DIRS:
            continue
        if not (item / "SKILL.md").exists():
            continue

        manifest_skill = manifest_skills.get(item.name)
        errs = validate_skill(item, manifest_skill, strict)
        all_errors.extend(errs)

    # Manifest ↔ directory alignment
    manifest_names = set(manifest_skills)
    dir_names = {
        d.name for d in ROOT.iterdir()
        if d.is_dir() and not d.name.startswith(".") and d.name not in IGNORE_DIRS
        and (d / "SKILL.md").exists()
    }
    for d in dir_names - manifest_names:
        all_errors.append(f"{d}: in repo but not in manifest")
    for m in manifest_names - dir_names:
        all_errors.append(f"{m}: in manifest but directory missing")

    if all_errors:
        print("Validation failed:\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)

    print("All skills valid.")
    sys.exit(0)


if __name__ == "__main__":
    main()
