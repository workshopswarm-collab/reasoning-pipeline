---
type: assumption_note
case_key: case-20260415-9a9c8ea3
research_run_id: fada9ee9-6541-4db6-8c5c-03ee00e94d25
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-16
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-16 be above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "settlement-surface", "binance", "date-sensitive"]
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
---

# Assumption

The Binance website 1-minute candle used for market settlement will match the economic content of Binance's public BTCUSDT spot API data closely enough that the API is a valid verification proxy for the contract.

## Why this assumption matters

The analysis relies on Binance API pulls to verify the relevant market level and recent one-minute closes, while the contract wording points specifically to the Binance trading interface candle display.

## What this assumption supports

- The conclusion that BTC is currently comfortably above 72k on the governing venue.
- The estimate that only a moderate but still nontrivial drawdown before noon ET would flip the market to `No`.
- Confidence that source-of-truth ambiguity is low rather than medium/high.

## Evidence or logic behind the assumption

Binance's public ticker and kline endpoints are standard direct venue data surfaces for the same BTCUSDT market named in the contract. In ordinary conditions, the UI candle display and the API reflect the same underlying matching-engine data.

## What would falsify it

Evidence that the Binance UI candle shown for the 12:00 ET minute materially differs from the API kline close used here, or that the contract interprets timezone/candle labeling differently from the API timestamps.

## Early warning signs

- Binance UI displays a different 1-minute close than API data for the same minute.
- Polymarket clarifies a specific UI-only interpretation that is not API-equivalent.
- Binance changes front-end chart sourcing or timezone labeling.

## What changes if this assumption fails

Confidence should drop, and direct UI verification at or near settlement would become mandatory. The market direction may still be the same, but provenance quality would weaken materially.

## Notes that depend on this assumption

- Main persona finding for base-rate on this case.
- Binance source note dated 2026-04-15 for this case.