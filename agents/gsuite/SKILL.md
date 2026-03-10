---
name: gsuite
description: Read, send, and manage Gmail, Google Calendar, and Google Drive. Use when the user asks about emails, calendar events, meetings scheduling, or Google Drive files.
argument-hint: "[action like 'check email', 'list events', 'search drive'] or [search query]"
allowed-tools:
  - Bash(gog *)
  - Bash(/Users/china/codeDev/gsuite-tools/bin/*)
  - Bash(cd /Users/china/codeDev/gsuite-tools && *)
  - Read
  - Grep
---

# Google Workspace Integration

Use **gog** (gogcli) as the primary CLI for all Google Workspace operations. Fall back to gsuite-tools only if gog fails or lacks a specific feature.

## Primary CLI: gog (gogcli)

- **Binary**: `/opt/homebrew/bin/gog` (v0.12.0, installed via Homebrew)
- **Config**: `/Users/china/Library/Application Support/gogcli/config.json`
- **Auth**: Credentials stored in OS keyring (secure)
- **Docs**: https://github.com/steipete/gogcli

### Account Selection

Use `--account <email>` (or `-a <email>`) to select which Google account to use.

Default account: `chinatchinat123@gmail.com` (personal)

Known accounts:
| Account | Gmail | Calendar | Drive |
|---|---|---|---|
| `chinatchinat123@gmail.com` | OK | OK | OK |

> **Note**: gsuite-tools has additional profiles (mentormates, mentormates-official, mentormates-contact, stanford). If you need those accounts and they're not in gog yet, fall back to gsuite-tools or run `gog auth add` to add them.

### Gmail

```bash
# Search emails (Gmail query syntax)
gog gmail search "from:someone@example.com subject:meeting"
gog gmail search "newer_than:7d is:unread"

# Read a message
gog gmail get <messageId>

# Send email
gog gmail send --to user@example.com --subject "Hi" --body "Hello"
gog gmail send --to user@example.com --cc other@example.com --subject "Hi" --body "Hello"

# Reply to a message (threads correctly)
gog gmail send --reply-to-message-id <messageId> --to user@example.com --subject "Re: Topic" --body "Reply text"
gog gmail send --thread-id <threadId> --reply-all --subject "Re: Topic" --body "Reply text" --quote

# Drafts (create, list, send, update, delete)
gog gmail drafts create --to user@example.com --subject "Draft" --body "Content"
gog gmail drafts create --reply-to-message-id <messageId> --to user@example.com --subject "Re: Topic" --body "Reply" --quote
gog gmail drafts list
gog gmail drafts send <draftId>

# Attachments
gog gmail send --to user@example.com --subject "Files" --body "See attached" --attach file.pdf
gog gmail attachment <messageId> <attachmentId>

# Labels & Organization
gog gmail labels list
gog gmail archive <messageId>
gog gmail mark-read <messageId>
gog gmail trash <messageId>

# Open in browser
gog gmail url <threadId>
```

### Calendar

```bash
# List events (default: upcoming from all calendars)
gog calendar events
gog calendar events --from today --to +7d
gog calendar events --from 2026-03-10 --to 2026-03-17

# Search events
gog calendar search "team meeting"

# Create event
gog calendar create primary --summary "Meeting" --start 2026-03-15T10:00:00 --end 2026-03-15T11:00:00
gog calendar create primary --summary "Lunch" --start 2026-03-15T12:00:00 --description "At restaurant" --location "123 Main St"

# List calendars
gog calendar calendars

# Free/busy
gog calendar freebusy --from today --to +1d

# Conflicts
gog calendar conflicts

# RSVP
gog calendar respond <calendarId> <eventId> --status accepted
```

### Drive

```bash
# List files
gog drive ls
gog drive ls --folder <folderId>

# Search
gog drive search "project proposal"

# Download / Read
gog drive download <fileId>
gog drive get <fileId>

# Upload
gog drive upload file.pdf
gog drive upload file.pdf --parent <folderId>

# Sharing
gog drive share <fileId> --email user@example.com
gog drive permissions <fileId>

# Folders
gog drive mkdir "New Folder"
```

### Google Docs, Sheets, Slides, Forms, Contacts, Tasks

```bash
# Docs
gog docs get <docId>
gog docs export <docId> --format md
gog docs create --title "New Doc" --body "Content"

# Sheets
gog sheets read <sheetId>
gog sheets write <sheetId> --range "A1" --values '["hello","world"]'

# Contacts
gog contacts search "John"

# Tasks
gog tasks list
gog tasks create --title "Follow up"
```

### Output Modes

- Default — colored terminal output (human-readable)
- `--json` / `-j` — structured JSON (best for scripting/parsing)
- `--plain` / `-p` — tab-separated values
- `--results-only` — in JSON mode, omit pagination metadata
- `--select=field1,field2` — in JSON mode, select specific fields

### Useful Flags

- `-a <email>` / `--account <email>` — select Google account
- `-n` / `--dry-run` — preview without making changes
- `-y` / `--force` — skip confirmations
- `--no-input` — never prompt (useful for automation)

---

## Backup CLI: gsuite-tools (deprecated — use only as fallback)

- **Repo**: `/Users/china/codeDev/gsuite-tools`
- **Remote**: `https://github.com/cyu60/gsuite-tools` (branch: `master`)
- All tools at `/Users/china/codeDev/gsuite-tools/bin/`
- Uses `--profile <name>` for account selection (default: `personal`)

### Configured Profiles (gsuite-tools only)

| Profile | Account | Gmail | Calendar | Drive |
|---|---|---|---|---|
| `personal` | chinatchinat123@gmail.com | OK | OK | OK |
| `stanford` | Stanford email | Blocked | Blocked | OK |
| `mentormates` | MentorMates admin | OK | OK | OK |
| `mentormates-official` | Official MentorMates Gmail | OK | OK | OK |
| `mentormates-contact` | contact@mentormates.ai | OK | OK | OK |

### gsuite-tools Commands (quick reference)

```bash
# Gmail
/Users/china/codeDev/gsuite-tools/bin/gmail-list -n 10 --profile personal
/Users/china/codeDev/gsuite-tools/bin/gmail-list "from:someone@example.com" --profile personal
/Users/china/codeDev/gsuite-tools/bin/gmail-read <message-id> --profile personal
/Users/china/codeDev/gsuite-tools/bin/gmail-send --to user@example.com --subject "Hi" --body "Hello" --profile personal

# Calendar
/Users/china/codeDev/gsuite-tools/bin/calendar-list -d 14 --profile personal
/Users/china/codeDev/gsuite-tools/bin/calendar-create --summary "Meeting" --start "2026-03-15T10:00:00" --profile personal

# Drive
/Users/china/codeDev/gsuite-tools/bin/drive-list "query" --profile personal
/Users/china/codeDev/gsuite-tools/bin/drive-read <file-id> --profile personal
```

### Troubleshooting (gsuite-tools)

- **NOT_AUTHENTICATED**: Run `/Users/china/codeDev/gsuite-tools/bin/gsuite-auth --profile <name>`
- **Token expired**: Re-run `gsuite-auth`
- **Build needed**: `cd /Users/china/codeDev/gsuite-tools && npm run build`

---

## When to use which

| Scenario | Tool |
|---|---|
| Any Gmail/Calendar/Drive operation | `gog` (primary) |
| Need mentormates/stanford/contact profiles | gsuite-tools (has those profiles) |
| Docs, Sheets, Slides, Forms, Contacts, Tasks | `gog` (only option) |
| Drafts, reply threading, attachments | `gog` (better support) |
| `gog` errors or auth issues | gsuite-tools (fallback) |

## Task: $ARGUMENTS
