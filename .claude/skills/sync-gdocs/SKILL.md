---
name: sync-gdocs
description: "Sync markdown files to/from Google Docs via pandoc and gws CLI."
---

# sync-gdocs

Sync markdown files to Google Docs with rich formatting (headings, bold, italic, lists). Uses [pandoc](https://pandoc.org/) for conversion and [gws CLI](../gws-shared/SKILL.md) for Google Drive operations.

## Prerequisites

- `pandoc` on `$PATH` (`brew install pandoc`)
- `gws` authenticated (see [gws-shared](../gws-shared/SKILL.md))

## Workflow

Markdown is the source of truth. Google Docs are for sharing with collaborators.

**Before any push:** check `.sync-state.json` for an existing fileId for the target markdown file. If one exists, use the update flow below — do not create a new doc. Only use "Create new" when no mapping exists.

**Side effect:** `gws drive files update` and `gws drive files delete` both emit a stray `download.html` in the working directory. `rm -f download.html` after these commands.

### Create a new Google Doc from markdown

```bash
pandoc <file>.md -f markdown-auto_identifiers -t docx -o <file>.docx
gws drive files create --upload <file>.docx --json '{"name": "<title>", "mimeType": "application/vnd.google-apps.document"}'
rm <file>.docx
```

Returns a file ID — save it for future updates.

**Fallback if create-with-conversion 500s:** on some files the inline docx→Google-Doc conversion endpoint returns 500 Internal Error consistently (raw docx upload still works). Upload as raw docx, then copy with conversion and delete the intermediate:

```bash
gws drive files create --upload <file>.docx --json '{"name": "<file>.docx", "parents": ["<FOLDER_ID>"]}'
gws drive files copy --params '{"fileId": "<RAW_ID>"}' --json '{"name": "<title>", "mimeType": "application/vnd.google-apps.document", "parents": ["<FOLDER_ID>"]}'
gws drive files delete --params '{"fileId": "<RAW_ID>"}'
rm -f download.html
```

### Update an existing Google Doc

```bash
pandoc <file>.md -f markdown-auto_identifiers -t docx -o <file>.docx
gws drive files update --params '{"fileId": "<ID>"}' --upload <file>.docx
rm <file>.docx
```

Overwrites the remote doc. Same file ID, sharing settings preserved.

### Download a Google Doc to markdown

```bash
gws drive files export --params '{"fileId": "<ID>", "mimeType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"}' -o <file>.docx
pandoc <file>.docx -f docx -t markdown -o <file>.md
rm <file>.docx
```

### Delete a Google Doc

See [gws-drive](../gws-drive/SKILL.md) — `gws drive files delete --params '{"fileId": "<ID>"}'`

## Round-trip notes

- Em dashes (`—`) become `---` after round-trip
- Pandoc wraps lines at ~72 chars and adds blank lines between sub-bullets
- Content and structure (headings, bold, lists) are preserved

## Known file IDs

All three live in the **Two Weeks Notice** Drive folder (`1NzihlB_n-QckL3BqCvAhNTlVh9OqO-nK`).

| Local | Drive name | Drive ID | Type |
|-------|------------|----------|------|
| `ideas/long-list.md` | Vincent List | `1OET7Mr27hotxBqBJL6VDigKhXl4wg4Lk11HcXzzLLr0` | Doc |
| `ideas/consolidated.csv` | Consolidated List | `1tLzDlkEeTDjlhpJdibZ9By0At9NQ-IVtwiiPXRxybt0` | Sheet |
| (Pavan's) | Pavan List | `1CmmEBEIZkJENpbNQjNkISf56WytaqMfkk8_eEWGVNXE` | Sheet (owned by Pavan; in folder via shortcut `1dKDf8RjwTL_K8jCuW8u9xi2fa8cu3mHL`) |

## Consolidated reactions sheet

Regenerate `ideas/consolidated.csv` from `ideas/long-list.md` (V rows) plus hardcoded P rows:

```bash
python3 .claude/skills/sync-gdocs/build_consolidated_sheet.py
```

Caveat: P rows are hardcoded in the script. Re-pull from Pavan's "Ideation April 2026" → `Ideas` tab and update the script if his list changes.

### Writing formulas to a sheet

Use `valueInputOption=USER_ENTERED` or `=` is stored as literal text:

```bash
gws sheets spreadsheets values update --params '{"spreadsheetId":"<ID>","range":"G2:G48","valueInputOption":"USER_ENTERED"}' --json '{"values":[["=..."], ["=..."]]}'
```

Caveat: dropdown cells store values as strings even when the options are numeric. Wrap with `N()` for safe numeric comparison and to treat empty as 0, e.g. `=IF(AND(N(E2)>=4, N(F2)>=4), "🎯", "")`.

### Moving files you don't own

Drive enforces a single parent per file. To move a file owned by someone else into your folder, `addParents` fails with `cannotAddParent` (you can't see/remove the owner's parent). Workaround: create a shortcut in your folder pointing to the file:

```bash
gws drive files create --json '{"name": "Display Name", "mimeType": "application/vnd.google-apps.shortcut", "parents": ["<FOLDER_ID>"], "shortcutDetails": {"targetId": "<FILE_ID>"}}'
```

Renames on the original file still work via `files update --json '{"name": "..."}'` if you have editor access, but be aware the rename is visible to the owner.

### Mapping Sheet comments to cells (anchors are opaque)

UI-created Sheet comments return an opaque `{"type":"workbook-range","range":"<integer>"}` anchor that no API (Drive or Sheets) decodes to a cell. See the memory note `reference_gsheets_comment_anchors.md` for the full rationale and links.

**Workaround used here:** drop comments in list-order, then snapshot the mapping by `createdTime`. Steps:

1. When commenting on a list of items, leave comments top-to-bottom with no skips (one per item).
2. Pull all comments with `pageSize:100` (default is 20 — will silently truncate):

   ```bash
   gws drive comments list --params '{"fileId":"<ID>","pageSize":100,"fields":"comments(id,content,anchor,createdTime,author(displayName))"}'
   ```
3. Sort by `createdTime` ascending — the i-th comment pairs with the i-th item in your known list order.
4. Persist the mapping (comment ID → item name + row) so replies can be tracked without re-inferring. For the consolidated sheet, this lives in `ideas/consolidated_comments.json`.

Caveat: only works when the commenter actually goes in order. If Pavan replies threaded to existing comments, those replies attach to the parent comment ID (not new top-level comments) so they don't break the order. But if he adds a brand-new top-level comment out of order, content-based inference is still needed.

## Sync state

State is tracked in `.sync-state.json` at the project root. Each file entry has:

- `driveFileId` — Google Doc ID
- `lastPushRevisionId` — revision ID at the time of last push
- `lastPushTime` — timestamp of last push
- `lastPullTime` — timestamp of last pull
- `processedCommentIds` — comment IDs already pulled into markdown

### Before pushing: check for remote changes

```bash
gws drive revisions list --params '{"fileId": "<ID>", "fields": "revisions(id,modifiedTime)"}'
```

Compare the latest revision ID against `lastPushRevisionId` in `.sync-state.json`:

- **Same** → safe to push
- **Different** → collaborator (Pavan) made changes → pull first, review diff, merge, then push

### After pushing: update state

Update `.sync-state.json` with the new revision ID and timestamp. Get the new revision:

```bash
gws drive revisions list --params '{"fileId": "<ID>", "fields": "revisions(id,modifiedTime)"}'
```

### After pulling comments: update state

Add processed comment IDs to `processedCommentIds` to avoid re-inserting them on next pull.

## Comments

Pushing a new file version via `files update --upload` replaces the entire doc and wipes existing comments. To preserve comment threads across pushes, use the full round-trip flow below.

### Full comment round-trip flow

1. **Pull comments** — save to `.sync-state.json` and insert as `<!-- FEEDBACK -->` in markdown
2. **Make content edits** in markdown, decide on replies
3. **Push updated content** (replaces doc, wipes comments)
4. **Re-create comments** via API, anchored to the same text in the new doc
5. **Add replies** to re-created comments
6. **Resolve** any that are done

### 1. Pull comments

```bash
gws drive comments list --params '{"fileId": "<ID>", "fields": "comments(id,content,quotedFileContent,resolved,author(displayName),createdTime,replies(content,author(displayName),createdTime))"}'
```

Save the full comment data (content, quotedFileContent, author, replies) to `.sync-state.json` under `pendingComments` before pushing. Insert into markdown:

```markdown
- **Idea Name** — one-line rationale
  <!-- FEEDBACK: Author Name (YYYY-MM-DD): "comment text" -->
  - What: ...
```

### 4. Re-create comments after push

```bash
gws drive comments create --params '{"fileId": "<ID>", "fields": "id,content,quotedFileContent"}' --json '{"content": "[Pavan]: original comment text", "quotedFileContent": {"mimeType": "text/html", "value": "anchored text"}}'
```

Prefix with `[Pavan]:` (or original author name) since all API-created comments show as the OAuth account (`vincent.ethier.x@gmail.com`).

### 5. Add replies

```bash
gws drive replies create --params '{"fileId": "<ID>", "commentId": "<NEW_COMMENT_ID>", "fields": "id,content"}' --json '{"content": "reply text"}'
```

`fields` param is required by the API — `"id,content"` is the minimum.

### 6. Resolve comments

```bash
gws drive replies create --params '{"fileId": "<ID>", "commentId": "<COMMENT_ID>", "fields": "id,content"}' --json '{"content": "Resolved", "action": "resolve"}'
```

Using `replies create` with `"action": "resolve"` resolves the comment in a single call.

## See also

- [gws-shared](../gws-shared/SKILL.md) — Auth and global flags
- [gws-docs](../gws-docs/SKILL.md) — Google Docs API
- [gws-drive](../gws-drive/SKILL.md) — Google Drive API
- [gws-drive-upload](../gws-drive-upload/SKILL.md) — Upload helper
