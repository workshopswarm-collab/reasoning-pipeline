---
type: source_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-13
source_name: Polymarket event page and embedded event metadata
source_type: market platform / contract surface
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-surface, market-implied-probability, source-of-truth]
---

# Summary

This source establishes the live market context: the weekly Ethereum hit-price market is active, the relevant slug is `what-price-will-ethereum-hit-april-13-19`, and the assignment-provided current price for the `↑ 2,400` outcome is 0.76. The public page also makes clear that resolution depends on the market's rules section, even though the fetchable text does not fully expose those rules.

## Key facts extracted

- The event title is `What price will Ethereum hit April 13-19?`.
- The event is part of Polymarket's recurring weekly Ethereum hit-price series.
- Embedded page data shows the event slug `what-price-will-ethereum-hit-april-13-19`, start date `2026-04-13`, and end date `2026-04-20T04:00:00Z`.
- Embedded page data shows the event is live and not yet closed.
- The assignment context states the current price for the `↑ 2,400` outcome is `0.76`, which I use as the market-implied probability baseline.
- The readable page text states traders should review the `Rules` section for the official resolution criteria and source, implying that exact source-of-truth details live there rather than in the lightweight fetch output.

## Evidence directly stated by source

- The page is for the exact market under analysis.
- It is a multi-outcome hit-price market, not a simple binary above/below market.
- The rules section is the governing contract surface for settlement.

## What is uncertain

- The public fetch output does not expose the exact wording of the rules section.
- The precise authoritative price feed or exchange used for settlement is therefore not directly recoverable from the lightweight fetch alone.
- Because the market is multi-outcome, the 0.76 price is not a clean unconditional probability of ETH touching $2,400 in isolation; it is the market price of that specific outcome share and may embed path/partition effects depending on contract structure.

## Why this source may matter

It is the primary contract surface for the market. It establishes the market-implied baseline and highlights the key risk-manager issue: source-of-truth ambiguity is low-to-moderate only after acknowledging that the exact rules are not fully visible from current extraction.

## Possible impact on the question

This source anchors the comparison point. It supports treating the crowd as strongly leaning toward a $2,400 touch during the week, but it also creates an explicit caution that the settlement source needs to be identified as the Polymarket rules/resolution source rather than assumed from generic spot pricing alone.

## Reliability notes

- Strong for identifying the market and current platform context.
- Only medium for full resolution interpretation because the exact rules text was not fully extractable in the current fetch.
- Best used together with direct spot-price sources for live contextual analysis.