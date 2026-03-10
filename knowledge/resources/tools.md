# Tools & Dev Environment

## Machine
- macOS (Darwin 25.2.0)
- Shell: zsh
- Python: 3.9 (miniforge3)
- Node.js: installed
- Package managers: Homebrew, npm, bun

## Claude Code Skills (Agents)
All skills at `~/.claude/skills/<name>/SKILL.md`:

| Skill | Trigger | Description |
|-------|---------|-------------|
| `/notion` | Notion questions | Search, read, create Notion content |
| `/gsuite` | Email/calendar/drive | Gmail, Calendar, Drive via gog CLI |
| `/apple-notes` | Apple Notes | Search, read, create notes + GitHub backup |
| `/daily-digest` | Evening digest | Calendar + email + browser → Obsidian + Notion + email |
| `/gameplan` | Tomorrow's plan | Goals + tasks + browser hygiene analysis |
| `/todo` | Task routing | Parse intent, route to Notion/Obsidian/memory |
| `/marketing-agenda` | Marketing prep | Tuesday meeting agenda → Notion + email |
| `/tech-agenda` | Tech prep | Monday meeting agenda → Notion + email |
| `/browser-history` | Browsing analysis | Digital hygiene, search history, recaps |
| `/daydreamers-content` | Content gen | LinkedIn posts + newsletters |
| `/image-gen` | Image creation | Gemini + OpenAI, side-by-side |
| `/nano-banana-2` | Image gen (Gemini) | Transparency, reference images, style transfer |

## Installed CLI Tools
| Tool | Binary | Version | Purpose |
|------|--------|---------|---------|
| gog | `/opt/homebrew/bin/gog` | 0.12.0 | Google Workspace CLI |
| notes | `/opt/homebrew/bin/notes` | — | Apple Notes CLI |
| peekaboo | `~/bin/peekaboo` | 3.0.0-beta3 | macOS screenshot CLI |
| codexbar | `/opt/homebrew/bin/codexbar` | — | AI usage stats |
| image-gen | `~/tools/image-gen/cli.ts` | — | AI image generation |
| nano-banana | `~/tools/nano-banana-2/` | — | Gemini image gen |

## Automation (Cron/Launchd)
| Job | Schedule | Type |
|-----|----------|------|
| Tech Agenda | Fri 10:03am | crontab |
| Marketing Agenda | Sun 10:03am | crontab |
| Apple Notes Sync | Daily 11pm | launchd |
| Daily Digest | Daily 9pm | crontab |
