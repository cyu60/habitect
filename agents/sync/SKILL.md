# Habitect Sync Agent

Keeps Notion tasks, Obsidian daily notes, Apple Notes todos, and Apple Calendar events in sync.

## CLI

```bash
# Full sync: read all sources, reconcile, write back
habitect-sync

# Show current state across all sources (no changes)
habitect-sync --status

# Preview what would change
habitect-sync --dry-run

# Add a task to ALL sources (Notion, Obsidian, Apple Notes)
habitect-sync --add "Task description"
```

## What It Syncs

| From | To | What |
|------|-----|------|
| Notion (High/Medium tasks due today/tomorrow) | Obsidian + Apple Notes | Task titles |
| Apple Notes Todo items | Obsidian | Task titles |
| Apple Calendar events | Obsidian daily notes | Calendar section |
| `--add` command | Notion + Obsidian + Apple Notes | New task everywhere |

## Source Locations
- **Notion**: Dev Tasks Tracker DB
- **Obsidian**: `daily-notes/YYYY-MM-DD.md` in vault
- **Apple Notes**: Most recent "Todo" note
- **Calendar**: via `gog calendar events` + AppleScript fallback

## Binary
- CLI: `/Users/china/tools/habitect-sync/bin/sync-sources`
- Symlink: `/opt/homebrew/bin/habitect-sync`
