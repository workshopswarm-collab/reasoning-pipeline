---
type: source_note
case_key: case-20260416-e0b8c17c
dispatch_id: dispatch-case-20260416-e0b8c17c-20260416T050131Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance API and Polymarket rules page
source_type: primary-plus-market-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: base-rate
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-analyses/2026-04-16/dispatch-case-20260416-e0b8c17c-20260416T050131Z/personas/base-rate.md]
tags: [source-note, binance, polymarket, btc, settlement]
---

# Summary

This note captures the core direct evidence for a date-specific BTC threshold market: Polymarket's own rule text and Binance's BTCUSDT API surfaces. Together they define both the governing settlement mechanics and the current structural context.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT 1 minute candle for 12:00 ET on the named date, using the candle's final close price.
- The threshold is strict: the final close must be higher than 72,000; equality would resolve No.
- The contract is specifically about Binance BTC/USDT, not another exchange or another BTC pair.
- Binance spot ticker returned BTCUSDT price of 75,000.00000000 on 2026-04-16 fetch.
- Binance daily klines for the prior ~30 days show BTC recently trading from the mid-60ks up through the mid-70ks, including daily closes above 72k on multiple recent days and a 2026-04-16 partial daily bar around 75,000.

## Evidence directly stated by source

- Direct settlement language came from the Polymarket event page rules section.
- Direct current-price and historical-range data came from Binance API endpoints:
  - `/api/v3/ticker/price?symbol=BTCUSDT`
  - `/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=30`

## What is uncertain

- The actual resolving value will be the 12:00 ET 1-minute close on 2026-04-20, not the current spot or any daily close.
- Daily candles do not show intraday noon ET specifically, so they are contextual rather than directly resolving.
- Short-horizon crypto volatility can move price several thousand dollars between now and resolution.

## Why this source may matter

The contract is narrow and rule-sensitive. A direct check of the named settlement source is necessary to avoid assuming wrong exchange, pair, timestamp, or price rule.

## Possible impact on the question

This source set supports a high but not near-certain Yes probability. BTC is currently comfortably above 72k on Binance and has spent several recent days above that level, but the contract still depends on a specific 1-minute close four days from now.

## Reliability notes

- Binance is the named governing source of truth for settlement, so it is authoritative for the specific contract.
- Polymarket is authoritative for interpreting the market's own rules.
- Evidence independence is only medium because the settlement source and contextual price source are both tied to Binance, though that is appropriate here because the contract itself names Binance.