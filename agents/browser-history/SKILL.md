---
name: browser-history
description: "Analyze browser history for digital hygiene, recaps, and search patterns. Use when the user asks about browsing habits, what they searched, internet usage, screen time, or wants a digital recap."
argument-hint: "[recap|searches|domains|timeline|recent] [--days N]"
allowed-tools:
  - Bash(/Users/china/.claude/skills/browser-history/bin/browser-export *)
  - Bash(browser-history *)
  - Read
  - Grep
---

# Browser History Analysis

You have a CLI tool to export and analyze browser history from Chrome (primary), Firefox, Arc, and Safari.

## CLI Tool

**`/Users/china/.claude/skills/browser-history/bin/browser-export`**

| Command | What it does |
|---------|-------------|
| `browser-export recap --days N` | Full recap: category breakdown, daily summary, digital hygiene signals |
| `browser-export recent --limit N` | Most recent pages visited |
| `browser-export searches --limit N` | Recent search queries (Google/Bing/DuckDuckGo) |
| `browser-export domains --days N` | Top domains by visit count |
| `browser-export timeline --days N` | Activity heatmap by hour of day |
| `browser-export dump --output FILE` | Full JSON export |

### Options
- `--days N` — look back N days (default 7)
- `--limit N` — number of results (default 30)
- `--browser B` — Chrome, Safari, Arc, Firefox, or all (default: all)

## How to Use This Skill

### For daily/evening reports:
Run `browser-export recap --days 1` to see what the user browsed today. Cross-reference with their daily note and Obsidian planning docs to assess alignment with goals.

### For digital hygiene analysis:
Run `browser-export recap --days 7` (or 30) and analyze:
- **Category breakdown** — how much time goes to productive vs. entertainment vs. social media
- **Late night activity** — any visits after 11 PM violate the Sleep Covenant
- **Search patterns** — what the user is researching/exploring
- **YouTube rabbit holes** — flag high Video/Entertainment percentages
- **Timeline** — peak activity hours vs. the ideal daily rhythm (9AM-6PM)

### For weekly/monthly reviews:
Combine browser data with Obsidian reviews and Notion tasks to give a complete picture:
1. `browser-export recap --days 7` for the week
2. `browser-export domains --days 7` for top sites
3. `browser-export searches --days 7` for research topics
4. Cross-reference with the 3-project rule (MentorMates, Daydreamers, Community)

### Digital hygiene signals to flag:
- **Social media > 20%** — warn about doomscrolling
- **Video/Entertainment > 20%** — likely YouTube rabbit holes (known pattern)
- **Late night visits (11PM+)** — Sleep Covenant violation
- **Low Development/AI Tools %** — are they building or just browsing?
- **High "Other" %** — random browsing, possible procrastination

### Key context about the user:
- Known procrastination pattern: YouTube/phone when anxious (identified at Insight workshop)
- Sleep covenant: 11 PM shutdown, no browsing after
- Ideal rhythm: deep work 10:30-12:30, shutdown at 6 PM
- The user WANTS honest feedback about browsing habits — don't sugarcoat

## Browser Notes
- **Chrome** is the primary data source (6,400+ entries, multiple profiles)
- **Arc** has no traditional history DB — only Top Sites available
- **Safari** is usually locked while running (can't copy the DB)
- **Atlas** is ChatGPT desktop app — conversations are encrypted
- Dependency: `pip install browser-history` (already installed)
