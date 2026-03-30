---
type: source_note
domain: culture
subdomain: film
entity: Project Hail Mary
topic: resolution-source anomaly on Box Office Mojo title URL
question: Will "Project Hail Mary" 2nd weekend domestic box office be greater than $54M?
driver: media-narratives
date_created: 2026-03-30
source_name: Box Office Mojo title URL in market description
source_type: box-office-metrics
source_url: https://www.boxofficemojo.com/title/tt28650488/
source_date: 2026-03-30
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: high
agent: market-implied
related_entities: []
related_drivers: [media-narratives]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/assumption-notes/case-20260330-0a94627e-market-implied-assumptions.md
  - qualitative-db/40-research/evidence-maps/case-20260330-0a94627e-market-implied-evidence-map.md
  - qualitative-db/40-research/agent-findings/market-implied/case-20260330-0a94627e-will-project-hail-mary-2nd-weekend-box-office-be-greater-than-54m.md
tags: [domain/culture, subdomain/film, source/box-office-metrics, market/project-hail-mary, source-anomaly]
---

# Summary

The exact Box Office Mojo title URL named in the market description currently resolves to a page titled **"The Super Mario Galaxy Movie"** rather than `Project Hail Mary`, creating a source-resolution anomaly that likely explains why the market is not priced closer to certainty despite The Numbers already showing a weekend above $54M.

## Key facts extracted

- The URL `https://www.boxofficemojo.com/title/tt28650488/` currently renders with the page title **"The Super Mario Galaxy Movie - Box Office Mojo"**.
- The visible page heading also shows **"The Super Mario Galaxy Movie (2026)"**, not `Project Hail Mary`.
- I did not extract a usable `Project Hail Mary` domestic daily table from this Box Office Mojo URL.

## Evidence directly stated by source

- The fetched HTML title tag contains `The Super Mario Galaxy Movie - Box Office Mojo`.
- The rendered page heading visible in the fetched HTML contains `The Super Mario Galaxy Movie (2026)`.

## What is uncertain

- This could be a temporary Box Office Mojo metadata/linking issue, a bad market link, or a genuine title-ID mismatch.
- It is unclear whether Box Office Mojo has the correct `Project Hail Mary` domestic daily page under a different URL.
- It is also unclear how quickly the market resolver will operationally handle the mismatch if it persists.

## Why this source may matter

This matters because the remaining uncertainty in the market is probably no longer driven mainly by ticket-sales performance. It is driven by **resolution mechanics**: whether the primary source is correctly linked and whether final figures settle above the threshold.

## Possible impact on the question

This anomaly is the strongest argument for not marking the market near-100% YES immediately. It introduces a nontrivial but still secondary operational risk channel even though the film-performance evidence itself is favorable.

## Reliability notes

Useful for documenting the operational state of the named resolution source, but weaker than The Numbers on the substantive gross figure because it does not currently provide a usable matching `Project Hail Mary` result at the cited URL.