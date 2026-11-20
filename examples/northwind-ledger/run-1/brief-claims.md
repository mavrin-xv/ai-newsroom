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
claims_scan: draft-v1.md, 9 claims, 7 not sourced
| Line | Kind | Status | Claim |
|---|---|---|---|
| 19 | vague | vague | Most teams spend far too long on month-end. |
| 19 | number, research | unsourced | Studies show that small businesses lose 50% of their finance time to manual work. |
| 19 | number | unsourced | With Northwind Ledger, teams cut close time in half! |
| 19 | superlative | unsourced | Our reconciliation module is the fastest way to tie out your accounts. |
| 19 | number | sourced via sources file | The median close in our pilot went from 9 working days to 5. |
| 23 | number, superlative | sourced via sources file | In our pilot, 31% of expense lines had no receipt on the first day of close. |
| 29 | number | unsourced | Weekly, it is a 20-minute job, and the odd line is still fresh in someone's memory. |
| 43 | number, vague | unsourced | Most teams that close in 7 working days follow a list like this one. |
| 51 | superlative | unsourced | Northwind Ledger is the best-in-class tool to help you do all of it. [Start your free close checklist](https://example.org/start). |

Same metric, different figures (check which is right):
- working days: 7 (line 43), 9 (line 19)
```

## Draft (line numbers are for your quotes)

```text
   1 | ---
   2 | title: The Ultimate Guide to Closing Your Books Faster With a Seamless Month-End Process
   3 | description: Learn how small service businesses can close the books faster with better receipt handling, bank matching and a clear month-end checklist that the whole team can follow.
   4 | ---
   5 | 
   6 | # The Ultimate Guide to Closing Your Books Faster With a Seamless Month-End Process
   7 | 
   8 | Month-end close is the process of reviewing, reconciling and finalising a company's accounts at the end of each month. For small service businesses it is often slow and painful.
   9 | 
  10 | ## TL;DR
  11 | 
  12 | - Receipts
  13 | - Bank matching
  14 | - A checklist
  15 | - Software helps
  16 | 
  17 | ## Introduction
  18 | 
  19 | Most teams spend far too long on month-end. Studies show that small businesses lose 50% of their finance time to manual work. Additionally, the longer the close takes, the later the owner sees real numbers, and the later the decisions get made. With Northwind Ledger, teams cut close time in half! Our reconciliation module is the fastest way to tie out your accounts. The median close in our pilot went from 9 working days to 5. It is worth noting that every business is different. Some will see more improvement than others. This guide walks you through the steps.
  20 | 
  21 | ## Step 1: Stop chasing receipts at the end
  22 | 
  23 | The shoebox is where month-end time goes. In our pilot, 31% of expense lines had no receipt on the first day of close. Every one of those is a message to a colleague, a wait, and a reminder.
  24 | 
  25 | Set one rule: a receipt is photographed the day the money is spent, or the card is paused. It sounds harsh. It works because the cost lands on the person who can fix it.
  26 | 
  27 | ## Step 2: Match the bank weekly, not monthly
  28 | 
  29 | Doing the bank match once a month means four weeks of lines at once. Weekly, it is a 20-minute job, and the odd line is still fresh in someone's memory.
  30 | 
  31 | Pick a fixed slot, Tuesday morning for example, and match everything that cleared since the last slot. Anything you cannot match goes on a short list with a name next to it.
  32 | 
  33 | ## Step 3: Use one checklist, in the same order, every month
  34 | 
  35 | ```
  36 | [ ] all receipts in
  37 | [ ] bank matched to the last day
  38 | [ ] payroll journal posted
  39 | [ ] accruals for unbilled work
  40 | [ ] accountant's list sent
  41 | ```
  42 | 
  43 | The order matters. Payroll and accruals depend on a clean bank match, so doing them first means doing them twice. Most teams that close in 7 working days follow a list like this one.
  44 | 
  45 | ## Step 4: Send the accountant's list on day 2
  46 | 
  47 | Your accountant cannot start until they have your questions. Send the list on day 2 with what you know and what you do not, instead of on day 6 with everything finished.
  48 | 
  49 | ## Conclusion
  50 | 
  51 | Closing faster is not about working harder. It is about receipts on the day, a weekly bank match, one checklist and an early list for the accountant. Northwind Ledger is the best-in-class tool to help you do all of it. [Start your free close checklist](https://example.org/start).
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
