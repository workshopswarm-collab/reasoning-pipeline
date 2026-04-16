---
type: source_note
case_key: case-20260415-fc70b9f6
dispatch_id: dispatch-case-20260415-fc70b9f6-20260415T072610Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT direct API check and Polymarket market/rules page
source_type: primary_plus_market_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-fc70b9f6/researcher-analyses/2026-04-15/dispatch-case-20260415-fc70b9f6-20260415T072610Z/personas/variant-view.md]
tags: [binance, polymarket, resolution-check, btc]
---

# Summary

This note records the direct resolution-mechanics check for the April 16 BTC-above-72k market and a spot-level Binance price check during the research run.

## Key facts extracted

- Polymarket's market page states the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final Close price above 72,000.
- The same page states the source of truth is Binance BTC/USDT with 1m candles selected, not other exchanges or pairs.
- Runtime timezone conversion check confirms 2026-04-16 12:00 ET equals 2026-04-16 16:00 UTC.
- Direct Binance API check on 2026-04-15 during this run returned BTCUSDT spot price 73,690.01.
- Direct Binance 1-minute kline API check during this run showed recent closes in the 73,678 to 73,728 area.

## Evidence directly stated by source

- Polymarket rules page directly states the settlement mechanics and governing source.
- Binance API directly returns current BTCUSDT price and recent 1-minute klines.

## What is uncertain

- Current price does not guarantee the exact 12:00 ET one-minute close on April 16.
- API spot and recent klines are a contextual pre-resolution check, not the resolving candle itself.
- There may still be material intraday volatility before the settlement minute.

## Why this source may matter

This is the cleanest available combination of source-of-truth mechanics plus current exchange state. It defines exactly what counts for settlement and shows BTC is currently above the threshold by roughly 1.7k.

## Possible impact on the question

These checks support a bullish baseline for Yes, but they also highlight the main neglected failure mode: this is a single-minute, single-venue close condition, so path dependence and exchange-specific print risk matter more than broad BTC directional conviction.

## Reliability notes

- Polymarket is authoritative for contract wording but not for the final underlying price itself.
- Binance is the named resolution source and therefore authoritative for the price print that matters.
- Evidence independence is only medium because the contextual exchange data and eventual settlement source both come from Binance, though that is appropriate here because the contract explicitly keys to Binance.