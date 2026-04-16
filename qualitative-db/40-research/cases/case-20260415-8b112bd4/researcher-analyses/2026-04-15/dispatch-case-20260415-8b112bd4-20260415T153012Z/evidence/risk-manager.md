---
type: evidence_map
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
research_run_id: e673a17b-2bcd-4d85-bc78-1f9dfefad023
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-for-2026-04-16-12-00-et-close-above-70000
question: "Will the Binance BTC/USDT 1-minute candle for 2026-04-16 12:00 ET close above 70000?"
driver: operational-risk
date_created: 2026-04-15
agent: risk-manager
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-8b112bd4/researcher-analyses/2026-04-15/dispatch-case-20260415T153012Z/personas/risk-manager.md"]
tags: ["evidence-map", "risk-manager", "timing-risk"]
---

# Summary

The evidence strongly favors Yes because the governing exchange is already pricing BTC/USDT around 73.7k, but the residual risk that matters is narrow and specific: a sufficiently sharp drawdown before the exact noon ET one-minute close on April 16.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-16 close above 70,000?

## Current lean

Lean Yes, high probability but not certainty.

## Prior / starting view

Starting view was that a 98.5% market price may be directionally right but potentially a bit overconfident given one-day crypto volatility and exact-minute settlement mechanics.

## Evidence supporting the claim

- Binance live ticker and recent klines show BTC/USDT around 73.67k on April 15.
  - Source: 2026-04-15-risk-manager-binance-live-price-check.md
  - Why it matters causally: the underlying is already comfortably above the threshold.
  - Direct or indirect: direct.
  - Weight: high.

- Binance 24-hour low in sampled data remains around 73.5k, still above 70k.
  - Source: 2026-04-15-risk-manager-binance-live-price-check.md
  - Why it matters causally: recent realized range has not threatened the strike.
  - Direct or indirect: direct contextual.
  - Weight: medium.

- Polymarket rules are simple and point directly to Binance BTC/USDT 1-minute close at 12:00 ET.
  - Source: 2026-04-15-risk-manager-binance-contract-and-api.md
  - Why it matters causally: lowers contract ambiguity and keeps the thesis focused on price path only.
  - Direct or indirect: direct for resolution mechanics.
  - Weight: high.

## Evidence against the claim

- The cushion is only about 5.2%, which is meaningful but absolutely reachable in one day for BTC.
  - Source: derived from live Binance price versus threshold.
  - Why it matters causally: a moderate crypto drawdown could flip resolution.
  - Direct or indirect: direct arithmetic plus contextual volatility reasoning.
  - Weight: high.

- Resolution depends on one exact minute close, not average trading above 70k across the day.
  - Source: Polymarket rules and Binance kline definition.
  - Why it matters causally: precise timing increases path dependence and tail risk.
  - Direct or indirect: direct.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Binance API and UI are expected to align for settlement, but the contract literally references the UI candles page. This is probably fine, but it is still a mild operational consideration.

## Conflict between inputs

No major factual conflict. The only real tension is between strong current spot support for Yes and the risk-manager's desire to haircut extreme confidence because the event has not settled yet.

## Key assumptions

- BTC avoids a >5% selloff into the settlement minute.
- Binance remains operationally normal around settlement.
- API/UI kline mapping remains effectively aligned for practical resolution reading.

## Key uncertainties

- Short-horizon BTC volatility over the next roughly 24 hours.
- Whether macro or crypto-specific news produces a fast downside move before noon ET.

## Disconfirming signals to watch

- BTC trading under 72k for sustained periods before settlement.
- A sharp broad-market risk-off move in crypto.
- Any Binance-specific outage or data discrepancy around the noon ET window.

## What would increase confidence

- BTC remaining above 72.5k-73k into the morning of April 16.
- Another verification check closer to settlement showing Binance 1-minute candles still well above 70k.

## Net update logic

The evidence moved the starting view from "probably Yes but verify the mechanics" to "Yes is very likely and the mechanics are clean." What prevented moving all the way to market-level confidence is not contradictory evidence; it is residual path risk plus exact-minute settlement sensitivity.

## Suggested downstream use

Use as orchestrator synthesis input and as a compact explanation for why a high-Yes view still deserves a small risk haircut.