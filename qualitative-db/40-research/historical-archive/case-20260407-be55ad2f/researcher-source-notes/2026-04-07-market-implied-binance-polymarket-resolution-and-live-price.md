---
type: source_note
case_key: case-20260407-be55ad2f
dispatch_id: dispatch-case-20260407-be55ad2f-20260407T193635Z
analysis_date: 2026-04-07
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260407-be55ad2f | market-implied
question: Will the price of Bitcoin be above $66,000 on April 8?
driver: operational-risk
date_created: 2026-04-07T15:39:00-04:00
source_name: Binance API and Polymarket market rules
source_type: primary_plus_resolution_context
source_url: https://api.binance.com/api/v3/exchangeInfo?symbol=BTCUSDT
source_date: 2026-04-07
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
downstream_uses: [qualitative-db/40-research/cases/case-20260407-be55ad2f/researcher-analyses/2026-04-07/dispatch-case-20260407-be55ad2f-20260407T193635Z/personas/market-implied.md]
tags: [binance, polymarket, resolution, btcusdt, source-of-truth]
---

# Summary

This source note captures the governing settlement mechanics from Polymarket and the direct Binance API checks used to validate timezone, 1-minute candle semantics, live BTC/USDT level, and practical API-rate-limit considerations.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle for **12:00 ET (noon)** on April 8, using the candle's final **Close** price.
- Polymarket specifies Binance's BTC/USDT chart with **"1m"** and **"Candles"** selected as the resolution source.
- Binance `exchangeInfo` for BTCUSDT returns `"timezone":"UTC"`, confirming Binance exchange timestamps are UTC-based rather than ET-based.
- Binance `klines` output shows each 1-minute candle is defined by UTC timestamps with explicit open and close times; converting recent rows to America/New_York maps cleanly to minute boundaries.
- Recent direct check: Binance `ticker/price` showed BTCUSDT around **68493.14**, materially above the 66,000 threshold.
- Recent direct check: Binance `ticker/24hr` showed lastPrice around **68481.83**, 24h change about **-1.93%**, daily high **69974.08**, daily low **67732.01**.
- Binance `exchangeInfo` exposes rate-limit metadata including request-weight limit **6000 per minute**, so low-frequency manual verification is straightforward and rate-limit risk is low for this run.

## Evidence directly stated by source

From Polymarket page:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Price precision is determined by the number of decimal places in the source."

From Binance API:
- `exchangeInfo` directly states exchange `timezone` is `UTC`.
- `klines` directly provide open time, close time, OHLCV, and final close value for each minute bar.
- `ticker/price` and `ticker/24hr` directly provide current BTCUSDT level and recent range context.

## What is uncertain

- The direct settlement value will not be known until the April 8 12:00 ET minute is complete.
- Polymarket wording references the Binance website chart rather than the public API endpoint explicitly, though the API and chart are very likely aligned because both are Binance BTC/USDT 1-minute candle data.
- Intraday crypto volatility remains capable of moving BTC by several percent before noon ET tomorrow.

## Why this source may matter

This is the core provenance surface for the case. It establishes both the exact settlement rule and the live underlying price relative to the threshold. It also resolves the case-specific mechanics checks: exchange timezone, candle definition, close field usage, and practical rate-limit handling.

## Possible impact on the question

The current BTCUSDT level being roughly 2.5k above the threshold supports a high-probability Yes view, but not certainty, because a ~3.6% downside move by noon ET would still flip the outcome. The UTC-based Binance timestamping means the researcher must translate the target minute correctly to **2026-04-08 16:00:00 UTC = 12:00:00 ET** before final manual settlement verification.

## Reliability notes

- Polymarket rules are the governing contract surface for what counts.
- Binance is the direct source-of-truth surface named in the contract.
- Evidence independence is limited because both core facts route through the same venue pair (Polymarket contract -> Binance source), but that is appropriate here because the market is explicitly source-bound.
- API-rate-limit risk for this run was low because only a handful of direct calls were needed.