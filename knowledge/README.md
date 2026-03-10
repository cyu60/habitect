# Knowledge Base

The single source of truth for Chinat's personal knowledge, context, and resources. Every agent in Habitect draws from this knowledge base to act with full context.

## Structure

```
knowledge/
├── personal/               # Identity & self-knowledge
│   ├── profile.md          # Bio, education, career, links
│   ├── goals.md            # Quarterly + long-term goals
│   ├── preferences.md      # Communication style, tool prefs, workflows
│   ├── habits.md           # Daily routines, patterns, productivity insights
│   └── values.md           # Core values, decision-making principles
├── projects/               # Active projects and context
│   ├── mentormates.md      # MentorMates platform
│   ├── voxforma.md         # VoxForma / Founder Signal Report
│   ├── daydreamers.md      # DayDreamers community
│   └── habitect.md         # This project (meta)
├── people/                 # Relationships and contacts
│   ├── team.md             # Core team members
│   ├── network.md          # Advisors, partners, investors
│   └── contacts.md         # Key contacts directory
├── resources/              # Access to tools, accounts, infrastructure
│   ├── repos.md            # All GitHub repos and local paths
│   ├── accounts.md         # SaaS accounts, API keys, services
│   ├── infrastructure.md   # Hosting, domains, databases
│   └── tools.md            # CLI tools, installed software, dev environment
├── skills/                 # Personal skills and capabilities
│   ├── technical.md        # Programming, AI/ML, frameworks
│   └── non-technical.md    # Speaking, writing, community building
├── immigration/            # O-1 visa process
│   └── status.md           # Current status, lawyers, timeline
└── README.md
```

## How Agents Use This

| Agent | Reads from | Purpose |
|-------|-----------|---------|
| daily-digest | goals.md, habits.md | Frame day against priorities, note pattern breaks |
| gameplan | goals.md, projects/*.md | Plan tomorrow aligned with quarterly goals |
| todo | projects/*.md, team.md | Route tasks to correct system and assignee |
| gsuite | people/*.md, contacts.md | Contextualize emails and meetings |
| apple-notes | profile.md | Cross-reference notes with structured knowledge |
| All agents | profile.md, preferences.md | Voice, identity, communication style |

## Principles

1. **One place, not many.** If info exists here, don't duplicate it elsewhere.
2. **Structured for machines.** Markdown with consistent headers so agents can parse it.
3. **Updated by agents.** Agents should update knowledge files when they learn new things (new contacts, completed goals, changed preferences).
4. **Human-readable.** You should be able to browse this like a wiki.
