---
type: source_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: prediction-markets
entity:
topic: polymarket-eth-above-2100-apr-10
question: Will the price of Ethereum be above $2,100 on April 10?
driver: operational-risk
date_created: 2026-04-09
source_name: Polymarket event page
source_type: market_rules_and_live_price_surface
source_url: https://polymarket.com/event/ethereum-above-on-april-10
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/market-implied.md]
tags: [polymarket, market-price, resolution-rules]
---

# Summary

This note captures the current market-implied view and the formal market wording from Polymarket.

## Key facts extracted

- The assigned current price is 0.94, while the visible event page scrape showed the 2100 line trading around 97.4% at fetch time.
- The market page states the market resolves Yes if the Binance 1-minute candle for ETH/USDT at 12:00 ET on Apr 10 has a final close price higher than 2100.
- The page states the resolution source is Binance ETH/USDT with 1m candles selected.
- The page states price precision is determined by the number of decimal places in the source.
- Adjacent ladder prices on the page were roughly 99% for 2000, 97% for 2100, 60% for 2200, and 7% for 2300, implying the market sees 2100 as comfortably in-the-money but not trivially guaranteed.

## Evidence directly stated by source

- Market wording and resolution source.
- Current market odds on nearby strikes.

## What is uncertain

- The event page scrape may lag slightly behind the assignment metadata; for this run I treat the assignment value 0.94 as the official baseline because it is provided in runtime context.
- The page itself does not explain whether the targeted “12:00” candle is indexed by open time or close time.

## Why this source may matter

This is the direct market surface. It tells us what the market is pricing and how sharply traders are distinguishing 2100 from nearby thresholds.

## Possible impact on the question

The nearby-strike ladder suggests the market is not merely saying ETH is strong; it is specifically pricing a cluster around the low 2200s, which supports a high Yes probability for 2100 without implying certainty.

## Reliability notes

Strong for observing market-implied probability and rule text, but weaker than Binance for ultimate settlement mechanics because Polymarket is downstream from the stated source of truth.