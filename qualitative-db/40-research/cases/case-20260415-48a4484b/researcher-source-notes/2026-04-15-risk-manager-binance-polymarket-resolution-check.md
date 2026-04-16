---
type: source_note
case_key: case-20260415-48a4484b
dispatch_id: dispatch-case-20260415-48a4484b-20260415T180644Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-48a4484b | risk-manager
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API + Polymarket market rules
source_type: primary_market_and_resolution_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, resolution-check, timing]
---

# Summary

This source note captures the governing market rules from Polymarket and a direct spot/tick-level verification from Binance, which is the market’s stated source of truth.

## Key facts extracted

- Polymarket rules say the market resolves to Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET on 2026-04-16** has a final **Close** price **higher than 72,000**.
- The source of truth is specifically Binance BTC/USDT, not other exchanges or pairs.
- As checked on 2026-04-15 around 18:11 UTC, Binance spot API returned BTCUSDT around **74,232.08**.
- Recent 1-minute klines fetched from Binance were all in the **74.2k** area, indicating contemporaneous trading materially above 72k.
- Because the contract resolves on the **12:00 ET one-minute close**, spot level now is informative but not dispositive; a sharp selloff before noon ET on Apr 16 would still flip the outcome.

## Evidence directly stated by source

- Polymarket directly states the exact resolution mechanics and exchange/pair dependence.
- Binance API directly states current BTCUSDT price and recent 1-minute candle closes.

## What is uncertain

- Binance web UI and API can differ in presentation, though the contract points to the Binance BTC/USDT candle series and the API should closely reflect that underlying market data.
- Current price does not guarantee the specific noon ET close on Apr 16.
- The remaining risk is path/timing risk rather than contract-interpretation risk after this check.

## Why this source may matter

This is the primary evidence because it establishes both the exact condition that must be satisfied and the current distance from the threshold.

## Possible impact on the question

The direct data strongly supports a Yes lean because BTC is currently more than $2,000 above the threshold, but it also highlights the core failure mode: a sufficiently large drawdown before the specific noon ET candle close would invalidate a simple spot-based thesis.

## Reliability notes

- Polymarket market page is the governing contract surface for resolution wording.
- Binance is explicitly named as the resolution source, making it the highest-authority price source for the contract.
- This source class is highly relevant and close to authoritative for settlement, but it does not remove forward price uncertainty.