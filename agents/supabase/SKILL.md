---
name: supabase
description: "Manage Supabase projects — list, pause, delete, check security. Use when the user asks about Supabase projects, security alerts, or database management."
argument-hint: "list | security | delete <ref-id> | pause <ref-id>"
allowed-tools:
  - Bash(npx supabase *)
  - Bash(echo *)
  - Read
---

# Supabase Project Management

## CLI

Supabase CLI is available via `npx supabase` (v2.72.8 installed).

## Active Projects

| Name | Ref ID | Org | Region | Notes |
|------|--------|-----|--------|-------|
| **PROD** (MentorMates) | nsxcypmjpizdjxrdncpe | dragvirirfrbubitqdeg | West US (N. California) | Main production |
| **Staging** (MentorMates) | moinycvhmmzjjtvqijzw | dragvirirfrbubitqdeg | West US (N. California) | Staging env |
| mentor-mate | sgobtvbxgcyulhvvmcnf | vercel_icfg | East US (N. Virginia) | Legacy Vercel-linked |
| Contextus-PROD | tjhqiqtbtoazflvhdllj | dragvirirfrbubitqdeg | East US (Ohio) | Has 20 security errors |
| GitFeat | sfpntyfjxzvufslbdtyb | dragvirirfrbubitqdeg | West US (Oregon) | Has 8 security errors |
| medical-education | lvgbzzeclwayyryxbrzy | bhbffctrcbcbkztzzfwt | West US (N. California) | Old (2023), 11 security errors |
| daydreamer-boardgames | zqbpgckvkocqzlmkjymy | dragvirirfrbubitqdeg | West US (N. California) | Recent (Mar 2026) |
| VibeCode | cevbaiojgpkltzycdlwd | dragvirirfrbubitqdeg | West US (N. California) | |
| Alphas | fmembthqkdemgjvxwfto | addbhkajqbkcjapzkxpo | West US (N. California) | |
| SpartaHack | vspiducqotienguaopyc | lxqisjdozocneieigale | West US (N. California) | Hackathon event |
| hacklytics | dahjbhlluerwohidnmnx | lxqisjdozocneieigale | West US (N. California) | Hackathon event |
| hackDavis | bbqabnrxchiunsaindjj | lxqisjdozocneieigale | East US (N. Virginia) | Hackathon event |
| HackathonIdeation | runtlxfmgybjhfqggrlo | vercel_icfg | East US (N. Virginia) | |
| AI-Presentation | gdtiqgyqbytprrobkuoo | vercel_icfg | East US (N. Virginia) | |
| stem-tutor | fqbvyfxrvgcibxuxhhuv | vercel_icfg | East US (N. Virginia) | |
| Modo Backend | onvqaxsumumdhjyggdke | wxwoqikzhlwjudznjuup | West US (N. California) | |

### Deleted
| Name | Ref ID | Deleted | Reason |
|------|--------|---------|--------|
| Contextus-STAGING | ynwxmzawsmocnyaveiib | 2026-03-10 | Unused, 8 security errors |

## Common Commands

```bash
# List all projects
npx supabase projects list

# Delete a project (irreversible!)
echo "y" | npx supabase projects delete <ref-id>

# Pause a project
npx supabase projects pause <ref-id>

# Security — check via dashboard
# https://supabase.com/dashboard/project/<ref-id>/database/security-advisor
```

## Task: $ARGUMENTS
