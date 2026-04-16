---
type: source_note
case_key: case-20260414-231e3ef7
dispatch_id: dispatch-case-20260414-231e3ef7-20260414T140546Z
analysis_date: 2026-04-14
persona: market-implied
domain: chess
subdomain: candidates-tournament
entity:
topic: case-20260414-231e3ef7 | market-implied
question: Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?
driver:
date_created: 2026-04-14
source_name: Polymarket market page and contract text
source_type: market-contract
source_url: https://polymarket.com/event/2026-fide-candidates-tournament-winner
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260414-231e3ef7/researcher-analyses/2026-04-14/dispatch-case-20260414-231e3ef7-20260414T140546Z/personas/market-implied.md
tags: [polymarket, contract, resolution-source]
---

# Summary

This source establishes the exact market wording, timing, and source-of-truth hierarchy. It is the governing contract surface for what counts as a win and what happens if Sindarov becomes unable to win before tournament end.

## Key facts extracted

- Market asks whether Javokhir Sindarov will win the 2026 FIDE Candidates Tournament.
- Tournament window on the market page is March 29 to April 16, 2026.
- If it becomes impossible for a listed player to win per FIDE rules, that player's market resolves No.
- If the event is cancelled, postponed after April 30, 2026, or no winner is declared within that timeframe, resolution is Other.
- Primary resolution source is official information from FIDE; consensus credible reporting is fallback.
- Assignment context states current price is 0.9905, implying about 99.05% win probability.

## Evidence directly stated by source

Directly stated contract text supports that official FIDE information is the governing source of truth, with credible-reporting consensus only as fallback. It also directly states impossibility logic matters before the formal declaration if FIDE rules make a win impossible.

## What is uncertain

- The market page fetch did not expose a live order-book or detailed price history in readable text.
- The market contract does not itself state current tournament standings.

## Why this source may matter

This source defines the exact resolution mechanics and therefore sets the standard for what evidence should dominate the analysis. Because price is extreme, source-of-truth discipline matters more than usual.

## Possible impact on the question

It makes official FIDE tournament information the primary settlement anchor. Any thesis that Sindarov is not effectively certain must point either to standings uncertainty, unresolved tie-break uncertainty, or a source-of-truth / operational issue.

## Reliability notes

Good for contract wording and resolution mechanics. Not sufficient alone for standings or tournament state, so it needs to be paired with official or strong contextual tournament-status reporting.
