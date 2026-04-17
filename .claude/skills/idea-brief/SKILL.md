---
name: idea-brief
description: Write a 1-2 page decision brief on a potential business idea. Output is markdown at ideas/briefs/<name>.md, optionally synced to Google Docs via sync-gdocs.
---

# idea-brief

For deciding whether to pursue an idea, not for pitching it. Written for a cold reader (someone who saw a 3-sentence summary of the idea and nothing else).

**Deliverable:** `ideas/briefs/<name>.md`, ~1,500–2,000 words, portable (no founder-specific claims).

## Section spine

1. **What [X] is** — 100–150 words. Punchy, declarative. Lead with the thesis noun, not the brand name. Define one key term inline.
2. **Assumptions this brief rests on** — 5 bullets max, all "why the problem is real." Keep commercial/moat points out; they live in §7 (avoids redundancy that kept surfacing in Rubric).
3. **Why now** — bullets with demand signals, recent cases, displaced buyer cohorts. Every cited company/case gets a one-line gloss. Every stat gets an inline source link `[[source](url)]`.
4. **Who else is doing this** — grouped landscape (e.g., observability / eval / consultancy / labs). Name the most direct competitor and why it's direct. End with 2–3 structural gaps.
5. **What's technically ready, and what isn't** — split into "ready," "not ready," "the scarce asset."
6. **Where we could enter** — 3–4 angles, presented for assessment (not ranked) unless explicitly asked to commit. Include one explicit "not a candidate" to sharpen.
7. **What makes it defensible** — moat bullets. Cross-check against §2 for redundancy.
8. **How it could make money** — revenue layers as a table (`layer | price range | comparable`). Include an honest caveat with a cited source.
9. **What would pressure the thesis** — not "what would kill it." Each pressure paired with a counter-lever.
10. **What we don't know yet** — open research questions.

Footer: italicized notes (name collision, etc.). No H2 for tiny notes.

### Thesis / navigation variant

When the ask is "help me navigate a space and line up reading" (not go/no-go), swap the spine for: thesis → confluence of trends (don't force convergence) → categories needing attestation → toolkit → historical patterns → candidate actors → load-bearing open question → what would pressure the thesis → reading list (with 3–4 top picks up top). Longer than the decision brief (2,500–3,500 words) because the reading list carries the payoff.

## Voice rules specific to briefs

Applies on top of `vincent-voice` general rules.

- **Cold reader.** Define jargon (LLM-as-judge, FDE, harness, rubric) inline on first use. One-line gloss for every cited company/case.
- **Agnostic of the founder.** No "Vincent's X background is credible." The brief must stand independently.
- **Soften absolute claims.** "None ships a reliability answer" → "None ships a customer-operable improvement loop." Absolute forms get cut the moment a counter-example surfaces.
- **Every stat has a source.** Verify with the link-verifier subagent — broken or weak sources undermine the whole brief.
- **Kill criteria get reframed as pressures.** Most threats aren't fatal; pair each with the counter-lever.

## Iteration pattern

One revision per draft. Between drafts, spawn focused subagents — don't bundle jobs.

- **Research round** — parallel `general-purpose` subagents, one per research slice (competitive landscape, demand signals, tech maturity, regulatory, founder questions). Each ≤800 words, bulleted, cites URLs. Don't ask for prose.
- **Conceptual critic** — when you do a thesis pivot, test whether it lands through every section. The old framing hides in section 2 or 7.
- **Simplicity critic** — tune for a cold reader. Specify the persona ("just saw a 3-sentence summary, doesn't know X / Y / Z"). Limit to top 5–8 priorities.
- **Link-verifier** — WebFetch every inline source; confirm URL resolves AND content backs the claim. Swap weak ones; report a replacement. For long reading lists (20+ items), fan out to parallel subagents, one per section — single-agent coverage tends to miss fabricated workshop URLs, wrong author order, and stale book-page ISBNs.
- **Final polish** — one pass for fat, buried leads, stale framings. Output: SHIP / SHIP-WITH-MINOR-EDITS / ANOTHER-PASS.

Use `AskUserQuestion` only for founder-only judgment calls (lead-wedge choice, pricing anchor, scope-commit vs. explore). Don't use it for routine structure questions.

## Common pitfalls

- Presenting ranked wedges when the ask was exploratory. Present as angles unless explicitly asked to commit.
- Commercial bets duplicated in §Assumptions and §Defensibility. Assumption = problem-reality; Defensibility = moat.
- Precise numbers the cited source doesn't support (e.g., "$380K ACV"). Soften to a range or generalize.
- Dates attached to events the source doesn't confirm. Drop the dates, keep the claim.
- Name-dropping tools/techniques (DSPy, TextGrad, etc.) without gloss. Either cut or gloss.
- Hyperbolic qualifiers ("single most important," "the scariest"). Replace with specifics.
- Founder-background tie-ins that make the brief non-portable.

## Sync to Google Docs

Use the `sync-gdocs` skill. Briefs live in the `Briefs` subfolder (ID `1aYXSiOu85xKCBrsqRc5r3x4FhW5t3lPS`) under "Two Weeks Notice" in Drive. Track each new `driveFileId` in `.sync-state.json` under `ideas/briefs/<name>.md`.
