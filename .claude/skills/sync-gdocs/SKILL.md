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

| File | Google Doc ID |
|------|---------------|
| `ideas/long-list.md` | `1OET7Mr27hotxBqBJL6VDigKhXl4wg4Lk11HcXzzLLr0` |

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
