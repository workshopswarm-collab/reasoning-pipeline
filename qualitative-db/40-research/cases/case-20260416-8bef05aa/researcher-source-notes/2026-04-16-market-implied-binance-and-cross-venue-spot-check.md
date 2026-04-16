---
type: source_note
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-market
entity: binance
topic: Current BTC spot context versus 72000 threshold
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: macro
date_created: 2026-04-16
source_name: Binance API with CoinGecko and Coinbase spot cross-check
source_type: primary exchange data plus contextual cross-checks
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [binance, btc]
related_drivers: [macro, liquidity]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/market-implied.md
tags: [source-note, binance, btc, spot-context]
---

# Summary

A direct Binance spot/API check plus two independent venue/context checks show BTC already trading materially above 72,000 at analysis time, around 73.9k-74.0k. That means the market is effectively pricing the probability that BTC can stay above 72,000 through the specific Apr 21 noon ET close rather than climb above it from below.

## Key facts extracted

- Binance BTCUSDT ticker at capture: `73977.13`.
- Recent Binance 1m closes in the sample were mostly `73852.97` to `73977.13`.
- CoinGecko BTC/USD check: `73893`.
- Coinbase BTC-USD spot check: `73970.365`.
- BTC was therefore about `1,900-2,000` dollars above the 72,000 threshold at capture, or roughly `2.6%-2.8%` above the line.

## Evidence directly stated by source

- Binance API is the best direct proxy available in-run for the exchange and pair named in the contract.
- Cross-venue checks show no obvious Binance-only dislocation at capture.

## What is uncertain

- This does not prove where BTC will close at 12:00 ET on Apr 21.
- The contract settles on the specific 12:00 ET 1m close, not on today’s spot print.
- Venue-specific basis between BTCUSDT and BTCUSD could matter slightly near the threshold, though the current margin above 72k is large enough that tiny basis differences are not the main issue right now.

## Why this source may matter

This is the main contextual evidence supporting the market price: BTC is already comfortably above the target line, so the live question is about persistence over a short horizon rather than a fresh breakout.

## Possible impact on the question

If BTC remains in the current regime, 72k should stay more likely than not by Apr 21 noon ET. A bearish move of roughly 2.7% or more by the settlement window would be needed to flip the answer to No.

## Reliability notes

High recency and high relevance. Binance is the governing venue, while CoinGecko and Coinbase improve independence by showing the broader market is in the same price neighborhood.
