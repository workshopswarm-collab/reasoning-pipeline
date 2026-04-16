---
type: source_note
case_key: case-20260413-61dcf900
dispatch_id: dispatch-case-20260413-61dcf900-20260413T184628Z
analysis_date: 2026-04-13
persona: risk-manager
domain: sports
subdomain: hockey
entity: nhl
topic: western-conference-wild-card-context
question: Will the Los Angeles Kings make the 2025-26 NHL Playoffs?
driver: seasonality
date_created: 2026-04-13
source_name: ESPN NHL Wild Card Standings
source_type: secondary standings aggregator
source_url: https://www.espn.com/nhl/standings/_/view/wild-card
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: Orchestrator
related_entities: [nhl]
related_drivers: [seasonality]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-61dcf900/researcher-analyses/2026-04-13/dispatch-case-20260413-61dcf900-20260413T184628Z/personas/risk-manager.md]
tags: [source-note, espn, standings, wildcard, contextual-source]
---

# Summary

ESPN's wild-card standings page extracted cleanly enough to show the Western Conference race shape on 2026-04-13. It lists Los Angeles as the second wild card team, not yet marked with an "x" clinch indicator, with Nashville, Winnipeg, and San Jose still below them and only a small number of games left.

## Key facts extracted

- In the Western Conference wild-card view, Utah is wild card 1 with an "x" clinch marker.
- Los Angeles Kings are listed as wild card 2 with no clinch marker shown in the extraction.
- Nashville, Winnipeg, and San Jose are listed behind Los Angeles.
- Several trailing teams are already marked eliminated.
- Standings are updated with the completion of each game.

## Evidence directly stated by source

- Los Angeles appears on the wild-card line rather than outside it.
- The source distinguishes clinched, eliminated, and still-live teams via symbols.
- The Kings were still shown as not yet clinched in the extracted page at fetch time.

## What is uncertain

- The extraction compresses columns, so point totals are awkward to parse from raw text.
- The exact remaining-game matrix and tie-break exposure are not fully legible from the extracted output alone.

## Why this source may matter

This is the clearest contextual evidence in the run for current competitive status: the Kings were in a playoff position, but the absence of a clinch marker means path risk remained alive.

## Possible impact on the question

This supports a Yes-lean because the Kings are currently above the line, but also supports discounting extreme confidence because they had apparently not yet clinched despite the market being 73.5%.

## Reliability notes

Good independent contextual source, but not the governing source of truth. Useful for race shape and disconfirming risk framing; should be paired with official NHL authority for settlement logic.