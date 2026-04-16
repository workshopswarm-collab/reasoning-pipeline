---
type: source_note
case_key: case-20260415-540d9abf
dispatch_id: dispatch-case-20260415-540d9abf-20260415T234706Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API docs + live SOLUSDT endpoints
source_type: primary_plus_contextual
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-540d9abf/researcher-analyses/2026-04-15/dispatch-case-20260415-540d9abf-20260415T234706Z/personas/risk-manager.md]
tags: [binance, resolution-source, kline, settlement, sol]
---

# Summary

This source note checks the governing settlement surface and confirms that Binance exposes the exact data shape needed to audit the contract: 1-minute SOLUSDT klines with an explicit close price field.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance SOL/USDT 1-minute candle labeled 12:00 ET on 2026-04-19, using the final candle close.
- Binance Spot API docs for `GET /api/v3/klines` state that kline/candlestick bars are available for `interval=1m` and include both open time and close price.
- Binance docs note that `timeZone` can be specified for interval interpretation; startTime/endTime remain interpreted in UTC.
- Live Binance endpoint checks on 2026-04-15 returned current SOLUSDT around 84.93 and recent 1-minute kline closes around 84.85-84.93.
- Since the live spot price is already above 80 by roughly 6% on 2026-04-15, the contract is currently in-the-money for Yes, but the decisive issue is whether SOL remains above 80 at the exact noon ET minute on 2026-04-19.

## Evidence directly stated by source

- Binance docs: `GET /api/v3/klines` returns kline bars, uniquely identified by open time, with close price in the 5th field of the array.
- Binance docs: accepted `timeZone` range is `[-12:00, +14:00]`; if provided, intervals are interpreted in that timezone.
- Live endpoint response example observed in-run: `{"symbol":"SOLUSDT","price":"84.93000000"}`.
- Live 1-minute kline example observed in-run had open time `2026-04-15T23:49:00Z`, close time `2026-04-15T23:49:59.999Z`, open price `84.85000000`, close price `84.93000000`.

## What is uncertain

- Polymarket wording references the Binance website candle at `12:00` ET rather than the API directly, so there is slight implementation ambiguity about whether the UI label maps exactly to the API kline open timestamp in ET. The contract language strongly suggests it does, but it is still worth flagging.
- This check does not prove what the 2026-04-19 noon ET candle will be; it only verifies the source-of-truth mechanics and the current state.
- A 6% buffer above 80 is meaningful but not enormous for SOL over ~3.7 days; crypto weekend volatility could erase it.

## Why this source may matter

This is the governing source-of-truth path for settlement and the key check against contract-mechanics error. It reduces risk of making the wrong call for the wrong reason.

## Possible impact on the question

The source supports a high-but-not-certain Yes lean. It materially undercuts any thesis that the market is unresolved because of missing settlement data access, but it does not eliminate price-path risk between now and the target noon ET candle.

## Reliability notes

- Primary for settlement mechanics: high.
- Primary for current spot/kline state: high.
- Not sufficient alone for final confidence because the market resolves in the future and depends on a specific minute close, not current price.
- Evidence independence is only medium because the Polymarket rule and Binance implementation are tightly linked rather than independent views.