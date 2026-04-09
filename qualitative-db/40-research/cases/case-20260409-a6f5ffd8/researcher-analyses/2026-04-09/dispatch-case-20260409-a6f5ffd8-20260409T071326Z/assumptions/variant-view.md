---
type: assumption_note
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
research_run_id: 91c6e753-6660-4782-abe5-e4e3eb34524b
analysis_date: 2026-04-09
persona: variant-view
domain: crypto
subdomain: bitcoin
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/variant-view.md"]
tags: ["assumption", "timing", "binance", "intraday"]
---

# Assumption

The relevant resolving candle is the Binance BTCUSDT 1-minute bar that opens at 16:00:00 UTC on 2026-04-09, because 12:00 ET on that date is 16:00 UTC under EDT.

## Why this assumption matters

If the ET-to-UTC mapping or Binance bar-label interpretation is wrong, the analysis could reference the wrong minute and misstate settlement mechanics.

## What this assumption supports

- the claim that the market is primarily an intraday price-risk question rather than a rules-ambiguity question
- the estimate that Yes is likely because BTC is already above 71k hours before the relevant 16:00 UTC minute

## Evidence or logic behind the assumption

- New York is on daylight saving time on 2026-04-09, so noon ET is noon EDT = UTC-4.
- Independent local conversion in Python returned 2026-04-09 12:00:00-04:00 = 2026-04-09 16:00:00+00:00.
- Binance kline docs identify bars by open time and expose UTC timestamps directly.

## What would falsify it

- Binance or Polymarket clarification showing that the 12:00 ET candle should be interpreted by close label rather than open label in a way that maps to a different UTC minute
- evidence that the specific UI chart used for settlement applies a different timezone/bar-label convention than the API documentation implies

## Early warning signs

- visible mismatch between Binance web chart candle labels and API open-time timestamps
- Polymarket comments or clarifications flagging a historical issue with noon-ET market resolution timing

## What changes if this assumption fails

The probability estimate would need immediate review because the relevant candle could shift by one minute or more, making the current timing interpretation too confident.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/variant-view.md
