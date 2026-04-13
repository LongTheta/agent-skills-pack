---
name: update-vscode-settings
risk_tier: 2
description: >-
  Modify VS Code user settings in settings.json. Use when you want to
  change editor settings, preferences, configuration, themes, font size, tab
  size, format on save, auto save, keybindings, or any settings.json values.
---

# Update VS Code settings

## Purpose

Modifies VS Code (or VS Code–compatible editor) user settings in `settings.json`. Changes themes, font size, tab size, format on save, keybindings, and other editor preferences. Tier 2: user approval required for settings.json writes; preserve existing settings; only add/modify what user requested.

## When to Use

- User wants to change editor settings, preferences, or configuration
- User asks about themes, font size, tab size, format on save, auto save, keybindings
- User wants to modify `settings.json` values
- User asks how to change workbench or editor settings in VS Code

## Inputs

| Input | Description |
|-------|-------------|
| User's intent | Which setting to change (e.g., font size, theme, format on save) |
| Current settings path | Infer from OS if not provided |

## Outputs

- **Updated settings.json** — With requested change(s)
- **Confirmation** — Note if reload/restart required

## Steps / Behavior

1. **Read existing settings** — Use settings path for OS (macOS: `~/Library/Application Support/Code/User/settings.json`; Linux: `~/.config/Code/User/settings.json`; Windows: `%APPDATA%\Code\User\settings.json`). Forks (e.g., VSCodium) use their vendor path under Application Support / `.config`.
2. **Identify setting** — Map user request to setting key (e.g., "bigger font" → `editor.fontSize`).
3. **Parse and update** — Handle JSON with comments; add or update requested setting; preserve all other settings.
4. **Validate** — Ensure valid JSON syntax before writing.
5. **Write** — Update settings file with proper formatting (2-space indentation).
6. **Inform user** — Confirm change; note if reload or restart needed.

### Common Setting Mappings

| User Request | Setting |
|--------------|---------|
| "bigger/smaller font" | `editor.fontSize` |
| "change tab size" | `editor.tabSize` |
| "format on save" | `editor.formatOnSave` |
| "word wrap" | `editor.wordWrap` |
| "change theme" | `workbench.colorTheme` |
| "hide minimap" | `editor.minimap.enabled` |
| "auto save" | `files.autoSave` |

### Important Notes

- **JSON with Comments:** VS Code supports `//` and `/* */`; preserve when possible.
- **Restart/Reload:** Some settings require reloading the window or restarting the editor.
- **Workspace vs User:** This skill covers user settings (global); workspace settings (`.vscode/settings.json`) are project-only.
- **Vendor-specific options:** Features not in stock VS Code may only be configurable via that product’s UI or separate config files; follow vendor documentation.

## Constraints

- **Trust Boundaries:** User input untrusted; validate setting keys and values. Safe: propose changes. Unsafe: settings.json writes—require user approval. Preserve existing settings: only add/modify what user requested.
- **Output Validation:** Validate JSON syntax before proposing. "These changes modify settings.json. Review before applying."
- **Limitations:** Paths and keys are VS Code–oriented; other editors use different config formats. Some options may require the vendor UI. JSON with comments; preserve comments when possible.
- **Safety Guardrails (Tier 2):** User approval required. Validate JSON before writing. Preserve existing settings; only modify requested key(s). Inform user if reload or restart needed.

## Examples

See [examples.md](examples.md) for example setting changes. Use [prompt-template.md](prompt-template.md) for structured invocation.

## Validation Checklist

- [ ] Confirm the setting path (user `settings.json` vs workspace `.vscode/settings.json`)
- [ ] Validate JSON syntax before writing
- [ ] Preserve existing settings; only modify the requested key(s)
- [ ] Inform user if reload or restart is needed

## Portability Notes

Settings paths and keys target VS Code and compatible editors. JetBrains, Sublime, and others use different config formats and locations.
