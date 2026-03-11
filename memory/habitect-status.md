# Habitect Status

## What It Is
- Single source of truth for all personal knowledge, agents, and tools
- Repo: `/Users/china/codeDev/habitect` — GitHub: `github.com/cyu60/habitect` (public)

## Current State (2026-03-10)

### Knowledge Base (`knowledge/`)
- `personal/` — profile, goals, habits, values, preferences
- `projects/` — mentormates, voxforma, daydreamers, habitect
- `people/` — team, advisors, contacts
- `resources/` — repos, accounts, tools, infrastructure
- `skills/` — technical + non-technical
- `immigration/` — O-1 status, lawyers, evidence checklist, timeline

### Agents (`agents/`)
- apple-notes, browser-history, daily-digest, daydreamers-content, gameplan, gsuite, image-gen, marketing-agenda, notion, tech-agenda, todo

### Data Sources & Sync
| Source | Role | Sync | Status |
|--------|------|------|--------|
| Obsidian | Deep thinking, goals, reflections | Read by gameplan/digest agents | Working |
| Notion | Work/team tasks, meetings | CLI tools (real-time) | Working |
| Apple Notes | Personal/ad hoc/mobile capture | Daily GitHub backup 11 PM (launchd) | Working |
| Gmail/Calendar | Communication, schedule | gog CLI (real-time) | Working |
| Google Drive | Documents, files, pitch decks | `gog drive ls/search/read` | Working — not yet in sync agent |
| Browser History | Productivity patterns | browser-export CLI | Working |
| iMessage | Personal conversations | AppleScript (list chats works) | Partial — sqlite needs Full Disk Access |
| WhatsApp | Messaging (221MB ChatStorage.sqlite) | sqlite3 direct query | Working — columns: ZFROMJID, ZTOJID, ZTEXT, ZMESSAGEDATE |
| WeChat | Messaging (10 msg DBs) | SQLCipher encrypted | Blocked — DBs encrypted, need decryption key |
| Apple Health | Fitness/activity from Apple Watch | Export XML or HealthKit shortcuts | Not yet set up |
| Location (FindMy) | iPhone location data | FindMy/Shortcuts | Not yet set up |

### Data Source Access Details
- **Google Drive**: `gog drive ls/search/read`. Reorganized into 13 folders (Career, Immigration, Stanford, MentorMates-Edumame, DayDreamers, Presentations, Creative, Business, Research, Media, Personal, Forms, Archive). Snapshot at `habitect/snapshots/gdrive/2026-03-10-manifest.json`.
- **iMessage**: AppleScript `tell application "Messages" to get the name of every chat` works. Direct sqlite (`~/Library/Messages/chat.db`) needs Full Disk Access.
- **WhatsApp**: `sqlite3 ~/Library/Group\ Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite`. Key columns: `ZFROMJID`, `ZTOJID`, `ZTEXT`, `ZMESSAGEDATE` (add 978307200 for unix epoch), `ZISFROMME`, `ZCHATSESSION`. Tested successfully.
- **WeChat**: Data at `~/Library/Containers/com.tencent.xinWeChat/Data/.../Message/msg_0.db` through `msg_9.db`. All DBs encrypted with SQLCipher. Contact DB also encrypted. Need decryption key (derived from wxid or memory dump).
- **Apple Health**: Export via Health app → XML, or use Shortcuts automation. Could use `healthkit-to-sqlite`.
- **Location**: FindMy doesn't expose API directly. Options: Shortcuts automation, or `findmy` Python library.

### Mnemo Architecture (Product Vision)
- **Input**: Extensible ingestion layer — any data source can be plugged in (waterfall: direct API → CLI tool → Browser Use → Computer Use)
- **View**: `knowledge/INDEX.md` — universal cross-reference mapping all info to 7 life domains (Ventures, Career, Academic, Creative, Operations, Personal, Communication)
- **Actuator**: MCP integration, SKILL.md portable agent files, `habitect-sync` CLI, shareable context bundles
- Notion page: `30bab088064e8053815cc5b7a72174b3` (Mnemo spec)

### Apple Notes Backup
- Repo: `cyu60/apple-notes-backup` (private)
- CLI: `/opt/homebrew/bin/notes`
- Export script: batched Python (20 notes/batch), handles 1773+ notes
- Cron: daily 11 PM via launchd (`com.chinat.apple-notes-sync`)
- Initial export: running (202/1773 as of setup)

### Sync Agent
- CLI: `habitect-sync` (`/opt/homebrew/bin/habitect-sync`)
- Source: `/Users/china/tools/habitect-sync/bin/sync-sources`
- Commands: `--status`, `--dry-run`, `--add "task"`, (default: full sync)
- Syncs: Notion tasks ↔ Obsidian daily notes ↔ Apple Notes Todo ↔ Apple Calendar
- Notion uses CLI tool for auth, parses text output for task names/status/priority/due
- Calendar reads via `gog calendar events` with AppleScript fallback

### Pending
- Angela Mapa email draft ready to send (O-1 refile response)
- Apple Notes initial export still completing (big "Notes" folder with 1449 notes not yet exported)
- Consider adding sync as daily cron (after Apple Notes sync at 11 PM)
- Integrate Google Drive into sync agent
- Build iMessage reader (AppleScript-based, since sqlite blocked)
- Fix WhatsApp sqlite query (check `.schema ZWAMESSAGE` for correct columns)
- Investigate Apple Health data export (HealthKit XML or Shortcuts)
- Investigate FindMy/Location data access
