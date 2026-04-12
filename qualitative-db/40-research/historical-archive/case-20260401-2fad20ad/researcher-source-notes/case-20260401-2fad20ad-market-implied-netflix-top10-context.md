---
type: source_note
domain: culture
subdomain: film
entity: Netflix Top 10 Movies
topic: Netflix global top 10 movie ranking context for War Machine market
question: Will "War Machine" be the #2 global Netflix movie this week?
driver: media-narratives
date_created: 2026-04-01
source_name: Netflix Tudum Top 10 Movies
source_type: official chart page
source_url: https://www.netflix.com/tudum/top10/films
source_date: 2026-04-01
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [Netflix, War Machine]
related_drivers: [media-narratives, seasonality]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260401-2fad20ad/researcher-analyses/2026-04-01/dispatch-case-20260401-2fad20ad-20260401T225601Z/personas/market-implied.md
tags: [domain/culture, subdomain/film, netflix, top10, war-machine, market-implied]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/researcher-source-notes/by-market/case-20260401-2fad20ad-market-implied-netflix-top10-context.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260401-2fad20ad
---

# Summary
Netflix's official Tudum Top 10 page for Global Movies (English) showed the 3/23/26-3/29/26 chart with #1 at 19.4M views, #2 at 10.3M views, #3 at 7.9M views, and lower ranks falling quickly after that. The same chart page prominently linked title detail pages including `/tudum/war-machine`, `/tudum/peaky-blinders-the-immortal-man`, `/tudum/kpop-demon-hunters`, and `/tudum/louis-theroux-inside-the-manosphere`. Raw page inspection showed `war-machine` attached to a `#1 in Movies` chart badge, `kpop-demon-hunters` to `#3 in Movies`, and `louis-theroux-inside-the-manosphere` to `#9 in Movies` on that weekly chart.

## Key facts extracted
- Netflix's official Global Movies (English) chart for 3/23/26-3/29/26 listed:
  - #1: 19.4M views
  - #2: 10.3M views
  - #3: 7.9M views
  - #4: 4.9M views
  - #5: 4.3M views
- Tudum linked directly to a War Machine title page from the chart surface.
- Raw HTML inspection of the chart page associated `war-machine` with `#1 in Movies`.
- The same inspection associated `kpop-demon-hunters` with `#3 in Movies` and `louis-theroux-inside-the-manosphere` with `#9 in Movies`.

## Evidence directly stated by source
- The official chart page is the resolution source class described by the market: Netflix's Global Top 10 Movies (English).
- The page states the weekly chart values for 3/23/26-3/29/26 and the methodology header for Global Movies.
- The page links War Machine among the featured charted titles.

## What is uncertain
- The readability extract did not cleanly label every title-name-to-rank pair in plain text.
- I inferred title/rank pairing for several entries from raw page HTML rather than from a cleaner official tabular export.
- I did not independently recover the identity of the #2 title from a separate official machine-readable endpoint.

## Why this source may matter
This is the official ranking surface the market description points to. It anchors the relevant distribution of view counts and strongly constrains what the market price can reasonably imply.

## Possible impact on the question
If War Machine was already #1 on the relevant weekly chart, a market pricing it around 95.85% to finish #2 looks very hard to justify unless the market is stale, mislabeled, or trading against an already-known resolved outcome. Even without fully identifying the #2 title, the official chart structure makes clear that War Machine was not merely in the competitive set for #2; it was above that slot.

## Reliability notes
Netflix Tudum Top 10 is the highest-credibility source for this market because the market description explicitly resolves off Netflix's global top 10 movie ranking update. The only limitation here is extraction quality from the public webpage, not source authority.