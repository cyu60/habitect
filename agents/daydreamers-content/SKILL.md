# DayDreamers Content Generation

Generate LinkedIn posts and Substack newsletter articles from DayDreamers session slides.

## When to Use

After each DayDreamers session, when user says things like:
- "generate posts for session X"
- "create linkedin content from the new session"
- "write newsletter for the latest daydreamers session"

## Workflow

### Step 1: Identify the Session

- Session HTML files live at: `/Users/china/codeDev/daydreamers-materials/cohort1/sessions/`
- Passcodes are in the README: `/Users/china/codeDev/daydreamers-materials/README.md`
- Live site: https://daydreamers-materials.vercel.app

### Step 2: Take Screenshots with Playwright

Use `bun` to run Playwright (installed globally via bun):

```javascript
// /tmp/screenshot-slides.mjs
import { chromium } from 'playwright';
// ... navigate to session URL, enter passcode, screenshot each .slide element
// Save to: /Users/china/codeDev/daydreamers-materials/images/slides/
```

Key details:
- Use `bun run /tmp/screenshot-slides.mjs` (not node — playwright is a bun global)
- Viewport: 1280x720, deviceScaleFactor: 2 for retina quality
- Enter passcode via `.gate input` + `.gate button`
- Screenshot each `.slide` element individually
- Naming: `session{N}-slide-{NN}.png`

### Step 3: Push Screenshots to GitHub

```bash
cd /Users/china/codeDev/daydreamers-materials
git add images/slides/
git commit -m "add slide screenshots for session N content generation"
git push origin main
```

Image URLs (Vercel — public, use these for Notion embeds):
`https://daydreamers-materials.vercel.app/images/slides/{filename}`

NOTE: The GitHub repo is **private**, so `raw.githubusercontent.com` URLs will 404.
Always use the Vercel deployment URL for public image hosting.

### Step 4: Read Slide Content

Use an Agent to read the session HTML file and extract structured slide content:
- Slide number, title, key points, quotes, frameworks

### Step 5: Generate LinkedIn Posts

For each meaningful slide (skip title slides, homework, feedback forms), write a LinkedIn post in Chinat's voice:
- **Tone:** calm, analytical, builder-first, slightly contrarian, never hypey
- **Format:** lowercase, short paragraphs, bullet points, strong hook
- **Structure:** Hook → Body → DayDreamers CTA → [slide screenshot] → hashtags
- **Hashtags:** #vibecoding #daydreamers + topic-specific
- **Length:** 150-300 words

### Step 6: Generate Substack Newsletter

Create a longer-form newsletter article that:
- Recaps the session theme and key takeaways
- Embeds multiple slide screenshots as visuals
- Goes deeper on 3-4 key frameworks/insights from the session
- Includes links to the live materials and companion apps
- Ends with a CTA (next session, sign up, etc.)
- Tone: same as LinkedIn but more expansive and educational

### Step 7: Create Posts in Notion Content Tracker

**Database ID:** `6cbf7c77-bb6e-4a96-8761-f9ce06451124`

**Properties to set:**
- Post Title (title): the LinkedIn post hook
- Week (select): Week N (increment from last used)
- Content Pillar (select): **Vibe Coding**
- Channels (multi_select): LinkedIn
- Status (status): Draft
- Priority (select): 🔴 High / 🟡 Medium / 🟢 Low
- Scheduled Date (date): weekdays starting from next Monday
- Notes (rich_text): "Session N, Slide X — [description]"

**Page content blocks:**
1. heading_2: "LinkedIn Post Draft"
2. paragraph: full post copy
3. divider
4. image (external URL from GitHub raw)

**Creating pages via Notion API:**
Write JSON to `/tmp/notion_postN.json`, then:
```bash
cd /Users/china/codeDev/notion-management && bash -c '
source bin/notion-config.sh
BODY=$(cat /tmp/notion_postN.json)
notion_request POST "/pages" "$BODY"
'
```

**Updating properties (pillar, dates):**
```bash
cd /Users/china/codeDev/notion-management && bash -c '
source bin/notion-config.sh
BODY="{\"properties\":{\"Content Pillar\":{\"select\":{\"name\":\"Vibe Coding\"}},\"Scheduled Date\":{\"date\":{\"start\":\"2026-03-10\"}}}}"
notion_request PATCH "/pages/{PAGE_ID}" "$BODY"
'
```

**Appending image blocks and updating text blocks:**

IMPORTANT: Use direct `curl` calls for updating blocks — the `notion_request` shell wrapper has escaping issues with rich_text content. Use this Python pattern:

```python
import json, subprocess

def notion_api(method, endpoint, body=None):
    env_path = "/Users/china/codeDev/notion-management/.env"
    token = None
    with open(env_path) as f:
        for line in f:
            if line.startswith("NOTION_TOKEN="):
                token = line.strip().split("=", 1)[1]
    headers = [
        "-H", f"Authorization: Bearer {token}",
        "-H", "Content-Type: application/json",
        "-H", "Notion-Version: 2022-06-28",
    ]
    url = f"https://api.notion.com/v1{endpoint}"
    cmd = ["curl", "-s", "-X", method, url] + headers
    if body:
        cmd += ["-d", json.dumps(body)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return json.loads(r.stdout) if r.stdout else None

# Append image block:
img_body = {"children": [{"object": "block", "type": "image",
    "image": {"type": "external", "external": {"url": IMG_URL}}}]}
notion_api("PATCH", f"/blocks/{PAGE_ID}/children", img_body)

# Update paragraph text:
update = {"paragraph": {"rich_text": [{"type": "text", "text": {"content": NEW_TEXT}}]}}
notion_api("PATCH", f"/blocks/{BLOCK_ID}", update)
```

For simple property updates (dates, pillar, etc.), `notion_request` shell wrapper works fine:
```bash
cd /Users/china/codeDev/notion-management && bash -c '
source bin/notion-config.sh
BODY="{\"properties\":{...}}"
notion_request PATCH "/pages/{PAGE_ID}" "$BODY"
'
```

## Substack Integration

Substack has **no official API**. Current options:
- **Unofficial TypeScript client:** `npm install substack-api` (jakub-k-slys/substack-api on GitHub)
- **Unofficial Python client:** `pip install substack-api` (NHagar/substack_api on GitHub)
- **Manual:** Draft the newsletter content in Notion, then copy-paste into Substack editor
- **n8n automation:** Can automate Substack Notes (short posts) but not full newsletters

For now, generate newsletter drafts as Notion pages that Chinat can copy into Substack.

## Content Pillar Options in Content Tracker

- Hackathons as Systems
- Practical Authority
- Insider Insights
- Sponsors & Logistics
- AI + Hackathons
- Fun / Personal
- **Vibe Coding** (added for DayDreamers content)

## Chinat's Content Voice Reference

From the Content Plan (Notion page `2f4ab088064e800baa72d3906507ddb9`):
- Positioning: "I help people design hackathons that actually create builders, not just weekend demos."
- Identity: hackathon architect, learning systems designer, builder pipeline thinker
- Tone: calm, analytical, builder-first, slightly contrarian, never hypey
- Avoid: event recaps, generic motivational content, over-polished carousels
- Formats: short frameworks (5-8 lines), contrarian takes, behind-the-scenes

## Key Session Info (Cohort 1)

| Session | Topic | Slides | Passcode |
|---------|-------|--------|----------|
| 1 | Mastering Vibe Coding | 13 slides | vibecoding |
| 2 | Build Your First AI App | 15 slides | buildapp |

## Posting Strategy (from Content Distribution SOP)

**Content Distribution SOP Notion page:** `73fe0cf83d3f484b93aee27614bc0ef6`

### Weekday Content Types (Mon-Fri) — AI, Vibe Coding & DayDreamers

| Day | Content Type | Description |
|-----|-------------|-------------|
| Monday | Testimonial | Social proof — quotes, results, screenshots from participants |
| Tuesday | Event Recap | Recaps of sessions — slides, photos, key moments |
| Wednesday | Insight / Nugget | Quick, valuable takeaway about AI, vibe coding, building |
| Thursday | Engagement | Comment-to-DM style — offer a resource in exchange for engagement |
| Friday | Story / Conversation | Deeper narrative — founder lesson, behind-the-scenes, personal reflection |

### Weekend Content (Sat-Sun) — Hackathon Insights

- Organizer interviews & takeaways
- Hackathon systems thinking
- Community stories & behind-the-scenes
- Deep dives on formats, judging, team formation

### Channels & Timing

| Channel | Best For | Ideal Posting Time (PT) |
|---------|----------|------------------------|
| LinkedIn | Thought leadership, insights | Tue-Thu, 8-10 AM |
| Instagram | Visual content, carousels, reels | Mon-Fri, 11 AM-1 PM |
| X (Twitter) | Hot takes, threads | Mon-Fri, 9-11 AM |
| YouTube | Tutorials, recaps, deep dives | Sat-Sun, 9 AM-12 PM |
| Substack | Deep dives, weekly roundups | Weekly (consistent day) |
| WhatsApp/Discord | Community nudges, event reminders | Same day as primary post |

### Scheduling Strategy

When interlacing vibe coding posts with existing hackathon/AI posts:
1. Front-load high-priority posts
2. Alternate vibe coding and hackathon content on weekdays
3. Use weekends exclusively for hackathon deep-dives
4. Match posts to content type by day (Mon=Testimonial, etc.)
5. Schedule 1 post per day, 7 days a week

### Newsletter (Substack) Strategy

After each DayDreamers session, create a newsletter that:
- Recaps the session with 3-4 key frameworks
- Embeds slide screenshots as visuals
- Links to live materials and companion apps
- Provides actionable homework for readers
- Published within 1 week of the session
