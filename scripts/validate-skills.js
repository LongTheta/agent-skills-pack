#!/usr/bin/env node
/**
 * Validate all skills in the repository.
 * Checks: SKILL.md exists, valid frontmatter, required files per manifest.
 * Exit code: 0 if valid, 1 if invalid.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const MANIFEST_PATH = path.join(ROOT, 'skills-manifest.json');

function readManifest() {
  const raw = fs.readFileSync(MANIFEST_PATH, 'utf8');
  return JSON.parse(raw);
}

function parseFrontmatter(content) {
  const match = content.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!match) return null;
  const yaml = match[1];
  const result = {};
  for (const line of yaml.split('\n')) {
    const colon = line.indexOf(':');
    if (colon === -1) continue;
    const key = line.slice(0, colon).trim();
    let value = line.slice(colon + 1).trim();
    if (value.startsWith('"') || value.startsWith("'")) {
      value = value.slice(1, -1);
    } else if (value.startsWith('>')) {
      value = value.slice(1).trim();
    }
    result[key] = value;
  }
  return result;
}

function validateSkill(skillDir, skillId, manifestFiles) {
  const errors = [];
  const skillPath = path.join(ROOT, skillDir);

  if (!fs.existsSync(skillPath)) {
    errors.push(`${skillId}: Directory not found`);
    return errors;
  }

  const skillMd = path.join(skillPath, 'SKILL.md');
  if (!fs.existsSync(skillMd)) {
    errors.push(`${skillId}: SKILL.md missing`);
    return errors;
  }

  const content = fs.readFileSync(skillMd, 'utf8');
  const fm = parseFrontmatter(content);

  if (!fm) {
    errors.push(`${skillId}: SKILL.md has no valid YAML frontmatter`);
    return errors;
  }

  if (!fm.name) {
    errors.push(`${skillId}: frontmatter missing 'name'`);
  } else if (fm.name !== skillId) {
    errors.push(`${skillId}: frontmatter 'name' (${fm.name}) does not match directory`);
  }

  if (!fm.description) {
    errors.push(`${skillId}: frontmatter missing 'description'`);
  } else if (fm.description.length > 1024) {
    errors.push(`${skillId}: description exceeds 1024 chars`);
  }

  // Support both legacy array and new object format for files
  if (manifestFiles) {
    if (Array.isArray(manifestFiles)) {
      for (const file of manifestFiles) {
        const filePath = path.join(skillPath, file);
        if (!fs.existsSync(filePath)) {
          errors.push(`${skillId}: missing ${file} (listed in manifest)`);
        }
      }
    } else if (typeof manifestFiles === 'object') {
      const filesToCheck = manifestFiles.required_files || manifestFiles.files || manifestFiles;
      for (const [key, relPath] of Object.entries(filesToCheck)) {
        if (relPath) {
          const filePath = path.join(ROOT, relPath);
          if (!fs.existsSync(filePath)) {
            errors.push(`${skillId}: missing ${relPath} (listed in manifest)`);
          }
        }
      }
    }
  }

  return errors;
}

function main() {
  const manifest = readManifest();
  const skills = manifest.skills || [];
  const skillDirs = new Set();

  for (const skill of skills) {
    const id = typeof skill === 'string' ? skill : (skill.name || skill.id);
    if (id) skillDirs.add(id);
  }

  const dirs = fs.readdirSync(ROOT, { withFileTypes: true })
    .filter(d => d.isDirectory() && !d.name.startsWith('.') && !['node_modules', 'scripts', 'docs', '.github', 'tests'].includes(d.name))
    .map(d => d.name);

  let allErrors = [];

  for (const skill of skills) {
    const id = typeof skill === 'string' ? skill : (skill.name || skill.id);
    const files = typeof skill === 'object' ? (skill.required_files || skill.files) : undefined;
    const errs = validateSkill(id, id, files);
    allErrors.push(...errs);
  }

  const manifestIds = new Set(skills.map(s => typeof s === 'string' ? s : (s.name || s.id)));
  for (const dir of dirs) {
    if (!manifestIds.has(dir)) {
      allErrors.push(`${dir}: present as directory but not in skills-manifest.json`);
    }
  }

  if (allErrors.length > 0) {
    console.error('Validation failed:\n');
    allErrors.forEach(e => console.error('  -', e));
    process.exit(1);
  }

  console.log('All skills valid.');
  process.exit(0);
}

main();
