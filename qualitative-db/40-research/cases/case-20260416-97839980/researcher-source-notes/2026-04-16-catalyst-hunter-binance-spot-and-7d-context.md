---
type: source_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-data
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: reliability
date_created: 2026-04-16
source_name: Binance SOLUSDT API spot and recent daily candles
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [sol]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/catalyst-hunter.md]
tags: [binance, solusdt, price, candles]
---

# Summary

Binance API data showed SOL/USDT around 85.37 at the spot check, with the prior week of daily candles mostly closing in the low-to-mid 80s and recent intraday ranges remaining above 80 except for some lows in the 81-83 area.

## Key facts extracted

- Binance ticker endpoint returned SOLUSDT price 85.37.
- Recent daily closes in the fetched 7-day window were approximately 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, and 85.31.
- Recent daily lows in that same window were roughly 82.62, 83.80, 81.27, 81.40, 83.30, 82.65, and 84.45 so far for the current day.
- This recent range suggests SOL is not barely clinging to 80; it has had several dollars of cushion over the threshold recently.

## Evidence directly stated by source

- Binance currently prices SOL/USDT above 80 by more than 5 points.
- The recent daily pattern indicates sustained trading above 80 rather than a single isolated spike.

## What is uncertain

- Daily candles are contextual rather than the exact resolution print.
- A sharp crypto-wide risk-off move before Sunday noon ET could still push SOL below 80.
- API spot price and daily candles do not capture weekend event risk or intraminute volatility at the exact resolving minute.

## Why this source may matter

This is the exchange family that governs settlement. Even though the exact contract resolves on a 1-minute candle close, current Binance spot and recent Binance trading context are the most directly relevant data for judging whether 80 is likely to hold by April 19 noon ET.

## Possible impact on the question

The current cushion above 80 and recent persistence above the threshold support a high Yes probability, unless a fresh catalyst creates a several-percent drawdown before resolution.

## Reliability notes

High relevance because Binance is the governing source family. Contextual limitation: the fetched data are not the exact future 1-minute settlement candle.