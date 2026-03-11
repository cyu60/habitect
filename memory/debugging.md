# Debugging Notes & Lessons Learned

## Drafting Emails — Use `gog gmail draft create`, NOT mailto:
**Problem**: `mailto:` URLs cannot render HTML — body shows as plain text or raw tags.
**Best solution**: Use `gog` CLI to create a Gmail draft, then open it in browser:
```bash
gog gmail draft create --account chinatchinat123@gmail.com \
  --to recipient@example.com \
  --subject "Subject" \
  --body-html "$(cat /tmp/email.html)"
# Returns draft_id, then open:
open "https://mail.google.com/mail/u/0/#drafts?compose=<draft_id>"
```
**Fallback**: AppleScript to Mail.app (write to `.scpt` file, never inline `-e` — quote escaping breaks).

## AppleScript Quote Escaping
**Problem**: `osascript -e '...'` fails when the embedded string contains single quotes (common in HTML/CSS).
**Solution**: Always write AppleScript to a temp `.scpt` file and execute it, never inline with `-e`.

## Resend API Rate Limits
**Problem**: Sending emails too fast (>2/sec) causes 429 errors.
**Solution**: Add `time.sleep(0.6)` between sends. Always include rate limiting in email-sending scripts.

## TDD Reminder
- When building automation scripts (email senders, API integrations), always test with `--dry-run` first
- Save HTML previews to `/tmp/` and visually inspect before sending
- For email: generate preview → verify rendering → then send
- For Notion API: log the request body before making the call
- Test one recipient first, then batch
