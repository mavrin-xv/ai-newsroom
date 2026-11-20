# Format editor verdict

- Topic: a four-change routine that cuts a small service firm's month-end close from 9 working days to 5.
- Segment: the operations lead or office manager who does the books (the owner signs off).
- Intent: fixing. The reader has a slow close now and wants steps to follow next month.
- Current format: guide
- Right format: guide
- Fit score: 8 / 10
- Verdict: aligned

## Why it fits

The draft is an outcome-titled guide with a summary block of 4 bullets (within 3-5). It has four ordered steps and a "When this does not apply" limits section, which is the required section. It ends with a CTA that gives the reader a concrete next action: run last month through the checklist.

The setup is in the right place. The steps run in the order a reader would do them, and Step 3 even explains why the order matters. The opening uses pilot numbers (9 to 5 days, 14 firms, 31% of lines without a receipt) as proof, not as a case study. That is the right weight for a guide. The vocabulary (shoebox, bank match, accountant's list) matches the audience, and no basics are explained.

A comparison or case format would be worse here. This reader has a problem now and does not need to choose between a spreadsheet, an accountant and software.

## Why not 10

The draft has 7 h2 headings against a format cap of 6 (Summary, Steps 1 to 4, When this does not apply, and the closing CTA heading). That is a mechanical break of the guide spec, not a mismatch of format. The fix is small, so the score stays at 8.

## Conversion moves

None needed, because the format is aligned. The one structural fix is to bring the h2 count to 6 or fewer:
1. Fold the CTA into the end of "When this does not apply", or make it an unheaded closing paragraph.
2. Alternatively, drop the "Summary" h2 and use a bold label, but keep the summary block itself.

```json
{
  "editor": "format",
  "score": 8,
  "summary": "Guide is the right format for a fixing reader; only the h2 count (7 vs max 6) breaks the spec.",
  "format_fit": "aligned",
  "current_format": "guide",
  "right_format": "guide",
  "findings": [
    {"severity": "blocking", "line": 62, "quote": "## Run your last month through the checklist",
     "issue": "The draft has 7 h2 headings (Summary, Steps 1-4, When this does not apply, this CTA); the guide format allows at most 6.",
     "fix": "Remove this h2 and make the CTA a closing paragraph under the limits section, or an unheaded final paragraph, so the count is 6."}
  ]
}
```
