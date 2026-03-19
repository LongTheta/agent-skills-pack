#!/usr/bin/env node
/**
 * Certification scoring for Jade CI/CD Agent Skills Pack.
 * Evaluates repository against federal-grade AI, DevSecOps, and security best practices.
 * Exit code: 0 if score >= threshold, 1 otherwise. Default threshold: 7.5.
 *
 * Usage:
 *   node scripts/certification-score.js
 *   node scripts/certification-score.js --threshold 8.0
 *   node scripts/certification-score.js --json
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const thresholdArg = process.argv.find(a => a.startsWith('--threshold='));
const THRESHOLD = thresholdArg ? parseFloat(thresholdArg.split('=')[1]) : parseFloat(process.env.CERT_THRESHOLD || '7.5');
const JSON_OUTPUT = process.argv.includes('--json');

const WEIGHTS = {
  structure: 0.10,
  validation: 0.15,
  skillStandardization: 0.20,
  aiSecurity: 0.20,
  trustBoundaries: 0.10,
  outputValidation: 0.10,
  riskTier: 0.10,
  auditability: 0.03,
  releaseReadiness: 0.02,
};

const REQUIRED_SECTIONS = [
  'When to Use',
  'Inputs',
  'Outputs',
  'Workflow',
  'Limitations',
  'Safety Guardrails',
  'Validation Checklist',
  'Portability Notes',
];
const SECTION_ALTERNATIVES = {
  'Safety Guardrails': ['Safety Guardrails', 'Validation Checklist', 'Enforcement'],
  'Workflow': ['Workflow', 'Evaluation Workflow', 'Conversion Format', 'Process', 'Steps', 'Gather Requirements'],
};

const AI_SECURITY_REQUIRED = [
  'trust boundaries',
  'prompt injection',
  'tool access',
  'output validation',
];

function exists(p) {
  try {
    return fs.existsSync(path.join(ROOT, p));
  } catch {
    return false;
  }
}

function readFile(p) {
  try {
    return fs.readFileSync(path.join(ROOT, p), 'utf8');
  } catch {
    return '';
  }
}

function parseFrontmatter(content) {
  const match = content.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!match) return null;
  const result = {};
  for (const line of match[1].split('\n')) {
    const colon = line.indexOf(':');
    if (colon === -1) continue;
    const key = line.slice(0, colon).trim();
    let value = line.slice(colon + 1).trim();
    if (value.startsWith('"') || value.startsWith("'")) value = value.slice(1, -1);
    else if (value.startsWith('>')) value = value.slice(1).trim();
    result[key] = value;
  }
  return result;
}

function getSkillDirs() {
  const manifest = JSON.parse(readFile('skills-manifest.json') || '{}');
  const skills = manifest.skills || [];
  return skills.map(s => (typeof s === 'string' ? s : s.name || s.id)).filter(Boolean);
}

function getManifestSkills() {
  const manifest = JSON.parse(readFile('skills-manifest.json') || '{}');
  const skills = manifest.skills || [];
  return skills.reduce((acc, s) => {
    if (typeof s === 'object' && s.name) acc[s.name] = s;
    return acc;
  }, {});
}

function hasSection(content, section) {
  const alts = SECTION_ALTERNATIVES[section] || [section];
  const lower = content.toLowerCase();
  return alts.some(alt => {
    const re = new RegExp(`^##+\\s+${alt.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\s*$`, 'im');
    return re.test(content) || lower.includes(`## ${alt}`) || lower.includes(`### ${alt}`);
  });
}

function scoreStructure(issues) {
  const checks = [
    ['README.md', 'README.md exists and is non-trivial'],
    ['LICENSE', 'LICENSE present'],
    ['CONTRIBUTING.md', 'CONTRIBUTING.md present'],
    ['SECURITY.md', 'SECURITY.md present'],
    ['CHANGELOG.md', 'CHANGELOG.md present'],
    ['CODEOWNERS', 'CODEOWNERS present'],
  ];
  let passed = 0;
  for (const [file, desc] of checks) {
    if (exists(file)) {
      if (file === 'README.md') {
        const content = readFile(file);
        if (content && content.length > 500) passed++;
        else issues.warn.push(`README.md exists but may be trivial (< 500 chars)`);
      } else {
        passed++;
      }
    } else {
      issues.block.push(`${desc} missing`);
    }
  }
  return (passed / checks.length) * 10;
}

function scoreValidation(issues) {
  let passed = 0;
  const total = 4;
  if (exists('scripts/validate-skills.js')) passed++;
  else issues.block.push('validate-skills.js script missing');

  if (exists('.husky') || exists('.git/hooks/pre-commit')) passed++;
  else issues.warn.push('Git hooks not configured (husky or .git/hooks)');

  const workflowsDir = '.github/workflows';
  if (exists(workflowsDir)) {
    const files = fs.readdirSync(path.join(ROOT, workflowsDir)).filter(f => f.endsWith('.yml') || f.endsWith('.yaml'));
    if (files.length > 0) passed++;
    else issues.warn.push('No CI workflow files found');
  } else {
    issues.block.push('CI workflows directory missing');
  }

  const validateContent = readFile('.github/workflows/validate.yml') || readFile('.github/workflows/ci.yml') || '';
  if (validateContent.includes('validate-skills') || validateContent.includes('validate_skills')) passed++;
  else issues.warn.push('Validation not referenced in CI');

  return (passed / total) * 10;
}

function scoreSkillStandardization(issues) {
  const dirs = getSkillDirs();
  if (dirs.length === 0) return 0;
  let totalScore = 0;
  for (const dir of dirs) {
    const skillPath = path.join(ROOT, dir, 'SKILL.md');
    if (!exists(path.join(dir, 'SKILL.md'))) {
      issues.block.push(`${dir}: SKILL.md missing`);
      continue;
    }
    const content = readFile(path.join(dir, 'SKILL.md'));
    const fm = parseFrontmatter(content);
    if (!fm) {
      issues.block.push(`${dir}: invalid YAML frontmatter`);
      continue;
    }
    let skillScore = 0;
    for (const section of REQUIRED_SECTIONS) {
      if (hasSection(content, section)) skillScore++;
    }
    totalScore += (skillScore / REQUIRED_SECTIONS.length) * 10;
  }
  return totalScore / dirs.length;
}

function scoreAiSecurity(issues) {
  if (!exists('docs/ai-security-model.md')) {
    issues.block.push('docs/ai-security-model.md missing');
    return 0;
  }
  const content = readFile('docs/ai-security-model.md').toLowerCase();
  let passed = 0;
  for (const term of AI_SECURITY_REQUIRED) {
    if (content.includes(term)) passed++;
    else issues.block.push(`ai-security-model.md missing: ${term}`);
  }
  return (passed / AI_SECURITY_REQUIRED.length) * 10;
}

function scoreTrustBoundaries(issues) {
  const dirs = getSkillDirs();
  if (dirs.length === 0) return 0;
  let withTb = 0;
  for (const dir of dirs) {
    const content = readFile(path.join(dir, 'SKILL.md'));
    if (content && /##\s+Trust Boundaries/im.test(content)) withTb++;
    else issues.block.push(`${dir}: missing Trust Boundaries section`);
  }
  return (withTb / dirs.length) * 10;
}

function scoreOutputValidation(issues) {
  const dirs = getSkillDirs();
  if (dirs.length === 0) return 0;
  let withOv = 0;
  for (const dir of dirs) {
    const content = readFile(path.join(dir, 'SKILL.md'));
    if (content && /##\s+Output Validation/im.test(content)) withOv++;
    else issues.block.push(`${dir}: missing Output Validation section`);
  }
  return (withOv / dirs.length) * 10;
}

function scoreRiskTier(issues) {
  const manifestSkills = getManifestSkills();
  if (Object.keys(manifestSkills).length === 0) return 0;
  let score = 10;
  for (const [name, skill] of Object.entries(manifestSkills)) {
    const rt = skill.risk_tier;
    if (rt === undefined || rt === null) {
      issues.warn.push(`${name}: missing risk_tier in manifest`);
      score -= 1;
    } else if (rt === 3) {
      if (!skill.security_reviewed) issues.block.push(`${name}: Tier 3 skill missing security_reviewed`);
      if (!skill.last_reviewed) issues.block.push(`${name}: Tier 3 skill missing last_reviewed`);
    }
  }
  return Math.max(0, Math.min(10, score));
}

function scoreAuditability(issues) {
  const manifestSkills = getManifestSkills();
  if (Object.keys(manifestSkills).length === 0) return 0;
  let withReview = 0;
  let withSecReview = 0;
  for (const [name, skill] of Object.entries(manifestSkills)) {
    if (skill.last_reviewed != null) withReview++;
    else issues.warn.push(`${name}: last_reviewed is null`);
    if (skill.security_reviewed != null) withSecReview++;
    else issues.info.push(`${name}: security_reviewed is null`);
  }
  const n = Object.keys(manifestSkills).length;
  return ((withReview / n) * 5 + (withSecReview / n) * 5);
}

function scoreReleaseReadiness(issues) {
  let passed = 0;
  if (exists('docs/release-readiness.md')) passed++;
  else issues.warn.push('docs/release-readiness.md missing');
  const changelog = readFile('CHANGELOG.md');
  if (changelog && /v1\.0\.0|1\.0\.0/i.test(changelog)) passed++;
  else issues.info.push('CHANGELOG may not contain v1.0.0');
  const workflows = exists('.github/workflows') && fs.readdirSync(path.join(ROOT, '.github/workflows')).length > 0;
  if (workflows) passed++;
  return (passed / 3) * 10;
}

function run() {
  const issues = { block: [], warn: [], info: [] };
  const scores = {};

  scores.structure = scoreStructure(issues);
  scores.validation = scoreValidation(issues);
  scores.skillStandardization = scoreSkillStandardization(issues);
  scores.aiSecurity = scoreAiSecurity(issues);
  scores.trustBoundaries = scoreTrustBoundaries(issues);
  scores.outputValidation = scoreOutputValidation(issues);
  scores.riskTier = scoreRiskTier(issues);
  scores.auditability = scoreAuditability(issues);
  scores.releaseReadiness = scoreReleaseReadiness(issues);

  let total = 0;
  for (const [k, w] of Object.entries(WEIGHTS)) {
    total += (scores[k] || 0) * w;
  }

  const passed = total >= THRESHOLD;

  if (JSON_OUTPUT) {
    console.log(JSON.stringify({
      score: Math.round(total * 10) / 10,
      threshold: THRESHOLD,
      passed,
      scores,
      issues,
    }, null, 2));
  } else {
    console.log('\nCertification Score: ' + (Math.round(total * 10) / 10) + ' / 10\n');
    console.log('Per-category breakdown:');
    console.log('  Structure & Governance:     ' + scores.structure.toFixed(1) + '/10');
    console.log('  Validation & Enforcement:   ' + scores.validation.toFixed(1) + '/10');
    console.log('  Skill Standardization:     ' + scores.skillStandardization.toFixed(1) + '/10');
    console.log('  AI Security Model:         ' + scores.aiSecurity.toFixed(1) + '/10');
    console.log('  Trust Boundaries:           ' + scores.trustBoundaries.toFixed(1) + '/10');
    console.log('  Output Validation:          ' + scores.outputValidation.toFixed(1) + '/10');
    console.log('  Risk Tier Enforcement:     ' + scores.riskTier.toFixed(1) + '/10');
    console.log('  Auditability:               ' + scores.auditability.toFixed(1) + '/10');
    console.log('  Release Readiness:          ' + scores.releaseReadiness.toFixed(1) + '/10');
    console.log('\n' + (passed ? 'PASS' : 'FAIL') + ' (threshold: ' + THRESHOLD + ')\n');

    if (issues.block.length > 0) {
      console.log('BLOCKERS:');
      issues.block.forEach(b => console.log('  - ' + b));
      console.log('');
    }
    if (issues.warn.length > 0) {
      console.log('WARNINGS:');
      issues.warn.forEach(w => console.log('  - ' + w));
      console.log('');
    }
    if (issues.info.length > 0) {
      console.log('INFO:');
      issues.info.forEach(i => console.log('  - ' + i));
      console.log('');
    }
  }

  process.exit(passed ? 0 : 1);
}

run();
