# Update Cursor Settings — Reference

## Settings File Locations

| OS | Path |
|----|------|
| macOS | `~/Library/Application Support/Cursor/User/settings.json` |
| Linux | `~/.config/Cursor/User/settings.json` |
| Windows | `%APPDATA%\Cursor\User\settings.json` |

## Common Settings

| Category | Examples |
|----------|----------|
| Editor | `editor.fontSize`, `editor.tabSize`, `editor.formatOnSave`, `editor.wordWrap` |
| Workbench | `workbench.colorTheme`, `workbench.iconTheme` |
| Files | `files.autoSave`, `files.exclude` |
| Terminal | `terminal.integrated.fontSize`, `terminal.integrated.shell.*` |

## Notes

- VSCode/Cursor settings support JSON with comments
- Some settings require window reload
- User vs workspace: User = global; Workspace = `.vscode/settings.json`
