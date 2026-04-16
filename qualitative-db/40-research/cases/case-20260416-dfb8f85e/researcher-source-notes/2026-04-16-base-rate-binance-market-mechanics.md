---
type: source_note
case_key: case-20260416-dfb8f85e
dispatch_id: dispatch-case-20260416-dfb8f85e-20260416T140232Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-21 close above 72000?
driver: reliability
date_created: 2026-04-16
source_name: Binance spot API market data docs + live BTCUSDT ticker
source_type: primary_and_direct
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [crypto, bitcoin, binance, resolution, source-note]
---

# Summary

Binance is the governing source of truth for this market, and its public market-data documentation plus live BTCUSDT ticker output make the resolution mechanics legible enough to audit. The relevant contract condition is the final close of the BTCUSDT 1-minute candle at 12:00 ET on April 21, not a daily close or cross-exchange composite price.

## Key facts extracted

- Binance spot API documents `GET /api/v3/klines` for 1-minute candles and identifies the returned close price field explicitly.
- Binance docs state that if `timeZone` is provided, kline intervals are interpreted in that timezone; accepted values include hour offsets like `-4`, which matches ET during April daylight saving time.
- The market wording says the resolution source is Binance BTC/USDT with `1m` candles selected.
- Live Binance BTCUSDT ticker on 2026-04-16 printed about `73729.99`, meaning spot is already modestly above the 72000 strike several days before resolution.
- Recent daily Binance BTCUSDT closes from April 7-16 were mostly above 72000, with brief dips below that level on April 8 and April 12.

## Evidence directly stated by source

- Binance market-data docs explicitly define the kline endpoint and show that the close price is a returned field in the candle array.
- Binance docs explicitly note timezone handling for kline interpretation.
- Polymarket rules explicitly state that the market resolves on the Binance 12:00 ET BTC/USDT 1-minute candle close.

## What is uncertain

- The public docs establish how candle data is represented, but they do not by themselves guarantee what Binance UI or exchange operations might look like if there is a transient outage near resolution.
- The market text references the Binance web trading interface specifically; API and UI should normally agree, but operational edge cases remain possible.

## Why this source may matter

This is the most important direct source because the market is mechanically settled by one exchange, one pair, one minute, and one close field. For a narrow date-and-time crypto contract, source mechanics matter almost as much as price direction.

## Possible impact on the question

Because BTCUSDT is already trading above 72000 and because the contract uses a single 1-minute Binance candle rather than a broader average, the main risk to a Yes view is short-horizon volatility around noon ET on April 21 rather than ambiguity about which price series counts.

## Reliability notes

High reliability for contract interpretation and current spot context. Moderate operational caveat because single-venue, single-minute settlement creates some fragility if Binance experiences a data or UI issue near the cut time.