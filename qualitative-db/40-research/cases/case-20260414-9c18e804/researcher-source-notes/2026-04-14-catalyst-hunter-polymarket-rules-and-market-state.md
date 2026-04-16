---
type: source_note
case_key: case-20260414-9c18e804
dispatch_id: dispatch-case-20260414-9c18e804-20260414T135145Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: btc
entity: btc
topic: polymarket market state and resolution framing
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Polymarket event page
source_type: market page / contract surface
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-analyses/2026-04-14/dispatch-case-20260414-9c18e804-20260414T135145Z/personas/catalyst-hunter.md]
tags: [polymarket, contract, resolution, market-implied-probability]
---

# Summary

Polymarket is the primary contract surface for this case. The fetched page confirms the event title and that the market is a multi-outcome weekly Bitcoin price-hit market for April 13-19. The assignment context provides the live current_price of 0.75 for the relevant outcome and the market URL. The readable fetch did not expose the full rule text cleanly, so source-of-truth ambiguity remains nonzero and should be stated explicitly in the main finding.

## Key facts extracted

- Market title matches the assigned question: "What price will Bitcoin hit April 13-19?"
- The case assignment states the relevant outcome current_price is 0.75, implying about 75% market probability.
- The event resolves on 2026-04-20 00:00 ET according to the assignment context.
- The fetched page text explicitly says the rules section governs official data sources and edge cases, but the fetch did not return the full rules text.

## Evidence directly stated by source

- The page is a prediction market with multiple outcomes for Bitcoin hit levels during April 13-19.
- Resolution depends on the rules section and official data sources on the page.

## What is uncertain

- The precise governing benchmark/exchange and whether intraday prints, wick trades, or venue-specific highs count were not visible in the readable fetch.
- Because the full rules text was not captured, there is residual source-of-truth ambiguity despite low overall case complexity.

## Why this source may matter

This is the primary contract and settlement surface, so it anchors market-implied probability and the resolution mechanics that determine what counts as a hit.

## Possible impact on the question

The main analytical burden is whether BTC can trade up through $76,000 within a short weekly window. The market page matters because even a bullish directional BTC view could be wrong if the specific source-of-truth requires a venue print that never occurs.

## Reliability notes

Primary for market framing and contract existence, but only partially captured through readable fetch. Good enough to anchor the market state; not good enough to eliminate all rule ambiguity.