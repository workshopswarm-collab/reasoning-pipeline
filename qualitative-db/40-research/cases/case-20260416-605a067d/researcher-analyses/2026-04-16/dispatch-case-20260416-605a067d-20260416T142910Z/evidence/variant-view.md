---
type: evidence_map
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
research_run_id: c6ed34d1-4a34-4db6-a398-47e7b8116f25
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: threshold-close-markets
entity: ethereum
topic: "ETH above 2200 on April 17 noon ET close"
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle on April 17 close above 2200?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["resolution-timing-risk"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-variant-view-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-variant-view-binance-live-price-and-candles.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/variant-view.md"]
tags: ["evidence-map", "ethereum", "binance", "threshold-market"]
---

# Summary

The evidence strongly favors Yes because ETH is already trading materially above 2200 on Binance, but the main neglected mechanism is that this contract is about one specific minute close tomorrow rather than any intraday touch or current spot state.

## Question being evaluated

Will the Binance ETH/USDT 12:00 ET 1-minute candle on April 17 close above 2200?

## Current lean

Lean Yes, but slightly less aggressively than the market.

## Prior / starting view

Starting view was that a low-90s market likely had the basic direction right because spot ETH was already above the line.

## Evidence supporting the claim

- Binance ticker and recent klines show ETH around 2297.6, about 4.4% above the threshold. Direct, high weight.
- Recent 1-hour context shows highs up to 2385.61 in the last 48 hours, suggesting the market is not merely hovering at the line. Direct/contextual, medium-high weight.
- Polymarket rule page confirms the market is specifically about Binance ETH/USDT and not a cross-venue interpretation issue. Direct contract evidence, high weight.

## Evidence against the claim

- Settlement is a single specific 12:00 ET 1-minute close on April 17, so a one-day downside move can still flip the answer even while current spot is above the line. Direct contract interpretation, high weight.
- Observed Binance context range over the last 48 hours spans down to 2285.10; while still above 2200, it shows meaningful realized volatility rather than a stable locked-in regime. Direct/contextual, medium weight.
- No governing-source proof for the actual April 17 noon candle exists yet; the event has not yet occurred, so current confidence is probabilistic rather than near-settled. Direct timing fact, medium weight.

## Ambiguous or mixed evidence

- Market price around 91% may reflect good calibration rather than overconfidence; the disagreement is modest.
- Limited contextual source diversity here means the variant case rests more on contract mechanics and volatility framing than on a separate external catalyst.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much discount should be applied for one more day of downside and for a single-minute-close settlement rule.

## Key assumptions

- Current above-threshold status is strong but not decisive because settlement is time-specific.
- A 4-5% drop before noon ET tomorrow remains plausible enough to matter.

## Key uncertainties

- Overnight macro or crypto-specific volatility before the settlement minute.
- Whether ETH holds comfortably above 2200 into the final hours before settlement.

## Disconfirming signals to watch

- Sustained price action back below 2250 before April 17 morning ET.
- A visible increase in downside volatility into the settlement window.

## What would increase confidence

- Additional late-stage verification on April 17 morning showing Binance ETH/USDT still comfortably above 2200.
- Continued hourly closes above 2300.

## Net update logic

The direct Binance evidence keeps the lean clearly on Yes, but the contract-specific timing rule prevents treating the question as already resolved. The variant edge is not a hard bearish thesis on ETH; it is a narrower claim that the market may underweight how much one future minute still matters in a short-dated crypto contract.

## Suggested downstream use

Use as synthesis input for modest caution against simply inheriting the low-90s market price without a timing-specific discount.