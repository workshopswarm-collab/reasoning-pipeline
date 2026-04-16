---
type: evidence_map
case_key: case-20260415-58166133
dispatch_id: dispatch-case-20260415-58166133-20260415T083617Z
research_run_id: 2560ec1b-1222-4587-9b33-c3904b0c7add
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: exchange-market-data
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-16
question: "Will the price of Bitcoin be above $72,000 on April 16?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance-btcusdt-1m-candle"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-58166133/researcher-analyses/2026-04-15/dispatch-case-20260415-58166133-20260415T083617Z/personas/risk-manager.md"]
tags: ["evidence-map", "crypto", "timing-risk", "settlement-risk"]
---

# Summary

The evidence nets to a Yes lean because current Binance BTCUSDT is above the strike by about 2.9%, but the main risk-manager adjustment is against overconfidence: the contract resolves on one exchange, one pair, one exact minute, and a sub-3% move over 31 hours is not a tail event in crypto.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for Apr 16, 2026 at 12:00 ET have a final close above 72,000?

## Current lean

Lean Yes, but with less confidence than the market price suggests.

## Prior / starting view

Starting view from market pricing was that Yes was likely, roughly mid-80s implied.

## Evidence supporting the claim

- Binance spot check showed BTCUSDT around 74,122.67.
  - source: 2026-04-15-risk-manager-binance-spot-and-kline-check.md
  - causal relevance: contract currently sits in-the-money on the named venue and pair
  - directness: direct venue evidence
  - weight: high
- Recent 1-minute and 1-hour Binance candles remained above 72,000.
  - source: same Binance source note
  - causal relevance: shows threshold buffer persists across recent intervals, not just a single stale quote
  - directness: direct venue evidence
  - weight: medium-high
- Recent daily Binance closes were above 72,000.
  - source: same Binance source note
  - causal relevance: supports that price regime is currently above strike
  - directness: direct venue evidence
  - weight: medium

## Evidence against the claim

- The cushion above strike is only about 2.9%.
  - source: derived from Binance spot check versus threshold
  - causal relevance: a modest crypto drawdown can erase it before settlement
  - directness: direct arithmetic on primary source
  - weight: high
- Resolution is tied to one exact 1-minute close at noon ET on Binance.
  - source: 2026-04-15-risk-manager-polymarket-rules-and-pricing.md
  - causal relevance: creates timing and venue-specific fragility that broader BTC strength does not eliminate
  - directness: direct contract evidence
  - weight: high
- This is not directly settled yet; roughly 31 hours remain.
  - source: runtime timing check and contract time mapping
  - causal relevance: leaves room for ordinary short-horizon volatility
  - directness: direct timing calculation
  - weight: medium-high

## Ambiguous or mixed evidence

- Polymarket pricing near 84-85% may be incorporating typical BTC volatility well enough, but it could also reflect complacency because spot is currently above the threshold.
- Binance API data is a strong primary source for current state, but the final contract references the candle display surface and future minute close, so operational mapping is still a minor but real concern.

## Conflict between inputs

There is no major factual conflict. The main issue is weighting: whether a roughly 2.9% buffer with 31 hours to go deserves mid-80s confidence or something closer to high-70s / low-80s confidence.

## Key assumptions

- Current Binance price regime remains broadly intact into settlement.
- No exchange-specific anomaly disrupts the relevant candle interpretation.
- A sub-3% downside move before noon ET is less likely than the market resolving above strike.

## Key uncertainties

- Near-term BTC volatility over the next 31 hours.
- Whether any macro or crypto-specific catalyst hits before settlement.
- Whether the exact noon ET minute prints below strike despite a broader day-above-threshold path.

## Disconfirming signals to watch

- BTCUSDT trading into low 72k or sub-72k territory on Binance before Apr 16 noon ET.
- Repeated lower highs / lower lows during the final hours.
- Any Binance display or data integrity issue affecting the settlement candle.

## What would increase confidence

- Continued Binance trading above roughly 73.5k into the final hours.
- Another verification pass closer to settlement showing sustained cushion.
- Evidence of low realized volatility into the noon ET window.

## Net update logic

The evidence preserves a Yes lean because current direct venue data is clearly above the strike, but the run downweights the market’s confidence because the contract is narrowly specified and the price cushion is not large relative to normal crypto short-horizon moves.

## Suggested downstream use

Use as an orchestrator synthesis input for probability calibration and for reminding other personas not to treat this as a settled Yes merely because current spot is above 72,000.