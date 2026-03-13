# Daily Digest — Design Spec & Test Cases

This file captures user feedback as testable requirements. Use this as a spec to validate future changes.

## Core Philosophy

The digest is an **evening reflection tool**, not a data dump. It should:
- Feel like a thoughtful friend recapping your day
- Make the reader feel **safe, secure, and ready to sleep** without anxiety
- Validate emotions and effort, not just list data
- Give permission to rest

## Day Summary Paragraph Requirements

### Tone & Voice
- [ ] Reads like a human wrote it, not a template engine
- [ ] Emotionally resonant — validates how the day felt
- [ ] Uses "you" second person, warm but not saccharine
- [ ] Closing gives explicit permission to rest and let go

### Content Structure
- [ ] **Opening**: How the day felt (intensity, energy)
- [ ] **What you did**: People you met, classes, work — described naturally, not listed
- [ ] **Projects**: What you're pushing forward, how it connects to bigger goals (MentorMates)
- [ ] **Weekly rhythm**: Was this day on-track for its role in the week?
- [ ] **Tomorrow preview**: Reassuring, not anxiety-inducing. "The plan is in place, you just show up."
- [ ] **Stretch goal**: Aspirational but explicitly optional. "If you want... but that's a bonus."
- [ ] **Enjoy closing**: "Close the laptop... you're safe to let go."

### Data Interpretation Rules
- [ ] **All-day calendar events = reminders/aspirational**, NOT things that happened. Say "you had X on your mind" not "you did X"
- [ ] **Calendar events should be taken with a grain of salt** — cross-reference with browser history/logs when possible
- [ ] **Extract other people's names** from meeting titles, don't include "Chinat Yu" as someone you met
- [ ] **Don't list raw event titles** — categorize (meetings, classes, work, social) and describe naturally
- [ ] **Email senders**: Show actual names, filter out promos/social/forums noise
- [ ] **Browser search terms**: Mention what the user was researching
- [ ] **Late-night browsing**: Gentle nudge, not scolding. "Your body was telling you..." not "Heads up!"

### Emotional Safety
- [ ] Closing must make reader feel: nothing is forgotten, nothing is slipping, tomorrow is handled
- [ ] If task list exists, explicitly name it: "{task} will be there tomorrow"
- [ ] Never create urgency or pressure at bedtime
- [ ] Frame stretch goals as optional bonuses, not expectations
- [ ] Sleep covenant references should be compassionate, not disciplinary

## Visual Design Requirements

### Email Layout
- [ ] Max-width: 720px (wider than typical email for readability)
- [ ] Font stack: DM Serif Display (headings), DM Sans (body), DM Mono (labels)
- [ ] Color palette: Daydreamers system (ink #0a0a0f, paper #f5f2ed, cobalt #1c3fdc, amber #d97706, green #16a34a, dust #9a9088)

### Header Gradient
- [ ] Dark ink background (#0a0a0f)
- [ ] Cobalt blue fuzzy glow — NOT purple
- [ ] Uses radial-gradient with cobalt rgba(28,63,220,.42) and amber rgba(217,119,6,.16)
- [ ] NO lighter cobalt/purple gradient (rgba(74,106,255,...) removed)
- [ ] Reference: Title slide (#s0) from `/Users/china/codeDev/daydreamers-materials/cohort1/sessions/session1-vibe-coding.html`

### Body
- [ ] Paper background (#f5f2ed) with subtle radial gradients at corners
- [ ] Sections with clear hierarchy — section headers in DM Mono uppercase
- [ ] Prayer section: dark ink background with softer version of header gradient

## Sections (7 total)

1. **Day Summary** — Conversational paragraph (see above)
2. **Today's Schedule** — Calendar events with time-of-day color coding
3. **Email Highlights** — Grouped by account, filtered for noise
4. **Digital Hygiene** — Browser stats, productivity %, category breakdown
5. **Active Projects** — From Notion Dev Tasks Tracker
6. **Tomorrow Preview** — Next day's events (reassuring framing)
7. **Evening Reflection** — Prompt + prayer with rotating verse

## Known Issues / Future Work

- [ ] Exercise and sleep metrics not yet integrated (no data source identified)
- [ ] Claude Code usage/logs for energy level context (not yet explored)
- [ ] Consider separate GitHub repo for digest development (user suggested)
- [ ] 9 PM cron job not yet set up
