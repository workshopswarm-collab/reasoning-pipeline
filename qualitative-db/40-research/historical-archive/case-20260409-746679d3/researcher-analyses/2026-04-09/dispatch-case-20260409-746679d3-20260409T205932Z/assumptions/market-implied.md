---
type: assumption_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: b29230d1-9199-41b0-bfbe-3521de8f43e7
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: spot-market-structure
entity:
topic: noon-et-binance-candle-interpretation
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: reliability
date_created: 2026-04-09
agent: market-implied
status: active
certainty: medium
importance: high
time_horizon: one-day
related_entities: []
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/market-implied.md"]
tags: ["assumption", "binance", "timezone", "candle-definition"]
---

# Assumption

The contract’s “Binance 1 minute candle for ETH/USDT 12:00 in the ET timezone” is best interpreted as the 1-minute bar whose open time is 12:00:00 ET on Apr 10, 2026, which corresponds to 16:00:00 UTC.

## Why this assumption matters

The market resolves on a single minute close, so an off-by-one-minute interpretation would directly change what print counts.

## What this assumption supports

- The conclusion that the relevant settlement bar is the bar opened at 16:00:00 UTC.
- The view that the market is mostly pricing spot level distance from 2100 rather than broader intraday path dependence.

## Evidence or logic behind the assumption

- Binance documentation says klines are uniquely identified by open time.
- Binance docs separate open time and close time explicitly in the kline response.
- Noon ET on Apr 10, 2026 converts to 16:00 UTC because New York is on daylight saving time.
- A future query at that exact UTC open returned no candle yet, which is consistent with the intended mapping.

## What would falsify it

- Polymarket clarification or historical precedent showing that these contracts interpret “12:00” as the candle closing at 12:00:59 ET rather than the candle opening at 12:00:00 ET.
- Binance UI behavior that labels candles by close time rather than open time in a way Polymarket uses for settlement.

## Early warning signs

- Ambiguous settlement discussions from Polymarket moderators or comments.
- A mismatch between Binance UI labels and API candle indexing around the target minute.

## What changes if this assumption fails

The directional probability might shift a few points because the wrong minute could be used, especially if ETH is trading near the threshold during the target window.

## Notes that depend on this assumption

- Main finding for market-implied persona.
- Binance contract/timing source note.
- Evidence map for this run.