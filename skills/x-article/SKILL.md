---
name: x-article
description: Write an X (Twitter) long-form article for any brand from its brand-profile.md - pick one of five formats by intent, build title, hook, body and close with seven levers, source every figure, then check title length, 5:2 cover, paragraph length, links and CTA with a script. Use when someone asks for an X article, a long-form X post, an X essay, or to turn a blog post or idea into an X article.
---

# X article

An X article is read on a phone, by someone who did not plan to read it. It earns the next line
or loses the reader. This skill writes one article for one brand, in one of five formats, and
checks the measurable parts before the author pastes it.

The brand comes from `brand-profile.md` (template: `templates/brand-profile.md`; fill it with
`newsroom-setup`). Nothing about voice, audience or CTA is hard-coded here.

## Inputs

- The topic, and what the article has to do: reach, trust, shares or teaching one skill.
- `brand-profile.md`: audience, voice, banned list, Proof table, CTA.
- Source material: notes, data, a blog post to adapt. Adapting means a new angle and hook for X,
  not the blog post pasted in.

If the profile is missing, stop and run `newsroom-setup`, or ask for the five fields this skill
cannot work without: audience, author voice, banned words, CTA url, what counts as proof.

## Procedure

1. **Pick the format.** One of five in `references/format-templates.md`, by the job:

   | Job | Format |
   |---|---|
   | reach and saves | Roundup |
   | authority | System |
   | trust with sceptical readers | Investigation |
   | shares | Case |
   | teach one skill | Before and after |

   Write one line on why this format. If two fit, take the one whose proof you actually have.

2. **Collect the figures first.** Climb `references/source-ladder.md` and log every figure in
   `sources.md` before drafting. A technical or niche topic needs current, named tools and real
   numbers; generic advice is the failure this step prevents.

3. **Draft the six parts**, using the levers in `references/levers.md`:

   ```text
   1. Title     outcome or figure + scope tag (or a named source / counter-claim)
   2. Hook      the gap or the scale, before line 3
   3. Reframe   why the old way breaks: one case, one number
   4. Body      the format's skeleton; at least one block the reader can copy
   5. Payoff    what gets better over time, or what the reader can do tomorrow
   6. Close     says the article stands alone, then one ask from the profile's CTA
   ```

4. **Apply the profile.** Author voice from `## Voices`, nothing from `## Banned`, only figures
   from `## Proof` or `sources.md`, CTA from `## CTA` within its `max`.

5. **Check the measurable parts.**

   ```bash
   python3 skills/x-article/scripts/x_article_check.py article.md --profile brand-profile.md
   python3 skills/newsroom-review/scripts/claims_scan.py article.md --sources sources.md --profile brand-profile.md
   ```

   Fix every FAIL. Read every WARN and decide.

6. **Review.** Run `newsroom-review` with `--format x-article` (add an `### x-article` block to
   the profile if it has none). Act on the verdict.

7. **Hand over** in this shape:

   ```text
   TITLE: <title>
   FORMAT: <format>, <one line why>
   COVER: <what the 5:2 cover shows, and its alt text>

   <the article>

   ---
   CTA: <the exact closing line>
   FIRST REPLY: <one reply the author posts under the article within minutes: an unfinished
                 thought or the question the article did not answer>
   CHECKS: x_article_check <n FAIL>, claims_scan <n unsourced>, review <verdict>
   ```

## Platform facts

Checked 2026-11 against help.x.com (Articles). Recheck before relying on them; platforms change.

- Articles are a feature of paid X plans; the author's account needs one to publish.
- The cover image is shown at 5:2. `x_article_check.py` checks the ratio from the file or from
  `cover_size:` in the front matter.
- Articles support headings, bold, lists, quotes, images, video, links and embedded posts.
- The title the checker uses is the front matter `title`, or the first H1.

## Rules

- One format per article.
- Every figure has a row in `sources.md`, or it is cut.
- At least one block the reader can copy: a checklist, a config, a prompt, a command.
- Paragraphs of one to three sentences; one link per paragraph.
- The close says the piece stands on its own before it asks.
- Match the register to the reader. Technical and finance readers punish hype faster than
  dryness.
- Do not import engagement tricks (reply gates, "like if you agree") into a brand whose profile
  bans them.

## Failure patterns

| Pattern | Fix |
|---|---|
| Title names a topic ("A guide to month-end") | Put the outcome or figure in it |
| Three lines of context before the point | Open on the case or the number |
| "Much faster", "huge savings" | The measured figure and its source |
| Nothing to copy | Add the checklist or config the body describes |
| The blog post pasted in | New hook and angle; cut what only works on the blog |
| Hard pitch in the first half | Move the ask to the end, after the proof |

## Example

`examples/northwind-ledger/x-article.md` is a System-format article adapted from the Northwind
guide. Check it:

```bash
python3 skills/x-article/scripts/x_article_check.py examples/northwind-ledger/x-article.md --profile examples/northwind-ledger/brand-profile.md
```
