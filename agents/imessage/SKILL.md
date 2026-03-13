---
name: imessage
description: Use when the user wants to search iMessage history, identify a Messages contact, draft or send an iMessage, or automate macOS Messages.app from this machine. Covers sqlite3 access to ~/Library/Messages/chat.db, Habitect's synced iMessage archive, and AppleScript/osascript sending flows. Trigger for requests like "send a text", "reply in iMessage", "check Messages", "who texted me", or "find our past iMessages".
---

# iMessage

Use this skill for local iMessage work on this Mac.

## Data sources

Prefer the fastest source that answers the question:

1. `~/Library/Messages/chat.db` for live message state
2. `/Users/china/codeDev/habitect/knowledge/communications/imessage-archive.jsonl` for broad text search
3. `/Users/china/codeDev/habitect/knowledge/communications/imessage-contacts.md` for contact stats and first/last message dates

## Search workflow

- If the user asks about past messages, start with `rg` on the Habitect archive for quick recall.
- If you need exact timestamps, attachments, or current state, query `~/Library/Messages/chat.db` with `sqlite3`.
- If the user gives a fuzzy recipient name, resolve it before sending. Prefer a phone number or email handle over a display name.

Example live query:

```bash
sqlite3 ~/Library/Messages/chat.db "SELECT h.id, m.text, datetime(m.date/1000000000 + 978307200, 'unixepoch', 'localtime') FROM message m JOIN handle h ON m.handle_id = h.ROWID WHERE m.text LIKE '%SEARCH_TERM%' ORDER BY m.date DESC LIMIT 20;"
```

## Sending workflow

Use `scripts/send-imessage.sh`.

Rules:
- Ask for confirmation before sending if the user did not explicitly ask you to send.
- Prefer `--handle` with a phone number or email.
- Use `--name` only when the exact Messages buddy name is known.
- Run send commands with escalated permissions because `osascript` needs access to Messages.app outside the sandbox.
- If AppleScript fails with connection or automation errors, check that Messages is signed in and that Terminal/Codex has Automation access.

Examples:

```bash
/Users/china/.codex/skills/imessage/scripts/send-imessage.sh --handle "+15551234567" "hi"
/Users/china/.codex/skills/imessage/scripts/send-imessage.sh --name "Jeffery - AMR || 176" "hi"
```

## Troubleshooting

- `Connection invalid`: rerun outside sandbox and make sure Messages.app is available.
- `No buddy found`: resolve the exact handle first; display names are brittle.
- Multiple matches for a name: stop and ask the user which contact to use.
