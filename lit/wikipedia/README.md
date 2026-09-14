# lit/wikipedia — citation harvesting

The instrument chosen against the coverage gap in `../../resources.md` §17.1:
neither OpenAlex nor Europe PMC reaches the monograph literature this project's
nexus material rests on, and a monograph cited with an ISBN and no URL appears in
no link list at all.

The `/wikipedia` skill parses `{{cite …}}` templates out of article wikitext, so
those works become visible. **They become visible, not verified.**

## Layout

```
harvest/        one JSON per source article, from the skill's `references` subcommand
aggregate.py    dedupes across articles and ranks; writes ranked.{md,csv}
ranked.md       the readable ranked list (top 60 multi-article works)
ranked.csv      all works, all fields
```

`harvest/` and the generated `ranked.*` are committed: they are small, and the
diff shows when an article's bibliography changes, which is itself data.

## Reproducing

```bash
export WIKIPEDIA_USER_AGENT="you/0.1 (you@example.org)"
S=~/.claude/skills/wikipedia/scripts/wikipedia_api.py
for t in "Gandhara" "Kushan Empire" "Dunhuang" "Silk Road" "Bagram" \
         "Greco-Buddhist art" "Palmyra" "Sogdia" "Mogao Caves" "Dunhuang manuscripts"; do
  uv run "$S" references "$t" --deduplicate \
    --output "lit/wikipedia/harvest/$(echo "$t" | tr ' ' '_').json"
done
uv run --no-project lit/wikipedia/aggregate.py
```

## The 2026-08-27 pass

10 articles · 821 citations · **730 distinct works** · 32 cited by more than one
article · **257 carry a durable identifier and no URL**.

That last figure is the point. Those 257 are invisible to any approach that reads
an article's external-link list, and invisible to the indexes this project can
search.

### What it produced immediately

- **Rong Xinjiang, "The Nature of the Dunhuang Library Cave and the Reasons for
  its Sealing" (1999)** — named in `resources.md` §17.3 as *the* acquisition
  target for Q8a, found here with a DOI. Not retrievable (Persée refused); now
  in `WANTED.md` with a resolved landing page instead of a name.
- **Ponampon's 2019 Cambridge thesis** on visionary experience in a Dunhuang
  manuscript — not on any list, open access, retrieved. See `../direct/`.

### Cautions

- **Ranking is by citing-article count.** It measures what Wikipedia editors
  reached for, not what the field considers authoritative. A general history of
  India ranks high because several articles need one; that is not centrality.
- **English templates only.** `{{Ouvrage}}` (fr) and `{{Literatur}}` (de) are not
  matched, and the Gandhāran and Iranian literature is disproportionately French
  and German. A non-English pass needs the skill's alias table extended first.
- **Cited is not live.** One harvested URL was already a 404 (see
  `../direct/MANIFEST.md`).
- **Dunhuang came back thin** — 27 citations against Palmyra's 243. On a question
  where Dunhuang is the negative case, the thinness of its encyclopedia
  bibliography is worth not over-reading: it bounds what this instrument can say,
  not what the field holds.
