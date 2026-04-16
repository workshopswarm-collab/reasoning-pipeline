---
type: source_note
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-15 be above 72000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance BTCUSDT live market data and kline API
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, resolution-source, btcusdt, 1m-candle]
---

# Summary

Binance is both the governing resolution source and the most direct market context source for this case. Direct API checks on 2026-04-13 show BTC/USDT trading around 73.8k, already above the 72k strike with roughly 42 hours remaining until the relevant 12:00 ET candle on 2026-04-15.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT at `73836.17000000` during this research run.
- Recent 1-minute klines fetched from Binance showed closes around `73456.70`, `73584.24`, `73753.26`, `73854.18`, and `73855.09`.
- The market rules specify the relevant observation is the Binance BTC/USDT 1-minute candle labeled 12:00 ET on Apr. 15, 2026, using the final candle close.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

- Binance is publishing current BTC/USDT spot pricing above 72,000 during the run.
- Binance supports direct retrieval of 1-minute candle close values, matching the market's resolution mechanism.

## What is uncertain

- This source alone does not predict where BTC/USDT will be at exactly 12:00 ET on Apr. 15.
- Binance API access now does not guarantee there will be no outage, methodology change, or unusual market move before resolution.
- The web UI uses ET framing in Polymarket's rules, while Binance server timestamps are UTC milliseconds; precise resolution requires correct timezone mapping on Apr. 15.

## Why this source may matter

This is the governing source of truth and the cleanest direct evidence for whether the market-implied 72.5% probability is plausible. Since current spot is already roughly 1.8k above strike, the market does not need a bullish breakout; it mainly needs BTC to avoid falling below 72k by the specified minute.

## Possible impact on the question

Directly supports a Yes-lean because current Binance price is above strike with moderate cushion. Also frames the main risk as short-horizon downside volatility or source/operational quirks, not lack of current spot support.

## Reliability notes

High credibility for resolution mechanics because Binance is the explicit settlement source. Independence is limited because the same source also defines the event outcome; a separate contextual source is still needed for a market-efficiency check rather than relying only on the settlement venue itself.