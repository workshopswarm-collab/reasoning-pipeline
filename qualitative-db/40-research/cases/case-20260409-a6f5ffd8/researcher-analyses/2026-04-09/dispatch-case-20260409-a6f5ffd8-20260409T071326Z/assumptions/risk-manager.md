---
type: assumption_note
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
research_run_id: 9ba8ba95-6b51-4d65-8da4-7c7ec7601023
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-9
question: "Will the price of Bitcoin be above $70,000 on April 9?"
driver: operational-risk
date_created: 2026-04-09
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/risk-manager.md"]
tags: ["assumption", "timestamp", "settlement", "binance", "noon-et"]
---

# Assumption

The contract will be interpreted using the Binance 1-minute BTCUSDT candle whose **open time is 12:00:00 ET (16:00:00 UTC)**, and the decisive value will be that candle’s final close price.

## Why this assumption matters

This case is unusually sensitive to timestamp interpretation. If the relevant candle were instead interpreted as the minute ending at noon ET rather than the minute beginning at noon ET, the settlement reference could shift by one minute and potentially change the result.

## What this assumption supports

- The directional probability estimate for Yes.
- The view that current spot trading above 70k several hours earlier is supportive but not dispositive.
- The conclusion that remaining risk is mostly path/timing risk rather than broad directional Bitcoin risk.

## Evidence or logic behind the assumption

- Polymarket explicitly says the resolution source is Binance BTC/USDT with 1m candles selected.
- Binance API docs say klines are uniquely identified by their **open time**.
- Noon ET on 2026-04-09 converts to 16:00 UTC, so the natural canonical candle identifier is open time 1775750400000.
- This interpretation matches standard exchange-kline semantics better than a close-time interpretation.

## What would falsify it

- A Polymarket clarification, moderator note, or historical settlement practice indicating they use the minute whose close occurs at 12:00 ET rather than the candle labeled 12:00 ET.
- Binance UI behavior showing a materially different candle labeling convention for the human-facing chart than the API docs imply.

## Early warning signs

- Public comments or disputes focusing on “which exact minute” rather than on price level.
- Inconsistent labeling between Binance UI, API, and Polymarket moderator explanations.

## What changes if this assumption fails

The probability estimate should be revised downward or at least widened, because the apparent edge from BTC trading above 70k earlier in the day would no longer map as cleanly onto the exact settlement minute.

## Notes that depend on this assumption

- Main risk-manager finding for this run.
- Binance rule-mechanics source note for this run.