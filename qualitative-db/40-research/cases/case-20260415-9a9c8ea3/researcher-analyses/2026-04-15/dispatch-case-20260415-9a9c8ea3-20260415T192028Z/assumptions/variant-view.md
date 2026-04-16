---
type: assumption_note
case_key: case-20260415-9a9c8ea3
research_run_id: 05123748-97c6-42ed-b68c-d970fe8417f0
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-16
question: "Will the price of Bitcoin be above $72,000 on April 16?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "settlement", "btc", "binance"]
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
---

# Assumption

The contract's practical meaning is that the relevant observation is the Binance BTC/USDT 1-minute candle that opens at 12:00:00 ET on April 16 and whose final close is recorded at the end of that minute.

## Why this assumption matters

The contract is highly date- and minute-specific, so a mistaken interpretation of which candle counts would directly break the forecast.

## What this assumption supports

- Treating current spot distance above $72,000 as relevant but not dispositive
- Framing the main residual risk as an overnight/intraday selloff before the noon ET settlement minute
- Assigning only a modest discount versus the market despite seeking a variant view

## Evidence or logic behind the assumption

- Polymarket explicitly says the relevant object is the Binance `1 minute candle for BTC/USDT 12:00 in the ET timezone (noon)` with the final `Close` price.
- Binance 1m kline API data shows each minute candle is naturally represented by a minute-open timestamp and a final close timestamp at the end of that minute.
- That makes the most natural operational reading the minute beginning at 12:00 ET.

## What would falsify it

- A clearer Polymarket clarification saying the relevant candle is instead the one ending at 12:00:00 ET rather than the one beginning at 12:00 ET
- Evidence that Binance's web chart labels minutes in a way that differs from the API interpretation

## Early warning signs

- Conflicting exchange/chart labeling around noon ET
- Resolution disputes in similar Polymarket daily BTC minute-close markets

## What changes if this assumption fails

The forecast should be recomputed around the correct minute definition, and confidence in any near-threshold interpretation would fall.

## Notes that depend on this assumption

- Main finding: `qualitative-db/40-research/cases/case-20260415-9a9c8ea3/researcher-analyses/2026-04-15/dispatch-case-20260415-9a9c8ea3-20260415T192028Z/personas/variant-view.md`
- Source note: `qualitative-db/40-research/cases/case-20260415-9a9c8ea3/researcher-source-notes/2026-04-15-variant-view-binance-polymarket-resolution-check.md`