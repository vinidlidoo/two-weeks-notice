# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Two Weeks Notice — a 2-week business idea brainstorming sprint between Vincent and Pavan (UK-based). Vincent manages ideas as markdown files in this repo and syncs them to Google Drive (a Doc for the long list, a Sheet for consolidated cross-reactions) for collaborative review.

## Architecture

- `ideas/` — markdown files containing business ideas (source of truth); `ideas/consolidated.csv` is the seed for the shared reactions sheet
- `ideas/briefs/` — 1–2 page decision / thesis briefs per idea (see `idea-brief` skill); synced to the `Briefs` subfolder in Drive (ID `1aYXSiOu85xKCBrsqRc5r3x4FhW5t3lPS`)
- `.sync-state.json` — tracks sync state between local markdown and Google Docs (revision IDs, processed comments)
- `.claude/skills/sync-gdocs/` — project skill documenting the full sync workflow; includes `build_consolidated_sheet.py` for the reactions sheet
- `.claude/skills/gws-*/` — symlinks to `.agents/skills/` (installed via `npx skills add`)
- `skills-lock.json` — pins gws skill versions from the googleworkspace/cli repo

## Key workflow: markdown to Google Docs sync

The sync pipeline uses `pandoc` for format conversion and `gws` CLI for Google Drive operations. Full details in the `sync-gdocs` skill. The short version:

- **Push:** `pandoc md → docx` then `gws drive files update --upload`
- **Pull:** `gws drive files export` then `pandoc docx → md`
- **Comments:** `gws drive comments list` → insert as `<!-- FEEDBACK: ... -->` inline in markdown
- **Before pushing:** always check `.sync-state.json` revision against remote to avoid overwriting Pavan's changes

## Tools

- `gws` — Google Workspace CLI, authenticated via OAuth on `vincent.ethier.x@gmail.com` (separate account, project ID: `gg-workspacecli-ethv`)
- `pandoc` — markdown/docx conversion (`brew install pandoc`)
- `npx skills` — manages gws skill installation and updates (`npx skills update`)

## Conventions

- Google Doc comments from Pavan are reflected locally as `<!-- FEEDBACK: Author (date): "text" -->` (compatible with neovim review workflow)
- Markdown is the source of truth; the long-list Doc is read-only for collaborators (round-tripped via comments). The consolidated reactions Sheet is editable by Pavan (scoring + cell comments)
- Use `gws` commands with `dangerouslyDisableSandbox: true` (requires IPC/network access)
- The `gws drive` upload path must be relative to the current directory (not absolute/tmp paths)
