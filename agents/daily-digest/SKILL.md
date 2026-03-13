---
name: daily-digest
description: "Generate an evening daily digest summarizing calendar, emails, browser history, and Notion tasks. Outputs to Obsidian daily note, Notion page, and a styled email to yourself. Run at 9 PM daily via cron or on-demand."
argument-hint: "[--dry-run] [--date YYYY-MM-DD] [--skip-email] [--skip-notion] [--skip-obsidian]"
allowed-tools:
  - Bash(/Users/china/.claude/skills/daily-digest/bin/daily-digest *)
  - Bash(/Users/china/codeDev/gsuite-tools/bin/*)
  - Bash(/Users/china/codeDev/notion-management/bin/*)
  - Bash(/Users/china/.claude/skills/browser-history/bin/*)
  - Bash(gog *)
  - Bash(sqlite3 *)
  - Bash(python3 *)
  - Bash(date *)
  - Bash(/opt/homebrew/bin/notes *)
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Agent
---

# Daily Evening Digest — Wind-Down Pipeline

The evening digest is part of the nightly shutdown ritual. It runs after `/750-words` and before the low-stimulation buffer. The goal is to **close every loop from the day** so you can sleep with a clear mind.

**Key rule**: This is decompression, not another activation block. Keep outputs concise, actionable, and calming.

## Nightly Sequence

```
9:00 PM  — /750-words (write + reflect + extract tasks)
9:15 PM  — /daily-digest (this skill — full inbox sweep + digest)
9:30 PM  — /gameplan (tomorrow's plan, weekly arc)
9:45 PM  — Low-stimulation buffer (NO Claude Code, no phone scroll)
10:30 PM — Wind down
11:00 PM — Sleep
```

## Pipeline Steps

### Step 1: Check all events, clean up meeting notes

Review across Granola, Notion, and Voice memos.

#### 1a. Look at all inboxes

**Communication channels** (search ALL, not just default):
- **WhatsApp**: `sqlite3 ~/Library/Group\ Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite "SELECT ZFROMJID, ZTEXT, datetime(ZMESSAGEDATE + 978307200, 'unixepoch') FROM ZWAMESSAGE WHERE ZMESSAGEDATE > strftime('%s', 'now', '-1 day') - 978307200 ORDER BY ZMESSAGEDATE DESC LIMIT 50;"`
- **iMessages**: `sqlite3 ~/Library/Messages/chat.db "SELECT h.id, m.text, datetime(m.date/1000000000 + 978307200, 'unixepoch') FROM message m JOIN handle h ON m.handle_id = h.ROWID WHERE m.date > (strftime('%s', 'now', '-1 day') - 978307200) * 1000000000 ORDER BY m.date DESC LIMIT 50;"`
- **Emails** — across ALL accounts:
  - `gog gmail search "newer_than:1d" --account chinatchinat123@gmail.com --max 20`
  - `gog gmail search "newer_than:1d" --account chinat@stanford.edu --max 20`
  - `gog gmail search "newer_than:1d" --account contact@mentormates.ai --max 20`
  - `gog gmail search "newer_than:1d" --account admin@mentormates.ai --max 20`
  - `gog gmail search "newer_than:1d" --account official@mentormates.ai --max 20`

**Calendars** — across all accounts:
- `gog calendar list --from <today> --to <tomorrow> --account chinatchinat123@gmail.com`
- `gog calendar list --from <today> --to <tomorrow> --account chinat@stanford.edu`

**Drive files opened** — across all accounts:
- `gog drive recent --account chinatchinat123@gmail.com --max 10`

**Local computer files opened**:
- `mdfind 'kMDItemLastUsedDate >= $time.today' -onlyin /Users/china/ 2>/dev/null | head -30`

**Notion meeting notes from the day**:
- Chinat's personal meeting notes
- MentorMates Notes
- Stanford Founders Notes
- Daydreamers meeting notes
- Query via Notion CLI: `/Users/china/codeDev/notion-management/bin/`

#### 1b. For each, clean up and organise
- Clean up notes, emails, calendar events
- Organise each bucket
- Flag anything that needs a reply or follow-up

#### 1c. Convert promises into explicit follow-ups
- Review meeting notes, daily note captures, and 750 words for outbound promises:
  - `I'll send`
  - `I shared`
  - `I'll follow up`
  - `send the links`
  - `introduce`
  - `circle back`
  - `could you start`
- For each one, decide:
  - `Done`
  - `Do`
  - `Delegate`
  - `Defer`
  - `Drop`
- Do not let these sit as vague notes. Either route them into tomorrow's plan or mark them resolved.

#### 1d. Review Apple Notes as a required bucket
- Run:
  - `notes recent 20`
  - `notes list "Todos & Gameplans"`
  - `notes list "Conversations"`
  - `notes search "todo"`
  - targeted `notes read-id ...` for anything modified today
- Treat Apple Notes captures as first-class inputs for triage, especially TODO lists, conversation notes, and quick captures from the same day

### Step 2: Check Claude Code + Codex conversation logs

- Claude Code logs: `~/.claude/projects/` JSONL files
- Codex logs: `~/.codex/sessions/` and `~/.codex/archived_sessions/` JSONL files
- Review the full target-day transcripts, not just the current chat window
- Extract user messages to see what was actually asked/built
- Cross-reference with morning gameplan to assess planned vs. actual

Add a short `AI Session Summary` to the daily note:
- total sessions reviewed
- `Claude Code` count
- `Codex` count
- main topics discussed

### Step 3: Extract all action items into a list

- Combine tasks from: emails, messages, meeting notes, Claude Code sessions, Codex sessions, 750 words
- Review what has been done vs. not done
- Present the full list to the user for review
- Update `### Also on your plate` in the daily note
- Merge duplicate tasks before presenting them
- Separate watcher items from tasks that genuinely require Chinat's time tomorrow
- Prefer a short, real list over a noisy exhaustive list

### Step 4: Update today's Obsidian daily note

Fill in the `## EVENING DIGEST` section:

```markdown
## EVENING DIGEST

### What was actually worked on?
[Summary of actual work done, from Claude Code logs + calendar + notes]

### AI Session Summary
- Total sessions reviewed: [N]
- Claude Code: [N]
- Codex: [N]
- Main topics: [short bullets]

### Which inbox items got cleared?
[List of emails replied to, messages answered, tasks completed]

### What slipped, and why?
[Honest assessment of what didn't happen and the real reason]

### What needs to move to Thursday?
[Carry-forward items with context]
```

Also:
- Add photos from iPhone (if available — check recent photos in `~/Library/Photos/`)
- Add interesting quotes/conversations from the day
- Add gratitude items

### Step 5: Show plan for tomorrow

- Remind of the bigger picture / mission (read from Obsidian quarterly goals)
- Look at Calendar events for tomorrow
- List out tasks to carry forward
- This feeds into `/gameplan` which runs next

### Step 6: Show plan for the week

- How tomorrow connects to the weekly arc
- Reference quarterly goals at `/Users/china/Desktop/Obsidian/Chinat's Notes/Reviews/2026 Plan.md`

### Step 7: Send report via email

- Send evening digest email to self (chinatchinat123@gmail.com) via `gog gmail send`
- Optionally send a shorter update to family (mom, sister, brother) — ask user first

## iMessage Sync (runs as part of digest)

```bash
python3 /Users/china/codeDev/habitect/bin/sync-imessages.py
```
Exports to `/Users/china/codeDev/habitect/knowledge/communications/`:
- `imessage-contacts.md` — contact index with message stats
- `imessage-archive.jsonl` — full searchable message archive
- `imessage-groups.md` — group chat membership
Supports incremental sync (only new messages after first run).

## Output Destinations

| Destination | Format |
|-------------|--------|
| Obsidian | Fills in `## EVENING DIGEST` in today's `Daily Notes/<date>.md` |
| Notion | Creates a page in the Meetings DB with calendar + browser data |
| Email | Summary email to chinatchinat123@gmail.com via `gog gmail send` |
| Family email | Optional shorter update to family members |

## Usage

```bash
# Run the full digest (all outputs)
/Users/china/.claude/skills/daily-digest/bin/daily-digest

# Dry run (terminal only, no email/notion/obsidian)
/Users/china/.claude/skills/daily-digest/bin/daily-digest --dry-run

# Run for a specific date
/Users/china/.claude/skills/daily-digest/bin/daily-digest --date 2026-03-09

# Skip specific outputs
/Users/china/.claude/skills/daily-digest/bin/daily-digest --skip-email
/Users/china/.claude/skills/daily-digest/bin/daily-digest --skip-notion
/Users/china/.claude/skills/daily-digest/bin/daily-digest --skip-obsidian
```

## Cron Schedule

Runs daily at 9 PM PT:
```
0 21 * * * /Users/china/.claude/skills/daily-digest/bin/daily-digest
```

## Key Paths

- Script: `/Users/china/.claude/skills/daily-digest/bin/daily-digest`
- Obsidian vault: `/Users/china/Desktop/Obsidian/Chinat's Notes/Daily Notes/`
- Obsidian quarterly goals: `/Users/china/Desktop/Obsidian/Chinat's Notes/Reviews/2026 Plan.md`
- Notion Meetings DB: `255ab088-064e-800e-b27d-f9bf93741625`
- Email recipient: chinatchinat123@gmail.com
- Uses `gog` CLI for Gmail/Calendar (not gsuite-tools)
- gog accounts: chinatchinat123@gmail.com, chinat@stanford.edu, contact@mentormates.ai, admin@mentormates.ai, official@mentormates.ai
- Claude Code logs: `~/.claude/projects/` (JSONL files)
- WhatsApp DB: `~/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite`
- iMessage DB: `~/Library/Messages/chat.db`
- Browser export: `~/.claude/skills/browser-history/bin/browser-export`

## Task: $ARGUMENTS
