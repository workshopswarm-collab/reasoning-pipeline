---
type: assumption_note
case_key: case-20260413-2d3a41aa
research_run_id: 188bb629-19bf-4aa1-bb8c-69e64b1d1a67
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-13
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-13 close above 70000?
driver: operational-risk
date_created: 2026-04-13
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: [btc]
related_drivers: [operational-risk, reliability]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/risk-manager.md]
tags: [assumption, timing-risk, bitcoin]
---

# Assumption

BTC/USDT will remain above 70,000 through the specific Binance 12:00 ET 1-minute closing print rather than only trading above 70,000 earlier in the day.

## Why this assumption matters

The market resolves on one exact minute close, so a bullish intraday trend is only relevant if it persists through that timestamp.

## What this assumption supports

- A high Yes probability.
- A view that the pre-noon cushion above 70,000 is likely sufficient.
- A conclusion that market confidence is broadly justified but still somewhat overconfident.

## Evidence or logic behind the assumption

- Binance spot data about 2h10m before resolution showed BTC/USDT in the 70,964-71,609 area, providing a roughly 1.4k+ cushion over the strike.
- When spot is materially above a threshold shortly before a single-minute close market, the threshold usually holds absent a sharp intraday reversal.

## What would falsify it

- A fast selloff that takes the Binance BTC/USDT 12:00 ET candle close to 70,000 or lower.
- Exchange-specific divergence on Binance versus other venues.

## Early warning signs

- Loss of the price cushion during late morning ET.
- Rising intraday realized volatility.
- Abrupt crypto risk-off move or exchange-specific dislocation.

## What changes if this assumption fails

The market resolves No even if BTC spent most of the morning above 70,000, demonstrating that path and timestamp risk were underweighted.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/risk-manager.md
- qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/evidence/risk-manager.md