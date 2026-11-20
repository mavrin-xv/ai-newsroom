---
name: article-producer
description: Produces a publish-ready blog or Medium-style article for any brand from its brand-profile.md - brief, sourced draft, structure lint, the five-editor newsroom-review loop until SHIP, then the publish package (title and description measured, title variants, slug, links checked against an allowed list, alt text, a plain markdown export). Use when someone asks to write, rewrite or package an article, blog post, guide, comparison or case study, or to turn notes or a transcript into one.
---

# Article producer

Writing the draft is a third of the work. The rest is the part that goes wrong quietly: a
figure nobody can trace, a description cut off in search results, a link to a slug that does
not exist. This skill runs the whole line, with a script at each step that can be measured.

The brand comes from `brand-profile.md` (template: `templates/brand-profile.md`; fill it with
`newsroom-setup`).

## Inputs

- A topic or a source: notes, a transcript, a rough draft, a product change.
- `brand-profile.md`. Without it, stop and run `newsroom-setup`.
- The format key from the profile's `## Formats` (`guide`, `comparison`, `case` or yours).
- The author, if the profile has more than one voice.

## Procedure

### 1. Brief (five lines, before any prose)

```text
Reader:   <who, from the profile's Audience, and the job they are doing when they search>
Format:   <format key>, because <one line>
Promise:  <the outcome the title will state, with its figure>
Proof:    <the figures you will use, each from Proof or a source you have>
Ask:      <the profile's CTA>
```

If you cannot fill **Proof**, the article is not ready to write. Get the figures first.

### 2. Sources

Log every figure in `sources.md` (template: `templates/sources.md`) before drafting, using the
ladder in `skills/x-article/references/source-ladder.md`. Write each figure exactly as the draft
will write it.

### 3. Draft

Follow the format block in the profile: its `requires` sections, its `h2_max`, the summary
block if `summary: required`. Then these rules, which the editors will check anyway:

- The title states the outcome. The H1 repeats it.
- The first paragraph has the case or the number; no definition, no "in today's world".
- One idea per paragraph, within `paragraph_max_sentences`.
- Code and tables carry a label; images carry alt text that says what the image shows.
- One section on when the advice does not apply.
- The close is one next step, linked to the CTA, not a recap.
- Internal links only to pages in the profile's `## Links`.

### 4. Mechanical checks

```bash
S=skills/newsroom-review/scripts
python3 $S/structure_lint.py draft.md --profile brand-profile.md --format guide
python3 $S/claims_scan.py draft.md --sources sources.md --profile brand-profile.md
python3 skills/article-producer/scripts/link_check.py draft.md --profile brand-profile.md
```

Fix what they report before spending five editors on it. A draft that fails the lint will come
back with the same items from the structure editor.

### 5. Review loop

Run `newsroom-review` on the draft. Apply the chief editor's fix list in one pass, all blocking
items and all recommended ones, then run the next round with `--prev`. Stop at SHIP, or at the
round cap, and hand the open items to a person with the reason the loop did not close.

Do not argue with a finding in the draft's favour inside the loop. If an editor is wrong
because the profile is unclear, fix the profile and say so in the next review.

### 6. Publish package

Write `fields.md` next to the draft:

```text
title: <the H1, or a search title within title_max>
description: <one or two sentences with the figure, within description_max>
slug: <lowercase-words-with-hyphens>
variant: <alternative title>        (two or three, for testing or for social)
canonical: <https url, if the piece is published in more than one place>
```

Check it:

```bash
python3 skills/article-producer/scripts/seo_fields.py fields.md --profile brand-profile.md
```

Then add, in the handover:

- alt text for every image, and a one-line brief for any image still to make;
- the plain markdown export (the reviewed draft, front matter removed if the platform does not
  read it);
- for platforms that allow a subtitle, a subtitle within the band in `seo_fields.py --subtitle`.

### 7. Cross-posting

If the article also goes to a platform that bans or penalises certain things (affiliate links,
calls to action, AI disclosure rules, a link limit), read that platform's current rules before
posting and write them into the profile's `## Channels` with the date you checked. The scripts
read the `- key: value` lines there; everything else is for the person posting.

For X, use the `x-article` skill: it is a different format, not the blog post pasted in.

## Handover

```text
DRAFT:     <path>, <words> words, format <key>
REVIEW:    round <n>, <verdict>, <path to review.md>
FIELDS:    seo_fields <n FAIL>, link_check <n unknown>
SOURCES:   <n> figures, <n> unsourced
OPEN:      <anything a person must decide, or "none">
```

## Rules

- No figure without a source row. No source row without a link or a named document.
- No slug guessed. If the page you want to link is not in `## Links`, ask for it or leave it out.
- The review loop applies fixes; it does not negotiate with them.
- Never publish. Hand the package to a person.

## Example

`examples/northwind-ledger/` holds the whole line for an invented bookkeeping company: the
profile, `draft-v1.md` (flawed on purpose), `draft-v2.md` and `draft-v3.md`, three review
rounds in `run-1/` to `run-3/`, `sources.md`, and `fields.md` (with one duplicate variant left
in on purpose, so `seo_fields.py` has something to catch).
