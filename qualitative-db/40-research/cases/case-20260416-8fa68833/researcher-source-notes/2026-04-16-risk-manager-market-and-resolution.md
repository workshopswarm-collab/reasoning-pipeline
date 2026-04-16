---
type: source_note
case_key: case-20260416-8fa68833
dispatch_id: dispatch-case-20260416-8fa68833-20260416T163913Z
analysis_date: 2026-04-16
persona: risk-manager
domain: sports
subdomain: soccer
entity: barcelona
topic: case-20260416-8fa68833 | risk-manager
question: Will FC Barcelona win on 2026-04-22?
date_created: 2026-04-16
source_name: Polymarket market page for Barcelona vs Celta de Vigo
source_type: market contract page
source_url: https://polymarket.com/event/lal-bar-cel-2026-04-22
source_date: 2026-04-16
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [barcelona]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-8fa68833/researcher-analyses/2026-04-16/dispatch-case-20260416-8fa68833-20260416T163913Z/personas/risk-manager.md]
tags: [polymarket, market-structure, resolution-source, first-90-minutes]
---

# Summary

Polymarket defines this as a first-90-minutes match-winner market for the scheduled April 22, 2026 Barcelona vs Celta de Vigo La Liga match. The page also explicitly states the governing resolution rule and fallback source logic.

## Key facts extracted

- Market asks whether FC Barcelona will win the upcoming game scheduled for April 22, 2026.
- A Barcelona win resolves Yes; any non-win resolves No.
- Resolution is based only on the first 90 minutes plus stoppage time; extra time or penalties are out of scope.
- If the game is postponed, market remains open until the game is completed.
- If canceled entirely with no make-up game, market resolves No.
- Primary resolution source is official statistics recognized by the governing body or event organizers; if final official stats are unavailable within two hours after conclusion, credible-reporting consensus may be used.

## Evidence directly stated by source

The market text directly states the resolution mechanics and source-of-truth hierarchy.

## What is uncertain

- The market page does not itself establish current team strength or expected lineups.
- It leaves some ambiguity about which exact official source would be used first in practice, but the hierarchy clearly points to governing-body or organizer-recognized official match statistics.

## Why this source may matter

This source governs what counts for settlement and narrows the question to regulation time only, which matters because a draw after 90 minutes is a No even if Barcelona were to advance or win later in another competition context.

## Possible impact on the question

This source mainly affects contract interpretation rather than underlying team strength. It lowers resolution ambiguity but leaves sporting probability to external evidence.

## Reliability notes

Strong for contract interpretation because it is the market's own rule text. Not sufficient alone for sporting probability estimation.