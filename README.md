# Habitect (Mnemo)

**A portable, universal memory layer for AI agents and humans.**

Your knowledge, context, and project history are scattered across dozens of tools — email, calendars, notes, Notion, browser tabs, voice memos, messages, and more. Every time you switch tools or start a new AI conversation, you lose context. Habitect solves this by building an extendable framework that ingests data from all of these sources into a single, unified context store — a true AI second brain.

> Think of it like Severance — you should be able to hot-swap an AI memory chip in and out of any AI agent, giving it full context instantly.

---

## The Problem

- **Scattered information**: Your knowledge lives across email, calendar, notes apps, Notion, Obsidian, browser history, voice recordings, photos, messages, and more
- **Constant copy-pasting**: Reconstructing context for every new tool, conversation, or agent is painful and slow
- **No portability**: Each AI platform keeps its own siloed memory with no incentive to expose or share it
- **Context rot**: The longer a conversation or project goes, the more relevant context gets lost

---

## Architecture — Three Core Components

### 1. Input (Data Ingestion)

An extensible ingestion layer designed so that **any data source can be plugged in**. Uses a waterfall approach, leveraging the best available tool for each source:

**Currently Connected:**

| Source | Type | Connector | Status |
|--------|------|-----------|--------|
| **Obsidian** | Notes (deep thinking, goals) | Direct file read | Working |
| **Notion** | Work tasks, meetings, projects | Custom CLI tools | Working |
| **Apple Notes** | Personal/ad hoc capture (1773+ notes) | AppleScript + GitHub backup | Working |
| **Gmail** | Email (5 accounts) | `gog` CLI | Working |
| **Google Calendar** | Schedule, meetings | `gog` CLI | Working |
| **Google Drive** | Documents, pitch decks, files | `gog` CLI | Working |
| **Browser History** | Browsing patterns, search history | `browser-export` CLI | Working |
| **GitHub** | Code, PRs, issues | `gh` CLI | Working |
| **iMessage** | Personal conversations, sponsor/partner outreach | sqlite3 (`~/Library/Messages/chat.db`) | Working |
| **WhatsApp** | Messaging, team comms, partner outreach | sqlite3 (`~/Library/Group Containers/.../ChatStorage.sqlite`) | Working |
| **WeChat** | Messaging, China/HK network | sqlite3 (`~/Library/Containers/com.tencent.xinWeChat/`) | Partial |
| **Apple Health** | Fitness/activity from Apple Watch | HealthKit export | Not yet connected |
| **Location (FindMy)** | iPhone location data | Shortcuts/FindMy | Not yet connected |

**Future connectors:**
- **Firecrawl** — web scraping and crawling
- **Exa** — semantic search across the web
- **Browser Use** — browser automation for capturing live context
- **Computer Use** — agents that scrape data from apps without APIs
- **User-defined connectors** — plugin interface for any source

### 2. View / Processor (Knowledge Interface)

A human-readable interface for exploring and managing your memory:

- **Knowledge base** (`knowledge/`) — structured markdown files organized by life domain
- **Universal Index** (`knowledge/INDEX.md`) — master cross-reference mapping every piece of information to its source system
- **Hierarchical and associative** — supports both tree structures and cross-domain links
- **Smart feeds** — surface relevant context based on what you're working on (via agents)

### 3. Actuator (Take Action)

The memory isn't just for reading — it enables agents and humans to *act* on context:

- **MCP integration** — expose memory as an MCP server so any compatible agent can read/write
- **SKILL.md files** — portable agent definitions that can be dropped into any agentic coding environment (Claude Code, Codex, Cursor) for instant project context
- **CLI tools** — `habitect-sync` for cross-system synchronization, plus per-source CLIs
- **Shareable context bundles** — export and share portable context for any project
- **Automated agents** — 13+ skills that act on context (daily digest, gameplan, content generation, task routing)

---

## Repository Structure

```
habitect/
├── knowledge/                     # Personal knowledge base (single source of truth)
│   ├── INDEX.md                   # Universal cross-reference (where everything lives)
│   ├── personal/                  # Identity, goals, habits, values, preferences
│   ├── projects/                  # MentorMates, VoxForma, DayDreamers, Habitect
│   ├── people/                    # Team, advisors, network, contacts
│   ├── resources/                 # Repos, accounts, infrastructure, tools
│   ├── skills/                    # Technical and non-technical capabilities
│   └── immigration/               # O-1 visa process, lawyers, timeline
├── agents/                        # AI agent definitions (SKILL.md files)
│   ├── apple-notes/               # Apple Notes search, read, create + GitHub backup
│   ├── browser-history/           # Digital hygiene analysis
│   ├── daily-digest/              # Evening reflection + day summary
│   ├── daydreamers-content/       # Content generation pipeline
│   ├── gameplan/                  # Tomorrow's gameplan with today's recap
│   ├── gsuite/                    # Gmail, Calendar, Drive via gog CLI
│   ├── image-gen/                 # AI image generation (Gemini + OpenAI)
│   ├── marketing-agenda/          # Weekly marketing meeting prep
│   ├── notion/                    # Notion workspace integration
│   ├── sync/                      # Cross-system task & calendar sync
│   ├── tech-agenda/               # Weekly tech meeting prep
│   └── todo/                      # Smart task router across systems
├── memory/                        # Persistent agent context across sessions
│   ├── MEMORY.md                  # Core memory (always loaded)
│   └── ...                        # Topic-specific memory files
├── snapshots/                     # Point-in-time snapshots for recovery
│   └── gdrive/                    # Google Drive reorganization snapshots
├── spec/                          # Design specs and test requirements
└── README.md
```

## Universal Life Domains

All information — across every system — maps to these 7 domains:

| Domain | What | Primary Systems |
|--------|------|----------------|
| **Ventures** | Active projects (MentorMates, VoxForma, DayDreamers, Habitect) | Notion, GitHub, Google Drive |
| **Career** | Immigration, resumes, speaking, networking | Google Drive, Gmail, Habitect knowledge |
| **Academic** | Stanford, JHU, research | Google Drive, Obsidian |
| **Creative** | Poetry, music, content creation | Apple Notes, Notion, Google Drive |
| **Operations** | Tools, agents, automation, infrastructure | Habitect agents/, CLI tools |
| **Personal** | Identity, health, reflections, media | Obsidian, Apple Notes, Google Drive |
| **Communication** | Email, iMessage, WhatsApp, WeChat, calendar | Gmail, iMessage (chat.db), WhatsApp (ChatStorage.sqlite), WeChat |

See `knowledge/INDEX.md` for the full cross-reference of where every piece of information lives.

## Data Sync

The `habitect-sync` agent keeps information synchronized across systems:

```bash
habitect-sync              # Full sync: read all sources, reconcile, write
habitect-sync --status     # Show current state across all sources
habitect-sync --dry-run    # Preview what would change
habitect-sync --add "task" # Add a task to ALL sources
```

**Sync paths:**
- Notion tasks ↔ Obsidian daily notes ↔ Apple Notes Todo ↔ Apple Calendar
- High-priority Notion tasks (due today/tomorrow) → Obsidian + Apple Notes
- Calendar events → Obsidian daily notes
- Apple Notes todos → Obsidian

## Agents

| Agent | Trigger | What it does |
|-------|---------|-------------|
| **daily-digest** | Daily 9 PM | Calendar + email + browser + Notion → Obsidian + Notion + styled email |
| **gameplan** | On-demand | Tomorrow's agenda layering Obsidian goals, Notion tasks, browser hygiene |
| **gsuite** | On-demand | Gmail, Calendar, Drive via `gog` CLI (5 accounts) |
| **notion** | On-demand | Search, read, query, create in Edumame/MentorMates workspace |
| **apple-notes** | On-demand | Search, read, create Apple Notes + daily GitHub backup (1773+ notes) |
| **browser-history** | On-demand | Digital hygiene — productivity %, categories, late-night patterns |
| **todo** | On-demand | Smart task router — parses intent, routes to Notion/Obsidian/memory |
| **marketing-agenda** | Weekly (Sun) | Tuesday marketing meeting prep → Notion + personalized emails |
| **tech-agenda** | Weekly (Fri) | Monday tech meeting prep → Notion + dev team email |
| **image-gen** | On-demand | AI image generation — Gemini + OpenAI, side-by-side comparison |
| **daydreamers-content** | On-demand | LinkedIn posts + newsletters from DayDreamers sessions |
| **sync** | On-demand | Cross-system task & calendar synchronization |
| **alarm** | On-demand | macOS Calendar alarms that sync to iPhone via iCloud |

## Automations

| Time | Job | Outputs To |
|------|-----|-----------|
| Daily 9:00 PM | Daily Digest | Obsidian + Notion + Email |
| Daily 11:00 PM | Apple Notes → GitHub | `cyu60/apple-notes-backup` |
| Fri 10:03 AM | Tech Agenda | Notion + Email |
| Sun 10:03 AM | Marketing Agenda | Notion + Email |

---

## Philosophy

- **Context is everything.** An agent that knows your schedule, inbox, browsing habits, projects, values, and sleep patterns can give you something no single app can.
- **Portable memory.** Your context should work in any AI agent, not be locked to one platform.
- **Evening reflection, not data dump.** The daily digest reads like a thoughtful friend recapping your day.
- **Explicit over clever.** Every agent skill is a readable markdown file. No black boxes.
- **Open and extendable.** The connector framework is designed so anyone can write and contribute new data source plugins.

---

## Why Frontier Labs Won't Solve This

- **Data moat**: OpenAI, Anthropic, and others have no incentive to make their internal memories portable — it's a lock-in mechanism
- **Interoperability gap**: No single lab will build connectors to every data source; this is an ecosystem play
- **Whoever builds the universal portable memory layer will build an incredibly valuable company**

---

## Vision

- Become the **universal portable memory layer** for AI agents
- Every person has their own **digital garden — a living second brain** where AI agents grow, adapt, and collaborate
- Open source, extendable system where the community builds connectors
- Long-term: shareable context bundles, MCP-native memory, app store for AI agents

---

## Built With

- [Claude Code](https://claude.ai/claude-code) skills system
- [`gog` (gogcli)](https://github.com/steipete/gogcli) for Google Workspace
- [Notion API](https://developers.notion.com/) via custom CLI tools
- Apple Notes via AppleScript
- Obsidian for personal knowledge management
- Supabase (backend, future)
- Firecrawl, Exa, Browser Use (future connectors)
