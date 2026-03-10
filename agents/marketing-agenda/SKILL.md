---
name: marketing-agenda
description: Generate and send the weekly Tuesday marketing meeting agenda. Creates a Notion page with carried-over action items and sends personalized prep emails to each team member. Run every Sunday via cron or on-demand.
argument-hint: "[--dry-run] [--no-email] [--no-notion] [--date YYYY-MM-DD]"
allowed-tools:
  - Bash(/Users/china/codeDev/notion-management/bin/marketing-agenda*)
  - Bash(/Users/china/codeDev/notion-management/bin/notion-*)
  - Bash(cd /Users/china/codeDev/notion-management && *)
  - Read
  - Grep
  - CronCreate
  - CronDelete
  - CronList
---

# Marketing Meeting Agenda Generator

Generates a Notion meeting page and sends personalized prep emails to the marketing team for the upcoming Tuesday meeting.

## CLI Tools

```bash
# Full pipeline: Notion page + personalized emails
/Users/china/codeDev/notion-management/bin/marketing-agenda [flags]

# Emails only (called by marketing-agenda, or standalone)
/Users/china/codeDev/notion-management/bin/marketing-agenda-emails [flags]
```

### Flags
| Flag | Description |
|------|-------------|
| `--dry-run` | Preview only — no Notion page, no emails sent (saves HTML previews to /tmp/) |
| `--no-email` | Create Notion page but skip emails |
| `--no-notion` | Send emails but skip Notion page creation |
| `--date YYYY-MM-DD` | Override meeting date (default: next Tuesday) |
| `--notion-url URL` | (emails script) Include this Notion page link in emails |

### Full Pipeline
1. Queries last marketing meeting from Notion Meetings DB for carried-over action items
2. Builds structured agenda (Updates, Overdue Tasks, Content Status, User Testing, Events, Open Discussion)
3. Creates Notion page with 📣 icon, toggle blocks per person, and Marketing tag
4. Sends **personalized prep emails** to each team member with:
   - Their specific tasks and action items based on role
   - Discussion topics to prepare for
   - Carried-over items mentioning them specifically
   - "Before the Meeting" checklist: **Done / In Progress / Blockers**
   - Direct Notion meeting page link
   - Link to [Sales & Marketing Tasks Tracker](https://www.notion.so/chinat/2c7ab088064e80c0b6a6d87163275c57?v=2c7ab088064e801993a7000c56b3ba7b) for corrections
5. Rate-limited at 0.6s between sends (Resend: 2 req/sec)

### Marketing Team (email recipients)
| Name | Email | Role |
|------|-------|------|
| Josie Trinh | trinhthucthaonghi@gmail.com | Marketing Lead |
| Kathryn (Catherine) Tanardy | ktanardy@gmail.com | Content Creator & User Testing Lead |
| Britney Budiman | britney.budiman@gmail.com | Social Media & Content Creator |
| Aurelia (Lia) Sindhu | aurelia.sindhu@gmail.com | Software Engineer & UX/UI Designer |
| Chinat Yu | cyu60@alumni.jh.edu | Founder & CEO |

### Key Notion IDs
- Meetings DB: `255ab088-064e-800e-b27d-f9bf93741625`
- Sales & Marketing Tasks Tracker: `2c7ab088064e80c0b6a6d87163275c57`
- Meeting icon: 📣

## Scheduling via Cron

### Session cron (Claude Code — ephemeral, 3-day max)
```
CronCreate with cron: "3 10 * * 0" and prompt: "Run /Users/china/codeDev/notion-management/bin/marketing-agenda"
```

### System crontab (persistent)
```bash
# Add to crontab -e:
3 10 * * 0 /Users/china/codeDev/notion-management/bin/marketing-agenda >> /tmp/marketing-agenda.log 2>&1
```

## Previewing Emails
```bash
# Dry run generates HTML previews at /tmp/email-preview-{name}.html
marketing-agenda --dry-run

# Open in browser to review
open /tmp/email-preview-josie.html
```

## Linked GitHub Repository
- **Local**: `/Users/china/codeDev/notion-management`
- **Remote**: `https://github.com/cyu60/notion-management.git` (branch: `master`)

## Task: $ARGUMENTS
