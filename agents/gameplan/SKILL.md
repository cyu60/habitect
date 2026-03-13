---
name: gameplan
description: "Generate tomorrow's gameplan with today's recap. Builds on /daily-digest by adding Obsidian quarterly goals, Notion task priorities, browser hygiene analysis, and the 3-project mapping. Use at end of day or when the user asks for tomorrow's plan."
argument-hint: "[optional: specific focus or question for tomorrow]"
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - Agent
---

# Evening Gameplan Report

This skill generates a purpose-driven gameplan for tomorrow. It layers on top of `/daily-digest` by adding strategic context from Obsidian and Notion.

## Planning Standard

Tomorrow's plan should be the result of triage, not a copy of every open task.

Before finalizing the plan:
- reconcile Notion tasks with meeting-note promises, inbox follow-ups, and 750 words captures
- reconcile recent Apple Notes TODOs and conversation notes
- merge duplicates
- mark blocked items as watcher items instead of active work
- reduce tomorrow to a list that is actually executable

## How to Generate

### Step 1: Run daily-digest for today's data (if not already run)
```bash
/Users/china/.claude/skills/daily-digest/bin/daily-digest --dry-run
```
This pulls calendar, emails, browser history. Use `--dry-run` to just display without writing to Obsidian/Notion/email.

### Step 2: Read Obsidian planning context (in parallel)

**Quarterly goals:**
```
Read: /Users/china/Desktop/Obsidian/Chinat's Notes/Reviews/2026 Plan.md
```
Extract: current quarter's goals, what's checked off, what's overdue.

**Core values & daily rhythm:**
```
Read: /Users/china/Desktop/Obsidian/Chinat's Notes/Personal/Chinat 2026 - Core Values & Annual Plan.md
```
Extract: 3 active projects, Critical Rules, daily rhythm, backburner list.

**Today's daily note:**
```
Glob: /Users/china/Desktop/Obsidian/Chinat's Notes/Daily Notes/<today's date>.md
```
Format: `Month Dayth, Year.md` (e.g., `March 10th, 2026.md`)

**This month's review:**
```
Read: /Users/china/Desktop/Obsidian/Chinat's Notes/Reviews/Monthly/- Mar 2026.md
```

### Step 3: Query Notion task DBs for upcoming deadlines
```bash
# MentorMates Dev Tasks
/Users/china/codeDev/notion-management/bin/notion-db-query 255ab088-064e-8095-b931-c005ceaafbbe

# Stanford Founders Tasks
/Users/china/codeDev/notion-management/bin/notion-db-query 886dd2f7-37c1-49a8-8bd5-be5ddce850fe

# DayDreamers Tasks
/Users/china/codeDev/notion-management/bin/notion-db-query 7c8ea482-2854-4783-8ba3-c62c100d9b35

# Sales & Marketing Tasks
/Users/china/codeDev/notion-management/bin/notion-db-query 2c7ab088-064e-80c0-b6a6-d87163275c57
```
Filter output for: Status = "Not started" or "In progress", highlight anything due this week.

### Step 4: Browser hygiene analysis
```bash
/Users/china/.claude/skills/browser-history/bin/browser-export recap --days 1
/Users/china/.claude/skills/browser-history/bin/browser-export searches --days 1
```

### Step 5: Claude Code + Codex conversation logs (TODAY'S ACTUAL WORK)
This is critical — the conversation logs reveal what Chinat actually worked on, asked about, and accomplished today.

```bash
# Find today's Claude Code session transcripts
find ~/.claude/projects/ -name "*.jsonl" -mtime 0 2>/dev/null
```

For each session file found, extract:
- **User messages** — what was asked/requested (type: "user", skip toolUseResult entries)
- **Assistant outputs** — what was built, researched, generated
- **Tools used** — what files were edited, commands run, skills invoked

```python
# Extract user messages from a session transcript
import json
with open(session_file) as f:
    for line in f:
        msg = json.loads(line.strip())
        if msg.get('type') == 'user' and not msg.get('toolUseResult'):
            content = msg.get('message', {}).get('content', '')
            # Extract text content
```

Cross-reference conversation logs with:
- The morning gameplan (what was planned vs. what was actually worked on)
- Notion tasks (did any tasks get completed or progressed?)
- Browser history (was browsing aligned with what was discussed in conversations?)

Also review Codex session logs for the same day:

```bash
find ~/.codex/sessions ~/.codex/archived_sessions -name "*.jsonl" -mtime 0 2>/dev/null
```

Carry forward the digest's short `AI Session Summary`:
- total sessions reviewed
- `Claude Code` vs `Codex` split
- main workstreams discussed

**Claude Code + Codex together are the most honest signal of what the day actually looked like.**

### Step 6: Read Apple Notes for any captures
```bash
notes recent 20
notes list "Todos & Gameplans"
notes list "Conversations"
```
Then read any Apple Note modified today that contains task captures, conversation outcomes, or quick thoughts that need routing.

### Step 7: Synthesize into the report

## Report Format

```markdown
## Evening Report — [Day], [Date]

---

### Today's Recap
- **What was accomplished:** [from Claude Code logs + daily note + calendar + browser activity]
- **What was actually worked on:** [from Claude Code conversation — the real signal]
- **What wasn't accomplished:** [planned tasks that didn't happen]
- **Why:** [honest — emotional regulation? meetings? scope creep?]

### Digital Footprint
- **[N] pages visited** | Top: [categories]
- **Searches:** [what was on your mind today]
- **Hygiene:** [productive %, entertainment %, late night visits]
- **Alignment:** [did browsing match the 3 active projects?]

### Tomorrow's ONE Highlight
**[Single most important task]**
Why: [connects to quarterly goal + purpose]
*"Does this serve the purpose I am called to?"* — [answer]

### Tomorrow's Schedule
[Day of week context + daily rhythm with specific tasks filled in]
```
09:00  Wake + exercise
09:30  Devotional + prayer
10:00  Gratitude (3) + set ONE highlight
10:30  Deep work: [SPECIFIC TASK]
12:30  Lunch + people time
14:00  [SPECIFIC MEETINGS from calendar]
16:30  Admin
17:00  750 words
18:00  Shutdown
```

### Top 3 Tasks
| # | Project | Task | Due |
|---|---------|------|-----|
| 1 | **MentorMates** | [from Notion] | [date] |
| 2 | **Daydreamers** | [from Notion] | [date] |
| 3 | **Community** | [from Notion] | [date] |

### Open Loops
- [overdue Notion tasks]
- [items mentioned in daily note but not resolved]
- [anything from quarterly plan that's slipping]

### Triage Decisions
- **Do tomorrow:** [short list only]
- **Delegate / watch:** [owned by someone else; you are tracking]
- **Defer:** [real but not tomorrow]
- **Drop / archive:** [stale or duplicate items removed from active focus]

### Anchor Question
> "Is what I am doing tomorrow striving toward a greater purpose — is it done according to the will of the Lord?"
[Brief reflection]

---
*"Everything that matters is captured. Tomorrow's highlight is clear. The rest is in God's hands."*
*Go to sleep, Chinat. There is always tomorrow.*
```

## Data Sources (Habitect)

All evening reviews pull from these sources to build a complete picture:

| Source | What it reveals | How to access |
|--------|----------------|---------------|
| **Claude Code logs** | What was actually built/discussed today | `~/.claude/projects/` JSONL files modified today |
| **Obsidian** | Plans, goals, reflections | Vault at `/Users/china/Desktop/Obsidian/Chinat's Notes/` |
| **Notion** | Tasks, meetings, projects | CLI at `/Users/china/codeDev/notion-management/bin/` |
| **Apple Notes** | Quick captures, synced gameplans | `osascript` to read Notes app |
| **Browser history** | Digital hygiene, actual browsing | `~/.claude/skills/browser-history/bin/browser-export` |
| **Google Calendar** | Meetings, schedule | `gog` CLI |
| **Gmail** | Communications, action items | `gog` CLI |

**Claude Code logs are the most honest signal.** They show what you actually asked for, what was built, what problems came up, and how time was really spent — no self-reporting bias.

## Principles
1. **Be honest.** If the daily note shows a 2 PM start or YouTube browsing, say so.
2. **Claude Code logs reveal the real work.** Cross-reference planned vs. actual conversations.
3. **Browser history reveals the real browsing.** Cross-reference planned vs. actual.
4. **ONE highlight, not five.** Aligned with the quarter's biggest bet.
5. **Flag violations:** Sleep Covenant (11PM+), 3-project rule, YouTube rabbit holes.
6. **End with peace.** The closing is a benediction, not a guilt trip.

## Weekly Rhythm
- Monday: Planning — weekly highlight
- Tuesday: Marketing meeting + outreach
- Wednesday: Deep build day (no meetings)
- Thursday: Workshops + teaching
- Friday: Ship day — push code, close loops
- Saturday: Flexible
- Sunday: REST — church, no work

## Task: $ARGUMENTS
```
