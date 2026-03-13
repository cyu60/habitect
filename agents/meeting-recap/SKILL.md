---
name: meeting-recap
description: Post-meeting cleanup, task extraction, and personalized recap email distribution for any Notion-based meeting. Use when the user asks to recap a meeting, clean up a meeting page, extract action items, create follow-up tasks, or send attendee recap emails.
---

# Meeting Recap Skill

Post-meeting cleanup, task extraction, and personalized email distribution for any Notion-based meeting.

## What it does

1. **Reads** the meeting page from Notion (by ID, URL, or search term)
2. **Cleans up** the page — sets icon, fills missing properties (Event Type, Tags, POC)
3. **Extracts action items** from the transcription's "Action Items" section
4. **Creates tasks** in the appropriate tracker DB (1 task per action item)
5. **Sends personalized recap emails** to attendees with: their action items highlighted, discussion summary, all action items, and Notion link

## CLI

```bash
/Users/china/codeDev/notion-management/bin/meeting-recap <page-id|url|search> [options]
```

### Options

| Flag | Description |
|------|-------------|
| `--type TYPE` | Meeting type: `marketing`, `tech`, `stanford-founders`, `daydreamers`, `generic`. Auto-detected from tags if omitted. |
| `--dry-run` | Preview all actions without making changes |
| `--no-email` | Skip sending recap emails |
| `--no-tasks` | Skip creating tasks in tracker |
| `--no-cleanup` | Skip page cleanup (icon, properties) |
| `--skip NAMES` | Comma-separated names to skip in emails (e.g., `--skip Chinat,Lia`) |

### Meeting Types

| Type | Icon | Task Tracker | Attendees |
|------|------|-------------|-----------|
| `marketing` | 📣 | Sales & Marketing Tasks (`2c7ab088...`) | Josie, Catherine, Brittany, Lia, Chinat |
| `tech` | 💻 | Dev Tasks (`255ab088...`) | Chinat, Jeffrey, Jason, Leah |
| `stanford-founders` | 🎓 | (not configured) | (not configured) |
| `daydreamers` | 🌟 | (not configured) | (not configured) |
| `generic` | 📝 | (none) | (none) |

### Examples

```bash
# Full recap for latest marketing meeting
meeting-recap 31fab088-064e-8121-be6b-f501b3d39be2 --type marketing --skip Chinat

# Dry run on a tech meeting (auto-detect type from tags)
meeting-recap "Tech Weekly March 7" --dry-run

# Just create tasks, no email
meeting-recap <page-id> --no-email

# Just send emails, no tasks or cleanup
meeting-recap <page-id> --no-tasks --no-cleanup
```

## How to invoke

When the user says things like:
- "recap the marketing meeting" / "send the meeting recap"
- "clean up the meeting page and send emails"
- "process the [meeting type] meeting"
- "extract action items from the meeting and add to tracker"

### Steps

1. Identify the meeting page — ask for the page ID/URL or search by title
2. Determine meeting type (or let auto-detect handle it)
3. Ask if anyone should be skipped from emails
4. Run: `meeting-recap <page-id> [--type TYPE] [--skip NAMES]`
5. Optionally do a `--dry-run` first if the user wants to preview

## Requirements

- `NOTION_TOKEN` in `/Users/china/codeDev/notion-management/.env`
- `RESEND_API_KEY` in `/Users/china/codeDev/MentorMates/.env.local`
- Notion CLI tools at `/Users/china/codeDev/notion-management/bin/`

## Extending

To add a new meeting type, edit the `MEETING_TYPES` dict in the script:
- Add icon, event_type, tags, tracker_db, attendees, gradient
- The tracker properties (title prop, status prop, etc.) default to the Sales & Marketing Tasks schema

To add new team members, update the `attendees` dict for the relevant meeting type and add their Notion user ID to `NOTION_USER_IDS` if known.
