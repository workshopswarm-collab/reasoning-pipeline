---
type: source_note
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API BTCUSDT spot data
source_type: exchange market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=30
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, price-data, source-note]
---

# Summary

Binance public spot-market data shows BTC/USDT trading well above 72,000 on the assignment date, with recent daily closes mostly in the 71k-75k range and the live spot price around 74.7k at the time of collection.

## Key facts extracted

- Binance ticker endpoint returned BTC/USDT at 74,748.92 on 2026-04-15 around 23:15 UTC.
- Recent daily closes from Binance were:
  - 2026-04-10: 72,962.70
  - 2026-04-11: 73,043.16
  - 2026-04-12: 70,740.98
  - 2026-04-13: 74,417.99
  - 2026-04-14: 74,131.55
  - 2026-04-15 partial/current day close field at collection time: 74,695.61
- Recent daily lows/highs show BTC has recently traded both below and well above 72,000, but the center of the recent range sits above the contract strike.
- A direct 1-minute kline query for 16:00 UTC (which corresponds to 12:00 ET during US daylight time in April) returned valid Binance minute candles for 2026-04-14 and 2026-04-15, supporting the contract’s timing interpretation.

## Evidence directly stated by source

- Binance API endpoints directly provide BTC/USDT ticker and kline values.
- The data directly shows recent price levels and recent realized distribution relative to 72,000.

## What is uncertain

- This source does not itself prove the final April 19 noon-ET minute close; it only gives current and recent context.
- Intraday BTC volatility over the next several days could still move price materially below the threshold by resolution time.
- The public API is a strong proxy for Binance market data, but the contract text points traders to the Binance trading UI candle close as the official resolution surface.

## Why this source may matter

This is the most relevant direct market-data source available for establishing whether 72,000 is currently in-the-money or out-of-the-money, how far spot is from the threshold, and whether the recent realized range makes the threshold structurally easy or hard to hold.

## Possible impact on the question

The source pushes the view toward Yes because BTC is currently about 3.8% above the threshold and has recently spent multiple days closing above it. It does not settle the market because the contract depends on a specific future one-minute close, but it materially informs the base-rate prior.

## Reliability notes

- High relevance because Binance is also the governing venue for settlement.
- Strong for current/recent price context.
- Slight source-of-truth caveat: the market resolves from the Binance UI candle close at a specific minute, not from a generic aggregated external price feed.