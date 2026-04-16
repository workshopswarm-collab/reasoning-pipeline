---
type: source_note
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-d9ca8ddf | base-rate
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT ticker and recent daily klines
source_type: exchange API / market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, spot-price, recent-range, verification]
---

# Summary

This source provides direct Binance market data relevant to the contract's named resolution venue. It does not yet provide the April 17 12:00 ET settlement candle, but it shows current spot level and recent daily trading range close to the event.

## Key facts extracted

- Binance ticker fetch showed BTCUSDT at 74,984.29 on 2026-04-15.
- The recent 7 daily klines show closes roughly: 71,787.97; 72,962.70; 73,043.16; 70,740.98; 74,417.99; 74,131.55; 74,984.29.
- Over those recent daily candles, BTC traded below 72,000 at least once on a close (70,740.98) and had intraday lows near or below the low 70s.
- Recent daily highs reached into the mid-75k to 76k area, indicating BTC is currently trading meaningfully above the threshold but not by an enormous multiple.

## Evidence directly stated by source

- Direct evidence on current Binance BTCUSDT level: yes.
- Direct evidence on recent realized Binance range and volatility: yes.
- Direct evidence on the exact April 17 noon ET settlement print: no, because that observation has not occurred yet.

## What is uncertain

- Daily klines do not show the exact 12:00 ET 1-minute close needed for settlement.
- The price can move materially between now and the event.
- Daily range data does not fully capture intraday path risk around the settlement minute.

## Why this source may matter

Because the contract settles on Binance, Binance-native price data is the most relevant context. The current spot being about 4% above the threshold supports a high Yes probability, but recent volatility and a nearby sub-72k close keep the probability below certainty.

## Possible impact on the question

This source supports an outside-view judgment that Yes should be favored, but not at a literal near-lock level unless one believes one-day downside risk to below 72,000 by the exact settlement minute is very small.

## Reliability notes

- Strong source quality for venue-consistent price context because it comes from Binance's own API.
- Limited by timeframe mismatch: current ticker and daily klines are contextual, not the final settlement candle.
- More useful when paired with the contract rules from Polymarket.
