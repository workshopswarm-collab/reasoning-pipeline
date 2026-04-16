---
type: evidence_map
case_key: case-20260414-76e5614f
dispatch_id: dispatch-case-20260414-76e5614f-20260414T182607Z
research_run_id: 6834636b-8572-4f97-93af-51ba8fdfd097
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-one-minute-candle-on-2026-04-17-close-above-72000
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 72000?"
driver: operational-risk
date_created: 2026-04-14
agent: risk-manager
status: draft
confidence: medium
conflict_status: low-direct-conflict-high-fragility
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "btc", "timing-risk", "contract-interpretation"]
---

# Summary

The evidence nets to a Yes lean, but the main risk is not fundamental Bitcoin weakness; it is overconfidence in a narrow timed threshold contract whose payout depends on a single Binance one-minute close.

## Question being evaluated

Will Binance BTC/USDT close above 72000 on the 12:00 ET one-minute candle on April 17, 2026?

## Current lean

Lean Yes, but with lower confidence than the market price implies.

## Prior / starting view

Starting baseline was the market-implied ~83% Yes from current_price 0.83.

## Evidence supporting the claim

- Live Binance ticker around 74603 at research time.
  - Direct source.
  - Matters because the market only needs BTC to stay above a threshold below current spot.
  - Weight: high.
- Recent Binance 1-minute klines around 74522-74573.
  - Direct source.
  - Matters because the actual settlement source is a Binance 1-minute close, so current minute-candle behavior is the right instrument class.
  - Weight: medium-high.
- Threshold is 72000 rather than a higher breakout level.
  - Contract/contextual fact.
  - Matters because current price has some cushion.
  - Weight: medium.

## Evidence against the claim

- The contract is path-fragile: only one exact minute close at 12:00 ET on April 17 counts.
  - Direct from contract wording.
  - Matters because a generally bullish BTC path can still lose on timing noise.
  - Weight: high.
- Current cushion is only about 3.6% above threshold.
  - Derived from direct spot reading.
  - Matters because BTC can plausibly move that much within ~46 hours.
  - Weight: high.
- Venue-specific dependence on Binance BTC/USDT rather than cross-exchange spot.
  - Direct from contract wording.
  - Matters because exchange-specific dislocation or operational weirdness is not hedged by broader market strength.
  - Weight: medium.

## Ambiguous or mixed evidence

- The Binance API and Binance UI should usually align, but the contract references the UI candle specifically; this is probably low ambiguity but not zero.
- Broader BTC directional context was not deeply expanded because the next likely source seemed unlikely to move the estimate by >5 points versus the direct contract-plus-spot evidence already gathered.

## Conflict between inputs

No major factual conflict across gathered inputs. The disagreement is mainly weighting-based: whether a current 3.6% cushion justifies an 83% Yes probability for a single future timed candle.

## Key assumptions

- BTC remains above 72000 on Binance into noon ET April 17.
- No Binance-specific anomaly meaningfully distorts the settlement print.
- Short-horizon volatility does not erase the current cushion.

## Key uncertainties

- BTC volatility over the next ~46 hours.
- Event or macro shocks before settlement.
- Minor operational ambiguity between API verification and final UI settlement surface.

## Disconfirming signals to watch

- BTC trading persistently below 73k before settlement.
- Heightened volatility into April 17 morning ET.
- Any Binance outage or chart irregularity near the resolution window.

## What would increase confidence

- BTC holding above 74k through April 16 and into April 17 morning ET.
- Additional direct check of Binance UI candle logic near settlement.
- Evidence that cross-exchange spot and Binance remain tightly aligned into the event.

## Net update logic

The evidence kept the lean on Yes because the market only needs persistence above an already-cleared level, but it reduced confidence versus the market because the contract is narrower than a generic "BTC stays strong" view. What mattered most was the combination of direct contract mechanics and the modest, not huge, current cushion above threshold.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review