# GSuite Integration Details

## Repo
- Local: `/Users/china/codeDev/gsuite-tools`
- GitHub: `github.com/cyu60/gsuite-tools` (branch: `master`)
- Language: Node.js/TypeScript, `googleapis` npm package
- Build: `cd /Users/china/codeDev/gsuite-tools && npx tsc`

## OAuth
- GCP Project: `chinat-apps`
- Client type: Desktop/installed app
- Client ID: `172148173775-b3neriqk0k0d75vkktkkl7kbgbp06m5k.apps.googleusercontent.com`
- Redirect: `http://localhost:3333/callback`
- Scopes: gmail.readonly, gmail.send, gmail.modify, calendar.readonly, calendar.events, drive.readonly, drive.metadata.readonly
- Tokens stored in: `tokens/<profile>.json` (gitignored)
- To add new test users: Google Cloud Console > APIs & Services > OAuth consent screen > Test users

## Profiles & Access Matrix

| Profile | Email | Gmail | Calendar | Drive |
|---|---|---|---|---|
| `personal` | chinatchinat123@gmail.com | OK | OK | OK |
| `stanford` | chinat@stanford.edu | Blocked (admin) | Blocked (admin) | OK |
| `mentormates` | admin@mentormates.ai | OK | OK | OK |
| `mentormates-official` | mentormatesofficial@gmail.com | OK | OK | OK |
| `mentormates-contact` | contact@mentormates.ai | OK | OK | OK |

Default profile: `personal` (set via GSUITE_PROFILE in .env)

## CLI Commands

All at `/Users/china/codeDev/gsuite-tools/bin/`:

| Command | Description |
|---|---|
| `gmail-list [query]` | List emails. Flags: `-q`, `-n <max>`, `--label`, `--profile` |
| `gmail-read <id>` | Read full email by message ID |
| `gmail-send --to <email> --subject <subj> --body <body>` | Send email. Flags: `--cc`, `--bcc`, `--thread`, `--html` |
| `calendar-list` | List events. Flags: `-d <days>`, `-n <max>`, `-c <calendarId>` |
| `calendar-create --summary <title> --start <ISO>` | Create event. Flags: `--end`, `-d`, `-l`, `-a <attendee>` |
| `drive-list [query]` | List/search files. Flags: `-q`, `-n <max>`, `-f <folderId>` |
| `drive-read <file-id>` | Read file (exports Docs as text, Sheets as CSV) |
| `gsuite-auth` | OAuth flow. Flags: `--profile <name>`, `--list`, `--remove <name>` |

## Known Limitations
- Stanford profile: Gmail and Calendar APIs blocked by Stanford Workspace admin policy. Only Drive works.
- App is in "Testing" mode — new accounts must be added as test users in GCP console first
- Future additions planned: Google Docs read/create/update, Google Sheets CRUD, Drive uploads

## gogcli (`gog`) — Extended Google Workspace CLI
- Installed via: `brew install gogcli` (v0.12.0)
- GitHub: https://github.com/steipete/gogcli
- Language: Go, 14+ Google services, OS keyring credential storage
- Credentials: Reuses same OAuth client from gsuite-tools (chinat-apps GCP project)
- Credentials path: `/Users/china/Library/Application Support/gogcli/credentials.json`
- Connected accounts:
  - chinatchinat123@gmail.com (all services)
  - chinat@stanford.edu (all services)
  - contact@mentormates.ai (all services)
  - admin@mentormates.ai (pending auth)
  - mentormatesofficial@gmail.com (pending auth)
- Use `--account <email>` to select account
- Use `--json` for structured output, `--plain` for TSV
