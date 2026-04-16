---
type: source_note
case_key: case-20260416-bac9c8f2
dispatch_id: dispatch-case-20260416-bac9c8f2-20260416T033803Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket rules page plus CoinGecko spot cross-check
source_type: market-rules-and-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, market-rules, coingecko, contextual-crosscheck]
---

# Summary

Polymarket's market page states that resolution is based specifically on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET, while a CoinGecko spot cross-check shows bitcoin around $75.0k at review time, broadly consistent with Binance and therefore suggesting the market is not being distorted by an obvious venue-specific price gap at the moment.

## Key facts extracted

- Polymarket lists the 74,000 line around 72%-73%, consistent with the assignment's `current_price: 0.71`.
- The rule is not generic BTC spot; it is specifically the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17.
- CoinGecko's simple price endpoint returned bitcoin at `75009` USD, close to Binance's `75042.98` BTCUSDT quote at nearly the same time.
- The current cushion above the threshold is roughly $1,000, which is small relative to routine intraday BTC volatility over a full day.

## Evidence directly stated by source

- Polymarket directly states the governing source, timing convention, and price condition.
- CoinGecko directly states a contemporaneous bitcoin USD spot level close to Binance.

## What is uncertain

- CoinGecko is contextual only; it cannot settle the market.
- A small current premium over 74,000 does not say much about the exact noon ET close tomorrow.
- The Polymarket page does not fully specify how a UI-labeled 12:00 ET candle maps to Binance's UTC-based backend if there is any display-layer discrepancy.

## Why this source may matter

This note clarifies the contract mechanics and checks that the broad market level is near the same zone across an independent contextual source, which matters because the variant case here is mostly about overconfidence and timing fragility rather than a claim that Binance is wildly off-market.

## Possible impact on the question

The combination supports a moderate yes lean, but also a live no path: if BTC slips only modestly before the exact settlement minute, the contract fails. That makes an aggressively bullish interpretation look somewhat overconfident.

## Reliability notes

Polymarket is authoritative for contract wording, while CoinGecko is only a contextual cross-check. Evidence independence is medium because the pricing cross-check is external to Binance, but all sources are still describing the same underlying bitcoin market regime.