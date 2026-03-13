---
name: tinyfish
description: Use Tinyfish to scrape websites, extract structured data, and automate web tasks with AI browser agents. Trigger when the user needs stealth web scraping, anti-bot bypass, structured extraction from complex pages, or Tinyfish-specific automation help.
---

# Tinyfish — AI Web Agent Skill

Use Tinyfish to scrape websites, extract structured data, and automate web tasks using AI-powered browser agents. Tinyfish agents navigate pages, handle anti-bot protections, and return structured JSON.

## When to Use

- Scraping websites that block traditional scrapers
- Extracting structured data from complex web pages
- Parallel web scraping at scale (up to 20 concurrent agents)
- Any web automation task that needs stealth/anti-bot bypass

## Setup

### API Key
```bash
export TINYFISH_API_KEY=your_key_here
```

Sign up at: https://agent.tinyfish.ai/signup

### Pricing
| Plan | Cost | Concurrent Agents |
|------|------|-------------------|
| Pay-As-You-Go | $0.015/step | 2 |
| Standard | $15/mo | 4 |
| Pro | $150/mo | 20 |

## API Reference

### Endpoint
```
POST https://agent.tinyfish.ai/v1/automation/run-sse
```

### Headers
```
Content-Type: application/json
X-API-Key: <TINYFISH_API_KEY>
Accept: text/event-stream
```

### Request Body
```json
{
  "url": "https://example.com",
  "goal": "Natural language description of what to extract/do",
  "browser_profile": "stealth",
  "proxy_config": {
    "enabled": true,
    "country": "US"
  }
}
```

- `browser_profile`: `"lite"` (fast, basic) or `"stealth"` (anti-bot bypass, residential proxies)
- `goal`: Natural language — describe what data to extract, Tinyfish AI handles navigation

### Response (SSE Stream)
Events stream back as `data: {json}` lines:
- `runId` — unique run ID
- `streamingUrl` — live browser view URL
- `purpose` — current step description
- `type: "COMPLETE"` — final result in `resultJson.parsed` or `resultJson.input`
- `type: "ERROR"` — error message

### Parsing Results
The result JSON can be in multiple locations:
1. `result.projects` (direct)
2. `resultJson.parsed` (SSE format)
3. `resultJson.input` (may be a JSON string that needs unquoting)
4. `data` field (some events)

## Existing Codebase

The exploration repo is at: `/Users/china/codeDev/hackathon-projects/tinyfish-exploration/`

### Key Files
| File | Description |
|------|-------------|
| `cmd/scrape-parallel/main.go` | Main parallel scraper (Go) — 10 concurrent agents |
| `cmd/fetch-results/` | Fetch results from completed Tinyfish runs |
| `internal/tinyfish/client.go` | Go API client with SSE parsing |
| `internal/tinyfish/orchestrator.go` | Parallel agent coordination |
| `data/` | Scraped hackathon JSON/CSV data |
| `logs/task-ids.json` | Run IDs for recovery |
| `hackathons.txt` | Hackathon slug list |

### Running the Scraper
```bash
cd /Users/china/codeDev/hackathon-projects/tinyfish-exploration

# Set API key
export TINYFISH_API_KEY=your_key

# Scrape default hackathons (2025 & 2026)
go run ./cmd/scrape-parallel

# Scrape specific hackathons
go run ./cmd/scrape-parallel treehacks-2025 calhacks-2025

# Load from file
go run ./cmd/scrape-parallel --file hackathons.txt

# Fetch results from previous runs
go run ./cmd/fetch-results
```

## Quick Usage from Any Project

### Python (one-shot scrape)
```python
import requests, json, os

def tinyfish_scrape(url: str, goal: str) -> dict:
    resp = requests.post(
        "https://agent.tinyfish.ai/v1/automation/run-sse",
        headers={
            "Content-Type": "application/json",
            "X-API-Key": os.environ["TINYFISH_API_KEY"],
            "Accept": "text/event-stream",
        },
        json={"url": url, "goal": goal, "browser_profile": "stealth"},
        stream=True,
    )
    for line in resp.iter_lines(decode_unicode=True):
        if not line.startswith("data: "):
            continue
        event = json.loads(line[6:])
        if event.get("type") == "COMPLETE":
            rj = event.get("resultJson", {})
            return json.loads(rj.get("parsed") or rj.get("input", "{}"))
    return {}
```

### curl
```bash
curl -N -X POST https://agent.tinyfish.ai/v1/automation/run-sse \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $TINYFISH_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "url": "https://example.com",
    "goal": "Extract all product names and prices as JSON array",
    "browser_profile": "stealth"
  }'
```

## Tips
- Use `"stealth"` browser profile for sites with bot detection
- Keep goals specific and request JSON output format
- For large scrapes, use the Go parallel scraper (handles 10+ concurrent agents)
- Run IDs are saved to `logs/task-ids.json` for recovery if timeouts occur
- Streaming URLs let you watch the agent work in real-time

## Links
- [Tinyfish Docs](https://docs.tinyfish.ai/)
- [Tinyfish Cookbook](https://github.com/tinyfish-io/tinyfish-cookbook)
- [Sign Up](https://agent.tinyfish.ai/signup)
- [Live Demo: Winning Hackathon Projects](https://www.winninghackathonprojects.com)
