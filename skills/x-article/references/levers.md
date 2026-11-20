# Seven levers

These are working rules collected from long-form posts that readers saved and shared, plus the
X help pages and posting guides listed in the README credits. They are heuristics, not measured
effects. When your own numbers disagree with a lever, your numbers win.

## 1. Title

The reader decides from the title. Three ingredients, at least two in every title:

- a precise outcome or figure ("in 5 working days", "3 changes");
- a scope tag that tells the reader how complete it is ("full checklist", "with the config");
- a named source or a counter-claim when there is no figure ("What the 2025 survey actually
  says").

Titles that lose: "A guide to X", "Thoughts on X", "Why X matters". They promise a topic, not a
result.

`x_article_check.py` fails a title over 100 characters and warns on a title with no figure.

## 2. Hook (the first three lines)

Two moves work, and both land before line three:

- **The gap.** Show the reader that their current way costs them, with one concrete case.
  "Nine working days. The owner saw the month's numbers on day ten."
- **The scale.** One figure that earns the right to teach. "We read 140 support tickets about
  month-end before writing this."

Never open on a definition, on "in today's world", or on a question the reader did not ask.

## 3. Structure

The format sets the depth (see `format-templates.md`). Within a format, repeat one shape per
section. A reader can get through 2,000 words when every section is built the same way, because
they know where the useful line is.

## 4. Specifics

- Name every tool, setting and step. "A checklist" is weaker than the five lines of the
  checklist.
- Attach a figure and a source to every claim. If you cannot source it, cut it or say that it
  is your own count and how you counted.
- Put at least one thing in the article the reader can copy: a config, a prompt, a checklist,
  a command. The checker warns when there is none.

## 5. Proof

- Put the receipts before the ask. The bigger the ask, the more proof comes before it.
- Show the method and one caveat that works against you. "The headline figure is the median;
  three of the 14 firms did not improve." Sceptical readers trust a writer who discounts their
  own number.
- For investigations, add what would prove you wrong.

## 6. Formatting

- Paragraphs of one to three sentences. The checker fails a paragraph over `--max-sentences`.
- Bold sub-heads, numbered lists, a code block where there is something to copy.
- One link per paragraph at most. Several links in one paragraph read as a sales page.

## 7. Close

The article is the funnel. From softest to hardest:

1. Save, repost, follow: the right close for a roundup.
2. The next piece: "the comparison of the three tools is next week".
3. A reply keyword ("reply CHECKLIST and I will send the file"): only for brands where this
   fits; many B2B and technical brands should not use it.
4. A link to the full version or the product.

Say first that the article stands on its own, then ask. Plant one or two forward references in
the body ("more on the bank match below") so the reader keeps going.

Point every close at the profile's `## CTA` and respect its `max`.
