# Brand profile: <brand name>

One file per brand. Every skill in this pack reads it. Each editor gets only the sections its
lane needs, so keep the H2 names exactly as they are. Lines of the form `- key: value` are read
by the scripts; everything else is read by the editors.

Fill it with `newsroom-setup`, or by hand. Leave a section empty rather than guessing: the
editors say what they could not check, which is better than checking against an invented rule.

## Brand

What you sell, to whom, in two sentences. What you never want to be mistaken for.

## Audience

- Who reads: role, company size, what they are responsible for.
- What they already know (do not explain it to them).
- Their words for their own problem: list 5 to 10 phrases they actually use.
- Words that mark an outsider: phrases that make this reader stop trusting the text.
- Where they share things: the team chat, a forum, a newsletter.

## Formats

One `###` block per format you publish. The first word of the heading is the format key used by
`--format`. The scripts read `words`, `h2_max`, `summary` (required or optional: a TL;DR block, which
does not count toward `h2_max`), `summary_bullets` and `requires` (H2 names that must be present,
comma separated).

The summary block is not counted toward `h2_max`; the CTA section is. Keep this sentence: the
editors read the profile, not the script, and without it they count the summary.

### guide
For readers who are learning or fixing. Outcome title, summary block, steps in order, one limits
section, CTA.
- words: 1000-2000
- h2_max: 6
- summary_bullets: 3-6
- summary: required
- requires: When this does not apply

### comparison
For readers who are evaluating. Criteria first, one table, a verdict per use case.
- words: 1200-2400
- h2_max: 6
- summary: required
- requires: How we compared

### case
For readers who are deciding. Starting numbers, what changed, end numbers, what it cost.
- words: 800-1600
- h2_max: 5
- requires: The starting point, The result

### x-article
Long-form on X. See the `x-article` skill for the skeleton.
- words: 900-2200
- h2_max: 7

## Channels

- title_max: 70
- description_max: 155
- paragraph_max_sentences: 4
- Where it is published, and any platform rules (disclosure lines, link limits, image ratios).

## Voices

One `###` block per author. Write it from 5 or more real samples, not from how the author
would like to sound.

### <Author name>
- Opens with: (for example, a number from a real customer, or a one-line claim)
- Signature moves: (constructions this person uses often)
- Rhythm: (short and flat, or long with asides)
- Numbers: (always exact, or rounded with a source)
- Never says: (their personal banned list)

## Banned

Words and constructions that never ship, one per line:
- best-in-class
- cutting-edge
- next-generation
- in today's fast-paced world

## Proof

Claims the brand is allowed to make, each with its source and date. The claims auditor treats
anything not here, and not linked in the draft, as unsourced.

| Figure | What it measures | Source | Date |
|---|---|---|---|

## Links

Pages the drafts may link to, one per line. The link check uses this list and never guesses a
slug.

## CTA

- url: https://example.org/start
- max: 2
- The one action each piece asks for, and how it is worded.
