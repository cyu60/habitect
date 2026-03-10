---
name: tech-agenda
description: Generate and send the weekly Monday tech meeting agenda. Creates a Notion page with task overview from Dev Tasks Tracker and sends email to the dev team. Intended to run every Friday via cron.
argument-hint: "[--dry-run] [--no-email] [--no-notion] [--date YYYY-MM-DD]"
allowed-tools:
  - Bash(/Users/china/codeDev/notion-management/bin/tech-agenda*)
  - Bash(/Users/china/codeDev/notion-management/bin/notion-*)
  - Bash(cd /Users/china/codeDev/notion-management && *)
  - Read
  - Grep
  - CronCreate
  - CronDelete
  - CronList
---

# Tech Weekly Meeting Agenda Generator

Generates a Notion meeting page and emails the tech team for the upcoming Monday tech weekly.

## CLI Tool

```bash
/Users/china/codeDev/notion-management/bin/tech-agenda [flags]
```

### Flags
| Flag | Description |
|------|-------------|
| `--dry-run` | Preview only — no Notion page created, no emails sent |
| `--no-email` | Create Notion page but skip emails |
| `--no-notion` | Send emails but skip Notion page creation |
| `--date YYYY-MM-DD` | Override meeting date (default: next Monday) |

### What it does
1. Finds the last tech/dev meeting in Notion Meetings DB
2. Extracts unchecked action items (carried-over tasks)
3. Queries all open tasks from Dev Tasks Tracker DB
4. Groups tasks by: overdue, in-progress, due this week, upcoming
5. Builds a structured Notion page with task tables, team toggles, and linked DB reference
6. Sends branded HTML email to the tech team with task summary and Notion link

### Tech Team (email recipients)
- Chinat Yu: cyu60@alumni.jh.edu
- Jeffrey Zhou: jefferyzhouehs@gmail.com
- Jason (Jiaze) Ke: jasonkjz123@gmail.com
- Aurelia (Lia) Sindhu: aurelia.sindhu@gmail.com

### Scheduling via Cron
To set up the Friday cron job (runs every Friday at 10am):
```
CronCreate with cron: "0 10 * * 5" and prompt: "/tech-agenda"
```

## Task: $ARGUMENTS
