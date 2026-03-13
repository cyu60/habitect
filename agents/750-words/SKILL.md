---
name: 750-words
description: "Add your daily 750 words freewrite to today's Obsidian daily note. The habit target is at least 750 words, while the note should record the true word count. Formats the entry, generates summary/tags from existing tag vocabulary, extracts TODOs and action items, reflects on patterns, and proposes follow-up actions. Use when the user shares their 750 words writing."
argument-hint: "<750 words text>"
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash(date *)
  - Glob
  - Grep
  - Agent
---

# 750 Words Skill

Add, format, and reflect on the user's daily 750 words freewrite in their Obsidian daily note.

## Obsidian Vault

- Vault: `/Users/china/Desktop/Obsidian/Chinat's Notes/`
- Daily notes: `/Users/china/Desktop/Obsidian/Chinat's Notes/Daily Notes/`
- Naming format: `March 10th, 2026.md` (English ordinal dates)

## How to find today's daily note

1. Get today's date with `date` command
2. Convert to the Obsidian naming format (e.g., "March 11th, 2026")
   - Use ordinal suffixes: 1st, 2nd, 3rd, 4th-20th, 21st, 22nd, 23rd, 24th-30th, 31st
3. Look for the file in the Daily Notes directory

## Entry Format

The 750 words section uses this exact template:

```markdown
-  #750-words-✍ || [Short descriptive title]
    - Writing time:: [HH:MM] - [HH:MM]
    - Time taken:: [minutes]
    - Tags:: [space-separated tags from APPROVED TAG LIST below]
        Summary: [One-line summary of the entry]
        Word count:: [actual word count]
            [Full prose body, preserving the user's exact words, indentation, wiki links, and nested bullets]
```

### Field Rules

- **Title**: Short phrase describing the main theme (e.g., "Agent systems and family reflections")
- **Writing time**: Use the time the user provides, or ask. Format: `HH:MM - HH:MM`
- **Time taken**: Minutes elapsed, or leave blank if unknown
- **Tags**: Pick 2-5 tags from the APPROVED TAG LIST below. Do NOT invent new tags.
- **Summary**: One sentence capturing the essence (can be informal, matches user's voice)
- **Word count**: Always replace this with the actual true word count for the preserved body text. Do not leave a macro or placeholder.
- **Body**: Preserve the user's exact text. Do not correct spelling or grammar. Keep all `[[wiki links]]`, `{{[[TODO]]}}` markers, nested bullets, and formatting exactly as written.

### Formatting Prohibitions

- Do **not** include the Twitter smartblock line.
- Do **not** include the `{{word-count}}` macro.
- The note should contain the literal numeric word count instead.

## APPROVED TAG LIST

These are the canonical tags from past 750 words entries. **Always reuse these. Never create new tags unless the content genuinely has no matching tag.**

### Emotions & State
- `#reflection`
- `#gratitude`
- `#stress`
- `#stress-and-anxiety`
- `#feeling/accomplished`
- `#feeling/lost`
- `#feeling/overwhelmed`
- `#doubts`
- `#motivation`
- `#mental-health`

### Personal & Relationships
- `#family`
- `#personal-relationships`
- `#close-friends`
- `#Friends`
- `#maintaining-connections`
- `#difficult-conversations`
- `#mentorship`
- `#Personal`
- `#沁沁`

### Growth & Development
- `#personal-development`
- `#personal-brand`
- `#learning`
- `#creativity`
- `#education`
- `#meditation`
- `#life-principles/view`
- `#vision-of-future`

### Productivity & Routine
- `#productivity`
- `#time-management`
- `#daily-routine`
- `#morning-routine`
- `#plans-for-the-day`
- `#procrastination`
- `#quality-of-sleep`
- `#sleep`
- `#physical-exercise`
- `#swimming`
- `#detox-days`
- `#distraction-list`
- `#30-day-challenges`

### Work & Projects
- `#Work`
- `#Workflow`
- `#Entrepreneurship`
- `#Ideas`
- `#AI`
- `#hackathon`
- `#internship`
- `#academics`

### Specific Projects/People (use sparingly)
- `#Oneira`
- `#ChatGPT`
- `#Podcast`
- `#writing`

## Where to Place in Daily Note

1. **Preferred**: Find a `## 750 Words` section if it already exists and replace/fill it
2. **If no section exists**: Add it BEFORE `## EVENING DIGEST` or `## Evening shutdown` or `{{👏 Day overview` — whichever comes first
3. **If none of those exist**: Add it at the end of the file

## After Adding the Entry: Reflect & Propose Actions

This is critical. After inserting the formatted 750 words, you MUST:

### Step 1: Reflect on the content

Analyze the writing for:
- **Emotional state**: How is the user feeling? Any recurring patterns from past entries?
- **Key themes**: What's top of mind? What's being processed?
- **People mentioned**: Who came up and in what context?
- **Projects/ideas mentioned**: What's being worked on or dreamed about?
- **Tensions or conflicts**: Any unresolved decisions or anxieties?

### Step 2: Extract actionable items

Find anything that implies a task, intention, or follow-up:
- Explicit TODOs (`{{[[TODO]]}}`, "I should...", "I need to...")
- Implicit intentions ("It would be nice to...", "I want to...")
- People to contact ("I should send X a message")
- Decisions to make ("What should I wear?", "Who is going?")
- Scheduling needs ("Schedule time to call them")

### Step 3: Propose concrete actions

Present the user with a structured reflection and actionable proposals:

```markdown
## 750 Words Reflection

**Emotional pulse**: [1-2 sentences on mood/state]

**Key themes**: [bullet list of 3-5 themes]

**Extracted tasks**:
- [ ] [Task 1 — with context]
- [ ] [Task 2 — with context]

**Proposed actions** (I can do these now if you'd like):
1. [Action — e.g., "Send Angel a message about X"]
2. [Action — e.g., "Add calendar reminder to call family weekly"]
3. [Action — e.g., "Research Friday gala details"]
```

Wait for the user to confirm which actions to take before executing any of them.

### Step 4: Update daily note sections

After user confirmation:
- Add extracted TODOs to the `## TOP 3 TASKS` / "Also on your plate" section
- Update `## Notes & Captures` with a timestamped summary of the 750 words themes
- Cross-reference any open loops in `## OPEN LOOPS` section
- Update `## BODY & HEALTH` if the writing mentions physical/sleep concerns

## Tag Selection Rules (IMPORTANT)

1. **Always check the approved list first.** If a tag fits, use it.
2. **Prefer broader tags over narrow ones.** Use `#AI` not `#GPT-4o`. Use `#family` not `#siblings`.
3. **Pick 2-5 tags.** Not more. Tags should cover the main themes, not every mention.
4. **Hierarchy tags use `/`**: `#feeling/overwhelmed`, `#life-principles/view`
5. **If you absolutely must create a new tag** (rare), note it in the response so the user can approve. New tags create new files in Obsidian that need cleanup.
6. **Case sensitivity matters.** Match the exact casing from the approved list.

## When to Use

750 words is a standalone freewrite — it can happen any time of day (morning, afternoon, or evening). The habit goal is to write **at least 750 words**; entries may be longer, and the note should record the real word count. It is NOT tied to the evening wind-down. If done at night, it should happen BEFORE `/daily-digest`, which handles the full wind-down pipeline.

## Habitect Integration

After processing, note any significant patterns, recurring themes, or new project/person references that should be synced to the Habitect knowledge base. Flag these to the user but do not auto-update habitect without confirmation.

## Task: $ARGUMENTS
