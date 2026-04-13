# Update VS Code settings — reference

## Settings file locations (VS Code)

| OS | Path |
|----|------|
| macOS | `~/Library/Application Support/Code/User/settings.json` |
| Linux | `~/.config/Code/User/settings.json` |
| Windows | `%APPDATA%\Code\User\settings.json` |

Forks (e.g., VSCodium) use parallel paths under their application ID.

## Common settings

| Category | Examples |
|----------|----------|
| Editor | `editor.fontSize`, `editor.tabSize`, `editor.formatOnSave`, `editor.wordWrap` |
| Workbench | `workbench.colorTheme`, `workbench.iconTheme` |
| Files | `files.autoSave`, `files.exclude` |
| Terminal | `terminal.integrated.fontSize`, `terminal.integrated.shell.*` |

## Notes

- VS Code settings support JSON with comments
- Some settings require window reload
- User vs workspace: User = global; Workspace = `.vscode/settings.json`
