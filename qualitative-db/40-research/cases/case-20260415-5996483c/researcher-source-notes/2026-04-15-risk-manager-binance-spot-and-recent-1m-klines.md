---
type: source_note
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 be above 70000?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API spot price and recent 1m klines
source_type: exchange primary data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, spot-price, kline, primary-data]
---

# Summary

This source captures live Binance BTC/USDT spot context and recent one-minute candle behavior from the exchange API named in the market rules.

## Key facts extracted

- Binance API returned BTC/USDT spot price **74,932.85** at research time on 2026-04-15.
- Recent 1-minute candles in the sampled five-minute window all closed well above **70,000**.
- The sampled closes were approximately **74,848.79**, **74,855.60**, **74,857.80**, **74,944.43**, and **74,932.85**.
- This places spot roughly **7.0%** above the 70,000 threshold with several days remaining before the April 20 noon ET resolution print.

## Evidence directly stated by source

Direct API outputs captured during the run:

- `{"symbol":"BTCUSDT","price":"74932.85000000"}`
- Recent 1m kline close values from `api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5` included:
  - 74848.79000000
  - 74855.60000000
  - 74857.80000000
  - 74944.43000000
  - 74932.85000000

## What is uncertain

- This is not the settlement candle; it only shows current and recent conditions on April 15.
- Short-dated crypto can move materially over several days, so current cushion does not guarantee the April 20 noon close remains above 70,000.
- The sampled five-minute window does not characterize all path volatility between now and resolution.

## Why this source may matter

It is the best direct context source because the contract resolves on Binance BTC/USDT itself. It confirms the asset is currently well above threshold on the governing venue, which materially supports a high Yes probability.

## Possible impact on the question

This strongly supports a Yes lean, but the risk-manager caveat is that the contract depends on one exact future minute close rather than a broad average or touch condition. That makes timing/path risk still relevant even with a large current cushion.

## Reliability notes

- High credibility and direct relevance because Binance is the governing source.
- Independence is limited when paired with the Polymarket page because both revolve around the same resolution venue, but they answer different questions: rules vs current governing-market state.
- Best used with an independent contextual market narrative source if available.