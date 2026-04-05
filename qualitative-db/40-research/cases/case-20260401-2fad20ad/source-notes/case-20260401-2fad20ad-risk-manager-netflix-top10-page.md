---
type: source_note
domain: culture
subdomain: streaming
entity: Netflix Top 10
topic: case-20260401-2fad20ad | War Machine weekly global Netflix movie ranking
question: Will "War Machine" be the #2 global Netflix movie this week?
driver: seasonality
date_created: 2026-04-01
agent: risk-manager
source_type: official platform page
source_url: https://www.netflix.com/tudum/top10
source_date: 2026-04-01
source_status: current
related_entities: [Netflix, War Machine]
related_drivers: [seasonality, media-narratives]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260401-2fad20ad/analyses/2026-04-01/dispatch-case-20260401-2fad20ad-20260401T225601Z/personas/risk-manager.md, qualitative-db/40-research/cases/case-20260401-2fad20ad/analyses/2026-04-01/dispatch-case-20260401-2fad20ad-20260401T225601Z/evidence/risk-manager.md]
tags: [source-note, netflix, top10, official-source, case-20260401-2fad20ad, risk-manager]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/source-notes/by-market/case-20260401-2fad20ad-risk-manager-netflix-top10-page.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260401-2fad20ad
---

# Source summary

Netflix's Tudum Top 10 page for Global Movies | English shows the week 3/23/26 - 3/29/26 and lists the top-10 movie view counts. The page extract shows:
- #1: 19.4M views
- #2: 10.3M views
- #3: 7.9M views
- #4: 4.9M views
- lower ranks continue below that

The same page also includes an "Explore The Most Watched Movies" section with a direct link to `/tudum/war-machine`.

## Key extracted facts

- The market's governing source class exists and is live: Netflix's own Top 10 page.
- For the relevant week, the #2 movie view count is 10.3M and sits materially above #3 at 7.9M.
- The gap between #2 and #3 in the page extract is 2.4M views, which is large enough that ordinary small extraction noise would not matter.
- The page extract itself does not clearly print the title names inline next to the ranks in readable markdown; the readable extraction preserves counts/ranks but not the associated labels.
- The same page links to a dedicated War Machine Tudum page, indicating War Machine is one of the notable active movie titles in the same ecosystem snapshot.

## Why this source matters

This is the official resolution source class named by the market rules. It is the highest-credibility evidence available for the ranking itself.

## Reliability notes

- Very high credibility on existence of the chart, date window, and rank/view-count structure.
- Medium extraction quality for title-to-rank mapping because the readable scrape drops some labels.
- Main residual risk is not the underlying source but the extraction layer failing to show the title beside the row.

## What remains uncertain

- The readable extract does not unambiguously show that the 10.3M #2 row is War Machine rather than another movie.
- If the live chart were to change late, the relevant question is whether War Machine is actually the title occupying the 10.3M row.

## Risk-manager take

The official page strongly supports that the market is near resolution and that the remaining uncertainty is mostly mapping/extraction risk rather than substantive ranking risk. That argues for a high probability, but not literal certainty.