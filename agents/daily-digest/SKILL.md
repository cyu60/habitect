---
name: daily-digest
description: "Generate an evening daily digest summarizing calendar, emails, browser history, and Notion tasks. Outputs to Obsidian daily note, Notion page, and a styled email to yourself. Run at 9 PM daily via cron or on-demand."
argument-hint: "[--dry-run] [--date YYYY-MM-DD] [--skip-email] [--skip-notion] [--skip-obsidian]"
allowed-tools:
  - Bash(/Users/china/.claude/skills/daily-digest/bin/daily-digest *)
  - Bash(/Users/china/codeDev/gsuite-tools/bin/*)
  - Bash(/Users/china/codeDev/notion-management/bin/*)
  - Bash(/Users/china/.claude/skills/browser-history/bin/*)
  - Read
  - Grep
---

# Daily Evening Digest

Generates a comprehensive daily summary by pulling data from all your tools, then outputs to three destinations.

## Data Sources

| Source | What it pulls |
|--------|--------------|
| Google Calendar | Today's events via `gog` (personal account) |
| Gmail | Recent emails via `gog` from personal, stanford, mentormates-contact |
| Browser History | Activity recap, category breakdown, searches, digital hygiene signals |
| Notion | In-progress dev tasks, today's meeting notes |

## Output Destinations

| Destination | Format |
|-------------|--------|
| Obsidian | Appends to/creates `Daily Notes/<date>.md` in the vault |
| Notion | Creates a page in the Meetings DB with calendar + browser data |
| Email | Styled HTML email to chinatchinat123@gmail.com (MentorMates design) |

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
- Notion Meetings DB: `255ab088-064e-800e-b27d-f9bf93741625`
- Email recipient: chinatchinat123@gmail.com
- Uses `gog` CLI for Gmail/Calendar (not gsuite-tools)
- gog accounts: chinatchinat123@gmail.com, chinat@stanford.edu, contact@mentormates.ai

## Task: $ARGUMENTS
