---
name: apple-notes
description: Search, read, create, and manage Apple Notes. Also syncs notes to GitHub daily. Use when the user asks about their Apple Notes, wants to create/find/read notes, or manage the GitHub backup.
argument-hint: "[action like 'search hackathon', 'read Todo', 'create note', 'sync'] or [search query]"
allowed-tools:
  - Bash(/Users/china/tools/apple-notes/bin/notes *)
  - Bash(/Users/china/codeDev/apple-notes-backup/bin/*)
  - Bash(notes *)
  - Read
  - Grep
---

# Apple Notes Integration

Access Apple Notes via CLI and maintain a GitHub backup.

## CLI Tool: `notes`

**Binary**: `/Users/china/tools/apple-notes/bin/notes` (also at `/opt/homebrew/bin/notes`)

### Commands

```bash
# List & Browse
notes list                    # List all note titles (ID, title, modified date)
notes list "Meetings"         # List notes in a specific folder
notes folders                 # List all folders with note counts
notes recent 10               # Show 10 most recent notes
notes count                   # Total note count

# Read
notes read "Todo"             # Read note by exact title (shows #1 if duplicates)
notes read "Todo" 2           # Read 2nd note with that title
notes read-id "<note-id>"     # Read by Apple Notes ID

# Search
notes search "hackathon"      # Search by title and content

# Create & Edit
notes create "Title" "Body"   # Create note in default folder
notes create-in "Work" "Title" "Body"  # Create in specific folder
echo "content" | notes create "Title"  # Create with piped content
notes append "Todo" "- New item"       # Append text to existing note

# Delete
notes delete "Note Title"     # Move note to trash
```

### Notes about Duplicate Titles

Many notes share the same title (e.g., multiple "Todo" notes). When reading:
- `notes read "Todo"` shows the most recent one and lists all matches with IDs
- `notes read "Todo" 2` reads the second match
- Use `notes read-id <id>` for exact targeting

## GitHub Backup

**Repo**: `/Users/china/codeDev/apple-notes-backup` — GitHub: `github.com/cyu60/apple-notes-backup` (private)

### Structure
```
apple-notes-backup/
├── bin/
│   ├── export-notes    # Python script: exports all notes to markdown
│   └── sync            # Bash script: export → git commit → push
├── notes/              # Exported notes organized by folder
│   ├── Notes/          # Default folder (largest)
│   ├── Meetings/
│   ├── Poems/
│   └── ...
├── manifest.json       # Export metadata (count, timestamp, folders)
└── logs/               # Sync logs (gitignored)
```

### Sync Commands

```bash
# Full sync: export all notes → commit → push
/Users/china/codeDev/apple-notes-backup/bin/sync

# Sync without pushing
/Users/china/codeDev/apple-notes-backup/bin/sync --no-push

# Export only (no git operations)
/Users/china/codeDev/apple-notes-backup/bin/export-notes
```

### Cron Schedule

Runs daily at 11 PM via launchd (`com.chinat.apple-notes-sync`).

## Key Folders

| Folder | Notes | Description |
|--------|-------|-------------|
| Notes | ~1449 | Default / uncategorized |
| Iphone 6 | 118 | Old phone notes |
| Poems | 71 | Poetry |
| Meetings | 32 | Meeting notes |
| Podcast Notes | 28 | Podcast summaries |
| Emails | 10 | Email drafts |
| Idea backlog | 10 | Ideas |

## Task: $ARGUMENTS
