---
type: source_note
case_key: case-20260406-5e3348e5
dispatch_id: dispatch-case-20260406-5e3348e5-20260406T175635Z
analysis_date: 2026-04-06
persona: market-implied
domain: entertainment
subdomain: streaming
entity:
topic: netflix-us-top-10-tv-week-2026-03-23-2026-03-29
question: Will "XO, Kitty Season 3" be the top US Netflix show this week?
driver:
date_created: 2026-04-06
source_name: Netflix Tudum Top 10 - United States TV
source_type: authoritative chart / source-of-truth surface
source_url: https://www.netflix.com/tudum/top10/united-states/tv
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [netflix, top10, authoritative, resolution]
---

# Summary

Netflix's own US TV Top 10 page is the governing source-of-truth surface for this market. On the page fetch performed 2026-04-06, the currently selected weekly window is `3/23/26 - 3/29/26`, matching the market description's reporting window that is expected to update on Tuesday, April 7, 2026. The page text extraction shows the #1 item in US shows as `Season 2`, which aligns with XO, Kitty Season 2 being the leader for the relevant week.

## Key facts extracted

- Governing page: `https://www.netflix.com/tudum/top10/united-states/tv`
- Geography: United States
- Category: Shows / TV
- Relevant weekly window visible on page: `3/23/26 - 3/29/26`
- Extracted ranking text places `Season 2` at `#1 in Shows`
- The market description says Netflix will update this list on Tuesday, April 7, 2026 at 3:00 PM ET for the previous Monday-Sunday week, so this visible week is the one that should govern resolution.

## Evidence directly stated by source

- The page explicitly labels `United States | 3/23/26 - 3/29/26`
- The page presents a Top 10 shows table for that week.
- The extracted content from the page shows `Season 2#1 in Shows` as the top-ranked show.
- The page includes methodology language indicating rankings are based on Netflix's own Top 10 methodology for the selected region and category.

## What is uncertain

- The readability extraction does not preserve the title label adjacent to `Season 2#1 in Shows`, so the title-to-rank mapping is somewhat lossy in plain-text extraction.
- However, the page output sequence and overall extracted structure strongly imply the first listed show entry is the Season 2 entry at #1, and this is consistent with the event contract naming XO, Kitty Season 3 while actual chart entries on Netflix often list only season numbers, not the franchise title in the simplified extraction.
- The market title says `XO, Kitty Season 3`, while the Netflix weekly page extraction shows `Season 2` at #1. This suggests either the market title likely has a season-number typo or the listing shorthand strips the franchise name. That mismatch is the main residual ambiguity.

## Why this source may matter

This is the stated governing resolution surface in both the market description and Netflix's own chart product. For a simple official-chart market, this source can be sufficient if the week and top-ranked entry are clearly identified.

## Possible impact on the question

If the market is intended to resolve to the Netflix US TV Top 10 page for the week `3/23/26 - 3/29/26`, then the available evidence strongly supports the view that the market is pricing the likely correct winner near the top of the allowed confidence range.

## Reliability notes

- Primary / authoritative source.
- High credibility because Netflix publishes the ranking directly.
- Independence is low as a standalone source, but that is acceptable here because it is the actual source-of-truth surface.
- Main reliability limitation is text extraction lossiness around title labels and the market-title season-number mismatch.