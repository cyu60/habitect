---
name: todo
description: "Add a TODO that gets routed to the right place — Notion, Obsidian, or memory. Helps break down the task, suggests timing, and files it automatically."
argument-hint: "[task description like 'work on daydreamers session 3 content' or 'fix the sign up flow bug']"
allowed-tools:
  - Bash(/Users/china/codeDev/notion-management/bin/*)
  - Bash(cd /Users/china/codeDev/notion-management && *)
  - Bash(gog *)
  - Read
  - Grep
  - Edit
  - Write
---

# TODO — Smart Task Router

When the user says `/todo [something]`, your job is to:

1. **Understand** what they're asking
2. **Help** — break it down, suggest timing, flag conflicts
3. **Route** — file it to the right destination(s)
4. **Confirm** — tell them where it went

## Routing Rules

Determine the category from the task description, then route accordingly:

| Category | Signal Words | Notion DB | DB ID | Also Update |
|----------|-------------|-----------|-------|-------------|
| **Dev/Product** | bug, feature, fix, build, refactor, deploy, API, UI | Dev Tasks Tracker | `255ab088-064e-8095-b931-c005ceaafbbe` | Memory Active TODOs |
| **Marketing** | content, post, LinkedIn, newsletter, outreach, partnership | Sales & Marketing Tasks | `2c7ab088-064e-80c0-b6a6-d87163275c57` | `memory/marketing-tasks.md` |
| **DayDreamers** | daydreamers, session, cohort, curriculum, slides, workshop | DayDreamers Tasks | `7c8ea482-2854-4783-8ba3-c62c100d9b35` | Memory Active TODOs |
| **General** | personal, reminder, call, email, follow up | General Tasks | `159ab088-064e-817c-85f6-da49b94a158a` | Memory Active TODOs |
| **Stanford Founders** | stanford founders, BASES, founder event | Stanford Founders Tasks | `886dd2f7-37c1-49a8-8bd5-be5ddce850fe` | Memory Active TODOs |

If unclear, ask the user which category fits.

## Steps

### Step 1: Parse & Help

Read the user's task description. Then:
- **Break it down** if it's vague: "Work on daydreamers session 3 content" → What specifically? Slides? Exercises? Reading materials?
- **Check calendar** for scheduling: `gog calendar events --from today --to +7d --account chinatchinat123@gmail.com --json` — find open blocks
- **Check existing tasks** in the target DB to avoid duplicates: query the Notion DB
- **Suggest priority and effort**: based on what you know about their schedule and active projects

Present a quick summary:
```
Task: Create Session 3 course content for DayDreamers
Category: DayDreamers
Priority: High (next cohort approaching)
Effort: Large
Suggested timing: Wednesday deep work block
Subtasks:
  1. Outline session topics and learning objectives
  2. Create slide deck
  3. Design hands-on exercises
  4. Prep demo materials
```

Ask if they want to adjust anything before filing.

### Step 2: Create in Notion

Use the Notion CLI to create the task:

```bash
cd /Users/china/codeDev/notion-management && bash -c '
source bin/notion-config.sh
BODY='"'"'{
  "parent": {"database_id": "<DB_ID>"},
  "properties": {
    "Name": {"title": [{"text": {"content": "<TASK_NAME>"}}]},
    "Status": {"status": {"name": "Not started"}},
    "Priority": {"select": {"name": "<PRIORITY>"}},
    "Due date": {"date": {"start": "<YYYY-MM-DD>"}}
  }
}'"'"'
notion_request POST "/pages" "$BODY"
'
```

For Dev Tasks, also set:
- Task type: Feature request / Bug / Polish
- Effort level: Small / Medium / Large
- Assignee (if known)

### Step 3: Add to Obsidian Daily Note

Append the TODO to today's Obsidian daily note under the "Current TODOs" section.

**Daily note path**: `/Users/china/Desktop/Obsidian/Chinat's Notes/Daily Notes/<date>.md`
**Date format**: `March 10th, 2026.md` (use ordinal suffixes: 1st, 2nd, 3rd, 4th...)

If the file exists, look for a `## Current TODOs` section and append there. If no such section exists, add one before the digest/reflection sections. If the file doesn't exist, create it with a basic header.

Format:
```markdown
## Current TODOs
- [ ] **[DayDreamers]** Create Session 3 course content — High priority, due Mar 14
- [ ] **[Dev]** Fix sign up flow bug — Medium priority
```

Include the category tag, task name, priority, and due date if known.

### Step 4: Update Memory

Add to the Active TODOs section in:
`/Users/china/.claude/projects/-Users-china-codeDev-MentorMates/memory/MEMORY.md`

Format: `- **[Project/Area]**: Task description (priority, due date)`

For marketing tasks, also append to:
`/Users/china/.claude/projects/-Users-china-codeDev-MentorMates/memory/marketing-tasks.md`

### Step 5: Confirm

Tell the user:
- What was created and where (Notion + Obsidian + Memory)
- The Notion page link (if available from API response)
- Suggested timing based on their calendar
- Any related existing tasks they should know about

## Key Paths

- Notion CLI: `/Users/china/codeDev/notion-management/bin/`
- Notion config (for API calls): `/Users/china/codeDev/notion-management/bin/notion-config.sh`
- Memory: `/Users/china/.claude/projects/-Users-china-codeDev-MentorMates/memory/`
- Obsidian daily notes: `/Users/china/Desktop/Obsidian/Chinat's Notes/Daily Notes/`

## Task: $ARGUMENTS
