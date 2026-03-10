# Habitect

## Overview
A second brain for managing agents, tools, and knowledge. The digital garden for AI ecosystems.

## Repos & Locations
- **Code**: `/Users/china/codeDev/habitect` — GitHub: `github.com/cyu60/habitect` (public)

## Architecture
- Agents defined as SKILL.md files (Claude Code skills system)
- Knowledge base in `knowledge/` directory
- Memory files in `memory/` directory
- Synced with `~/.claude/skills/` (skills) and `~/.claude/projects/*/memory/` (memory)

## Sync Strategy
Habitect is the **source of truth**. Data flows:
- **Obsidian** ↔ Habitect knowledge (goals, reflections, quarterly planning)
- **Notion** ↔ Habitect knowledge (team, tasks, meetings, projects)
- **Apple Notes** → GitHub backup (daily 11 PM) → searchable from Habitect
- **Gmail/Calendar** → accessed via gog CLI → daily digest
- **Browser history** → analyzed by browser-history agent → daily digest

## Current Focus
- Build out knowledge base as single source of truth
- Keep all sources (Obsidian, Notion, Apple Notes) synced
- Add knowledge layer that agents reference for context
