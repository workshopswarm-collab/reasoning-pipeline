---
type: source_note
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance API spot price and recent 1m klines; Coinbase ticker cross-check
source_type: exchange API / market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/market-implied.md]
tags: [binance, coinbase, spot-price, btc, context]
---

# Summary

This source note captures the live market context around research time: Binance BTCUSDT spot was already above the strike and Coinbase BTC-USD was nearly identical, which supports the market's positive lean but does not settle the April 17 noon ET outcome.

## Key facts extracted

- Binance API ticker showed BTCUSDT around 74,645.30 at fetch time.
- Recent Binance 1-minute klines showed closes around 74,796.34, 74,815.10, 74,724.69, 74,668.45, and 74,638.76, all above 74,000.
- Coinbase BTC-USD ticker cross-check showed about 74,659.5 at nearly the same timestamp.
- Cross-venue dispersion looked small at that moment, which reduces concern that Binance-specific pricing was far off from broader spot context.

## Evidence directly stated by source

- Binance current ticker price was above 74,000.
- Binance recent one-minute closes were above 74,000.
- Coinbase spot was also above 74,000 at the same general time.

## What is uncertain

- This only establishes current context roughly 11 hours before the relevant noon ET settlement window.
- BTC can move materially intraday; being above the strike now does not guarantee being above it at the relevant candle close.
- Coinbase is contextual only because the contract resolves specifically on Binance BTC/USDT.

## Why this source may matter

The market-implied question is fundamentally a short-horizon spot-price question. When current Binance spot is already modestly above the strike and another major venue aligns closely, the market has a plausible reason to price Yes above 50% but not near certainty.

## Possible impact on the question

Supports a mild-to-moderate Yes lean rather than an extreme one. The market's ~65% appears consistent with current spot being above the strike by roughly 0.9% while there is still enough time for meaningful reversal before noon ET.

## Reliability notes

High recency and high relevance. Binance API is close to the contract's source of truth, though the exact resolving observation is a future specific 12:00 ET one-minute close. Coinbase provides a useful independent contextual cross-check but is not a settlement source.