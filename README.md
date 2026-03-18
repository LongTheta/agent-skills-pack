# agent-skills-pack

Cursor/IDE skills repository. Each skill lives in its own directory and can be versioned, shared, or published independently.

## Skills

### Security & Compliance
| Skill | Description |
|-------|-------------|
| [ai-agent-architecture](ai-agent-architecture/) | Design and evaluate AI agent systems across 7 layers |
| [ai-devsecops-policy-enforcement](ai-devsecops-policy-enforcement/) | Policy enforcement for CI/CD and GitOps pipelines |
| [cve-detect-and-remediate](cve-detect-and-remediate/) | Detect vulnerable dependencies and propose remediations |
| [dod-zero-trust-architect](dod-zero-trust-architect/) | DoD Zero Trust Architecture evaluation and design |
| [security-evaluator](security-evaluator/) | Security and compliance evaluation for systems |
| [tool-evaluator](tool-evaluator/) | Evaluate tools for enterprise adoption |
| [zero-trust-gitops-enforcement](zero-trust-gitops-enforcement/) | Zero Trust principles in CI/CD and GitOps |

### Cursor / IDE
| Skill | Description |
|-------|-------------|
| [create-rule](create-rule/) | Create Cursor rules for persistent AI guidance |
| [create-skill](create-skill/) | Create new Agent Skills for Cursor |
| [create-subagent](create-subagent/) | Create subagents for complex tasks |
| [migrate-to-skills](migrate-to-skills/) | Migrate existing content to skills format |
| [shell](shell/) | Shell and terminal operations |
| [update-cursor-settings](update-cursor-settings/) | Modify Cursor/VSCode user settings |

## Usage

1. **Clone or sync** this repo to your machine.
2. **Link skills** to Cursor:
   - Copy desired skill folders into `~/.cursor/skills/` (or your skills path)
   - Or use symlinks: `mklink /D "skill-name" "path\to\agent-skills-pack\skill-name"`
3. **Install** via Cursor Settings → Skills if using managed skills.

## Structure

Each skill directory contains:
- `SKILL.md` — Main skill definition (required)
- `examples.md` — Example prompts (optional)
- `reference.md` — Reference material (optional)
- `prompt-template.md` — Template for prompts (optional)

## Contributing

Each skill is self-contained. Add or update skills in their own directories. Keep `SKILL.md` as the entry point.
