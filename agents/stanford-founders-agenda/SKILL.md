---
name: stanford-founders-agenda
description: Generate and send the weekly Stanford Founders meeting agenda. Creates a Notion page with Demo Day workstream updates, open tasks, dinner leads, and upcoming events, then sends personalized prep emails to each core team member. Run every Saturday via cron or on-demand.
argument-hint: "[--dry-run] [--no-email] [--no-notion] [--date YYYY-MM-DD]"
allowed-tools:
  - Bash(/Users/china/codeDev/notion-management/bin/stanford-founders*)
  - Bash(/Users/china/codeDev/notion-management/bin/notion-*)
  - Bash(cd /Users/china/codeDev/notion-management && *)
  - Read
  - Grep
  - CronCreate
  - CronDelete
  - CronList
---

# Stanford Founders Weekly Agenda Generator

Generates a Notion meeting page and sends personalized prep emails to the Stanford Founders core team for the upcoming Monday meeting.

## CLI Tools

```bash
# Full pipeline: Notion page + personalized emails
/Users/china/codeDev/notion-management/bin/stanford-founders-agenda [flags]

# Emails only (called by stanford-founders-agenda, or standalone)
/Users/china/codeDev/notion-management/bin/stanford-founders-emails [flags]
```

### Flags
| Flag | Description |
|------|-------------|
| `--dry-run` | Preview only — no Notion page, no emails sent (saves HTML previews to /tmp/) |
| `--no-email` | Create Notion page but skip emails |
| `--no-notion` | Send emails but skip Notion page creation |
| `--date YYYY-MM-DD` | Override meeting date (default: next Monday) |
| `--notion-url URL` | (emails script) Include this Notion page link in emails |

### Full Pipeline
1. Queries last Stanford Founders weekly sync for carried-over action items
2. Queries open tasks from Stanford Founders Task Tracker (grouped by priority)
3. Queries upcoming events from Event Tracker
4. Queries dinner/sponsorship leads from Dinner Lead Tracker
5. Builds structured agenda in Notion with 🚀 icon:
   - Demo Day countdown
   - Workstream updates (Startup Selection, Marketing, Sponsorship/Speakers/Logistics)
   - Task review by priority
   - Dinner series & sponsorship pipeline
   - Upcoming events & HK opportunities
6. Sends **personalized prep emails** to each core team member with:
   - Their specific tasks by role/workstream
   - Discussion topics to prepare
   - Carried-over items mentioning them
   - "Before the Meeting" checklist: Progress / Next Steps / Blockers
   - Demo Day countdown
   - Direct Notion meeting page link
7. Rate-limited at 0.6s between sends (Resend: 2 req/sec)

### Core Team (email recipients)
| Name | Role | Workstreams |
|------|------|-------------|
| Jenny | CO (Lead) | General |
| Chinat | VP of Education | Startup Selection, Sponsorship, Accelerator |
| Advit | Events & Sponsors | Startup Selection, Sponsorship |
| Kristi | VP of Healthcare | Startup Selection |
| Arthur | Communities | Investor Relations |
| Deonna | VP of AI | Logistics |
| Yash | VP of Fintech | Marketing |
| Coco | Events | Marketing |
| Francesco | Deep Tech & Aerospace | Speakers & Panels |

**Note:** Most team emails are not yet configured in the script. Add emails to `stanford-founders-emails` as you collect them.

### Key Notion IDs
- Stanford Founders Hub: `2a8db4d6-e341-40f2-96ee-bb903c4b83a8`
- Meeting Tracker DB: `0de42092-2d9d-48dc-988c-f88f69e06a71`
- Task Tracker DB: `886dd2f7-37c1-49a8-8bd5-be5ddce850fe`
- Event Tracker DB: `6a02c56f-2e4b-4394-a070-a59a5f4c8378`
- Dinner Lead Tracker DB: `509223e0-acbb-4094-9480-a67707add08d`
- People DB: `aeb8b3a6-e45d-4d33-9c1c-a9a9ad5ecf6b`
- Meeting icon: 🚀

## Scheduling via Cron

### Session cron (Claude Code — ephemeral, 3-day max)
```
CronCreate with cron: "0 10 * * 6" and prompt: "Run /Users/china/codeDev/notion-management/bin/stanford-founders-agenda"
```

### System crontab (persistent)
```bash
# Add to crontab -e:
0 10 * * 6 /Users/china/codeDev/notion-management/bin/stanford-founders-agenda >> /tmp/stanford-founders-agenda.log 2>&1
```

## Previewing Emails
```bash
# Dry run generates HTML previews at /tmp/sf-email-preview-{name}.html
stanford-founders-agenda --dry-run

# Open in browser to review
open /tmp/sf-email-preview-chinat.html
```

## Linked GitHub Repository
- **Local**: `/Users/china/codeDev/notion-management`
- **Remote**: `https://github.com/cyu60/notion-management.git` (branch: `master`)

## Task: $ARGUMENTS
