---
type: source_note
case_key: case-20260415-04e7318a
dispatch_id: dispatch-case-20260415-04e7318a-20260415T145259Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-04e7318a | market-implied
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance market-data surfaces
source_type: primary-plus-authoritative-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-04e7318a/researcher-analyses/2026-04-15/dispatch-case-20260415-04e7318a-20260415T145259Z/personas/market-implied.md]
tags: [binance, polymarket, resolution-mechanics, live-price]
---

# Summary

This source note captures the governing contract mechanics from the Polymarket market page plus direct Binance market-data checks relevant to whether the market-implied 87% price for "above 70,000" looks reasonable.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance BTC/USDT **1-minute candle for 12:00 ET on 2026-04-20** has a final **Close** price higher than **70,000**.
- Polymarket states the governing venue is **Binance BTC/USDT**, not other exchanges or pairs.
- Binance spot API showed BTCUSDT around **74,148.70** during this research run.
- Binance 24-hour ticker showed BTCUSDT around **74,170.62**, down about **1.443%** over 24 hours, with intraday range **73,514 to 75,688**.
- Binance daily klines for the prior several sessions showed closes roughly: **73,043.16**, **70,740.98**, **74,417.99**, **74,131.55**, **74,148.70**.
- ET noon on 2026-04-20 maps to **2026-04-20 16:00:00 UTC**, which matters for any later verification pass.
- Binance API documentation for `/api/v3/klines` confirms 1m kline/candlestick bars are an official market-data endpoint and that timezone interpretation can matter for intervals.

## Evidence directly stated by source

- Polymarket directly states the exact settlement mechanics and source of truth.
- Binance developer docs directly state that `/api/v3/klines` returns candlestick bars identified by open time and supports `1m` interval data.
- Binance market-data endpoints directly provide the live spot price and recent daily trading range.

## What is uncertain

- The public API check attempted for a narrow historical 1m window around an earlier ET noon returned no rows in that specific query shape, so this run does not independently verify the exact historical noon candle formatting via API output.
- The market does not resolve off a daily close or off a non-Binance composite index, so exchange-specific microstructure remains a small but real implementation risk.
- A five-day BTC move large enough to cross back below 70,000 remains plausible even if not base-case.

## Why this source may matter

It establishes both the exact contract rule and the live baseline that the market is pricing against. Because the market is already at 87%, the key question is not whether BTC is generally strong, but whether Binance BTC/USDT is likely to remain above 70,000 at one precise minute on one precise day.

## Possible impact on the question

These sources support the view that the market is pricing a relatively modest requirement: BTC is currently about 4,100+ above the threshold, so Yes wins unless BTC falls roughly 5.5% or more by the exact settlement minute. That makes a high Yes probability plausible, but not so close to certainty that timing/exchange specifics can be ignored.

## Reliability notes

- Polymarket is authoritative for the contract wording but not for the underlying price itself.
- Binance is authoritative for the underlying venue and price surface named in the contract.
- Evidence independence is moderate rather than high because both pieces are part of the same resolution chain.
- The main residual risk is implementation/market-structure ambiguity around the exact 1-minute close, not broad source credibility.