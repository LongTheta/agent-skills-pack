# Create Repository Foundation — Reference

## .gitignore Patterns by Language

| Language | Key entries |
|----------|-------------|
| Python | __pycache__, *.pyc, venv, .venv, .pytest_cache, dist, *.egg-info |
| Node | node_modules, dist, .env, .next, .nuxt |
| Go | /bin, /vendor (if used) |
| Rust | /target |
| Java/Kotlin | /build, .gradle, *.class |

## Common Additions

- IDE: .idea, .vscode (or commit shared settings)
- OS: .DS_Store, Thumbs.db
- Build: *.log, coverage/, .coverage

## README Sections

1. Project name and one-line description
2. Install / setup
3. Usage (minimal example)
4. Contributing (link to CONTRIBUTING.md)
5. License

## License Sources

- MIT: https://opensource.org/licenses/MIT
- Apache-2.0: https://www.apache.org/licenses/LICENSE-2.0

Replace [year] and [copyright holder] with actual values.
