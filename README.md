# Habitect

**A second brain for managing agents, tools, and knowledge.**

Your digital garden where AI agents, personal knowledge, and workflows grow together.

## What is this?

Habitect is the connective tissue between your AI tools. Instead of juggling dozens of apps with fragmented context, Habitect gives every agent access to shared memory, shared context, and a unified view of your life.

## Structure

```
habitect/
├── agents/              # AI agent definitions and scripts
│   ├── daily-digest/    # Evening reflection + day summary
│   ├── browser-history/ # Digital hygiene analysis
│   ├── gsuite/          # Gmail, Calendar, Drive
│   ├── notion/          # Notion workspace integration
│   ├── marketing-agenda/# Weekly marketing meeting prep
│   ├── tech-agenda/     # Weekly tech meeting prep
│   ├── image-gen/       # AI image generation
│   └── daydreamers-content/ # Content generation
├── memory/              # Persistent context across sessions
├── spec/                # Design specs and test requirements
└── README.md
```

## Agents

| Agent | What it does |
|-------|-------------|
| **daily-digest** | Evening reflection that pulls calendar, email, browser history, and Notion tasks into a human, emotionally-aware summary. Outputs to Obsidian, Notion, and styled email. |
| **gsuite** | Gmail, Calendar, Drive operations via `gog` CLI |
| **notion** | Notion workspace search, read, query, create |
| **browser-history** | Digital hygiene analysis — productivity %, categories, late-night patterns |
| **marketing-agenda** | Weekly Tuesday marketing meeting prep with Notion + email |
| **tech-agenda** | Weekly Monday tech meeting prep |
| **image-gen** | AI image generation (Gemini + OpenAI) |

## Philosophy

- **Context is everything.** An agent that knows your schedule, inbox, browsing habits, projects, values, and sleep patterns can give you something no single app can.
- **Evening reflection, not data dump.** The daily digest reads like a thoughtful friend recapping your day — emotionally resonant, reassuring, permission to rest.
- **Digital garden.** Your agent ecosystem grows organically. Add tools, connect context, prune what doesn't work.

## Built with

- Claude Code skills system
- `gog` (gogcli) for Google Workspace
- Notion API via custom CLI tools
- Browser history analysis
- Daydreamers design system
