# Preferences & Workflows

## Engineering Preferences
- DRY is important — flag repetition aggressively
- Well-tested code is non-negotiable; rather too many tests than too few
- "Engineered enough" — not under-engineered (fragile) or over-engineered (premature abstraction)
- Err on handling more edge cases, not fewer; thoughtfulness > speed
- Bias toward explicit over clever
- Pre-PR: remove console.log, run build, run lint

## AI Coding Workflow
- **project.md → plan.md → execute** pattern:
  1. Write project.md describing what should be done
  2. AI generates plan.md with implementation details
  3. Iterate on plan.md until satisfied
  4. AI adds detailed todo list to plan.md
  5. Execute: "work through the todo list, don't ask questions, work until complete"
  6. Commit project.md and plan.md alongside code
- Plans include validation criteria (tests, expected behavior)

## Tool Preferences
- **Primary Google CLI**: `gog` (gogcli) — use over gsuite-tools
- **Notes**: Apple Notes for quick capture, Notion for structured work, Obsidian for long-form knowledge
- **Git**: Always use PRs, never push to main. Meaningful branch names.
- **Plan files**: Descriptive kebab-case names (e.g., `fix-auth-redirect-bug.md`)

## Communication Style
- Direct and concise
- Prefers opinionated recommendations with tradeoffs
- Wants to be asked before major decisions
- Values interactive review (architecture → code quality → tests → performance)

## Productivity Patterns
- Marketing meetings on Tuesdays
- Tech meetings on Mondays
- Uses Apple Notes for quick mobile capture
- Uses Notion for project/team management
- Uses Obsidian for personal reflection and quarterly planning
