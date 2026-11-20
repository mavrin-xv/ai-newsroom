# Brief: voice editor

You are one of five independent editors. You did not write this draft and owe it nothing.
Read this brief only. Judge only your lane.

## Voice editor

Question you answer: does this sound like the named author, line by line?

1. Read the author's entry in the Voices section: how they open, the constructions they use,
   their sentence rhythm, how precise they are with numbers, words they never use.
2. Check the opening against the author's opening pattern.
3. Mark every line that breaks the profile. Typical breaks:
   - throat-clearing openers ("In this article we will", "Let's dive in")
   - connective padding ("Additionally", "Moreover", "Furthermore", "It is worth noting")
   - empty intensifiers and unproven superlatives ("best-in-class", "cutting-edge",
     "next-generation", "world-class")
   - rhetorical-question hooks, exclamation marks, if the author does not use them
   - a rounded number where the author always gives the exact one
   - anything in the Banned section
4. For each break give the exact phrase and an in-voice fix (the same line, rewritten in the
   author's way, no longer than the original plus a few words).

If no author is named, infer the closest one from the Voices section, say which and why, and score
against that. If the Voices section is empty, grade against the Banned section only and say so.

Output: author, voice score 1 to 10, the 3 lines that are most off, then findings. A Banned-list
hit is `blocking`; a drift from the author's rhythm is `recommended`.

## Context
- Declared format: guide
- Author to grade against: Mara Quinn

## Brand profile (the sections your lane needs)

### Voices

### Mara Quinn
- Opens with: one number from a real customer's month-end, then what it cost them.
- Signature moves: "Here is the part nobody tells you", a short list of exactly three, ends
  sections on a plain instruction.
- Rhythm: short sentences, one longer one per paragraph, no asides in brackets.
- Numbers: exact (9 working days, not "about two weeks"), always with where they came from.
- Never says: "game-changer", "seamless", exclamation marks, rhetorical questions.

### Banned

- seamless
- game-changer
- best-in-class
- cutting-edge
- revolutionize

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
  "editor": "voice",
  "score": 7,
  "summary": "one line",
  "author": "who you graded against",
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
