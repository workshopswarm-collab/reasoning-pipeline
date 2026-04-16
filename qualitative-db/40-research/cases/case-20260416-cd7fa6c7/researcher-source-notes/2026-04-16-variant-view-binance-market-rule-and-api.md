---
type: source_note
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-cd7fa6c7 | variant-view
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance kline API docs
source_type: primary-rule + primary-technical-doc
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/variant-view.md]
tags: [polymarket, binance, resolution, btcusdt, 1m-candle]
---

# Summary

The governing rule is narrower than a generic “BTC above 74k on Apr 17” framing. Resolution depends specifically on the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 17, using the final Close price for that minute. Binance API documentation confirms klines are identified by open time and expose a distinct close field and close time.

## Key facts extracted

- Polymarket rule: market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET (noon) on Apr 17 has a final Close price strictly higher than 74,000.
- Polymarket rule: exchange and pair are fixed to Binance BTC/USDT, not other exchanges or pairs.
- Binance kline docs: `/api/v3/klines` returns OHLCV bars; klines are uniquely identified by open time.
- Binance kline response includes close price and kline close time, which makes the relevant bar auditable in API terms.
- The date/timing mapping for Apr 17 12:00 ET corresponds to Apr 17 16:00:00Z open time because New York is on EDT (UTC-4).

## Evidence directly stated by source

- Polymarket directly states the resolution source and exact condition.
- Binance docs directly state the kline structure and timing semantics.

## What is uncertain

- Whether Binance website UI and API display remain perfectly aligned at settlement, though they should usually match.
- Whether any exchange-specific transient wick or minute-end move could materially diverge from broader spot composites.

## Why this source may matter

This source defines what actually has to happen for the contract to resolve Yes. For a time-specific 1-minute candle market, the main neglected risk is not broad BTC direction but minute-level path dependence on one exchange at one timestamp.

## Possible impact on the question

This pushes analysis away from “Is BTC generally trading above 74k?” toward “How likely is Binance BTC/USDT to finish the exact noon ET minute above 74k?” A thin margin above 74k can still be fragile if the market is treating spot level as equivalent to the settlement condition.

## Reliability notes

High reliability for contract interpretation because Polymarket is the governing market rule source and Binance docs are the governing technical reference for the data object being referenced.