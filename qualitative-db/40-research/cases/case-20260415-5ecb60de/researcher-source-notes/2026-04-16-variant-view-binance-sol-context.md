---
type: source_note
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: spot-price
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API + Polymarket rules page
source_type: primary-plus-contract
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=10
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/variant-view.md]
tags: [binance, polymarket, source-note, settlement, sol]
---

# Summary

This note captures the direct settlement surface and a compact Binance price-context check relevant to the April 19 SOL > 80 market.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance SOL/USDT 1-minute candle for **12:00 ET** on April 19, using the final **Close** price.
- Binance spot API reports `exchangeInfo.timezone = UTC`, so ET noon must be translated carefully when querying machine-readable Binance endpoints.
- Binance `exchangeInfo` for `SOLUSDT` shows `PRICE_FILTER.tickSize = 0.01000000`, implying 2-decimal price precision for the spot pair.
- Recent Binance daily closes before the assignment were approximately:
  - Apr 6: 82.57
  - Apr 7: 83.33
  - Apr 8: 84.83
  - Apr 9: 84.93
  - Apr 10: 81.53
  - Apr 11: 86.51
  - Apr 12: 83.72
  - Apr 13: 84.90
- Recent 1-minute data around the assignment time showed SOL/USDT trading around 84.8-85.4, comfortably above 80.

## Evidence directly stated by source

- Binance 1m and 1d kline endpoints directly provide OHLCV candles for SOL/USDT.
- Binance exchange metadata directly states UTC timezone and the symbol trading rules.
- Polymarket directly states the governing source of truth and the exact qualifying candle.

## What is uncertain

- This source set does not determine the April 19 noon ET candle yet; it only frames current distance from the 80 threshold.
- Short-horizon crypto volatility could still move SOL materially before settlement.
- Polymarket webpage extraction can duplicate sections, so contract wording should be read carefully but not over-interpreted from duplicated markup.

## Why this source may matter

The market is rule-sensitive and date-specific. The decisive issue is not generic SOL price direction but whether the exact Binance candle, in the correct timezone mapping, closes above 80 with Binance’s price precision.

## Possible impact on the question

These sources support a high but not near-certain Yes view: spot context is currently several dollars above 80, but the exact contract still requires the April 19 12:00 ET one-minute close to remain above the line.

## Reliability notes

- Binance API is the strongest machine-readable direct source for current and historical SOL/USDT candles and symbol precision.
- Polymarket’s own rules page is the authoritative contract-definition surface.
- Independence is only moderate because contract mechanics and price context ultimately both rely on Binance as the source of truth.