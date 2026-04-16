---
type: evidence_map
case_key: case-20260414-4d440738
dispatch_id: dispatch-case-20260414-4d440738-20260414T195302Z
research_run_id: 89ce95f4-22f2-44ac-ba39-4e52cfbb381b
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 68000?"
driver: reliability
date_created: 2026-04-14
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4d440738/researcher-analyses/2026-04-14/dispatch-case-20260414-4d440738-20260414T195302Z/personas/market-implied.md"]
tags: ["evidence-netting", "btc", "settlement-risk"]
---

# Summary

The net evidence supports a high-probability Yes outcome, but the 94% market price appears somewhat overconfident once the exact Binance noon-ET minute-close condition and ordinary crypto downside tails are accounted for.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle close at 12:00 ET on 2026-04-20 print above 68,000?

## Current lean

Lean Yes, high probability, but below the market-implied 93.5-94%.

## Prior / starting view

Starting from the market price, the default prior is that traders see the strike as safely in-the-money because spot is already in the mid-70k area.

## Evidence supporting the claim

- Binance spot around 74.2k, about 9.2% above the strike. Direct, high weight.
- Recent 7 daily Binance lows remained above about 70.5k, meaning the strike is below the recent sampled range. Direct contextual, medium-high weight.
- Polymarket strike ladder is smooth: 68k at 94%, 70k at 85%, 72k at 73%, 74k near 51%, suggesting the market has a coherent implied distribution rather than a clearly stale mispricing. Market-derived contextual evidence, medium weight.

## Evidence against the claim

- Crypto can move 8-10% over six days without requiring a regime break; the current cushion is meaningful but not enormous. Indirect/contextual, medium weight.
- Resolution depends on one exchange and one minute candle at noon ET, not on broader BTC spot over the day, which adds nonzero timing and venue-specific failure risk. Direct contract interpretation, medium weight.
- Extreme market probability itself is a warning sign requiring extra verification; there is no authoritative source that already settles the future event. Meta-evidentiary, low-medium weight.

## Ambiguous or mixed evidence

- Lack of an independent macro/news catalyst in this pass cuts both ways: no obvious bearish trigger now, but also no catalyst-based case for treating 94% as nearly locked.

## Conflict between inputs

There is little factual conflict. The main difference is weighting: current spot and recent range support a strong Yes lean, while contract narrowness and crypto volatility argue against near-certainty.

## Key assumptions

- Recent Binance range is informative enough for a six-day horizon.
- No major shock or exchange-specific disruption occurs before the settlement minute.
- The Polymarket ladder is reasonably efficient and not badly stale.

## Key uncertainties

- Near-term realized volatility through April 20.
- Potential weekend/macro event risk.
- Whether Binance-specific microstructure creates extra downside tail at the exact minute.

## Disconfirming signals to watch

- BTC retracing toward or below 70k on Binance before April 20.
- Sudden deterioration in crypto risk sentiment.
- Any Binance market-structure anomaly near settlement.

## What would increase confidence

- Continued Binance trading above 72k through the weekend.
- Additional independent volatility/context data showing sub-10% downside tails over similar horizons are rarer than implied here.
- Clear confirmation that noon-ET candle mapping to Binance display introduces minimal ambiguity.

## Net update logic

The market prior largely survives scrutiny: current spot and recent range justify a high Yes probability. The update is only modestly bearish versus market because 94% leaves too little room for an ordinary six-day BTC drawdown or a settlement-minute-specific miss.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why this persona mostly respects, but slightly discounts, the market price.