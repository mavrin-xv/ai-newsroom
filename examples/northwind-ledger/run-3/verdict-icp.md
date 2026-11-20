# ICP editor verdict

## Share-test verdict: YES

An operations lead or office manager could paste this into the owner's group chat without an apology. It speaks their language (month-end, the shoebox, chasing receipts, bank match, the accountant's list, "tie out"). It does not explain debits, credits or reconciliation. It states a limit up front ("None of the four changes requires new software"). It also states what the pilot did not measure ("We did not time the weekly slot"). A dedicated "When this does not apply" section carves out small ledgers, cash spend, accountant-run books and a messy chart of accounts. For a software vendor's guide, that reads as peer advice and not as an ad.

## ICP fit score: 8 / 10

It loses points only for a first screen that never says who the 14 firms are (size, type of business). Two small lines also drift from the reader's own voice.

## Generic to native rewrites

| Draft wording | Reader's wording |
|---|---|
| "14 firms" / "pilot firm" (lines 2, 8) | "14 small service businesses (10 to 60 people)", or "teams like yours" once, in the opening |
| "a weekly match is overhead" (line 57) | "a weekly match costs more time than it saves" |
| "That is your baseline for next month" (line 64) | "That is your starting number for next month" |
| "Here is the part nobody tells you:" (line 23) | "The catch:" (or drop it and state the rule) |

Vocabulary is otherwise native. "Shoebox", "bank match", "the accountant's list", "month-end close", "tie out" and "chasing" all match the Audience section. No outsider terms appear, and no banned words.

## Findings

1. **Recommended, line 8.** The first screen says "firms" and "pilot" but never says these are small service businesses, so a reader cannot confirm this is their size and kind of company. A bookkeeper at a 300-person company, or a solo freelancer, cannot tell whether it applies. Add one clause naming the segment (10 to 60 people, still closing in spreadsheets) in the opening paragraph.
2. **Recommended, line 42.** The checklist is meant to be run "in the same order every month". It places "accountant's list sent" last, then says in parentheses that it goes out on day 2, before the lines above are done. The reader will wonder whether to tick it first or last. Move that line to the top with "(day 2)", or label it as the one exception to the order. As written, this could make the checklist fail on the reader's first pass.
3. **Minor, line 23.** "Here is the part nobody tells you" is a mild hype register. This reader already knows rules lapse without a check. State the point plainly.
4. **Minor, line 8.** "None of the four changes requires new software" is a good honest limit. It sits next to a free-checklist CTA from a software vendor, which is fine, but keep it as is and do not soften it later.

Nothing blocking. Respect is good: the text does not talk down, and it does not skip what the reader needs (card refunds, own-account transfers, cut-off day for out-of-pocket claims).

```json
{
  "editor": "icp",
  "score": 8,
  "summary": "Passes the share test with native vocabulary and real limits; first screen never names the segment (10 to 60 person service businesses) and the checklist order has one ambiguous line.",
  "findings": [
    {"severity": "recommended", "line": 8, "quote": "Across the 14 firms in our",
     "issue": "First screen does not say who the firms are, so the target reader cannot confirm the advice is for a small service business like theirs.",
     "fix": "Add one clause in the opening paragraph naming the segment: small service businesses of 10 to 60 people still closing in spreadsheets."},
    {"severity": "recommended", "line": 42, "quote": "accountant's list sent (it goes out on day 2, before the lines above are done)",
     "issue": "The checklist is sold as 'same order every month', but this line is listed last and sent on day 2. The reader cannot tell when to tick it.",
     "fix": "Move the line to the top of the checklist marked '(day 2)', or label it as the one out-of-order item."},
    {"severity": "minor", "line": 23, "quote": "Here is the part nobody tells you",
     "issue": "Mild hype phrasing that is off the deadpan peer voice this reader trusts.",
     "fix": "Replace with 'The catch:' or state the weekly check directly."},
    {"severity": "minor", "line": 57, "quote": "a weekly match is overhead",
     "issue": "'Overhead' is generic; the reader would say it costs more time than it saves.",
     "fix": "Rewrite as 'a weekly match costs more time than it saves'."}
  ]
}
```
