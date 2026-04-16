---
type: assumption_note
case_key: case-20260416-f29db686
research_run_id: 98495dac-9c0c-499a-8239-ecb00277f89b
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: short-term
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/risk-manager.md"]
tags: ["assumption-note", "btc", "timing-risk"]
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
---

# Assumption

A spot cushion of roughly 1.0% above the strike about 15 hours before settlement is helpful but not robust enough to dominate the contract's single-minute timing risk.

## Why this assumption matters

The risk-manager view depends on treating this as a narrow time-window contract rather than a broad directional daily close. If the current cushion is judged too weak relative to normal BTC intraday volatility, then confidence should be capped even if spot is presently above 74,000.

## What this assumption supports

- A modest Yes lean rather than a high-confidence Yes.
- A view slightly below or roughly in line with market rather than much higher.
- Emphasis on path risk and noon-ET minute-close fragility.

## Evidence or logic behind the assumption

- Binance spot during this run was around 74,771, only about 771 points above the strike.
- BTC can plausibly move more than 1% over a 15-hour horizon, especially around US trading hours.
- The contract resolves on one exact Binance one-minute close, so temporary weakness at the wrong minute is enough for No even if broader trend remains constructive.

## What would falsify it

- Evidence that BTC volatility regime is unusually compressed and noon-ET downside excursions below 74,000 are materially less likely than normal.
- A materially larger cushion before settlement, such as sustained trading well above 75,500 to 76,000.
- A sharp contraction in realized volatility into settlement.

## Early warning signs

- Failure to hold above 74,500 overnight.
- Rapid rejection from local highs with heavier downside momentum into US hours.
- Exchange-specific dislocations or unusual Binance weakness versus broader market.

## What changes if this assumption fails

If the cushion proves more durable than assumed, the fair probability should move upward toward the upper-60s or low-70s. If the cushion proves less durable, the contract becomes closer to a coin flip or worse despite current spot being above strike.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/risk-manager.md