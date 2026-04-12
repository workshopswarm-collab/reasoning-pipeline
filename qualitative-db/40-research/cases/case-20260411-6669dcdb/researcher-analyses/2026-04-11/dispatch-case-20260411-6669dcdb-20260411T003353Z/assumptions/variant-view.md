---
type: assumption_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
research_run_id: d06bec79-0ba7-476e-8ede-4cfa29c129bb
analysis_date: 2026-04-11
persona: variant-view
domain: crypto
subdomain: market-structure
entity: bitcoin
topic: bitcoin-above-72k-on-april-11
question: "Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-11 close above 72000?"
driver: operational-risk
date_created: 2026-04-11
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/variant-view.md"]
tags: ["timing", "resolution", "binance"]
---

# Assumption

The Binance website candle referenced by Polymarket will align in practice with Binance public BTCUSDT 1-minute API data for the 16:00 UTC candle that corresponds to 12:00 ET on 2026-04-11.

## Why this assumption matters

The contract is rule-sensitive: a mismatch between UI display, timezone interpretation, or API-vs-chart data could matter more than broad Bitcoin price direction.

## What this assumption supports

- The conclusion that current price action above 72,000 makes Yes more likely than the market price alone suggests.
- The use of Binance API observations as a valid pre-resolution verification pass.
- The view that residual risk is mostly path risk into noon ET rather than settlement-source ambiguity.

## Evidence or logic behind the assumption

- Polymarket explicitly names Binance BTC/USDT and a 1-minute candle close.
- Binance public endpoints expose the same `BTCUSDT` pair and 1-minute kline structure.
- Noon ET on 2026-04-11 converts cleanly to 16:00 UTC because New York is on EDT at that date.
- In ordinary market-data use, Binance UI candles and API klines are expected to reflect the same underlying market feed.

## What would falsify it

- Evidence that the Binance chart page used for settlement labels candles differently from the API.
- Evidence that Polymarket or UMA has historically interpreted the `12:00 ET` candle differently from the 16:00 UTC minute.
- Evidence of Binance chart revision, outage, or symbol mapping differences that produce a different close.

## Early warning signs

- Disagreement between Binance UI and API for the same minute.
- Public trader confusion about whether the relevant candle is the minute starting at 12:00 ET or ending at 12:00 ET.
- Sudden Binance chart irregularities near the resolution window.

## What changes if this assumption fails

Confidence should drop materially and the variant case that the market may be slightly underpricing Yes would weaken, because rule ambiguity would deserve more weight.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/variant-view.md