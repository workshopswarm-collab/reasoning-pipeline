---
type: source_note
case_key: case-20260413-9dc5221c
dispatch_id: dispatch-case-20260413-9dc5221c-20260413T190728Z
analysis_date: 2026-04-13
persona: risk-manager
domain: sports
subdomain: chess
entity:
topic: market resolution rules for 2026 FIDE Candidates winner market
question: Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market rules page
source_type: market contract page
source_url: https://polymarket.com/event/2026-fide-candidates-tournament-winner
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9dc5221c/researcher-analyses/2026-04-13/dispatch-case-20260413-9dc5221c-20260413T190728Z/personas/risk-manager.md]
tags: [market-rules, resolution, polymarket, chess]
---

# Summary

The market contract resolves to the player who wins the 2026 FIDE Candidates Tournament, with FIDE designated as the primary resolution source and consensus credible reporting as fallback. It also specifies cancellation/postponement logic and that players who become unable to win under FIDE rules resolve to No.

## Key facts extracted

- The contract resolves to the player that wins the 2026 FIDE Candidates Tournament scheduled for March 29-April 16, 2026.
- If it becomes impossible for a listed player to win under FIDE rules, that contract resolves No.
- If the event is cancelled, postponed beyond April 30, 2026, or no winner is declared by then, the market resolves to Other.
- Primary resolution source is official FIDE information; credible-reporting consensus is fallback.

## Evidence directly stated by source

- "The primary resolution source will be official information from FIDE; however, a consensus of credible reporting may also be used."
- "If at any point it becomes impossible for a listed player to win the 2026 FIDE Candidates Tournament per the rules of the FIDE, the corresponding market will resolve to 'No'."
- "If the 2026 FIDE Candidates Tournament is cancelled, or postponed after April 30, 2026, or there is otherwise no winner declared within that timeframe, this market will resolve to 'Other'."

## What is uncertain

- The contract page itself does not establish whether the market's listed player set is complete or whether prices are internally coherent across runners.
- It does not address potential edge cases beyond the broad fallback language.

## Why this source may matter

This source governs resolution mechanics. For a risk-manager memo, it matters because high-confidence prices can hide contract/path risks distinct from competitive strength.

## Possible impact on the question

The source makes clear that the right source-of-truth is FIDE, not media speculation. It also highlights modest but real non-performance paths: administrative impossibility, cancellation/postponement, or lack of declared winner by the deadline.

## Reliability notes

High relevance for contract interpretation, but not an independent source on chess strength. It should be paired with FIDE event information rather than used alone.