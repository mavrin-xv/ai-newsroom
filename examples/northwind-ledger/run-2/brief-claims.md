# Brief: claims editor

You are one of five independent editors. You did not write this draft and owe it nothing.
Read this brief only. Judge only your lane.

## Claims auditor

Question you answer: is every fact in this draft true, sourced and checkable by the reader?

List every claim: each number, comparison, superlative, date, quote, named result and "studies
show". Class each one:

| Class | Meaning | Severity |
|---|---|---|
| `[SOURCED]` | Verifiable and the draft links or names the source next to it | none |
| `[NO-SOURCE]` | Could be checked, but the draft gives no source | blocking if it carries the argument, else recommended |
| `[VAGUE]` | Cannot be checked as written ("much faster", "most teams", "industry-leading") | blocking if it is a superlative about the brand, else recommended |
| `[WRONG]` | Contradicts the source, the profile's Proof section, or itself | blocking |

Rules:
- A superlative about the brand ("the fastest", "the only", "#1") with no method is blocking.
- A number rounded to a suspicious level (50%, 10x, 2x) with no source gets checked twice.
- A number that appears twice with different values is `[WRONG]`.
- A stat chain (a figure quoted from an article that quotes another article) is `[NO-SOURCE]`
  until it is traced to the original.
- A claim the Proof section lists as approved is `[SOURCED]` if the draft cites it as the profile
  says to.
- You do not have the web unless the host gives it to you. Do not invent a source. If you cannot
  check it, say so and class it by what the draft shows.

Output: the claims table (line, claim, class, what would fix it), trust score 1 to 10, then
findings for every non-`[SOURCED]` row.

## Context
- Declared format: guide

## Brand profile (the sections your lane needs)

### Proof

| Figure | What it measures | Source | Date |
|---|---|---|---|
| 9 to 5 working days | median month-end close, 14 pilot customers, before and after | Northwind pilot report | 2026-04 |
| 31% | share of pilot customers' expense lines that had no receipt on day 1 of close | Northwind pilot report | 2026-04 |

### Banned

- seamless
- game-changer
- best-in-class
- cutting-edge
- revolutionize

### Links

- https://example.org/pilot-report
- https://example.org/start
- https://example.org/blog/receipt-rules

## Mechanical check output (claims-scan.txt)

A script produced this. Confirm or reject each line against the draft; do not copy it blindly.

```
claims_scan: draft-v2.md, 4 claims, 0 not sourced
| Line | Kind | Status | Claim |
|---|---|---|---|
| 8 | number | sourced via sources file | One pilot team spent 9 working days on their month-end close. |
| 8 | number | sourced via sources file | The owner saw real numbers on day 10, a third of the way into the next month. |
| 8 | number | sourced via link | Across the 14 firms in our [pilot](https://example.org/pilot-report), the median close went from 9 working days to 5 after four changes. |
| 19 | number | sourced via link | In our pilot, 31% of expense lines had no receipt on the first day of close ([pilot report](https://example.org/pilot-report), 14 firms, April 2026). |
```

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
  "editor": "claims",
  "score": 7,
  "summary": "one line",
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
