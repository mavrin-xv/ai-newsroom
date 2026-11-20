# Source ladder

Every figure in a draft comes from the highest rung you can reach, and every figure gets one row
in `sources.md` (template: `templates/sources.md`). A figure without a row is cut before review.
`claims_scan.py --sources sources.md` checks this mechanically.

| Rung | Source | How to cite it in the sentence |
|---|---|---|
| 1 | Primary data: your own logs and pilots, official docs, specs, regulator or government statistics | "(our pilot, 14 firms, April 2026)" or a link |
| 2 | Large independent studies with a stated method and sample | "(<publisher>, <year>, n = <sample>)" |
| 3 | Industry associations and foundation reports | name the body and the year |
| 4 | Vendor data | label it in the sentence: "per <vendor>'s own survey" |
| 5 | Your own count, done for this piece | one line of method: "we counted 40 forum threads, November 2026" |

One link per paragraph at most.

## Traps

- **Chains.** A blog cites a blog that cites a 2014 study. Follow it to the origin or drop it.
- **Old numbers shown as current.** Say the year next to the figure.
- **The wrong place.** A global figure presented as one country's or one industry's.
- **The converted.** A vendor surveying its own customers about its own category.
- **Round numbers with no origin.** "80% of teams..." with nothing behind it.
- **The same metric, two figures.** If the intro says 7 days and the body says 9, the claims scan
  flags it. Pick the sourced one.

## Row format

```text
| Figure | What it is | Source | Rung | Checked |
| 31% | share of expense lines with no receipt on day 1 of close, 14 pilot firms | https://example.org/pilot-report | 1 | 2026-11-02 |
```

Write the figure exactly as the draft writes it ("9 working days", not "9"), so the scan can
match it.
