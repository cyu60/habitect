#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import re
import shutil
import zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_ROOT = REPO_ROOT / "data" / "linkedin" / "raw"
PROCESSED_ROOT = REPO_ROOT / "data" / "processed"
KNOWLEDGE_NOTE = REPO_ROOT / "knowledge" / "people" / "linkedin.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Import a LinkedIn full data export into Habitect."
    )
    parser.add_argument("zip_path", help="Path to the LinkedIn export zip archive.")
    parser.add_argument(
        "--snapshot-date",
        help="Snapshot label in YYYY-MM-DD format. Defaults to the date parsed from the filename.",
    )
    return parser.parse_args()


def infer_snapshot_date(zip_path: Path, explicit: str | None) -> str:
    if explicit:
        dt.date.fromisoformat(explicit)
        return explicit

    match = re.search(r"(\d{2})-(\d{2})-(\d{4})", zip_path.name)
    if match:
        month, day, year = match.groups()
        return f"{year}-{month}-{day}"

    return dt.date.today().isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv_skip_preamble(zf: zipfile.ZipFile, member: str, header_prefix: str) -> list[dict]:
    lines = zf.read(member).decode("utf-8-sig").splitlines()
    header_index = next(
        index for index, line in enumerate(lines) if line.startswith(header_prefix)
    )
    return list(csv.DictReader(lines[header_index:]))


def parse_connection_date(value: str) -> dt.date:
    return dt.datetime.strptime(value.strip(), "%d %b %Y").date()


def parse_invitation_datetime(value: str) -> dt.datetime:
    return dt.datetime.strptime(value.strip(), "%m/%d/%y, %I:%M %p")


def linkedin_handle(url: str) -> str:
    parsed = urlparse((url or "").strip())
    path = parsed.path.strip("/")
    if not path:
        return ""
    parts = path.split("/")
    return parts[-1] if parts else ""


def ensure_dirs(snapshot_date: str) -> tuple[Path, Path]:
    raw_dir = RAW_ROOT / snapshot_date
    files_dir = raw_dir / "files"
    files_dir.mkdir(parents=True, exist_ok=True)
    PROCESSED_ROOT.mkdir(parents=True, exist_ok=True)
    KNOWLEDGE_NOTE.parent.mkdir(parents=True, exist_ok=True)
    return raw_dir, files_dir


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def summarize_profile(profile_rows: list[dict]) -> dict:
    if not profile_rows:
        return {}
    row = profile_rows[0]
    return {
        "name": " ".join(part for part in [row.get("First Name", ""), row.get("Last Name", "")] if part).strip(),
        "headline": (row.get("Headline") or "").strip(),
        "industry": (row.get("Industry") or "").strip(),
        "geo": (row.get("Geo Location") or "").strip(),
        "summary": (row.get("Summary") or "").strip(),
    }


def build_knowledge_note(
    snapshot_date: str,
    archive_rel: str,
    raw_files_rel: str,
    connections_rel: str,
    invitations_rel: str,
    profile: dict,
    normalized_connections: list[dict],
    normalized_invitations: list[dict],
) -> str:
    total_connections = len(normalized_connections)
    email_count = sum(1 for row in normalized_connections if row["email"])
    company_count = sum(1 for row in normalized_connections if row["company"])
    position_count = sum(1 for row in normalized_connections if row["position"])
    outgoing = [row for row in normalized_invitations if row["direction"] == "OUTGOING"]
    incoming = [row for row in normalized_invitations if row["direction"] == "INCOMING"]
    org_counts = Counter(row["company"] for row in normalized_connections if row["company"])
    month_counts = Counter(row["connected_on_iso"][:7] for row in normalized_connections)
    earliest = min(row["connected_on_iso"] for row in normalized_connections)
    latest = max(row["connected_on_iso"] for row in normalized_connections)

    lines = [
        "# LinkedIn Network",
        "",
        "> LinkedIn export snapshot imported into Habitect.",
        f"> Latest import: {snapshot_date}",
        "",
        "## Snapshot Files",
        f"- Raw archive: `{archive_rel}`",
        f"- Extracted export: `{raw_files_rel}`",
        f"- Normalized connections: `{connections_rel}`",
        f"- Normalized invitations: `{invitations_rel}`",
        "- Detailed person-level rows stay in the local ignored `data/` tree and are not pushed to the public repo.",
        "",
        "## Profile",
        f"- Name: {profile.get('name', 'Unknown')}",
        f"- Headline: {profile.get('headline', '') or 'N/A'}",
        f"- Location: {profile.get('geo', '') or 'N/A'}",
        f"- Industry: {profile.get('industry', '') or 'N/A'}",
        "",
        "## Relationship Summary",
        f"- Connections: {total_connections}",
        f"- Connections with public email: {email_count}",
        f"- Connections with company listed: {company_count}",
        f"- Connections with role listed: {position_count}",
        f"- Invitation records: {len(normalized_invitations)}",
        f"- Incoming invitations: {len(incoming)}",
        f"- Outgoing invitations: {len(outgoing)}",
        f"- Earliest connection in export: {earliest}",
        f"- Most recent connection in export: {latest}",
        "",
        "## Top Organization Clusters",
        "",
        "| Organization | Connections |",
        "| --- | ---: |",
    ]

    for org, count in org_counts.most_common(15):
        lines.append(f"| {org} | {count} |")

    lines.extend(
        [
            "",
            "## Connection Velocity",
            "",
            "| Month | New Connections |",
            "| --- | ---: |",
        ]
    )
    for month, count in sorted(month_counts.items(), reverse=True)[:12]:
        lines.append(f"| {month} | {count} |")

    return "\n".join(lines) + "\n"


def build_private_report(
    snapshot_date: str,
    normalized_connections: list[dict],
    normalized_invitations: list[dict],
) -> str:
    recent_connections = sorted(
        normalized_connections, key=lambda row: row["connected_on_iso"], reverse=True
    )[:50]
    outgoing = [row for row in normalized_invitations if row["direction"] == "OUTGOING"]
    recent_outgoing_with_message = [
        row for row in sorted(outgoing, key=lambda row: row["sent_at_iso"], reverse=True) if row["message"]
    ][:25]

    lines = [
        f"# LinkedIn Relationship Detail ({snapshot_date})",
        "",
        "> Local-only report generated from the LinkedIn export.",
        "> This file lives under ignored `data/processed/` and is not meant for GitHub sync.",
        "",
        "## Most Recent Connections",
        "",
        "| Connected On | Name | Company | Role | LinkedIn | Email |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in recent_connections:
        lines.append(
            f"| {row['connected_on']} | {row['full_name']} | {row['company'] or '-'} | {row['position'] or '-'} | {row['linkedin_url'] or '-'} | {row['email'] or '-'} |"
        )

    lines.extend(
        [
            "",
            "## Recent Outgoing Invitations With Notes",
            "",
            "| Sent At | To | Message | Profile |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in recent_outgoing_with_message:
        lines.append(
            f"| {row['sent_at']} | {row['counterparty_name']} | {row['message'].replace('|', '/')} | {row['counterparty_profile_url'] or '-'} |"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    zip_path = Path(args.zip_path).expanduser().resolve()
    if not zip_path.exists():
        raise SystemExit(f"Zip file not found: {zip_path}")

    snapshot_date = infer_snapshot_date(zip_path, args.snapshot_date)
    raw_dir, files_dir = ensure_dirs(snapshot_date)

    archive_dest = raw_dir / f"linkedin-export-{snapshot_date}.zip"
    shutil.copy2(zip_path, archive_dest)

    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(files_dir)
        profile_rows = list(csv.DictReader(zf.read("Profile.csv").decode("utf-8-sig").splitlines()))
        connections = read_csv_skip_preamble(zf, "Connections.csv", "First Name,Last Name")
        invitations = read_csv_skip_preamble(zf, "Invitations.csv", "From,To,Sent At")

    normalized_connections = []
    for row in connections:
        first_name = (row.get("First Name") or "").strip()
        last_name = (row.get("Last Name") or "").strip()
        full_name = " ".join(part for part in [first_name, last_name] if part).strip()
        connected_date = parse_connection_date(row["Connected On"])
        url = (row.get("URL") or "").strip()
        normalized_connections.append(
            {
                "full_name": full_name,
                "first_name": first_name,
                "last_name": last_name,
                "linkedin_url": url,
                "linkedin_handle": linkedin_handle(url),
                "email": (row.get("Email Address") or "").strip(),
                "company": (row.get("Company") or "").strip(),
                "position": (row.get("Position") or "").strip(),
                "connected_on": row["Connected On"].strip(),
                "connected_on_iso": connected_date.isoformat(),
            }
        )

    normalized_invitations = []
    for row in invitations:
        sent_at = parse_invitation_datetime(row["Sent At"])
        direction = (row.get("Direction") or "").strip()
        counterparty_name = (row.get("To") if direction == "OUTGOING" else row.get("From") or "").strip()
        counterparty_profile_url = (
            row.get("inviteeProfileUrl") if direction == "OUTGOING" else row.get("inviterProfileUrl") or ""
        ).strip()
        normalized_invitations.append(
            {
                "from_name": (row.get("From") or "").strip(),
                "to_name": (row.get("To") or "").strip(),
                "sent_at": row["Sent At"].strip(),
                "sent_at_iso": sent_at.isoformat(timespec="minutes"),
                "direction": direction,
                "message": (row.get("Message") or "").strip(),
                "inviter_profile_url": (row.get("inviterProfileUrl") or "").strip(),
                "invitee_profile_url": (row.get("inviteeProfileUrl") or "").strip(),
                "counterparty_name": counterparty_name,
                "counterparty_profile_url": counterparty_profile_url,
            }
        )

    connections_path = PROCESSED_ROOT / f"linkedin-connections-{snapshot_date}.csv"
    invitations_path = PROCESSED_ROOT / f"linkedin-invitations-{snapshot_date}.csv"
    private_report_path = PROCESSED_ROOT / f"linkedin-relationship-detail-{snapshot_date}.md"

    write_csv(
        connections_path,
        [
            "full_name",
            "first_name",
            "last_name",
            "linkedin_url",
            "linkedin_handle",
            "email",
            "company",
            "position",
            "connected_on",
            "connected_on_iso",
        ],
        normalized_connections,
    )
    write_csv(
        invitations_path,
        [
            "from_name",
            "to_name",
            "sent_at",
            "sent_at_iso",
            "direction",
            "message",
            "inviter_profile_url",
            "invitee_profile_url",
            "counterparty_name",
            "counterparty_profile_url",
        ],
        normalized_invitations,
    )

    note = build_knowledge_note(
        snapshot_date=snapshot_date,
        archive_rel=archive_dest.relative_to(REPO_ROOT).as_posix(),
        raw_files_rel=files_dir.relative_to(REPO_ROOT).as_posix(),
        connections_rel=connections_path.relative_to(REPO_ROOT).as_posix(),
        invitations_rel=invitations_path.relative_to(REPO_ROOT).as_posix(),
        profile=summarize_profile(profile_rows),
        normalized_connections=normalized_connections,
        normalized_invitations=normalized_invitations,
    )
    KNOWLEDGE_NOTE.write_text(note, encoding="utf-8")
    private_report_path.write_text(
        build_private_report(snapshot_date, normalized_connections, normalized_invitations),
        encoding="utf-8",
    )

    print(f"Imported LinkedIn export into snapshot {snapshot_date}")
    print(f"Archive SHA-256: {sha256(archive_dest)}")
    print(f"Raw files: {files_dir}")
    print(f"Connections CSV: {connections_path}")
    print(f"Invitations CSV: {invitations_path}")
    print(f"Private detail report: {private_report_path}")
    print(f"Knowledge note: {KNOWLEDGE_NOTE}")
    print(f"Connections: {len(normalized_connections)}")
    print(f"Invitations: {len(normalized_invitations)}")


if __name__ == "__main__":
    main()
