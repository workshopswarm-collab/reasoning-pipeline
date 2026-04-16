---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchange-price
topic: solana-above-80-on-april-19
question: Is current Binance SOL/USDT price action far enough above 80 to justify a high Yes probability for Apr. 19 noon ET?
driver: reliability
date_created: 2026-04-16
source_name: Binance SOLUSDT ticker and 1m klines API
source_type: primary exchange data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-07c415fe/researcher-analyses/2026-04-16/dispatch-case-20260416-07c415fe-20260416T031541Z/personas/risk-manager.md]
tags: [binance, primary-source, price-data, verification]
---

# Summary

This source note captures the primary-source verification pass using Binance data, which is the same exchange family named by the contract for settlement.

## Key facts extracted

- Binance ticker endpoint returned **SOLUSDT = 85.30000000** at fetch time.
- Recent 1-minute Binance klines showed closes clustered around **85.19 to 85.28**, indicating spot was not merely flickering above 80 but sitting about **6%+ above the threshold**.
- Time to resolution was approximately **84.7 hours** from the analysis timestamp, so there is meaningful remaining path risk despite current spot being above the strike.

## Evidence directly stated by source

- Current Binance spot/ticker price was above 80.
- Recent Binance one-minute candles also closed above 80.
- The observed tape near 85 suggests that if resolution occurred immediately, Yes would likely resolve.

## What is uncertain

- These API endpoints are not the exact Binance web UI candle panel referenced by Polymarket, even though they are highly relevant proxies from the same venue.
- Four days is long enough for crypto to move materially; current spot cannot settle a future date-specific market.
- The endpoints do not independently prove what the 2026-04-19 12:00 ET candle will be.

## Why this source may matter

This is the strongest direct evidence for the current state of the underlying. It meaningfully supports a high Yes probability while also clarifying the main failure mode: the market still needs SOL/USDT on Binance to remain above 80 specifically at the designated minute.

## Possible impact on the question

The source supports a Yes-leaning view because current price is clearly above the threshold. But from a risk-manager perspective it also argues against overconfidence: a 6%-7% cushion in crypto with ~3.5 days remaining is comfortable, not deterministic.

## Reliability notes

Binance is the named source of truth for settlement, so this is high-quality direct evidence. The main caveat is exact implementation parity between public API outputs and the final candle visible on Binance's UI at settlement time.