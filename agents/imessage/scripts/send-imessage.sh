#!/bin/bash
set -euo pipefail

usage() {
  echo "Usage: $0 --handle <phone-or-email> <message>"
  echo "   or: $0 --name <exact-messages-buddy-name> <message>"
  exit 1
}

[[ $# -ge 3 ]] || usage
mode="$1"
recipient="$2"
shift 2
message="$*"

case "$mode" in
  --handle)
    osascript - "$recipient" "$message" <<'APPLESCRIPT'
on run argv
  set recipientHandle to item 1 of argv
  set outgoingText to item 2 of argv
  tell application "Messages"
    set targetService to first service whose service type = iMessage
    set targetBuddy to buddy recipientHandle of targetService
    send outgoingText to targetBuddy
  end tell
end run
APPLESCRIPT
    ;;
  --name)
    osascript - "$recipient" "$message" <<'APPLESCRIPT'
on run argv
  set recipientName to item 1 of argv
  set outgoingText to item 2 of argv
  tell application "Messages"
    set targetService to first service whose service type = iMessage
    set matchingBuddies to every buddy of targetService whose name is recipientName
    if (count of matchingBuddies) is 0 then error "No Messages buddy found for name: " & recipientName
    if (count of matchingBuddies) is greater than 1 then error "Multiple Messages buddies matched name: " & recipientName
    send outgoingText to item 1 of matchingBuddies
  end tell
end run
APPLESCRIPT
    ;;
  *)
    usage
    ;;
esac
