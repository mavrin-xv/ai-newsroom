# AGENTS.md

Notes for coding agents (Claude Code, Codex, Cursor, others) working on this repository.

## What this is

Four Agent Skills for an editorial desk: `newsroom-setup` writes the brand profile, `article-producer` and `x-article` write, `newsroom-review` runs five blind editors and a chief editor. The product is the `SKILL.md` text plus small Python scripts. No server, no database, no network calls.

## Layout

- `skills/<name>/SKILL.md`: what the agent does and when. Frontmatter has `name` (same as the folder) and `description` only. Under 500 lines; long material goes in `references/`.
- `skills/newsroom-review/scripts/newsroom_profile.py`: the shared parser for `brand-profile.md`. The other skills import it from `../../newsroom-review/scripts`, so the skills must be installed side by side.
- `skills/newsroom-review/references/editors.md`: the five editor lanes. Each editor gets only its brief from `review_run.py packet`, never another editor's verdict.
- `templates/`: `brand-profile.md` and `sources.md`. Keep the H2 names; the scripts find sections by name.
- `examples/northwind-ledger/`: an invented bookkeeping company. `draft-v1.md` is flawed on purpose and `fields.md` holds one duplicate title variant on purpose. Do not fix them. `run-1/` to `run-3/` are real outputs of the review loop.

## Rules

- No real companies, people, emails or domains other than example.org in examples.
- Scripts use the Python standard library only, Python 3.8+, each with `--help` and documented exit codes.
- A rule the editors must apply goes in the profile text, not only in a script. Editors read the profile.
- Platform facts (X articles, title lengths) carry the date they were checked.

## Checks before you finish

```bash
S=skills; E=examples/northwind-ledger
for f in $S/*/scripts/*.py; do python3 "$f" --help >/dev/null || echo "FAIL $f"; done
python3 $S/newsroom-review/scripts/structure_lint.py $E/draft-v1.md --profile $E/brand-profile.md --format guide | tail -1  # 11 FAIL, 2 PASS
python3 $S/newsroom-review/scripts/structure_lint.py $E/draft-v3.md --profile $E/brand-profile.md --format guide | tail -1  # 0 FAIL, 13 PASS
python3 $S/newsroom-review/scripts/claims_scan.py $E/draft-v3.md --sources $E/sources.md --profile $E/brand-profile.md | head -1  # 5 claims, 0 not sourced
python3 $S/newsroom-review/scripts/review_run.py merge $E/run-2 --prev $E/run-1/merged.json | head -3   # Round 2. Verdict proposal: FIX
python3 $S/article-producer/scripts/link_check.py $E/draft-v3.md --profile $E/brand-profile.md; echo $?   # unknown or bare: 0, exit 0
python3 $S/article-producer/scripts/seo_fields.py $E/fields.md --profile $E/brand-profile.md | tail -1    # 1 FAIL, 6 PASS
python3 $S/x-article/scripts/x_article_check.py $E/x-article.md --profile $E/brand-profile.md | tail -1   # 0 FAIL, 0 WARN, 9 PASS
```
