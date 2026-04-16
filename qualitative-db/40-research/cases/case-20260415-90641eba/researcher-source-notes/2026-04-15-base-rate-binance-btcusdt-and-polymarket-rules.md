---
type: source_note
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: BTC/USDT level relative to 70000 and contract settlement mechanics
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 be above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API ticker/klines plus Polymarket event rules page
source_type: primary_and_contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/base-rate.md]
tags: [source-note, crypto, bitcoin, binance, polymarket]
---

# Summary

This note captures the governing resolution mechanics from the Polymarket market page and a direct Binance price check relevant to the outside-view estimate.

## Key facts extracted

- Polymarket states this market resolves Yes if the **Binance BTC/USDT 1-minute candle at 12:00 ET on April 20, 2026** has a final **Close** price **higher than 70,000**.
- The market is specifically about **Binance BTC/USDT**, not other exchanges or pairs.
- Binance API ticker check on 2026-04-15 returned **BTCUSDT = 73974.00000000**.
- Binance daily kline data for recent days showed closes mostly in the high-60k to mid-70k range, with recent closes including:
  - 2026-04-13 UTC close: **74417.99**
  - 2026-04-14 UTC close: **74131.55**
  - 2026-04-15 partial/current day API snapshot price: **73974.00**
- The Polymarket page showed the 70,000 line trading around **88-89%** at fetch time, consistent with assignment current_price 0.87.

## Evidence directly stated by source

- Polymarket directly states the contract mechanics, governing source, pair, timeframe, and close-based condition.
- Binance directly states current BTCUSDT price via the exchange API and recent daily candles via klines.

## What is uncertain

- The Binance web UI fetch did not render usable candle content in web_fetch, so direct proof of the exact eventual April 20 12:00 ET 1-minute candle is not yet available and cannot be observed because the event is still in the future.
- Recent daily closes are contextual, not direct evidence for the exact noon-ET 1-minute close on April 20.
- Crypto volatility over five days could still move BTC materially below or above 70,000 by settlement.

## Why this source may matter

- It identifies the governing source of truth explicitly.
- It verifies that BTC is currently several thousand dollars above the threshold, which is the main fact supporting a high but not near-certain outside-view probability.
- It reduces ambiguity about whether this is a touch/high market or a close-at-a-specific-minute market.

## Possible impact on the question

- Because the contract is a **single-minute close-above** market rather than a touch market, the base rate should be somewhat lower than analogous touch-style contracts when the asset is merely above the threshold.
- Current Binance spot materially above 70,000 supports Yes, but five days remain, so the outside view still needs to price in ordinary crypto drawdown risk and exact-minute closing risk.

## Reliability notes

- Polymarket market rules are high-value but still contextual until final settlement because market pages can be incomplete or rendered dynamically; here the key rules text was visible in fetch output.
- Binance API is the strongest direct contextual price source available in-run and is tightly aligned with the contract’s stated governing venue.
- Evidence independence is limited because both the contract and contextual price evidence center on Binance, but that is appropriate given Binance is the stated source of truth.