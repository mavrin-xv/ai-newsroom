# ICP editor verdict

## Share-test verdict

**Yes.** An operations lead or office manager could paste this into the owner's group chat without apologizing. The opening names a concrete pain (owner sees real numbers on day 10), the steps are specific (Tuesday slot, card pause, day-2 list), and the "When this does not apply" section reads as honest, not as hedging. The only line I would expect someone to trim before sharing is the "nobody tells you" aside in line 23.

## ICP fit score: 8 / 10

## Check by check

1. **Share test.** Passes. The refund and own-account-transfer tip (line 33) and the "time yours for the first month" advice (line 31) read as written by someone who has closed a month.
2. **Vocabulary.** Strong. It uses "shoebox", "chasing receipts", "bank match", "the accountant's list", and "month-end". It avoids every outsider term in the profile. A few spots lean generic (see rewrites below).
3. **Segment clarity.** Good. The first paragraph says small service firms, a 9-day close and an owner waiting on numbers, so a 10 to 60 person firm recognises itself at once. It is clearly not for a beginner, since it never explains debits, credits or reconciliation.
4. **Trust posture.** Very good. The limits section has four real exclusions (low volume, cash spend, accountant-run books, a broken chart of accounts). Line 21 admits the card-pause rule "sounds harsh".
5. **Respect.** Mostly good. It does not explain accounting basics. One gap is the weekly slot "is short" with no figure, which leaves an operations lead without the number they would want to defend the routine to the owner.

## Generic to native rewrites

- "the weekly slot is short" (line 31) to a native, checkable phrase such as "the weekly bank match is a short slot, usually well under an hour for a few hundred lines", but only if the pilot data supports it. Otherwise say plainly that the draft has no figure and the reader should time their own.
- "No routine survives a ledger nobody trusts" (line 60) to the reader's phrase: "No routine survives books that don't tie out."
- "Here is the part nobody tells you:" (line 23) to a plain statement: "The rule only holds if someone checks it weekly."
- "expense lines" / "lines" is acceptable, but "card lines" or "bank lines" matches the reader's "bank match" framing more closely in line 19.

## Findings

- No blocking findings. Nothing in the draft fails the share test on a fixable line.
- Recommended: line 23 uses a teaser opener that reads as content-marketing tone, and this reader will skim past it.
- Recommended: line 31 gives no time figure for the weekly match, which is the one number this reader needs to sell the routine to the owner.
- Minor: line 8 says day 10 is "a third of the way into the next month". Ten working days is roughly half a month, so a careful operations lead may stop on the arithmetic. Say "in the second week of the next month".
- Minor: line 60 "ledger nobody trusts" could use the reader's own words ("it doesn't tie out").

```json
{
  "editor": "icp",
  "score": 8,
  "summary": "Passes the share test: native vocabulary, clear segment in the first paragraph, honest limits section; only small tone and precision fixes remain.",
  "findings": [
    {"severity": "recommended", "line": 23, "quote": "Here is the part nobody tells you:",
     "issue": "Teaser opener reads as content-marketing tone; this reader skims past it and it mildly undercuts the plain, peer voice of the rest.",
     "fix": "State the point directly: 'The rule only holds if someone checks it weekly.'"},
    {"severity": "recommended", "line": 31, "quote": "the weekly slot is short",
     "issue": "No figure for the weekly match time; the operations lead needs a number to defend the routine to the owner.",
     "fix": "Give the pilot's typical weekly time if the data supports it, otherwise say plainly that it is unmeasured and the reader should time their own."},
    {"severity": "minor", "line": 8, "quote": "a third of the way into the next month",
     "issue": "Day 10 in working days is about half a month; a careful reader may stop on the arithmetic.",
     "fix": "Say 'in the second week of the next month' or state calendar days."},
    {"severity": "minor", "line": 60, "quote": "No routine survives a ledger nobody trusts.",
     "issue": "Generic phrasing where the reader has a native one.",
     "fix": "Use 'books that don't tie out'."}
  ]
}
```
