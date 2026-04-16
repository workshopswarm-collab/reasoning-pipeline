---
type: source_note
case_key: case-20260416-33b4e3b5
dispatch_id: dispatch-case-20260416-33b4e3b5-20260416T021538Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: reliability
date_created: 2026-04-15
source_name: Binance Spot API and market rule surface
source_type: exchange API + market rules
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=30
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [crypto, sol, binance, polymarket, base-rate]
---

# Summary

Binance is both the governing resolution source and the best direct context source here. Current SOL/USDT spot is around $84.8-$84.9, above the $80 threshold by roughly 6%. Recent Binance daily and hourly closes show SOL has spent most of the last two weeks above $80, but the threshold is still close enough that a modest down move by noon ET on Apr. 19 would flip the market.

## Key facts extracted

- Polymarket rules say this resolves from the Binance SOL/USDT 1-minute candle at 12:00 ET on Apr. 19, using the final close price for that minute.
- Binance API docs state klines are uniquely identified by open time, and `timeZone` can be specified so intervals are interpreted in that timezone.
- Current Binance spot/ticker during this run was about 84.79-84.91.
- In the last 29 completed daily candles before the current partial day, 28 closed above 80.
- In those same 29 completed daily candles, 22 daily lows stayed above 80, implying 7 days dipped below 80 intraday even though most later closed back above.
- In the last 167 completed hourly candles before the current partial hour, all 167 hourly closes were above 80.
- Recent 24h Binance stats showed high 85.83, low 82.65, weighted average 84.04, last price 84.79.

## Evidence directly stated by source

- Binance market-data docs: `GET /api/v3/klines` returns candlestick bars, identified by open time; intervals can be interpreted in a specified timezone.
- Binance spot endpoints returned current SOLUSDT spot and recent daily/hourly/1m candles.
- Polymarket rules explicitly define the winning condition as the Binance SOL/USDT 12:00 ET 1-minute candle close being higher than 80.

## What is uncertain

- The source does not directly tell us where SOL will trade at noon ET on Apr. 19; it only establishes current state and recent frequency.
- The Polymarket wording references Binance web UI candles, while verification here used Binance public API docs/endpoints; those should normally align, but that remains a small operational assumption.
- Crypto trades continuously, so macro/news shocks over the next ~3.5 days could still move SOL materially.

## Why this source may matter

This is the key source because it governs settlement and also gives the most direct outside-view context on how often SOL has recently sat above or below the threshold on the same exchange/pair that will decide the market.

## Possible impact on the question

The source supports a base-rate view that Yes is favored because current price is comfortably above 80 and recent Binance closes have mostly stayed above 80. It also limits confidence because intraday dips below 80 have still happened several times, so a high-80s probability should not be treated like certainty.

## Reliability notes

High reliability for contract mechanics and current exchange data. Moderate inferential power for a date-specific future candle because recent-frequency evidence is still only a short-window base rate and crypto can move sharply over multiday horizons.