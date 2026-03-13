---
name: wind-down
description: "Perform the low-stimulation shutdown ritual after the evening review: close the day, set tomorrow's highlight, update the note, and stop activation. This is a state-change skill, not an inbox sweep."
argument-hint: "[optional: focus like 'late night', 'after dinner', 'high stress']"
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash(date *)
  - Glob
  - Agent
---

# Wind-Down

This skill is the final stage of the evening pipeline.

Its job is not to gather more information. Its job is to get you out of execution mode and into sleep mode.

In normal use, this is often just the final 5-10 minute close at the end of `/evening-review`, not a big separate workflow.

## Boundary

Use `/wind-down` when:
- the real work of the day is already known
- the digest and gameplan are either done or good enough
- the problem is no longer "what matters?" and is now "how do I stop?"

Do **not** turn `/wind-down` into:
- more coding
- more PR review
- more inbox checking
- more "just one quick fix"

If major uncertainty remains about what happened or what is owed, switch back to `/daily-digest`.

## Inputs

Preferred inputs:
- today's daily note
- the latest `/daily-digest` output
- the latest `/gameplan` output
- `/Users/china/codeDev/habitect/knowledge/projects/why-this-work-exists.md`

If the digest has **not** been run, do a minimal shutdown-safe triage from the daily note only. Do not expand into a full systems sweep unless the user explicitly asks for it.

## Output Standard

The output should be short and calming. It should leave behind:
- tomorrow's ONE highlight
- 3-5 real carry-forward items max
- a brief `Watch / Defer / Drop` remainder
- a short `why this work exists` / calling reminder
- a concrete shutdown checklist

## Procedure

### 1. Read the current state
- Read today's daily note
- Reuse the existing digest / gameplan if present
- Read `/Users/china/codeDev/habitect/knowledge/projects/why-this-work-exists.md`
- If missing, do only the smallest triage needed to avoid sleeping with unresolved ambiguity

### 2. Reconnect to purpose
- Re-anchor in the bigger picture before ending the day
- Remember that the work is not a prestige contest and not a worth-proving exercise
- In the Christian frame: worth is already secure in the eyes of the Lord, so tomorrow's plan does not need to carry identity pressure
- Briefly reflect on calling, freedom, resilience, forgiveness, and courage:
  what part of today's work felt aligned with service and calling, and what part came from fear or proving?
- If useful, leave behind one sentence of prayer, gratitude, repentance, or release
- When relevant, recall the Hong Kong founder-pathway thread and the Clement conversation so daily execution stays tied to the larger mission

### 3. Collapse the task field
- Keep only the few items that genuinely matter tomorrow
- Everything else becomes `Watch`, `Defer`, or `Drop`
- Do not carry giant backlogs into the wind-down section

### 4. Lock tomorrow
- Set tomorrow's ONE highlight
- If needed, tighten the top 3 tasks and alarms in the daily note
- Keep tomorrow small enough to be executable

### 5. Update the note
- Add a short timestamped entry in `## Notes & Captures`
- Add or update a `## Wind-Down` or equivalent shutdown block if useful
- Record the lesson if the same pattern repeated tonight

### 6. Shut stimulation down
- Phone away from bed
- Lights low
- Water / bathroom / brush teeth
- Audio, prayer, or paper only
- No scrolling in bed

### 7. Hard stop rule

If you got home late, feel mentally activated, or it is already after 10 PM:
- no new project work
- no new debugging
- no new "research"
- capture one line if needed, then stop

## Relationship To Other Skills

- `/750-words` = reflection input
- `/daily-digest` = evidence sweep + triage
- `/gameplan` = tomorrow's executable plan
- `/wind-down` = optional shutdown-only close
- `/evening-review` = umbrella skill that can orchestrate the whole sequence

## Task: $ARGUMENTS
