# Verdict: format editor

- Topic: how a small service firm shortens its month-end close with four routine changes.
- Segment: the operations lead or office manager who does the books (the owner signs off).
- Reader intent: fixing. They have a slow close now and want steps they can run next month.
- Current format: guide
- Right format: guide
- Format fit: 8 of 10
- Verdict: aligned

## Why it fits

The draft has an outcome title, a summary block with 4 bullets (limit 3 to 5), four steps in order, one limits section ("When this does not apply", which the format requires) and a CTA. Countable H2s outside the summary are 6 (four steps, limits, CTA), which is exactly h2_max. The setup is not buried at the end. The reader can start with Step 1 and follow in order. The checklist in Step 3 is a real runbook artifact, which suits a fixing reader. The pilot numbers sit in the intro and Step 1, so the guide has proof without turning into a case study. Length looks inside 700 to 1600 words.

## Small frictions (not a mismatch)

- The title and the opening paragraph lean toward a case study ("How 14 firms cut..."). The body is a guide, so this is acceptable. The fixing reader gets the steps within one scroll.
- Step 1 points forward to Step 2 ("same Tuesday slot as the bank match in Step 2"), so a reader following strictly in order meets a dependency before it is explained.
- The Step 3 checklist lists the accountant's list last but says it goes out on day 2, while Step 4 comes after the checklist. The order on the page and the order in time differ.

## Conversion moves

None needed. Optional polish only.

```json
{
  "editor": "format",
  "score": 8,
  "summary": "Right format: a guide for a reader fixing a slow month-end, with ordered steps, a checklist, summary and a limits section; only minor ordering friction.",
  "format_fit": "aligned",
  "current_format": "guide",
  "right_format": "guide",
  "findings": [
    {"severity": "recommended", "line": 23, "quote": "Put the receipt count on the same Tuesday slot as the bank match in Step 2.",
     "issue": "A step in a follow-in-order guide depends on a later step the reader has not reached yet.",
     "fix": "Move the Tuesday-slot instruction into Step 2, or say in Step 1 only that a weekly check comes in Step 2."},
    {"severity": "minor", "line": 42, "quote": "accountant's list sent (it goes out on day 2, before the lines above are done)",
     "issue": "The checklist order differs from the real time order, and the explanation of that sits in the item itself.",
     "fix": "Put the accountant's list first in the checklist with a day-2 label, or add a one-line note that it is out of sequence on purpose."}
  ]
}
```
