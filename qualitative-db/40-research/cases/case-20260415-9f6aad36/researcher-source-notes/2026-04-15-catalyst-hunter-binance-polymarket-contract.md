---
type: source_note
case_key: case-20260415-9f6aad36
dispatch_id: dispatch-case-20260415-9f6aad36-20260415T082436Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: binance-resolution-mechanics-and-current-price
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on April 16, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API and Polymarket market page
source_type: primary_market_data_and_contract_page
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-9f6aad36/researcher-analyses/2026-04-15/dispatch-case-20260415-9f6aad36-20260415T082436Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, resolution-source, price-level]
---

# Summary

This source set establishes the governing contract mechanics and gives a direct current Binance BTC/USDT reference price for comparison against the 72,000 threshold.

## Key facts extracted

- Polymarket says the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16, 2026 has a final Close price higher than 72,000.
- The contract explicitly uses Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by Binance's displayed source precision.
- Binance spot ticker at fetch time showed BTCUSDT at 73,970.88.
- Recent Binance 1-minute klines around 04:22-04:26 ET on April 15, 2026 were clustered near 73,915-73,974, i.e. about 1,971 points above the 72,000 threshold.

## Evidence directly stated by source

- Direct contract text from Polymarket names Binance BTC/USDT 1-minute candle close at 12:00 ET as source of truth.
- Direct Binance API output gave ticker price 73,970.88000000 for BTCUSDT.
- Direct Binance kline output showed the latest fetched minute closed at 73,970.88.

## What is uncertain

- The contract resolves on April 16 at 12:00 ET, not at current time; current spot only informs distance-to-threshold, not the final answer.
- The Polymarket page text is authoritative for visible rules, but exact settlement behavior still depends on Binance data availability and final displayed close at the relevant minute.
- Intraday BTC volatility could erase a ~2.7% cushion before noon ET tomorrow.

## Why this source may matter

This is the core source-of-truth bundle. It defines what counts and anchors the current state relative to the threshold.

## Possible impact on the question

The contract is mechanically straightforward: all material conditions are Binance BTC/USDT, the specific 12:00 ET one-minute candle on April 16, and a final close strictly above 72,000. With BTC currently near 73,971, the market starts from a favorable level, but the remaining question is whether any catalyst before noon ET tomorrow can push Binance spot below the threshold at that exact minute.

## Reliability notes

- Binance API is direct primary market data, high reliability for current spot context.
- Polymarket market page is the direct visible contract rules surface.
- Independence is limited because both sources concern the same contract/venue mechanics, so a contextual market source is still useful for catalyst framing.