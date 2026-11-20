---
name: newsroom-setup
description: Sets up a brand for the newsroom pack by interviewing the owner and writing brand-profile.md - audience and their own words, formats with measurable limits, channel rules, banned list, a Proof table where every figure has a source and date, allowed links, the CTA - plus one voice profile per author built from 5 or more real writing samples. Use when someone starts with this pack, says "set up my brand", "make a brand profile", "add an author voice", or when another newsroom skill stops because brand-profile.md is missing.
---

# Newsroom setup

Every other skill in this pack reads one file: `brand-profile.md`. The editors are only as good
as what it says. This skill fills it by asking, not by guessing, and leaves a section empty when
the answer is not known. An empty section makes an editor say "not checked"; an invented rule
makes it enforce something nobody decided.

## Output

`brand-profile.md` in the project root (or the path the user gives), built from
`templates/brand-profile.md`. Keep its H2 names exactly; the scripts and the editor briefs find
sections by name.

## Procedure

### 1. Collect what already exists

Ask for these before asking any question. Most brands have half of the profile written down
somewhere.

- the website's home and pricing pages, or a product one-pager;
- a style guide or tone notes, if any;
- 3 published articles the owner considers good, and 1 they regret;
- the list of pages that articles may link to;
- any numbers the company already uses in sales: case studies, pilot reports, benchmarks.

Read them. Draft every section you can from them, and mark each line you inferred with
`(inferred)` so the owner can confirm or strike it.

### 2. Interview for the rest

Ask one block at a time, in this order, and write the answers straight into the file. Do not ask
a question the material already answered.

| Section | Ask |
|---|---|
| Brand | What do you sell, to whom? What would you hate to be mistaken for? |
| Audience | Who reads and decides? What do they already know? Which words do they use for their own problem? Which words make them stop reading? Where do they share links? |
| Formats | Which kinds of article do you publish? For each: the word range, how many sections at most, whether it opens with a summary, which section must always be there. |
| Channels | Where is it published? Title and description length limits? Any platform rules (disclosure, link limits, image ratio)? |
| Banned | Which words never ship? |
| Proof | Which figures can we use? For each: what it measures, where it comes from, the date. |
| Links | Which URLs may an article link to? |
| CTA | The one action you want from a reader, its URL, how many times per article at most. |

For **Audience**, push for the reader's own phrases. "Month-end" and "the shoebox" are useful;
"finance teams struggle with efficiency" is not. If the owner does not know, ask for 5 support
tickets, sales call notes or forum threads and take the phrases from those.

For **Proof**, a figure without a source does not go in the table. Put it under a line
`Not yet sourced:` so it is visible and not usable.

### 3. Voice profiles, from samples

One `### <Author name>` block under `## Voices` per author. Build it from 5 or more pieces that
author wrote without heavy editing. Fewer than 5 gives you the habits of one article.

Read the samples and fill each line with what the samples show, quoting a short example:

- **Opens with:** how the first paragraphs start, in 4 of 5 samples.
- **Signature moves:** constructions that recur in at least 3 samples.
- **Rhythm:** sentence length, asides, how sections end.
- **Numbers:** exact or rounded, and whether they come with a source.
- **Never says:** words this author avoids where others in the niche use them.

Write what the author does, not what they would like to do. If the owner wants a different voice
than the samples show, write the samples' voice and add a line `Wants to move toward:`; the
voice editor will flag the gap instead of pretending it is closed.

### 4. Check it

```bash
python3 skills/newsroom-review/scripts/structure_lint.py examples/northwind-ledger/draft-v1.md --profile brand-profile.md --format guide
```

Any draft will do. If the script errors on a format, a `- key: value` line is malformed or a
format heading is missing. Then show the owner the file and every `(inferred)` line, and remove
the marker on each line they confirm.

## Rules

- Never invent a figure, a rule or a voice trait. Leave it empty or mark it `(inferred)`.
- Keep the sentence about the summary block under `## Formats`: the editors read the profile
  text, and without it they count the summary as a section.
- One brand per file. A second brand gets its own file and its own `--profile`.
- Re-run step 3 when a new author joins, not the whole interview.

## Example

`examples/northwind-ledger/brand-profile.md` is a filled profile for an invented bookkeeping
company, with one voice, four formats, a Proof table and a CTA.
