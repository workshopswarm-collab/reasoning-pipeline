---
type: source_note
case_key: case-20260414-4e668883
dispatch_id: dispatch-case-20260414-4e668883-20260414T133938Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: markets
entity: ethereum
topic: eth-2400-apr13-19-polymarket-rules-and-market-state
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-14
source_name: Polymarket event page fetch
source_type: market page / contract surface
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4e668883/researcher-analyses/2026-04-14/dispatch-case-20260414-4e668883-20260414T133938Z/personas/catalyst-hunter.md]
tags: [polymarket, ethereum, threshold-market, rules]
---

# Summary

This source anchors the live market state and the governing contract surface for the weekly Ethereum price-hit ladder. The fetchable page clearly identifies the event and current ladder pricing, but the public readability extract does not expose the full rules text cleanly, so exact resolution mechanics still need to be stated cautiously.

## Key facts extracted

- The event is `What price will Ethereum hit April 13-19?`.
- The public page fetch shows `↑ 2,400` as one of the leading outcomes and reports it around **89%** in the page text snapshot available to retrieval.
- The same fetch says the relevant resolution criteria live in the page `Rules` section.
- The assigned run context states `current_price: 0.9235` for the specific market `Will Ethereum reach $2,400 April 13-19?`, which is the market-implied probability baseline for this run.

## Evidence directly stated by source

- The event title and bucket structure are explicit.
- The page text states traders should review the `Rules` section for the exact official data source and settlement criteria.
- The fetch confirms that the market is currently pricing the $2,400 threshold very aggressively.

## What is uncertain

- The fetch did **not** cleanly expose the exact authoritative rules wording for what specific venue / pair / candle rule governs settlement.
- Because the event page is a multi-outcome ladder, the public summary text may mix event-level and bucket-level context.
- The visible 89% page snapshot and the assigned `current_price: 0.9235` are close in direction but not identical; I treat the assignment field as the run baseline and the page fetch as a qualitative verification that the market is extremely bullish on the 2,400 rung.

## Why this source may matter

This is the primary source for the market-implied baseline and the governing source-of-truth surface. It also establishes that the market is already at an extreme-probability posture, which raises the required verification standard.

## Possible impact on the question

A very high market price implies the crowd believes either (a) ETH is already close enough that a touch is highly likely, or (b) the contract mechanics are touch-friendly enough that the remaining path is easy. If the exact rules are more permissive than a close-above framing, that supports the Yes case; if rules are less clear than the price implies, that is a meaningful caution.

## Reliability notes

Reliable for event identity and broad market state. Less reliable than a direct API/rules extract for exact settlement wording because the readability fetch did not preserve the full rules section cleanly.