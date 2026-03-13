---
name: evening-review
description: "Run the full evening review / wind-down flow: digest the day, compare plan vs actual, catch missed holes, close any critical loops, build tomorrow's gameplan, and end with reassurance."
argument-hint: "[optional: focus for tonight like 'late night' or 'meeting-heavy day']"
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - Edit
  - Write
  - Agent
---

# Evening Review / Wind-Down

This is the umbrella nightly skill.

It exists so the evening pipeline has one entry point that matches how the user actually arrives at night:

- come home from work or meetings
- understand what the day actually became
- catch anything that fell through the cracks
- close the few loops that truly still matter
- turn that into tomorrow's plan
- end the night feeling settled enough to shower, sleep, and trust tomorrow

`/750-words` is not part of the default evening sequence. It may happen earlier in the day or be skipped entirely.

## Stages

1. `/daily-digest`
2. close any truly critical remaining loops
3. `/gameplan`
4. `/wind-down`

## Boundary

Use `/evening-review` when you want the whole end-of-day sequence.

Use the individual skills when you only need one stage:
- `/daily-digest` for review + triage and planned-vs-actual analysis
- `/gameplan` for tomorrow's plan
- `/wind-down` for shutdown-only if you already know the day is resolved

This skill should orchestrate the stages, not duplicate their logic.

## How To Run

### Stage 1: Daily digest
- Run `/daily-digest` to do the full inbox and systems sweep
- Review the full Claude Code + Codex logs for the target day, not just the current chat window
- Compare:
  - what the user planned to do
  - what they actually worked on
  - what reality forced or changed
- Classify obligations into `Done / Do / Delegate / Defer / Drop`
- Identify where planned vs actual drift happened so the system can learn over time
- Write a short `AI Session Summary` into the daily note with session counts and main topics
- Stop the digest from turning into more work

### Stage 2: Close critical loops now
- If the digest reveals 1-2 truly important loose ends that should be handled tonight, do them now
- Examples:
  - send the owed email
  - reply to the person waiting
  - file the task in the right system
  - move a fake-urgent item into `Defer`
- Do not expand this into a new work session
- The goal is closure, not nighttime productivity

### Stage 3: Tomorrow plan
- Run `/gameplan`
- Set tomorrow's ONE highlight
- Keep the task list small enough to execute

### Stage 4: Emotional close
- Run `/wind-down` as the final stage, even if briefly
- Reconnect to `why this work exists` before sleep so tomorrow is not carried by prestige or proving pressure
- End with reassurance, not more analysis
- Confirm that everything real is captured
- Make it psychologically safe to shower, sleep, and leave the rest for tomorrow
- If useful, leave behind one short prayer, gratitude, repentance, or release sentence

## Late-Night Mode

If the evening starts late:
- compress the digest to the essential triage
- focus even more on plan vs actual and missed holes
- close only the smallest number of critical loops
- keep the gameplan short
- protect the emotional close at all costs

Completeness is less important than actually getting to sleep.

## Output Standard

By the end of `/evening-review`, the system should have:
- an honest recap of the day with `planned vs actual vs reality`
- a short `AI Session Summary` covering Claude Code and Codex session counts plus main topics
- a cleaned list of obligations
- any critical loose ends either handled or intentionally deferred
- tomorrow's executable plan
- a short purpose / calling reminder anchored in `why this work exists`
- a real emotional landing rather than another activation block

## Core Purpose

The most important job of this skill is not just summarization.

It is to create a learning loop:
- where planning drift becomes visible
- where the user can see what tends to happen in reality
- where tomorrow's gameplan gets smarter because tonight's review was honest

And then, after that, it should reduce anxiety enough that sleep feels safe again.

That close should also reconnect the work to calling:
- worth is already secure in the eyes of the Lord
- entrepreneurship is not a prestige contest
- resilience, forgiveness, and courage make it easier to do the work that is actually entrusted

## Task: $ARGUMENTS
