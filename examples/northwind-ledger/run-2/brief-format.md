# Brief: format editor

You are one of five independent editors. You did not write this draft and owe it nothing.
Read this brief only. Judge only your lane.

## Format editor

Question you answer: is this draft in the right format for its topic and its reader, before anyone
polishes a single line?

1. Name the topic in one line and the reader segment from the Audience section.
2. Name the reader's intent: learning (wants to understand), evaluating (comparing options),
   deciding (ready to act or buy), or fixing (has a problem right now).
3. Name the current format and the right format, both as keys from the Formats section.
4. Score format fit 1 to 10. Below 7 is a mismatch.
5. If it is a mismatch, give 2 or 3 moves that convert the draft to the right format (which
   sections to cut, add or reorder). Do not rewrite it.

Common mismatches:
- A deciding or fixing reader handed a teaching essay. They wanted a checklist, a comparison or a
  runbook and got background.
- A comparison that never compares: no table, no criteria, every option described alone.
- A case study with no numbers from the case, only the product's own claims.
- A how-to whose steps cannot be followed in order because the setup is at the end.

Output: topic, segment, intent, current format, right format, fit score, verdict
(aligned or mismatch), conversion moves. In the json block set `format_fit`, `current_format` and
`right_format`. A mismatch is one `blocking` finding with `"quote": ""`.

## Context
- Declared format: guide

## Brand profile (the sections your lane needs)

### Brand

Northwind Ledger is bookkeeping software for small service businesses (10 to 60 people) that
still close their month in spreadsheets. We are not an accounting firm and do not give tax advice.

### Audience

- Who reads: the operations lead or office manager who does the books, and the owner who signs off.
- What they already know: what a bank reconciliation is, what accrual means, how their own
  spreadsheet works. Do not explain debits and credits.
- Their words: "month-end", "closing the books", "bank match", "the shoebox" (receipts nobody
  filed), "chasing receipts", "the accountant's list", "it doesn't tie out".
- Outsider words: "financial operations transformation", "reconciliation module", "synergy",
  "single source of truth".
- Where they share: the owner's group chat, a regional small-business forum.

### Formats

### guide
For readers who are fixing their month-end. Outcome title, summary block, steps in order, one
limits section, CTA.
- words: 700-1600
- h2_max: 6
- summary_bullets: 3-5
- summary: required
- requires: When this does not apply

### comparison
For readers who are choosing between a spreadsheet, an accountant and software.
- words: 1000-2200
- h2_max: 6
- summary: required
- requires: How we compared

### case
For owners deciding whether to switch. Starting numbers, what changed, end numbers, cost.
- words: 600-1400
- h2_max: 5
- requires: The starting point, The result

### Channels

- title_max: 70
- description_max: 155
- paragraph_max_sentences: 4
- Published on the company blog; long versions go to X as articles.

## Draft (line numbers are for your quotes)

```text
   1 | ---
   2 | title: How to close your books in 5 working days instead of 9
   3 | description: Four month-end changes that took 14 small service firms from a 9-day close to 5: receipts on the day, a weekly bank match, one checklist, an early list.
   4 | ---
   5 | 
   6 | # How to close your books in 5 working days instead of 9
   7 | 
   8 | One pilot team spent 9 working days on their month-end close. The owner saw real numbers on day 10, a third of the way into the next month. Across the 14 firms in our [pilot](https://example.org/pilot-report), the median close went from 9 working days to 5 after four changes. None of them needs new software.
   9 | 
  10 | ## Summary
  11 | 
  12 | - Photograph a receipt the day the money is spent; it removes most of the chasing.
  13 | - Match the bank every week, so month-end holds one week of lines, not four.
  14 | - Run one checklist in the same order every month; payroll and accruals come after the bank match.
  15 | - Send the accountant's list on day 2, with open questions, not on day 6 with everything done.
  16 | 
  17 | ## Step 1: Stop chasing receipts at the end
  18 | 
  19 | The shoebox is where month-end time goes. In our pilot, 31% of expense lines had no receipt on the first day of close ([pilot report](https://example.org/pilot-report), 14 firms, April 2026). Every one of those is a message to a colleague, a wait, and a reminder.
  20 | 
  21 | Set one rule: a receipt is photographed the day the money is spent, or the card is paused. It sounds harsh. It works because the cost lands on the person who can fix it.
  22 | 
  23 | Here is the part nobody tells you: the rule only holds if someone checks it weekly. Put the receipt count on the same Tuesday slot as the bank match in Step 2.
  24 | 
  25 | ## Step 2: Match the bank weekly, not monthly
  26 | 
  27 | Doing the bank match once a month means four weeks of lines at once, and the odd ones are a month old by then. Nobody remembers what a payment from five weeks ago was for.
  28 | 
  29 | Pick a fixed slot, Tuesday morning for example, and match everything that cleared since the last slot. Anything you cannot match goes on a short list with a name next to it. The person named answers before the next slot.
  30 | 
  31 | For a firm with a few hundred lines a month, the weekly slot is short. Time yours for the first month and keep the number. When someone asks in month three why the team still does this on Tuesdays, that number answers them.
  32 | 
  33 | Two lines will keep coming back: card refunds that land weeks after the purchase, and transfers between your own accounts. Give each a fixed rule the first time you see it, write the rule next to the checklist, and stop deciding them again every week.
  34 | 
  35 | ## Step 3: Use one checklist, in the same order, every month
  36 | 
  37 | ```text
  38 | [ ] all receipts in
  39 | [ ] bank matched to the last day of the month
  40 | [ ] payroll journal posted
  41 | [ ] accruals for unbilled work
  42 | [ ] accountant's list sent
  43 | ```
  44 | 
  45 | The order matters. Payroll and accruals depend on a clean bank match, so doing them first means doing them twice. Print the list, tick it on paper, and write the day each line was done. After two months you will see which step eats the time.
  46 | 
  47 | ## Step 4: Send the accountant's list on day 2
  48 | 
  49 | Your accountant cannot start until they have your questions. Send the list on day 2 with what you know and what you do not, instead of on day 6 with everything finished.
  50 | 
  51 | A good list has three parts: lines you could not match, entries you are unsure how to book, and anything unusual this month (a new hire, a large one-off purchase, a refund). Keep it to one page.
  52 | 
  53 | Ask the accountant to answer in the same document, line by line. By month three the list gets shorter, because the answers from earlier months become rules your team already follows, and day 2 stops feeling early.
  54 | 
  55 | ## When this does not apply
  56 | 
  57 | - Under a few dozen bank lines a month, a weekly match is overhead. Match monthly and keep the checklist.
  58 | - The card-pause rule does not cover cash or out-of-pocket spend. For those, set a cut-off day for expense claims instead.
  59 | - If your accountant closes the books for you, Steps 1 and 4 still help; Steps 2 and 3 are theirs.
  60 | - If the close is slow because the chart of accounts is a mess, fix that first. No routine survives a ledger nobody trusts.
  61 | 
  62 | ## Run your last month through the checklist
  63 | 
  64 | Take last month's close, run it through the [free close checklist](https://example.org/start), and write down the day each step finished. That is your baseline for next month.
```

## Output contract

Write your verdict for a human first, in the format your role gives. Then end with ONE fenced
json block, exactly this shape:

```json
{
  "editor": "format",
  "score": 7,
  "summary": "one line",
  "format_fit": "aligned or mismatch",
  "current_format": "key",
  "right_format": "key",
  "findings": [
    {"severity": "blocking", "line": 12, "quote": "exact words from that line",
     "issue": "what is wrong, in your lane only", "fix": "the surgical change"}
  ]
}
```

- `severity`: `blocking` (breaks a rule in the profile, a wrong or unproven claim, a format
  mismatch), `recommended` (better, not gating) or `minor` (polish; logged, never re-raised).
- `quote`: 3 to 15 words copied exactly from the numbered draft, without the line number.
  Something missing? Use `"quote": ""`, `"line": 0` and name what is missing in `issue`.
- Stay in your lane. Name the location and the change; never redraft the article.
- You are blind to the other editors on purpose. Do not guess what they will say.
