# MentorMates Memory

## Key References
- [Notion & Email integration](notion-and-email.md) - DB IDs, team emails, Resend setup, weekly workflow
- [Notion workspace details](notion-workspace.md) - Page IDs, team members, meeting history
- [Marketing meeting tasks](marketing-tasks.md) - Outstanding action items from meetings
- [Team profiles](team-profiles.md) - Detailed info for each team member (education, LinkedIn, etc.)
- [Cron jobs](cron-jobs.md) - All scheduled jobs, scripts, logs, and management commands
- [Obsidian vault details](obsidian-vault.md) - Vault paths, key files, planning framework, import scripts

## Project
- MentorMates: Next.js 15 hackathon mentor-participant feedback platform
- Supabase backend, TailwindCSS, TypeScript
- Main repo: `/Users/china/codeDev/MentorMates` — GitHub: `github.com/edumame/MentorMates`
- VoxForma (Founder Signal Report): `/Users/china/codeDev/voxforma` — GitHub: `github.com/edumame/voxforma`
- Daydreamers materials: `/Users/china/codeDev/daydreamers-materials/`
- Obsidian vault: `/Users/china/Desktop/Roam2Obsidian transition/Roam-Export-1683384736080/` — GitHub: `github.com/cyu60/obsidian-vault`

## AI Coding Workflow
- **project.md → plan.md → execute** pattern:
  1. Write `project.md` describing what should be done
  2. Have AI generate `plan.md` from project.md with implementation details
  3. Iterate on plan.md until satisfied
  4. AI adds a detailed todo list to the end of plan.md
  5. Execute: "work through the todo list, don't ask questions, work until complete"
  6. Commit project.md and plan.md alongside the code
- Plan.md serves as a reproducible spec — future better models can re-evaluate and improve it
- Consider: design/plan/debug doc separation (per-feature design docs, phased plans, debug hypothesis docs)
- Plans should include validation criteria (tests, expected behavior)

## Skills & Automation
- `/notion` skill at `~/.claude/skills/notion/SKILL.md` — search, read, create Notion content
- `/gsuite` skill at `~/.claude/skills/gsuite/SKILL.md` — Gmail, Calendar, Drive across multiple Google accounts
- `/marketing-agenda` skill at `~/.claude/skills/marketing-agenda/SKILL.md` — auto-generate Tuesday meeting agenda
- `/tech-agenda` skill at `~/.claude/skills/tech-agenda/SKILL.md` — auto-generate Monday tech meeting agenda
- `/daydreamers-content` skill at `~/.claude/skills/daydreamers-content/SKILL.md` — generate LinkedIn posts + newsletters from DayDreamers sessions
- `/browser-history` skill at `~/.claude/skills/browser-history/SKILL.md` — analyze browsing habits, digital hygiene, search history, recaps
- `/daily-digest` skill at `~/.claude/skills/daily-digest/SKILL.md` — evening digest: calendar, emails, browser, Notion → Obsidian + Notion + email
- `/image-gen` skill at `~/.claude/skills/image-gen/SKILL.md` — generate images with Gemini (Nano Banana 2) + OpenAI (gpt-image-1.5), side-by-side comparison
- `/nano-banana-2` skill at `~/.claude/skills/nano-banana-2/SKILL.md` — Gemini-only image gen with transparency, reference images, style transfer
- CLI scripts at `/Users/china/codeDev/notion-management/bin/` — `tech-agenda`, `marketing-agenda`
- GSuite CLI at `/Users/china/codeDev/gsuite-tools/bin/` — Gmail, Calendar, Drive tools (Node.js/googleapis)
- Browser export script at `~/.claude/skills/browser-history/bin/browser-export` — recap, searches, domains, timeline, recent
- Persistent cron: see [cron-jobs.md](cron-jobs.md) for full schedule and management

## Image Generation
- `image-gen` CLI at `~/tools/image-gen/cli.ts` — GitHub: `github.com/cyu60/image-gen`
  - Unified CLI: `image-gen "prompt" [-p gemini|openai|both] [-s 1K|2K|4K] [-a 16:9]`
  - Gemini key: `~/.nano-banana/.env` (GEMINI_API_KEY)
  - OpenAI key: reads from `~/codeDev/MentorMates/.env.local` (OPENAI_API_KEY)
- `nano-banana` CLI at `~/tools/nano-banana-2/` — reference images, transparency, style transfer
- Models: Gemini Flash (Nano Banana 2, ~$0.067/img), OpenAI gpt-image-1.5 (latest, 4x faster than 1.0)

## Installed Tools (steipete)
- **CodexBar** — `/Applications/CodexBar.app` + `/opt/homebrew/bin/codexbar` — menu bar usage stats for Claude/Codex/Gemini/etc.
- **Peekaboo** — `~/bin/peekaboo` (v3.0.0-beta3) — macOS screenshot CLI for AI agents. Needs Screen Recording + Accessibility permissions.

## GSuite Integration
- **Primary CLI**: `gog` (gogcli v0.12.0) — `/opt/homebrew/bin/gog`, installed via Homebrew
  - Covers Gmail, Calendar, Drive, Docs, Sheets, Slides, Forms, Contacts, Tasks, Chat
  - Account selection: `--account <email>` or `-a <email>`
  - Supports drafts, reply threading, attachments, batch ops
  - Auth via OS keyring; config at `~/Library/Application Support/gogcli/config.json`
  - Authenticated account: `chinatchinat123@gmail.com`
- **Backup CLI**: gsuite-tools (deprecated, fallback only)
  - Repo: `/Users/china/codeDev/gsuite-tools` — GitHub: `github.com/cyu60/gsuite-tools`
  - Still needed for: mentormates, mentormates-official, mentormates-contact, stanford profiles
  - Profile selection: `--profile <name>` (default: `personal`)
- See [gsuite-details.md](gsuite-details.md) for full reference

## Content Generation
- Content Tracker DB: `6cbf7c77-bb6e-4a96-8761-f9ce06451124`
- Content Plan page: `2f4ab088064e800baa72d3906507ddb9`
- Content Distribution SOP: `73fe0cf83d3f484b93aee27614bc0ef6`
- Screenshot script: `/Users/china/codeDev/daydreamers-materials/scripts/screenshot-slides.mjs` (run with `bun`)
- Screenshots hosted at: `daydreamers-materials.vercel.app/images/slides/` (NOT raw.githubusercontent — repo is private)
- Use direct `curl` for Notion block updates (notion_request wrapper has escaping issues with rich_text)
- Posting schedule: Mon=Testimonial, Tue=Event Recap, Wed=Insight, Thu=Engagement, Fri=Story, Sat-Sun=Hackathon
- Content pillars: Hackathons as Systems, Practical Authority, Insider Insights, Sponsors & Logistics, AI + Hackathons, Fun/Personal, Vibe Coding
- Substack: no official API — draft newsletters in Notion, copy to Substack manually

## User Preferences
- Chinat prefers DRY code, thorough testing, explicit over clever
- Uses Notion CLI tools at `/Users/china/codeDev/notion-management/bin/`
- Marketing meetings are on Tuesdays
- Wants Notion info cached/logged so he doesn't have to reshare pages
