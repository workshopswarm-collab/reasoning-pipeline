---
type: source_note
case_key: case-20260416-bac9c8f2
dispatch_id: dispatch-case-20260416-bac9c8f2-20260416T033803Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-bac9c8f2 | base-rate
question: Will the Binance BTC/USDT 1-minute candle closing at 12:00 PM ET on 2026-04-17 close above 74000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules page plus Binance BTCUSDT 1m kline API spot checks
source_type: primary_and_authoritative_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-bac9c8f2/researcher-analyses/2026-04-16/dispatch-case-20260416-bac9c8f2-20260416T033803Z/personas/base-rate.md]
tags: [polymarket, binance, resolution, timing, btc]
---

# Summary

This note captures the contract mechanics from Polymarket and a direct spot-check of Binance 1-minute BTCUSDT klines relevant to the market's noon-ET settlement condition.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 17 has a final Close above 74,000.
- The market is specifically about Binance BTC/USDT, not another exchange or pair.
- Price precision is determined by Binance's quoted decimal precision.
- ET noon on 2026-04-17 converts to 2026-04-17 16:00:00 UTC.
- Binance public 1-minute klines show the latest available close near research time at 2026-04-16 03:39 UTC was 74,996.64.
- Binance kline history shows the noon-ET close on 2026-04-15 was 73,792.01, below 74,000.
- Over the last 24 hours available before research time, 74.7% of 1-minute closes were above 74,000; over the last 48 hours, 86.6% were above 74,000.
- Over the last 8 available daily noon-ET observations, only 1 of 8 closes was above 74,000 (12.5%), though this is a very small sample and includes earlier lower-price days.

## Evidence directly stated by source

Directly from Polymarket:
- resolution is tied to the Binance BTC/USDT 1-minute candle at 12:00 PM ET on the specified date
- the deciding field is the final Close price
- the threshold is strict: higher than 74,000

Directly from Binance kline data:
- recent spot level around research time was roughly 75,000
- an exact prior analog minute (2026-04-15 12:00 ET) closed below 74,000

## What is uncertain

- Binance API data fetched here does not yet include the target 2026-04-17 16:00 UTC candle because the market has not resolved.
- The short-term path over roughly the next 36 hours could still move BTC below 74,000 by the target minute.
- Small historical noon-only sample is noisy and may understate the current regime if BTC has recently shifted upward.

## Why this source may matter

This is the key provenance pair for the case: Polymarket defines what counts, and Binance is the governing price source. Together they pin down timing, timezone, pair, and comparison field.

## Possible impact on the question

The contract mechanics are clear enough that the main forecasting task is not legal interpretation but whether BTC can remain above 74,000 specifically at noon ET on April 17. Current spot and recent minute-level distribution support a Yes lean, but the nearest prior daily noon analog closed slightly below threshold, which is the most relevant simple base-rate caution.

## Reliability notes

- Polymarket is the direct rule surface for the contract, so credibility for settlement interpretation is high.
- Binance is the stated source of truth for the deciding price, so credibility for the relevant price field is high.
- Evidence independence is only medium because both data points are tightly tied to the same market structure rather than independent explanatory sources.
- There remains mild operational ambiguity around whether UI and API views perfectly align, but the contract language strongly suggests the Binance 1-minute close is the decisive object.