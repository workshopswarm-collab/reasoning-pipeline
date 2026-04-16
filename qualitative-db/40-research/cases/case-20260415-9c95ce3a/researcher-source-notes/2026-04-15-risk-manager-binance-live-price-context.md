---
type: source_note
case_key: case-20260415-9c95ce3a
dispatch_id: dispatch-case-20260415-9c95ce3a-20260415T173129Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance public BTCUSDT ticker and kline API snapshot
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-9c95ce3a/researcher-analyses/2026-04-15/dispatch-case-20260415-9c95ce3a-20260415T173129Z/personas/risk-manager.md]
tags: [binance, btcusdt, live-price, short-horizon]
---

# Summary

This source provides current Binance BTC/USDT context close to the research time. It does not settle the market, but it shows BTC/USDT already trading materially above 72,000 on April 15, two days before resolution.

## Key facts extracted

- Binance public ticker returned BTCUSDT price 74118.80000000 at research time.
- Recent 1-minute klines around 17:34-17:36 UTC on April 15 showed closes around 74117-74143.
- Recent 1-hour klines still showed BTCUSDT in the high-73k to low-74k area during the sampled window.
- This means spot is already about 2.9% above the 72,000 threshold.

## Evidence directly stated by source

Direct API outputs captured during the run:
- ticker price: 74118.80000000
- 1m close at 2026-04-15T17:35:00Z: 74118.80000000
- 1m close at 2026-04-15T17:36:00Z: 74117.38000000

## What is uncertain

- This is a snapshot, not a forecast.
- The market resolves on April 17 at 12:00 ET, not on April 15.
- Short-horizon crypto volatility can erase a low-single-digit cushion quickly.
- Public API data and webpage chart display should usually align, but the contract specifically references the Binance chart interface.

## Why this source may matter

It establishes the starting distance to threshold. For risk analysis, the key question becomes whether a roughly 2k drawdown over the next ~44 hours is sufficiently plausible to justify discounting the 82% market price.

## Possible impact on the question

The source is supportive of a Yes lean because the market starts above threshold, but it also sharpens the real downside path: a modest adverse move, not a regime collapse, could flip the contract to No.

## Reliability notes

Binance is the named resolution source, so using its own public market data is high-value and close to primary. Reliability is strong for current context, but this note is still contextual rather than dispositive because resolution depends on a later timestamp.