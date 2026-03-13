---
name: habitect
description: "Read, update, and sync the Habitect knowledge base — the single source of truth for personal knowledge, projects, people, and agents. Use when the user asks to update project info, check knowledge, sync across systems, or reference habitect."
argument-hint: "update voxforma | read projects | sync | status"
allowed-tools:
  - Read
  - Edit
  - Write
  - Glob
  - Grep
  - Bash(habitect-sync *)
  - Bash(ls *)
  - Bash(cat *)
---

# Habitect — Personal Knowledge Base

Single source of truth for all personal knowledge, agents, and tools.

## Location

- **Repo**: `/Users/china/codeDev/habitect` — GitHub: `github.com/cyu60/habitect`
- **Sync CLI**: `/opt/homebrew/bin/habitect-sync`

## Structure

```
habitect/
├── knowledge/
│   ├── personal/       # profile, goals, habits, values, preferences
│   ├── projects/       # mentormates.md, voxforma.md, daydreamers.md, habitect.md
│   ├── people/         # team, advisors, contacts
│   ├── resources/      # repos, accounts, tools, infrastructure
│   ├── skills/         # technical + non-technical
│   └── immigration/    # O-1 status, lawyers, evidence checklist
├── agents/             # agent configs (mirrors ~/.claude/skills/)
├── memory/             # mirrors claude memory files
├── snapshots/          # point-in-time backups
└── spec/               # system design docs
```

## Key Project Files

| Project | File | Description |
|---------|------|-------------|
| MentorMates | `knowledge/projects/mentormates.md` | Hackathon platform, team, architecture |
| VoxForma | `knowledge/projects/voxforma.md` | Founder Signal Report / Alpha Foundry / SF Demo Day form |
| Daydreamers | `knowledge/projects/daydreamers.md` | Workshop/course materials |
| Habitect | `knowledge/projects/habitect.md` | This knowledge base itself |

## Common Operations

### Read project info
```bash
cat /Users/china/codeDev/habitect/knowledge/projects/<project>.md
```

### Update project info
Edit the relevant file in `knowledge/projects/`.

### Sync across systems
```bash
habitect-sync              # Full sync: Notion ↔ Obsidian ↔ Apple Notes ↔ Calendar
habitect-sync --status     # Check sync status
habitect-sync --dry-run    # Preview what would sync
habitect-sync --add "task" # Add a task across all systems
```

### Keep in sync with Claude memory
When updating habitect knowledge files, also update the corresponding Claude memory file at:
`/Users/china/.claude/projects/-Users-china-codeDev-MentorMates/memory/`

Key mappings:
- `habitect/memory/MEMORY.md` ↔ Claude `memory/MEMORY.md`
- `habitect/memory/team-profiles.md` ↔ Claude `memory/team-profiles.md`
- `habitect/memory/notion-and-email.md` ↔ Claude `memory/notion-and-email.md`

### Push changes to GitHub
```bash
cd /Users/china/codeDev/habitect && git add -A && git commit -m "update: <description>" && git push
```

## Data Sources (Connected)

| Source | Access | Status |
|--------|--------|--------|
| Obsidian | Direct file read/write | Working |
| Notion | CLI at `/Users/china/codeDev/notion-management/bin/` | Working |
| Apple Notes | CLI at `/opt/homebrew/bin/notes` | Working |
| Gmail/Calendar | `gog` CLI | Working |
| Google Drive | `gog drive` | Working |
| Browser History | `~/.claude/skills/browser-history/bin/browser-export` | Working |
| iMessage | sqlite3 `~/Library/Messages/chat.db` | Working |
| WhatsApp | sqlite3 `~/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite` | Working |
| WeChat | sqlite3 `~/Library/Containers/com.tencent.xinWeChat/` | Partial |

## Communication Channels

For searching across all messaging platforms for contacts, leads, or past conversations:

```bash
# iMessage — search messages
sqlite3 ~/Library/Messages/chat.db "SELECT h.id, m.text, datetime(m.date/1000000000 + 978307200, 'unixepoch') FROM message m JOIN handle h ON m.handle_id = h.ROWID WHERE m.text LIKE '%SEARCH_TERM%' ORDER BY m.date DESC LIMIT 20;"

# WhatsApp — search messages
sqlite3 ~/Library/Group\ Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite "SELECT ZFROMJID, ZTEXT, datetime(ZMESSAGEDATE + 978307200, 'unixepoch') FROM ZWAMESSAGE WHERE ZTEXT LIKE '%SEARCH_TERM%' ORDER BY ZMESSAGEDATE DESC LIMIT 20;"

# Gmail — search via gog
gog gmail search "SEARCH_TERM" --max 20

# WeChat — check for accessible DB files
find ~/Library/Containers/com.tencent.xinWeChat/ -name "*.db" 2>/dev/null
```

### Key Notion DBs for DayDreamers

| Database | ID |
|----------|-----|
| DayDreamers Hub | `2f0ab088-064e-80d1-ae11-dff5a90723e0` |
| DayDreamers Tasks | `7c8ea482-2854-4783-8ba3-c62c100d9b35` |
| Leads Tracker | `54216c81-f4c6-45e0-b84f-a052d67af962` |
| Content Tracker | `6cbf7c77-bb6e-4a96-8761-f9ce06451124` |
| HK Hackathon Sponsor Tracker | `ede453ed-53c9-4c44-8604-0870f0ef711c` |

## Search Protocol

**IMPORTANT**: When the user asks to search for anything (contacts, leads, conversations, project info, etc.), launch **parallel sub-agents** to search ALL data sources simultaneously. Be thorough — don't miss any source. The user expects comprehensive results across every connected channel.

Launch agents in parallel for:
1. **Habitect knowledge files** — Grep/Read through `knowledge/` directory
2. **Notion** — Query relevant DBs (tasks, leads, content tracker, etc.)
3. **Gmail** — `gog gmail search`
4. **Calendar** — `gog calendar`
5. **iMessage** — sqlite3 query on `~/Library/Messages/chat.db`
6. **WhatsApp** — sqlite3 query on WhatsApp ChatStorage.sqlite
7. **Apple Notes** — `notes search`
8. **Browser History** — browser-export search
9. **Obsidian** — Grep through Obsidian vault

Each sub-agent should search its source independently and return findings. Combine all results into a unified response.

## Learning Loop

When a sweep misses something important and the user corrects it, update durable context in the same task when feasible:
- the relevant skill instructions
- Habitect memory files
- mirrored Claude memory files, if applicable

Examples that must be captured durably:
- new required inbox buckets
- corrected operating rules for daily digest / gameplan
- recurring miss patterns, such as not converting meeting-note promises into follow-ups
- Apple Notes capture patterns, such as `Todos` or conversation notes holding real action items
- task-hygiene rules, such as merging duplicates and separating watcher items from active work

Do not leave these corrections only in chat history.

## Task: $ARGUMENTS
