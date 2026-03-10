---
name: notion
description: Search, read, query, and create pages in the Edumame/MentorMates Notion workspace. Use when the user asks about Notion pages, meetings, tasks, events, partnerships, or wants to create/update Notion content.
argument-hint: "[search query] or [action like 'create meeting', 'read page', 'query tasks']"
allowed-tools:
  - Bash(/Users/china/codeDev/notion-management/bin/notion-*)
  - Bash(cd /Users/china/codeDev/notion-management && *)
  - Bash(bash -c 'source /Users/china/codeDev/notion-management/bin/notion-config.sh && *)
  - Read
  - Grep
---

# Notion Workspace Integration

You have CLI tools to interact with the Edumame/MentorMates Notion workspace.

## CLI Tools

All tools are at `/Users/china/codeDev/notion-management/bin/`:

| Command | Usage |
|---------|-------|
| `notion-search <query>` | Search pages/databases by keyword. Flags: `--type page\|database`, `--limit N` |
| `notion-read <page-id-or-url>` | Read page metadata + content. Flags: `--meta`, `--blocks`, `--all` |
| `notion-read-blocks <id> [depth]` | Recursively read nested blocks (default depth 3) |
| `notion-db-query <db-id>` | Query a database. Flags: `--filter-json '{}'`, `--sort-field <field>`, `--sort-dir asc\|desc`, `--limit N` |
| `notion-db-schema <db-id>` | Show database property names, types, and options |
| `notion-index` | Rebuild local workspace cache |
| `notion-map` | Display workspace tree from cache |

**Important**: The `.env` file is at `/Users/china/codeDev/notion-management/.env`. When calling tools directly via their path, they source their own config. When using the Notion API directly via curl, you must source `bin/notion-config.sh` first in a bash subshell:

```bash
cd /Users/china/codeDev/notion-management && bash -c '
source bin/notion-config.sh
notion_request POST "/pages" "$BODY"
'
```

## Key Database IDs

| Database | ID |
|----------|-----|
| Dev Tasks Tracker | `255ab088-064e-8095-b931-c005ceaafbbe` |
| Meetings | `255ab088-064e-800e-b27d-f9bf93741625` |
| People | `24eab088-064e-8029-b0f5-c57106224024` |
| Companies | `24aab088-064e-80c3-baf3-e56faa7f0a93` |
| Events | `29eab088-064e-81d4-aaa9-e5c31551c94d` |
| Partnership Tracker | `2ddab088-064e-8028-8faf-df3cc35bb967` |

## Key Page IDs

| Page | ID |
|------|-----|
| Edumame Hub | `266ab088-064e-8037-b584-c554326d3af7` |
| Marketing Vision 2026 | `729d7e28-47aa-49f5-a7ca-50a5119a573f` |

## Database Schemas (Quick Reference)

### Meetings DB
- Name (title), Notes (rich_text), Event Type (select: Hackathon, Summit, Conference, External Meeting, Internal Meeting, Workshop, Weekly Meeting, Internal Goal, Networking, Incubator Interview, User Testing, Daily Standup), Event Date (date), Tags (multi_select: Observer, Sponsor, Milestone, Marketing, etc.), POC (people), Mentor Mates People (relation → People DB), Companies/Partner (relation → Companies DB)

### Dev Tasks DB
- Task name (title), Description (rich_text), Task type (multi_select: Bug, Feature request, Polish), Status (status: Backlog, Not started, In progress, Done, Done - Archive), Priority (select: High, Medium, Low), Effort level (select: Small, Medium, Large), Assignee (people), Due date (date)

## Team Notion User IDs
- Chinat Yu: `1a70b78e-0195-4056-9e6e-7807f424e2f8`
- Jeffery Zhou: `4af8840a-f82d-4367-838e-58a01093f99c`
- Aurelia (Leah): `253d872b-594c-81b1-9015-00025a8d06fe`

## Creating Pages via API

To create a page in a database, use `notion_request POST "/pages"` with a JSON body. Example for creating a meeting:

```bash
cd /Users/china/codeDev/notion-management && bash -c '
source bin/notion-config.sh
BODY='"'"'{"parent":{"database_id":"255ab088-064e-800e-b27d-f9bf93741625"},"properties":{"Name":{"title":[{"text":{"content":"Meeting Title"}}]},"Event Type":{"select":{"name":"Internal Meeting"}},"Event Date":{"date":{"start":"2026-03-10"}}}}'"'"'
notion_request POST "/pages" "$BODY"
'
```

To add content blocks to a page, use `notion_request PATCH "/blocks/{page-id}/children"` with a `{"children": [...]}` body containing block objects.

## Block Types for Content Creation

```python
# Common block constructors:
{"object":"block","type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":"Title"}}]}}
{"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":"Text"}}]}}
{"object":"block","type":"bulleted_list_item","bulleted_list_item":{"rich_text":[{"type":"text","text":{"content":"Item"}}]}}
{"object":"block","type":"to_do","to_do":{"rich_text":[{"type":"text","text":{"content":"Task"}}],"checked":false}}
{"object":"block","type":"divider","divider":{}}
```

## Linked GitHub Repository

This skill wraps the CLI tools in the **notion-management** repo:
- **Local path**: `/Users/china/codeDev/notion-management`
- **Remote**: `https://github.com/cyu60/notion-management.git` (branch: `master`)

### Keeping the repo in sync
When you add or modify CLI tools (new scripts in `bin/`, config changes, etc.):
1. Make the changes in `/Users/china/codeDev/notion-management/`
2. Commit and push to `cyu60/notion-management`
3. Update this skill file if the change adds new commands, databases, or workflows

When this skill file itself evolves (new DB IDs, new workflows, new block patterns):
1. Update this file at `~/.claude/skills/notion/SKILL.md`
2. If the change is relevant to the repo (e.g. new CLI tool docs), also update the repo README
3. Commit and push the repo changes

The goal is that the **repo has the tools** and the **skill has the context** — they should stay in sync.

## Automation Scripts

| Script | Description | Schedule |
|--------|-------------|----------|
| `marketing-agenda` | Generate Notion meeting page + send personalized prep emails | Sunday 10:03am → Tuesday meeting |
| `marketing-agenda-emails` | Send personalized emails (called by marketing-agenda or standalone) | Part of marketing-agenda |
| `weekly-meeting-sync` | Process tech weekly meeting → Notion tasks + GitHub issues | After tech weekly meetings |

### Related Skill
- **`/marketing-agenda`** — Dedicated skill for the marketing meeting automation (see `~/.claude/skills/marketing-agenda/SKILL.md`)

## Key Database IDs (Additional)

| Database | ID |
|----------|-----|
| Sales & Marketing Tasks Tracker | `2c7ab088-064e-80c0-b6a6-d87163275c57` |

## Workflow Guidelines

1. **Search first** before reading — use `notion-search` to find relevant pages
2. **Check memory** at `/Users/china/.claude/projects/-Users-china-codeDev-MentorMates/memory/` for cached workspace info (page IDs, team details, meeting history, marketing tasks)
3. **Use `notion-read-blocks`** for full content including transcriptions (set depth 2-3)
4. **Update memory files** after discovering new important info (page IDs, decisions, action items)
5. Marketing meetings are on **Tuesdays** — meeting notes follow a standard template
6. Marketing meeting icon: 📣 | Daily standup icon: 🎈 | Dev weekly icon: 💻

## Task: $ARGUMENTS
