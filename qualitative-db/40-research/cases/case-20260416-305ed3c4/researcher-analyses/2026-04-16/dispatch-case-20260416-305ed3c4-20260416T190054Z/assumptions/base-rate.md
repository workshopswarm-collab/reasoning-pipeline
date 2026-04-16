---
type: assumption_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
research_run_id: 70993f7c-d48e-4ede-83aa-fc22b3160c95
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: ethereum
topic: "ETH/USDT noon ET threshold stability"
question: "Will the Binance ETH/USDT 1-minute candle for 12:00 ET on 2026-04-17 close above 2200?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/base-rate.md"]
tags: ["assumption-note", "crypto", "threshold-market"]
---

# Assumption

ETH/USDT will avoid a roughly 6% downside move from current spot into the specific 12:00 ET one-minute Binance close window on 2026-04-17.

## Why this assumption matters

The market is already priced near certainty, so most of the probability mass against Yes comes from the possibility of a sharp downside move or exchange-specific anomaly before the narrow resolution minute.

## What this assumption supports

- A high-90s Yes probability rather than a merely moderate edge.
- The view that the market’s extreme pricing is broadly justified.
- The conclusion that generic outside-view priors should be heavily updated by the present price buffer and short time horizon.

## Evidence or logic behind the assumption

- Current Binance ETHUSDT spot and recent one-minute klines are around 2343-2344, above the threshold by about $144.
- Over the last 24 hours Binance showed an intraday low of 2285.10, still above 2200.
- With less than a day to resolution, the required move is not impossible in crypto but is meaningfully larger than ordinary minute-to-minute noise.

## What would falsify it

- ETHUSDT trades down near or below 2200 before the resolution minute.
- A sudden market-wide crypto shock materially increases intraday volatility.
- Exchange-specific execution, outage, or data-display problems make the settlement candle unreliable or different from API expectations.

## Early warning signs

- Sustained trade below roughly 2260 before the final morning.
- Broad crypto risk-off move with BTC and majors selling off sharply overnight.
- Binance service instability affecting ETHUSDT charting or candle publication.

## What changes if this assumption fails

The probability of Yes would drop sharply, and the market could move from a near-lock framing to a genuinely contested threshold question.

## Notes that depend on this assumption

- Main finding: `qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/base-rate.md`