# Habitect Scripts

## LinkedIn Full Data Export

Export all your LinkedIn data (connections, messages, profile, skills, endorsements, etc.).

### Automated (Playwright)

Connects to your existing Chrome browser so you stay logged in.

1. Quit Chrome completely (Cmd+Q)
2. Relaunch with remote debugging:
   ```bash
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
   ```
3. Run the script:
   ```bash
   node scripts/linkedin-export.js
   ```

Downloads are saved to `data/linkedin/`.

### Manual

1. Go to https://www.linkedin.com/mypreferences/d/download-my-data
2. Click **"Want something in particular?"** to expand all categories
3. Select all checkboxes
4. Click **"Request archive"**
5. Wait for LinkedIn's email (minutes for connections, up to 24h for full data)
6. Return to the same page and click **"Download"**

The download is a `.zip` containing CSVs (connections, messages, profile, skills, endorsements, etc.).

## Import Into Habitect

After you have the export zip, normalize the relationship data and add it to Habitect:

```bash
python3 scripts/import-linkedin-export.py ~/Downloads/Complete_LinkedInDataExport_03-12-2026.zip.zip
```

Outputs:
- Raw snapshot under `data/linkedin/raw/<date>/` (local only, gitignored)
- Normalized relationship tables under `data/processed/` (local only, gitignored)
- Private detail report under `data/processed/` (local only, gitignored)
- Public-safe knowledge summary at `knowledge/people/linkedin.md`
