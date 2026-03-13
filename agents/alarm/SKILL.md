---
name: alarm
description: Set, list, and manage alarms via macOS Calendar events that sync to iPhone via iCloud. Supports relative times (+30m), specific times (7:30am), and labels. Use when the user wants to set a reminder, alarm, wake-up time, or timer.
argument-hint: "set 7:30am Wake up | list | delete 1 | clear"
allowed-tools:
  - Bash(alarm *)
  - Read
---

# alarm

Manage alarms via macOS Calendar events with alerts. Events are created in a dedicated "Alarms" calendar and sync to iPhone via iCloud.

## Command

```bash
alarm <command> [args]
```

## Commands

| Command | Description |
|---------|-------------|
| `alarm set <time> [label]` | Set an alarm |
| `alarm list` | List upcoming alarms (next 7 days) |
| `alarm delete <index\|name>` | Delete by list index or name match |
| `alarm clear` | Delete all alarms |

## Time Formats

| Format | Example | Description |
|--------|---------|-------------|
| `HH:MMam/pm` | `7:30am`, `2pm` | Specific time (today, or tomorrow if passed) |
| `HH:MM` | `14:00` | 24-hour format |
| `+Xm`, `+Xh`, `+XhYm` | `+30m`, `+1h30m` | Relative from now |
| `tomorrow HH:MMam` | `tomorrow 6:00am` | Tomorrow at time |
| `YYYY-MM-DD HH:MM` | `2026-03-11 7:30` | Full date and time |

## Examples

```bash
# Wake-up alarm
alarm set 7:30am "Wake up"

# Quick timer
alarm set +45m "Check oven"

# Tomorrow morning
alarm set tomorrow 6:00am "Early meeting"

# Shorthand (no "set" needed)
alarm 2pm "Standup"

# Manage
alarm list
alarm delete 1
alarm delete "Wake up"
alarm clear
```

## How It Works

- Creates events in a dedicated "Alarms" calendar in macOS Calendar.app
- Each event has a display alert set to trigger at event time
- Events sync to iPhone via iCloud automatically
- **Tip**: In iPhone Settings > Focus, allow Calendar notifications so alarms ring even in DND/Focus mode

## Source

- CLI: `~/tools/alarm/cli.ts`
- Runtime: Bun

## Task: $ARGUMENTS
