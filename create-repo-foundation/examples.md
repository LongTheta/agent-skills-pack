# Create Repository Foundation — Examples

## Example 1: Python Library

**Input:** "Create a Python library repo foundation"

**Outputs created:**
- `.gitignore` — Python, venv, __pycache__, .pytest_cache, dist/, *.egg-info
- `README.md` — Project name, pip install, basic usage
- `LICENSE` — MIT
- `CONTRIBUTING.md` — PR process, pytest, black
- `pyproject.toml` — Minimal [project], [build-system]
- `src/<package>/__init__.py`, `tests/`

## Example 2: Node.js CLI

**Input:** "Scaffold a Node.js CLI project"

**Outputs created:**
- `.gitignore` — node_modules, dist, .env
- `README.md` — npm install -g, usage
- `LICENSE` — MIT
- `CONTRIBUTING.md` — npm test, ESLint
- `package.json` — name, version, bin, scripts
- `src/cli.js`, `tests/`

## Example 3: Monorepo

**Input:** "Create foundation for a TypeScript monorepo with packages/"

**Outputs created:**
- `.gitignore` — node_modules, dist, .turbo
- `README.md` — Workspace setup, package scripts
- `LICENSE`, `CONTRIBUTING.md`
- `package.json` — workspaces
- `packages/` placeholder, `apps/` if applicable
