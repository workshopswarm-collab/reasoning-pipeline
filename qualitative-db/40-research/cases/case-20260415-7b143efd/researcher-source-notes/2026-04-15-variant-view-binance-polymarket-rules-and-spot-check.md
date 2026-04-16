---
type: source_note
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API + Polymarket rules page + Coinbase spot cross-check
source_type: primary-plus-context
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [variant-view.md, variant-view.sidecar.json]
tags: [binance, polymarket, settlement-rules, spot-check, btc]
---

# Summary

This source bundle establishes the governing settlement mechanics and verifies the current market context from direct surfaces. The Polymarket event page states the contract resolves from the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20, specifically the final Close price for that minute. Binance API spot and recent 1-minute klines show BTC/USDT trading around 74.25k-74.32k on April 15, materially above the 70k threshold, while Coinbase spot is broadly consistent as a contextual cross-check rather than the settlement source.

## Key facts extracted

- Polymarket rules: the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20 has a final Close above 70,000.
- The contract is exchange-specific: Binance BTC/USDT, not BTC/USD and not another venue.
- Price precision is determined by Binance source decimals.
- Current displayed market price for the 70,000 line on the Polymarket page is about 86% Yes.
- Binance ticker price on April 15 spot check: about 74,273.07 BTCUSDT.
- Recent Binance 1-minute klines sampled around 13:20-13:23 UTC on April 15 show closes roughly 74,257-74,322.
- Coinbase spot cross-check at the same time shows BTC around 74,273.165 USD.
- Noon ET on April 20, 2026 converts to 16:00 UTC because New York is on EDT.

## Evidence directly stated by source

- Polymarket directly states the exact source-of-truth and the required condition.
- Binance directly states current BTCUSDT ticker price and recent 1-minute candle closes.
- Coinbase directly states current BTC spot in USD as a contextual cross-check.

## What is uncertain

- Current spot tells us only that BTC is above 70k now, not where it will print at the exact April 20 12:00 ET close.
- Binance API is an acceptable verification surface for current pricing and minute-candle structure, but final market settlement is described by Polymarket as using the Binance trading interface candle close.
- Cross-venue basis could matter at the margin in other markets, but here BTC is several thousand dollars above threshold, so minor basis is unlikely to dominate unless price drops sharply first.

## Why this source may matter

This bundle is enough to confirm the contract mechanics, timing, and the main variant question: whether an 86% market price is too confident given that a single exchange-specific one-minute close four-plus days away can still be invalidated by a moderate drawdown or a venue-specific wick/close difference.

## Possible impact on the question

The source bundle supports a bullish baseline because BTC is currently well above 70k, but it also supports a variant caution: the market is not asking whether BTC stays generally strong, but whether one exact Binance 1-minute close at noon ET on April 20 remains above 70k. That narrower structure makes an extreme 86% probability somewhat fragile to short-horizon volatility.

## Reliability notes

- Polymarket rules page is the governing contract surface for interpretation: high relevance, moderate ambiguity because it references the Binance UI rather than an immutable API endpoint.
- Binance API is highly relevant and direct for current BTCUSDT pricing, though not literally the stated settlement screen.
- Coinbase is independent contextual confirmation of broad BTC level, but not authoritative for settlement.
- Evidence independence is medium: Binance and Polymarket are tightly linked for settlement logic, Coinbase adds one independent market-context check.