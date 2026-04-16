---
type: source_note
case_key: case-20260415-868fc947
dispatch_id: dispatch-case-20260415-868fc947-20260415T090047Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API + Polymarket market rules
source_type: primary_market_and_resolution_source
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-868fc947/researcher-analyses/2026-04-15/dispatch-case-20260415-868fc947-20260415T090047Z/personas/variant-view.md]
tags: [source-note, polymarket, binance, btc, resolution]
---

# Summary

This note captures the governing market wording from Polymarket and a direct Binance spot/1-minute API check used to anchor how far BTC is currently trading above the 72,000 threshold.

## Key facts extracted

- Polymarket says the market resolves from the Binance BTC/USDT 1-minute candle for **12:00 ET (noon)** on 2026-04-16.
- Resolution condition is the candle's final **Close** price being **higher than 72,000**, not merely touching it.
- The contract is exchange-specific: **Binance BTC/USDT**, not a broader BTC/USD composite.
- ET noon on 2026-04-16 converts to **2026-04-16 16:00:00 UTC**.
- Direct Binance API checks on 2026-04-15 around 09:00 UTC showed BTCUSDT around **74.0k-74.2k**, roughly 2k above the threshold.
- Binance 24h stats at check time showed: last price **74034.23**, high **76038.00**, low **73514.00**.

## Evidence directly stated by source

- Polymarket rules explicitly define the settlement source and condition.
- Binance API directly reports recent BTCUSDT last price and recent 1-minute close data.

## What is uncertain

- The decisive candle is not until 2026-04-16 12:00 ET, so current price only gives distance-to-threshold, not settlement.
- Public API values and site chart values can differ slightly by moment, but not enough here to change the broad conclusion that spot is materially above 72k at check time.

## Why this source may matter

This is the core source-of-truth setup. Because the market is date-sensitive and wording-sensitive, correctly identifying the precise exchange, pair, time window, and price field matters more than broader crypto commentary.

## Possible impact on the question

The direct price check supports the market's bullish baseline: BTC is already meaningfully above 72k. But the same primary-source framing also highlights the neglected risk: resolution depends on one exact future 1-minute close on Binance, so a transient intraday drawdown or exchange-specific divergence could still flip the contract even if BTC remains broadly strong.

## Reliability notes

- Polymarket market page is authoritative for contract wording but not for future outcome.
- Binance is the governing underlying data source for resolution and therefore the most important primary source.
- Exchange APIs are high-value direct evidence for current state, though they do not eliminate overnight volatility risk.