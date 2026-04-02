---
type: source_note
domain: culture
subdomain: streaming
entity: netflix
topic: official Netflix global top 10 movies chart for 2026-03-23 to 2026-03-29
question: Will "War Machine" be the #2 global Netflix movie this week?
driver: media-narratives
date_created: 2026-04-01
source_name: Netflix Tudum Top 10 Movies
source_type: official chart / platform data
source_url: https://www.netflix.com/tudum/top10/films
source_date: 2026-03-31
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [netflix]
related_drivers: [media-narratives, product-launches]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/agent-findings/variant-view/case-20260401-2fad20ad-will-war-machine-be-the-2-global-netflix-movie-this-week-794.md
tags: [source-note, domain/culture, entity/netflix, market/netflix-top10]
---

# Summary

Netflix's official global English-movies Top 10 page for the week 2026-03-23 to 2026-03-29 shows a clear gap between the #2 and #3 films: #2 has 10.3M views and #3 has 7.9M views. The same page's linked title universe prominently includes `War Machine` alongside other likely high-ranking contenders such as `Peaky Blinders: The Immortal Man`, `KPop Demon Hunters`, and `Louis Theroux: Inside the Manosphere`.

## Key facts extracted

- Market-relevant reporting window is `3/23/26 - 3/29/26` on Netflix's official global Top 10 movies page.
- The page lists weekly global English-movie rankings with views, runtime, and hours viewed.
- For the relevant week, the top three slots show:
  - #1: 19.4M views
  - #2: 10.3M views
  - #3: 7.9M views
- The #2 versus #3 gap is 2.4M views, or roughly 30% of #3's view count.
- The page's featured / linked titles include `War Machine`, `Peaky Blinders: The Immortal Man`, `KPop Demon Hunters`, and `Louis Theroux: Inside the Manosphere`.

## Evidence directly stated by source

- Netflix explicitly states these are the `Global Top 10 Movies` for the week.
- Netflix explicitly states the ranking is based on views and provides hours viewed and runtime.
- The methodology note says regional groupings are based on UN statistics divisions and that some titles may be unavailable in all regions.

## What is uncertain

- The readability extract did not preserve title-to-rank mapping cleanly, so this source alone is stronger on the size of the rank gaps than on directly proving which title occupies each numbered slot.
- The presence of `War Machine` in the page's title universe does not, by itself, prove it is the #2 title without better parsing or another confirming source.
- If Polymarket resolves from the rendered Netflix page title mapping rather than just the numeric table, that mapping still matters operationally.

## Why this source may matter

This is the resolution-defining source family. Even with imperfect extraction, it shows the relevant week and that the #2 slot was not a near-tie with #3. That narrows the plausible variant case: the main credible disagreement is not that the #2 race was razor-thin, but that title identification / parsing / stale market interpretation could be wrong.

## Possible impact on the question

This source pushes toward agreement with a high probability on the market favorite if `War Machine` is indeed the title associated with the 10.3M-views slot. The variant angle is mostly operational: if the crowd is leaning on unofficial summaries or ambiguous page rendering, the residual risk is title mapping error rather than a substantive late challenger overtaking it.

## Reliability notes

- Official Netflix chart page, so high credibility for the underlying ranking data.
- Extraction quality is imperfect because the page is dynamic and readability strips some title-label structure.
- Best used together with title-specific Tudum pages or direct page inspection when exact title-to-rank linkage matters.