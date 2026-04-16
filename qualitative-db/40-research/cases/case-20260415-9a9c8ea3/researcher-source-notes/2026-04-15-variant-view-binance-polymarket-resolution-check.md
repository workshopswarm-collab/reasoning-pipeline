---
type: source_note
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API + Polymarket market rules
source_type: primary-plus-resolution-context
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, resolution, timing, btc]
---

# Summary

This note checks the actual settlement mechanics and current distance from the $72,000 threshold using Binance as the named source of truth and Polymarket's own rule text.

## Key facts extracted

- Polymarket says this market resolves on the Binance BTC/USDT 1-minute candle for `12:00` ET on April 16, using the candle's final `Close` price.
- The rule is explicitly exchange-specific: Binance BTC/USDT, not another exchange or pair.
- Binance API 1-minute klines show candles indexed by minute-open time with a final close timestamp ending `:59.999` for that minute.
- Recent Binance API spot price around research time was about `74,644-74,649`, roughly `2,644-2,649` above the $72,000 threshold.
- Binance 24h stats at check time showed low `73,514`, high `74,786.72`, weighted average `74,135.60`, suggesting the market was not just barely above the strike but sitting materially above it.

## Evidence directly stated by source

- Polymarket rule text: resolve `Yes` if the Binance 1-minute candle for BTC/USDT `12:00` ET on the specified date has a final close higher than the threshold.
- Binance API directly provides BTCUSDT 1m kline close values and timestamps.

## What is uncertain

- Polymarket points users to the Binance web chart surface, while this note verifies with Binance's public API rather than the visual chart UI.
- There is still overnight price risk between now and the noon ET settlement minute.
- The exact interpretation of the `12:00` ET candle is inferred as the minute beginning at 12:00:00 ET and closing at 12:00:59.999 ET, consistent with Binance 1m kline mechanics.

## Why this source may matter

This is the highest-quality combination for this case: the market's own rules define what counts, and Binance provides the direct exchange data series the contract references.

## Possible impact on the question

This pushes toward `Yes` because BTC is currently trading well above the threshold, but it also highlights the real variant risk: the contract depends on one exact exchange-specific 1-minute close at noon ET tomorrow, so a large intraday drop or exchange-specific dislocation would be enough to flip resolution.

## Reliability notes

- Binance is the named resolution source, so source-of-truth quality is high for price data.
- Polymarket's own rules are authoritative for contract interpretation.
- Independence is only medium because both pieces are part of the same settlement stack rather than independent market forecasting evidence.