---
type: source_note
case_key: case-20260413-e2ee488e
dispatch_id: dispatch-case-20260413-e2ee488e-20260413T222544Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-15 be above 70000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance BTCUSDT API and Polymarket market rules page
source_type: primary_and_resolution
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000 ; https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-e2ee488e/researcher-analyses/2026-04-13/dispatch-case-20260413-e2ee488e-20260413T222544Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, resolution-source, price-threshold, timing]
---

# Summary

This note captures the governing contract mechanics and the live BTC/USDT reference level used for the catalyst-hunter view.

## Key facts extracted

- Polymarket states this market resolves to Yes if the **Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 15, 2026** has a final **Close** price higher than 70,000.
- Polymarket explicitly says the source is the Binance BTC/USDT chart with **1m** and **Candles** selected.
- The contract is specifically about **Binance BTC/USDT**, not other exchanges or pairs.
- Direct Binance API checks on 2026-04-13 showed spot BTCUSDT around **74.1k** and the recent sampled 1-minute history stayed above 70k throughout the returned window.
- In a 1000-minute Binance 1m sample pulled on 2026-04-13, the minimum sampled low was about **70,566.99** and minimum sampled close was about **70,579.00**.

## Evidence directly stated by source

- From Polymarket rules: the decisive condition is the final **Close** of the **12:00 ET** one-minute candle on the named date.
- From Binance API: current BTCUSDT spot was approximately **74,126-74,144** during the checks on 2026-04-13, well above the 70,000 threshold.

## What is uncertain

- The direct Binance API checks establish current level and recent buffer, but they do not settle the future April 15 12:00 ET close.
- The returned kline sample was limited to the most recent 1000 one-minute bars, so it is a short-horizon verification pass rather than a full multiday distribution.
- Binance UI wording can differ from API conventions, so the exact displayed candle label on the web chart should still be understood as the contract’s governing source-of-truth surface.

## Why this source may matter

This is the core source set for both the settlement mechanics and the current buffer relative to the threshold. For a narrow date-and-price market, that is the most important evidence layer.

## Possible impact on the question

Because the contract only cares about one specific Binance 1-minute close at noon ET on April 15, current BTC trading around 74.1k creates a buffer of roughly 4.1k over the threshold. That makes the market highly likely to resolve Yes unless a large downside move occurs before the target minute.

## Reliability notes

- Polymarket rules page is the direct contract wording but remains secondary to the eventual Binance price print it references.
- Binance exchange/API data is the authoritative source-of-truth family for the underlying price condition.
- Independence is limited because both the live reference price and eventual settlement source come from Binance, but that is appropriate here because the contract is explicitly exchange-specific.