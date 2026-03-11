# Scheduled Jobs (Cron)

All managed via system crontab (`crontab -e` to edit, `crontab -l` to list).

## Active Jobs

| Job | Schedule | Script | Log | Added |
|-----|----------|--------|-----|-------|
| Tech Weekly Agenda | Fri 10:03am | `/Users/china/codeDev/notion-management/bin/tech-agenda` | `/tmp/tech-agenda.log` | 2026-03-09 |
| Marketing Agenda | Sun 10:03am | `/Users/china/codeDev/notion-management/bin/marketing-agenda` | `/tmp/marketing-agenda.log` | 2026-03-09 |
| Apple Notes Sync | Daily 11:00pm | `/Users/china/codeDev/apple-notes-backup/bin/sync` | `apple-notes-backup/logs/` | 2026-03-10 |

## What Each Job Does

### Tech Weekly Agenda (Friday → Monday meeting)
- Queries Dev Tasks Tracker for all open tasks
- Reads last tech meeting for carried-over action items
- Creates Notion page in Meetings DB with task overview, team toggles, agenda
- Emails: Chinat, Jeffrey, Jason, Leah
- Flags: `--dry-run`, `--no-email`, `--no-notion`, `--date YYYY-MM-DD`

### Marketing Agenda (Sunday → Tuesday meeting)
- Reads last marketing meeting for carried-over action items
- Creates Notion page with agenda sections
- Emails: Josie, Britney, Catherine, Leah, Chinat
- Flags: `--dry-run`, `--no-email`, `--no-notion`, `--date YYYY-MM-DD`

### Apple Notes Sync (Daily at 11 PM)
- Exports all Apple Notes to markdown files organized by folder
- Commits changes to git with stats (new/modified/deleted)
- Pushes to `github.com/cyu60/apple-notes-backup` (private)
- Managed via launchd: `com.chinat.apple-notes-sync`
- Manual run: `/Users/china/codeDev/apple-notes-backup/bin/sync`
- Flags: `--no-push`, `--force`

## Management Commands

```bash
crontab -l              # List all jobs
crontab -e              # Edit jobs (opens in $EDITOR)
cat /tmp/tech-agenda.log      # Check tech agenda logs
cat /tmp/marketing-agenda.log # Check marketing agenda logs
```

## Notes
- Only runs when Mac is on and awake at scheduled time
- If missed, run manually: `/Users/china/codeDev/notion-management/bin/tech-agenda`
- Consider GitHub Actions migration for cloud reliability
