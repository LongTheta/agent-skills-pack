---
name: update-cursor-settings
risk_tier: 2
description: >-
  Modify Cursor/VSCode user settings in settings.json. Use when you want to
  change editor settings, preferences, configuration, themes, font size, tab
  size, format on save, auto save, keybindings, or any settings.json values.
---

# Update Cursor Settings

## Purpose

Modifies Cursor/VSCode user settings in settings.json. Changes themes, font size, tab size, format on save, keybindings, and other editor preferences. Tier 2: user approval required for settings.json writes; preserve existing settings; only add/modify what user requested.

## When to Use

- User wants to change editor settings, preferences, or configuration
- User asks about themes, font size, tab size, format on save, auto save, keybindings
- User wants to modify `settings.json` values
- User asks "how do I change X in Cursor" for editor/workbench settings

## Inputs

| Input | Description |
|-------|-------------|
| User's intent | Which setting to change (e.g., font size, theme, format on save) |
| Current settings path | Infer from OS if not provided |

## Outputs

- **Updated settings.json** — With requested change(s)
- **Confirmation** — Note if reload/restart required

## Steps / Behavior

1. **Read existing settings** — Use settings path for OS (macOS: `~/Library/Application Support/Cursor/User/settings.json`; Linux: `~/.config/Cursor/User/settings.json`; Windows: `%APPDATA%\Cursor\User\settings.json`).
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

- **JSON with Comments:** VSCode/Cursor supports `//` and `/* */`; preserve when possible.
- **Restart/Reload:** Some settings require reloading the window or restarting Cursor.
- **Workspace vs User:** This skill covers user settings (global); workspace settings (`.vscode/settings.json`) are project-only.
- **Commit Attribution:** For CLI agent, modify `~/.cursor/cli-config.json`; for IDE agent, use UI (Cursor Settings > Agent > Attribution), not settings.json.

## Constraints

- **Trust Boundaries:** User input untrusted; validate setting keys and values. Safe: propose changes. Unsafe: settings.json writes—require user approval. Preserve existing settings: only add/modify what user requested.
- **Output Validation:** Validate JSON syntax before proposing. "These changes modify settings.json. Review before applying."
- **Limitations:** Cursor/VSCode-specific; paths and settings differ for other editors. Some settings require UI (e.g., Agent Attribution); cannot modify via settings.json. JSON with comments; preserve comments when possible.
- **Safety Guardrails (Tier 2):** User approval required. Validate JSON before writing. Preserve existing settings; only modify requested key(s). Inform user if reload or restart needed.

## Examples

See [examples.md](examples.md) for example setting changes. Use [prompt-template.md](prompt-template.md) for structured invocation.

## Validation Checklist

- [ ] Confirm the setting path (settings.json vs cli-config.json vs UI)
- [ ] Validate JSON syntax before writing
- [ ] Preserve existing settings; only modify the requested key(s)
- [ ] Inform user if reload or restart is needed

## Portability Notes

Settings paths and keys are Cursor/VSCode-specific. Other editors (e.g., JetBrains, Sublime) use different config formats and locations.
