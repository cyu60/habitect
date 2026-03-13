---
name: note
description: "Capture a voice note, random thought, or quick idea into today's Obsidian daily note. Adds a timestamped entry to 'Notes & Captures', extracts TODOs into 'Current TODOs', and updates the schedule/plan if the note implies changes. Use when the user dictates a thought, update, reflection, random idea, or brain dump."
argument-hint: "<note text>"
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash(date *)
  - Glob
---

# voice-note / random-note

Capture voice notes and random thoughts into today's Obsidian daily note with timestamps, TODO extraction, and schedule updates.

## Obsidian Vault

- Vault: `/Users/china/Desktop/Obsidian/Chinat's Notes/`
- Daily notes: `/Users/china/Desktop/Obsidian/Chinat's Notes/Daily Notes/`
- Naming format: `March 10th, 2026.md` (English ordinal dates)

## How to find today's daily note

1. Get today's date with `date` command
2. Convert to the Obsidian naming format (e.g., "March 10th, 2026")
   - Use ordinal suffixes: 1st, 2nd, 3rd, 4th-20th, 21st, 22nd, 23rd, 24th-30th, 31st
3. Look for the file in the Daily Notes directory

## What to do with a voice note / random note

### 1. Add to "Notes & Captures" section

Find the `## Notes & Captures` section and append a timestamped entry:

```markdown
- **HH:MM AM/PM** — One-line summary of the note
  - *Detail or sub-point if needed*
  - *Action item or insight if applicable*
```

Use the current time from `date` command. Keep the summary concise but capture the key info.

### 2. Extract TODOs into "Current TODOs" section

If the note contains tasks, intentions, or things the user wants to do, add them to the `### Current TODOs (in progress right now):` section under `## TOP 3 TASKS`:

```markdown
- [ ] Task description — brief context
```

If the section doesn't exist, create it after the TOP 3 TASKS table and before "Also on your plate".

### 3. Update the schedule if needed

If the note implies a change to the day's plan (e.g., "I need to leave now to get there on time", "skipping the 2pm meeting", "moving shower to evening"):
- Update the relevant time block in the `## TODAY'S SCHEDULE` code block
- Update the `## ALARMS TO SET` table if alarm times changed
- Update `## BODY & HEALTH` if relevant

### 4. Extract action items

If the voice note contains a specific TODO or action item, note it in the capture with a checkbox:
```markdown
- **9:30 AM** — Realized I need to prep slides for the 3pm meeting
  - [ ] Draft 3 slides before 2:30 PM buffer
```

### 5. Extract lessons/meta-observations

If the voice note contains a planning insight (like "I should account for travel time"), add it as an italicized sub-bullet so it stands out for future gameplan generation:
```markdown
  - *Future planning: always add 15-min buffer for campus transit*
```

### 6. Handle random ideas / brain dumps

For unstructured thoughts, ideas, or brainstorms:
- Still timestamp them in Notes & Captures
- Tag the type in the summary line: idea, brainstorm, random thought, reflection
- If it relates to an open loop, cross-reference it in the `## OPEN LOOPS` section
- If it's actionable, also add to Current TODOs

```markdown
- **2:45 PM** — 💡 Idea: could use Ghost Social matching for Demo Day networking
  - Cross-ref: Stanford Founders Demo Day (May 7)
  - [ ] Pitch this to Sophia at next check-in
```

## Task: $ARGUMENTS
