# Final review format

The chief editor writes this. Keep it to one screen when the verdict is SHIP and to two when it
is FIX. A REWRITE review is short on purpose: list the format moves and stop, because line edits
on a draft that changes shape are wasted.

```markdown
# Review: <draft title>

**Verdict: FIX** (round 2 of 5). <One sentence: why.>

| Editor | Score | One line |
|---|---|---|
| Format | 8 | Aligned: comparison for an evaluating reader |
| Structure | 6 | 2 FAIL: summary block, close |
| Voice (author name) | 7 | Two padding connectives, one exclamation |
| ICP | 7 | Passes the share test once the limits section lands |
| Claims | 5 | 1 WRONG, 2 NO-SOURCE |

## Blocking (fix all before the next round)

1. **Line 14** "cuts close time in half" (claims, voice). Source the figure or replace it with the
   measured one from the Proof section: "from 9 to 5 working days in the pilot".
2. ...

## Recommended (fix if cheap)

1. **Line 31** (icp). "reconciliation module" reads as vendor talk; the reader says "bank match".

## Conflicts resolved

- Line 22: voice wanted the long anecdote kept, structure wanted it cut. Kept 2 sentences of it:
  format fit and the reader beat the author's habit.

## One highest-leverage change

<The single fix that moves the most scores.>

## Minor ledger (logged, not re-raised)

- Line 40: "utilize" to "use".

## Noticed, not reviewed

- <optional, one line each>
```

## Verdict meanings

| Verdict | When | What happens next |
|---|---|---|
| SHIP | No blocking items, every score 6 or more, recommended items under the limit | Publish package (`article-producer` step 6) |
| FIX | Any blocking item, or any score under 6, or too many recommended | Apply the fixes, run the panel again with `--prev` |
| REWRITE | Format mismatch, or 3+ blocking items from structure and claims together | Redraft in the right format, then a full new panel |

The thresholds are defaults in `scripts/review_run.py merge` (`--recommended-limit`,
`--max-rounds`). Change them there, not in this file.
