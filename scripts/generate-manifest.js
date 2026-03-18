#!/usr/bin/env node
/**
 * Generate skills-manifest.json from folder contents.
 * Outputs the rich manifest schema (repo, categories, skills with triggers, files object).
 * Use --dry-run to print without writing.
 *
 * For trigger extraction from SKILL.md, use: npm run generate-manifest:py
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const MANIFEST_PATH = path.join(ROOT, 'skills-manifest.json');

const IGNORE_DIRS = new Set(['.git', 'node_modules', 'scripts', 'docs', '.github']);

const SECURITY_SKILLS = new Set([
  'ai-agent-architecture', 'ai-devsecops-policy-enforcement', 'cve-detect-and-remediate',
  'dod-zero-trust-architect', 'security-evaluator', 'tool-evaluator', 'zero-trust-gitops-enforcement'
]);

function getSkillFiles(skillPath, skillName) {
  const base = skillName + '/';
  return {
    skill: (fs.existsSync(path.join(skillPath, 'SKILL.md'))) ? base + 'SKILL.md' : null,
    examples: (fs.existsSync(path.join(skillPath, 'examples.md'))) ? base + 'examples.md' : null,
    template: (fs.existsSync(path.join(skillPath, 'prompt-template.md'))) ? base + 'prompt-template.md' : null,
    reference: (fs.existsSync(path.join(skillPath, 'reference.md'))) ? base + 'reference.md' : null
  };
}

function parseSkillFrontmatter(skillPath) {
  const skillMd = path.join(skillPath, 'SKILL.md');
  if (!fs.existsSync(skillMd)) return null;
  const content = fs.readFileSync(skillMd, 'utf8');
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
      value = value.slice(2).replace(/\n/g, ' ').trim();
    }
    result[key] = value;
  }
  return result;
}

function inferSummary(desc) {
  if (!desc) return '';
  const idx = desc.search(/\b(Use when|Trigger on|Use for)\b/i);
  const text = idx >= 0 ? desc.slice(0, idx).trim() : desc;
  return text.replace(/[.,;]+$/, '').slice(0, 200) + (text.length > 200 ? '...' : '');
}

function main() {
  const dryRun = process.argv.includes('--dry-run');
  const dirs = fs.readdirSync(ROOT, { withFileTypes: true })
    .filter(d => d.isDirectory() && !d.name.startsWith('.') && !IGNORE_DIRS.has(d.name))
    .map(d => d.name)
    .sort();

  const skills = [];

  for (const dir of dirs) {
    const skillPath = path.join(ROOT, dir);
    const skillMd = path.join(skillPath, 'SKILL.md');
    if (!fs.existsSync(skillMd)) continue;

    const fm = parseSkillFrontmatter(skillPath);
    const category = SECURITY_SKILLS.has(dir) ? 'security-compliance' : 'ide-authoring';
    const desc = (fm && fm.description) || '';

    skills.push({
      name: dir,
      category,
      summary: inferSummary(desc),
      triggers: [dir.replace(/-/g, ' ')],
      files: getSkillFiles(skillPath, dir),
      tags: [],
      status: 'active'
    });
  }

  const manifest = {
    repo: 'agent-skills-pack',
    description: 'Production-ready Agent Skills for security, DevSecOps, Zero Trust, and IDE workflows. Designed for Cursor and other AI agent IDEs.',
    version: '0.1.0',
    repository: 'https://github.com/LongTheta/agent-skills-pack',
    license: 'MIT',
    categories: [
      { id: 'security-compliance', label: 'Security & Compliance' },
      { id: 'ide-authoring', label: 'IDE & Authoring' }
    ],
    skills
  };

  const out = JSON.stringify(manifest, null, 2);

  if (dryRun) {
    console.log(out);
    return;
  }

  fs.writeFileSync(MANIFEST_PATH, out + '\n', 'utf8');
  console.log('Generated skills-manifest.json');
}

main();
