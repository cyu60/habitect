# Habitect

**A second brain for managing agents, tools, and knowledge.**

Your digital garden where AI agents, personal knowledge, and workflows grow together.

---

## Problem

- Today, AI users juggle dozens of apps and agents.
- Context and memory are fragmented across tools — chatbots, note apps, coding assistants, email, calendars.
- New "must try" AI apps appear daily, but there's no **central hub** to manage them or integrate into a coherent workflow.
- Users lack a way to connect their **personal knowledge** with their **AI agent ecosystem**.

---

## Solution — Habitect

The **Digital Garden for AI Agents**:

- A **"second brain"** where all your AI agents, tools, and knowledge connect.
- Combines **personal knowledge management (PKM)** with **agent knowledge management (AKM)**.
- Your "garden" grows as you add AI tools, apps, and workflows — each rooted in shared context and memory.

### Core Features

1. **Contextus Memory** — Git-tree inspired system for conversations and workflows. Persistent context that agents share across sessions.
2. **SNOW Framework** (System prompt, Navigation, Overview, Workflow) — Structure for defining and managing agent interactions.
3. **Agent Plug-Ins** — Add custom AI tools, apps, or APIs. Build your own ecosystem.
4. **Knowledge Layer** — Unified context so agents "know what you know." Your notes, emails, calendar, browser history, and documents — all accessible.
5. **Interface** — A Notion-like workspace with chat + modular apps.

---

## Why Now

- Explosive growth of AI apps → chaos for users.
- Shift from single "super AI" to **multi-agent ecosystems**.
- Need for infrastructure: a **hub that unifies fragmented AI experiences**.

---

## Architecture

```
habitect/
├── agents/                    # AI agent definitions and skills
│   ├── apple-notes/           # Apple Notes search, read, create + GitHub backup
│   ├── browser-history/       # Digital hygiene analysis
│   ├── daily-digest/          # Evening reflection + day summary
│   ├── daydreamers-content/   # Content generation pipeline
│   ├── gameplan/              # Tomorrow's gameplan with today's recap
│   ├── gsuite/                # Gmail, Calendar, Drive via gog CLI
│   ├── image-gen/             # AI image generation (Gemini + OpenAI)
│   ├── marketing-agenda/      # Weekly marketing meeting prep
│   ├── notion/                # Notion workspace integration
│   ├── tech-agenda/           # Weekly tech meeting prep
│   └── todo/                  # Smart task router across systems
├── memory/                    # Persistent context across sessions
│   ├── MEMORY.md              # Core memory (always loaded)
│   ├── cron-jobs.md           # Scheduled automations
│   ├── team-profiles.md       # Team member details
│   └── ...                    # Topic-specific memory files
├── spec/                      # Design specs and test requirements
└── README.md
```

## Agents

| Agent | What it does |
|-------|-------------|
| **daily-digest** | Evening reflection that pulls calendar, email, browser history, and Notion tasks into a human, emotionally-aware summary. Outputs to Obsidian, Notion, and styled email. |
| **gameplan** | Tomorrow's gameplan — layers Obsidian goals, Notion task priorities, and browser hygiene on top of daily-digest. |
| **gsuite** | Gmail, Calendar, Drive operations via `gog` CLI (primary) with gsuite-tools fallback. |
| **notion** | Notion workspace search, read, query, create — connected to Edumame/MentorMates workspace. |
| **apple-notes** | Search, read, create Apple Notes + daily GitHub backup of 1700+ notes. |
| **browser-history** | Digital hygiene analysis — productivity %, categories, late-night patterns. |
| **todo** | Smart task router — parses intent, breaks down tasks, routes to Notion, Obsidian, or memory. |
| **marketing-agenda** | Weekly Tuesday marketing meeting prep with Notion page + personalized emails. |
| **tech-agenda** | Weekly Monday tech meeting prep with task overview from Dev Tasks Tracker. |
| **image-gen** | AI image generation — Gemini (Nano Banana 2) + OpenAI (gpt-image-1.5), side-by-side comparison. |
| **daydreamers-content** | LinkedIn posts + newsletters from DayDreamers sessions. |

## Automations

| Job | Schedule | What it does |
|-----|----------|-------------|
| Tech Agenda | Fri 10:03am | Generate Monday tech meeting agenda → Notion + email |
| Marketing Agenda | Sun 10:03am | Generate Tuesday marketing agenda → Notion + email |
| Apple Notes Sync | Daily 11:00pm | Export all Apple Notes to markdown → commit → push to GitHub |
| Daily Digest | Daily 9:00pm | Calendar + email + browser + Notion → Obsidian + Notion + email |

---

## Philosophy

- **Context is everything.** An agent that knows your schedule, inbox, browsing habits, projects, values, and sleep patterns can give you something no single app can.
- **Evening reflection, not data dump.** The daily digest reads like a thoughtful friend recapping your day — emotionally resonant, reassuring, permission to rest.
- **Digital garden.** Your agent ecosystem grows organically. Add tools, connect context, prune what doesn't work.
- **Explicit over clever.** Every agent skill is a readable markdown file. No black boxes.

---

## Market

- **Early adopters**: AI power users, researchers, indie hackers.
- Expands to **knowledge workers**, **startups**, and **teams** who want shared agent gardens.
- Comparable spaces: Notion ($10B), Roam, Obsidian, Mem.
- New angle: adding **AI agent orchestration** on top of knowledge management.

---

## Vision

- Become the **operating system for AI ecosystems**.
- Every person or team has their own **digital garden — a living second brain** where AI agents grow, adapt, and collaborate.
- Long-term: App store for AI agents, decentralized digital gardens that interconnect.

---

## Call to Action

We're looking for:

- **Early pilot users** to test agent + knowledge integration.
- **Investors/partners** interested in the future of multi-agent ecosystems.
- **Builders** who want to grow this digital garden together.

---

## Built With

- [Claude Code](https://claude.ai/claude-code) skills system
- [`gog` (gogcli)](https://github.com/steipete/gogcli) for Google Workspace
- [Notion API](https://developers.notion.com/) via custom CLI tools
- Apple Notes via AppleScript
- Obsidian for personal knowledge management
- Daydreamers design system
