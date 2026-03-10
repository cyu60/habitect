# Notion & Email Integration Notes

## Notion API Access
- Token: stored in `.env.local` as `NOTION_TOKEN`
- CLI toolkit at `/Users/china/codeDev/notion-management/` (private repo: cyu60/notion-management)
- Commands: `notion-search`, `notion-read`, `notion-read-blocks`, `notion-db-query`, `notion-db-schema`, `notion-index`, `notion-map`
- Workspace: 1177 pages, 23 databases (as of 2026-03-10)

## Key Notion Database IDs
- Dev Tasks Tracker: `255ab088-064e-8095-b931-c005ceaafbbe`
- Meetings: `255ab088-064e-800e-b27d-f9bf93741625`
- People: `24eab088-064e-8029-b0f5-c57106224024`
- Companies: `24aab088-064e-80c3-baf3-e56faa7f0a93`
- Events: `29eab088-064e-81d4-aaa9-e5c31551c94d`
- Partnership Tracker: `2ddab088-064e-8028-8faf-df3cc35bb967`

## Dev Tasks DB Schema
- Task name (title), Description (rich_text), Task type (multi_select: Bug/Feature request/Polish),
  Status (status: Backlog/Not started/In progress/Done/Done - Archive), Priority (select: High/Medium/Low),
  Effort level (select: Small/Medium/Large), Assignee (people), Due date (date)

## Team Notion User IDs
- Chinat Yu: `1a70b78e-0195-4056-9e6e-7807f424e2f8`
- Jeffery Zhou: `4af8840a-f82d-4367-838e-58a01093f99c`
- Aurelia (Leah): `253d872b-594c-81b1-9015-00025a8d06fe` (not in workspace users, found via task assignment)
- Jason/Jiaze Ke: no linked Notion user ID (not in workspace)

## Team Emails & People DB IDs
- Chinat Yu: cyu60@alumni.jh.edu (also chinatchinat123@gmail.com) — People DB: `26bab088-064e-80d4-a7ff-e4d4e48cb5b1`
- Josie Trinh: trinhthucthaonghi@gmail.com — People DB: `31fab088-064e-8170-8a34-d5854934c193`
- Angel Lui: lyyluiyanyan@gmail.com — People DB: `31fab088-064e-81dd-9dd4-dc5e9151a49f`
- Britney Budiman: britney.budiman@gmail.com — People DB: `31fab088-064e-814f-8dc5-d81c5a0c09f4`
- Jeffrey Zhou: jefferyzhouehs@gmail.com — People DB: `31fab088-064e-8131-975d-f283774438e1`
- Aurelia (Lia) Sindhu: aurelia.sindhu@gmail.com (also sindhuna@uci.edu) — People DB: `31fab088-064e-819f-9dd4-f16379ce0680`
- Kathryn (Catherine) Tanardy: ktanardy@gmail.com — People DB: `2acab088-064e-80d5-b08a-cfcfe7f80b36`
- Jiaze Ke (Jason): jasonkjz123@gmail.com — People DB: `26bab088-064e-80a1-9568-e8caf50352f0`
- Renee Koay: reneekoay123@gmail.com — People DB: `26bab088-064e-80e6-986b-e22f3ef079ef`

### Marketing Meeting Email List
- Josie Trinh: trinhthucthaonghi@gmail.com
- Britney Budiman: britney.budiman@gmail.com
- Kathryn Tanardy: ktanardy@gmail.com
- Aurelia (Lia) Sindhu: aurelia.sindhu@gmail.com
- Chinat Yu: cyu60@alumni.jh.edu

## Sending Emails via Resend
- API Key in `.env.local` as `RESEND_API_KEY`
- From address: `MentorMates <notifications@hello.mentormates.ai>`
- Direct API call:
```bash
curl -s -X POST https://api.resend.com/emails \
  -H "Authorization: Bearer $RESEND_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"from":"MentorMates <notifications@hello.mentormates.ai>","to":["email@example.com"],"subject":"Subject","html":"<p>Body</p>"}'
```
- Batch limit: 50 recipients per email (Resend limit)
- MentorMates also has Nodemailer/Gmail for legacy emails

## Weekly Meeting → Tasks Workflow
1. Read latest "Weekly Meeting" from Meetings DB
2. Use `notion-read-blocks` to get transcription with action items
3. Extract tasks from action items (check for duplicates against existing GitHub issues)
4. Create Notion tasks in Dev Tasks Tracker with proper schema fields
5. Create GitHub issues in edumame/MentorMates with cross-links
6. Update Notion descriptions with GitHub issue URLs
7. Optionally email task summaries to assignees via Resend
