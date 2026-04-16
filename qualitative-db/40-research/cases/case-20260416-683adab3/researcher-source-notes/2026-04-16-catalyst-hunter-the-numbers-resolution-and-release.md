---
type: source_note
case_key: case-20260416-683adab3
dispatch_id: dispatch-case-20260416-683adab3-20260416T160048Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: culture
subdomain: film-box-office-and-ranking-surfaces
entity: the-numbers
topic: Lee Cronin's The Mummy opening weekend box office resolution mechanics and release timing
question: Will "Lee Cronin's The Mummy" Opening Weekend Box Office be between 10m and 15m?
driver:
date_created: 2026-04-16
source_name: The Numbers title page plus market resolution text
source_type: primary resolution/context
source_url: https://www.the-numbers.com/movie/Lee-Cronins-The-Mummy-(2026)
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities:
  - the-numbers
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-683adab3/researcher-analyses/2026-04-16/dispatch-case-20260416-683adab3-20260416T160048Z/personas/catalyst-hunter.md
tags:
  - source-note
  - box-office
  - resolution-mechanics
  - release-date
---

# Summary
The key authoritative surface for settlement is The Numbers movie page, as incorporated by the market description. The page confirms the domestic wide release date as April 17, 2026, while the contract text specifies that final 3-day weekend numbers for April 17-19 on the movie's Box Office tab are the governing source once they are no longer studio estimates.

## Key facts extracted
- The Numbers lists domestic release as April 17, 2026 (wide) by Warner Bros.
- International rollout begins April 15, 2026, but the contract resolves on the domestic 3-day opening weekend.
- The market text says settlement uses The Numbers "Daily Box Office Performance" / Weekend Box Office Performance figures for the 3-day opening weekend April 17-19.
- The contract explicitly says the relevant figure typically includes Thursday previews.
- If values sit exactly on a bracket boundary, the higher bracket wins.
- If finality is ambiguous, both The Numbers and Box Office Mojo must confirm finalized figures before resolution.

## Evidence directly stated by source
- Domestic Releases: April 17th, 2026 (Wide) by Warner Bros. (The Numbers title page).
- Market rules: resolve according to The Numbers 3-day opening weekend figure once final, not studio estimates; if ambiguous, wait for both The Numbers and Box Office Mojo confirmation.

## What is uncertain
- The fetched public The Numbers page did not expose the future weekend-performance table before release, so no direct current numeric weekend estimate comes from the governing source yet.
- The contract text references The Numbers Box Office tab / weekend-performance surface, which may display richer data than the general readability extract captured here.

## Why this source may matter
This is the governing source-of-truth layer for resolution mechanics and the cleanest confirmation of what dates/counting rules matter.

## Possible impact on the question
The date and counting mechanics narrow the relevant catalyst window to previews plus Friday-Sunday domestic performance. Because the bracket is specifically 10m-15m and boundary hits resolve upward, a number exactly at 15.0 would count against the target bracket.

## Reliability notes
High reliability for settlement mechanics because the market explicitly names The Numbers as the primary source. Medium completeness for current pre-release analysis because the extracted page does not expose all tabular box-office fields in this capture.
