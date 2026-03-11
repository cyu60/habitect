# Habitect Conversation History Migration Plan

> Extract ALL conversation histories across every channel, then update all Habitect data sources
> (Notion, Obsidian, Apple Notes, Google Drive) with the extracted intelligence.
>
> Created: 2026-03-10

---

## Phase 1: Extract Conversations from All Channels

### 1A. iMessage ✅ ACCESSIBLE
- **Location**: `~/Library/Messages/chat.db` (SQLite)
- **Tables**: `message`, `handle`, `chat`, `chat_message_join`, `chat_handle_join`
- **Access**: `sqlite3` — works with Full Disk Access
- **Script needed**: Query all conversations, join with handles to get contact names/numbers, export as JSON
- **Output**: `data/exports/imessage/` — one JSON per conversation thread

```sql
-- Key query pattern
SELECT m.rowid, m.text, m.date, m.is_from_me, h.id AS contact
FROM message m
JOIN handle h ON m.handle_id = h.rowid
ORDER BY m.date;
```

### 1B. WhatsApp ✅ ACCESSIBLE
- **Location**: `~/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite` (221MB)
- **Tables**: `ZWAMESSAGE`, `ZWACHATSESSION`, `ZWAMEDIAITEM`, `ZWAPROFILEPUSHNAME`
- **Access**: `sqlite3` — works
- **Existing script**: `scripts/export_whatsapp.py` (already built)
- **Output**: `data/exports/whatsapp/` — one JSON per chat session

### 1C. Gmail ✅ ACCESSIBLE
- **Access**: `gog gmail search` / `gog gmail read` CLI
- **Strategy**: Search by contact, by project keyword, by date range
- **Key searches**:
  - Sponsor leads: Lovable, GitHub, ElevenLabs, Cursor, Anthropic, DeepMind, Manus, MongoDB, Vercel, Perplexity
  - Immigration: Angela Mapa, Pegah, Assel, tryalma.ai
  - Team: MentorMates team emails
  - Stanford: Academic contacts, program admin
  - VCs/investors: from VC & Incubator network
- **Output**: `data/exports/gmail/` — JSON grouped by thread/contact

### 1D. WeChat ❌ BLOCKED (encrypted)
- **Location**: `~/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/3cd97a8d965df7236c081189ab3d98a9/`
- **DBs**: `Message/msg_0.db` through `msg_7.db`, `Contact/wccontact_new2.db`, `Group/group_new.db`
- **Problem**: SQLCipher encrypted, SIP prevents debugger attach, `pywxdump` is Windows-only
- **Unblock options**:
  1. **Disable SIP** (Recovery Mode → `csrutil disable`) → use `lldb` to extract key → re-enable SIP
  2. **Windows VM** with pywxdump (fully supported)
  3. **Manual export** from WeChat Mac UI (right-click chat → Chat History)
  4. **WeChat mobile export** to a Windows PC
- **Output (when unblocked)**: `data/exports/wechat/` — one JSON per conversation

### 1E. Slack ❌ NOT CONNECTED
- **Status**: Not yet investigated
- **Likely approach**: Slack API token or export from workspace settings
- **Output**: `data/exports/slack/`

### 1F. Google Calendar ✅ ACCESSIBLE
- **Access**: `gog calendar` CLI
- **Strategy**: Export all events with attendees — reveals meeting context and relationships
- **Output**: `data/exports/calendar/`

### 1G. Browser History ✅ ACCESSIBLE
- **Location**: `~/Library/Application Support/Google/Chrome/Default/History` (SQLite)
- **Strategy**: Search URLs/titles for project-relevant browsing (company research, lead pages)
- **Output**: `data/exports/browser/`

---

## Phase 2: Process & Classify Conversations

For each extracted conversation, use Claude to:

1. **Identify participants** → map to known contacts in Notion People DB
2. **Classify by domain** → Ventures / Career / Academic / Creative / Personal
3. **Extract entities**:
   - People (name, role, email, company)
   - Companies (name, industry, relationship type)
   - Action items / commitments / follow-ups
   - Key dates, deadlines, events
   - Deals / partnerships / sponsorships (status, amounts)
   - Project references (MentorMates, DayDreamers, VoxForma, Habitect)
4. **Determine what's new** → diff against existing Habitect knowledge
5. **Output**: `data/processed/` — structured JSON per conversation with extracted entities

---

## Phase 3: Update Habitect Data Sources

### 3A. Notion Updates
| Database | What Gets Updated | ID |
|----------|------------------|----|
| People DB | New contacts, updated roles/emails/companies | `24eab088-064e-8029-b0f5-c57106224024` |
| Companies DB | New companies, updated relationship status | `24aab088-064e-80c3-baf3-e56faa7f0a93` |
| Meetings DB | Meeting notes enriched with pre/post conversation context | `255ab088-064e-800e-b27d-f9bf93741625` |
| Partnership Tracker | Sponsor/partner status updates from conversations | `2ddab088-064e-8028-8faf-df3cc35bb967` |
| Leads Tracker (DayDreamers) | Hackathon sponsor lead intel from all channels | `54216c81-f4c6-45e0-b84f-a052d67af962` |
| Stanford Founder Leads | VoxForma lead updates from conversations | `509223e0-acbb-4094-9480-a67707add08d` |
| Content Tracker | Content ideas/plans mentioned in conversations | `6cbf7c77-bb6e-4a96-8761-f9ce06451124` |
| VC & Incubator DB | Investor contacts & intel from conversations | `ed6702c8-26d2-4bb5-9797-861802c32e3c` |
| Events DB | Events mentioned in conversations | `29eab088-064e-81d4-aaa9-e5c31551c94d` |

### 3B. Habitect Knowledge Base (local files)
| File | What Gets Updated |
|------|------------------|
| `knowledge/projects/daydreamers.md` | Sponsor intel, community leads, content ideas |
| `knowledge/projects/mentormates.md` | Partner convos, user feedback, team decisions |
| `knowledge/projects/voxforma.md` | Stanford dinner leads, VC conversations |
| `knowledge/people/team.md` | Team member updates, new collaborators |
| `knowledge/personal/goals.md` | Goals/commitments mentioned in conversations |
| `knowledge/immigration/status.md` | Lawyer conversations, visa updates |

### 3C. Google Drive
- Upload conversation summaries to relevant project folders
- Update pitch decks / sponsor lists with new intel
- Store raw exports as backup in `Drive → Archive/conversation-exports/`

### 3D. Obsidian
- Create/update daily notes with conversation highlights per day
- Update quarterly goals with commitments found in conversations
- Link people mentions to existing Obsidian pages

### 3E. Apple Notes
- Update relevant project notes with conversation insights
- Add new contacts to appropriate folders

---

## Phase 4: Verification & Sync

1. **Diff report**: Generate a summary of all changes made across all systems
2. **Cross-reference**: Ensure no duplicate entries created
3. **Run `habitect-sync`**: Sync Notion ↔ Obsidian ↔ Apple Notes ↔ Calendar
4. **Update INDEX.md**: Reflect any new data sources or mappings

---

## Execution Order

```
Step 1: Create data/exports/ directory structure
Step 2: Run iMessage export script
Step 3: Run WhatsApp export script (existing)
Step 4: Run Gmail export (by contact + by keyword)
Step 5: Run Calendar export
Step 6: Run Browser History export
Step 7: [MANUAL] Unblock WeChat → export
Step 8: [MANUAL] Connect Slack → export
Step 9: Process all exports through Claude (classify, extract entities)
Step 10: Generate diff report (what's new vs. what Habitect already knows)
Step 11: User reviews diff → approves updates
Step 12: Execute Notion updates (batch API calls)
Step 13: Execute Habitect knowledge file updates
Step 14: Upload summaries to Google Drive
Step 15: Update Obsidian notes
Step 16: Update Apple Notes
Step 17: Run habitect-sync
Step 18: Final verification report
```

---

## Data Directory Structure

```
data/
├── exports/
│   ├── imessage/          # Raw conversation JSONs
│   ├── whatsapp/          # Raw conversation JSONs
│   ├── gmail/             # Raw email thread JSONs
│   ├── wechat/            # Raw conversation JSONs (when unblocked)
│   ├── slack/             # Raw conversation JSONs (when connected)
│   ├── calendar/          # Event exports with attendees
│   └── browser/           # Relevant browsing history
├── processed/
│   ├── entities/          # Extracted people, companies, deals
│   ├── by-project/        # Conversations grouped by project
│   ├── by-person/         # Conversations grouped by contact
│   └── diff-report.json   # What's new vs. existing knowledge
└── migration-log.json     # Audit trail of all updates made
```

---

## Blockers & Dependencies

| Blocker | Impact | Resolution |
|---------|--------|-----------|
| WeChat encryption | ~30% of conversations inaccessible | Disable SIP temporarily OR use Windows VM |
| Slack not connected | Unknown conversation volume | Get Slack workspace token |
| Gmail rate limits | May need to batch over time | Use `gog` CLI with pauses |
| Notion API rate limits | Batch updates need throttling | 3 requests/sec with retry |
| WhatsApp schema | Need to verify ZWAMESSAGE columns | Test with `scripts/export_whatsapp.py` |

---

## Privacy & Safety

- All exports stay LOCAL in `data/` (gitignored)
- No raw messages uploaded to cloud — only summaries and extracted entities
- Sensitive content (passwords, financial, medical) filtered out during processing
- `data/` directory already in `.gitignore`

---

*This plan will be executed incrementally. Each phase produces artifacts that feed into the next.*
