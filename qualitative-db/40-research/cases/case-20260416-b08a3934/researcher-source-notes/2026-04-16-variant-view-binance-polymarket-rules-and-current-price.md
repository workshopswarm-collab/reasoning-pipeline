---
type: source_note
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance spot API/docs
source_type: primary-plus-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [variant-view.md, variant-view.sidecar.json]
tags: [polymarket, binance, resolution-mechanics, btc-price]
---

# Summary

The governing contract says this market resolves from the Binance BTC/USDT **1-minute candle labeled 12:00 in ET** on April 17, using the candle's final **Close** price. Current Binance spot data places BTC around $75.1k late on April 15 ET, materially above the $72k threshold. The important variant-view issue is not the broad BTC direction but whether market confidence underweights execution and resolution-path fragility: a one-minute close on a named venue can still fail on exchange-specific dislocation, sudden intraday drawdown, or time-label misunderstanding.

## Key facts extracted

- Polymarket rules explicitly say the market resolves "Yes" if the Binance BTC/USDT **1 minute candle for 12:00 in the ET timezone (noon)** on April 17 has a final **Close** price above 72,000.
- The market is specifically about **Binance BTC/USDT**, not other exchanges or other pairs.
- Binance spot API docs for `/api/v3/klines` say klines are uniquely identified by open time, support `interval=1m`, and allow a `timeZone` parameter for interval interpretation; `startTime` and `endTime` are still interpreted in UTC.
- 2026-04-17 12:00 ET converts to **2026-04-17 16:00:00 UTC**.
- Binance spot ticker on 2026-04-15 22:40 ET showed BTCUSDT around **75,115-75,118**, roughly **4.3% above** the 72,000 threshold.
- Binance 24h stats showed a 24h low near **73,514** and a high near **75,425**, implying the threshold is currently comfortably but not absurdly below spot.

## Evidence directly stated by source

- Direct contract language from Polymarket defines the exact settlement source and condition.
- Binance docs directly describe kline endpoint behavior and open-time identification.
- Binance ticker and 24h endpoints directly report current BTCUSDT spot level and recent range.

## What is uncertain

- The exact visual labeling on the Binance front-end chart at settlement time may still matter if UI behavior differs from API interpretation.
- BTC can move several percent in less than a day; current cushion is meaningful but not resolution-proof.
- Exchange-specific wick/dislocation risk exists even if broader crypto prices remain above 72k elsewhere.

## Why this source may matter

This source pair covers both the **source of truth** (Polymarket contract and named Binance venue) and the **current state** of the underlying market. That is sufficient to anchor a probability estimate for a short-horizon, date-specific crypto threshold market.

## Possible impact on the question

Taken together, these sources support a high-probability Yes baseline while preserving a credible No variant path through venue-specific or intraday execution risk. The variant case is weaker than the consensus but not negligible because settlement depends on one minute on one venue, not a broad daily-average BTC narrative.

## Reliability notes

- Polymarket contract text is authoritative for market mechanics.
- Binance API documentation is high-quality contextual evidence for how the relevant candle is defined and queried, though the contract references the Binance UI chart rather than the API directly.
- Binance live ticker and 24h stats are direct current-state evidence but obviously not forward-settling evidence.