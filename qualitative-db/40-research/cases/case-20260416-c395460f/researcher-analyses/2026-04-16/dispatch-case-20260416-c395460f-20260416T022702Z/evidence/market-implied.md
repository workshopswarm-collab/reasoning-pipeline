---
type: evidence_map
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
research_run_id: 94ac9173-5138-4674-9bf1-859e6b7026a2
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-price
entity: sol
topic: will-the-binance-sol-usdt-12-00-et-1-minute-candle-close-be-above-80-on-april-19-2026
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close be above 80 on April 19, 2026?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["market-implied", "evidence-map", "threshold-market"]
---

# Summary

The market's high Yes price looks mostly explained by current spot being above the threshold with limited time left, but the contract's narrow settlement minute keeps residual downside risk meaningful.

## Question being evaluated

Will Binance SOL/USDT print a final close above 80 on the 12:00 ET one-minute candle on April 19, 2026?

## Current lean

Lean Yes, with probability somewhat below the market but still high.

## Prior / starting view

Starting from the market price, the natural prior was that traders were mainly pricing current spot cushion and short time-to-expiry.

## Evidence supporting the claim

- **Binance live price around 84.96** — direct, high weight. This puts SOL clearly above the threshold with a modest but real buffer.
- **Recent Binance daily closes mostly above 80** — direct, medium weight. Suggests the threshold has recently been in-the-money on a repeated basis rather than only on a single spike.
- **Only about three days remain** — contextual, medium weight. Less time for a large adverse move than in a longer-dated contract.
- **Polymarket price around 89%** — contextual, medium weight. Suggests crowd participants broadly agree the threshold is likely to hold.

## Evidence against the claim

- **SOL is a volatile crypto asset** — contextual, high weight. A move of ~6% over a weekend is not rare enough to ignore.
- **Resolution is one narrow minute at noon ET** — direct contract feature, high weight. Even if SOL trades above 80 for much of the period, the contract still loses on one badly timed dip.
- **Recent daily lows did go below 80 in the sample** — direct, medium weight. This shows sub-80 prints are still plausible, not purely hypothetical.

## Ambiguous or mixed evidence

- Recent strong price action supports Yes, but could also mean short-term positioning is crowded and therefore fragile.
- The market's 89% price may reflect real information, but it could also slightly underprice short-horizon realized volatility around a single-minute settlement.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much probability mass should be assigned to ordinary crypto volatility over the remaining time window.

## Key assumptions

- Current spot level remains a useful anchor through the final day.
- No major market-wide shock hits crypto before the settlement minute.
- Binance settlement mechanics remain straightforward and available.

## Key uncertainties

- Weekend macro/crypto risk sentiment.
- Whether SOL can avoid a sub-80 dip exactly at the noon ET measurement minute.
- Whether realized volatility over the next three days is closer to calm recent conditions or to SOL's fatter-tail downside behavior.

## Disconfirming signals to watch

- SOL losing 82 and failing to recover.
- BTC/ETH turning sharply lower into the weekend.
- Increasing intraday wickiness toward or below 80 on Binance.

## What would increase confidence

- Continued Binance trading above 84 into April 18-19.
- Lower realized intraday volatility heading into settlement.
- Stronger confirmation that the market is not missing any contract nuance beyond the already-checked source-of-truth rule.

## Net update logic

The evidence keeps the base view positive because the contract is already somewhat in-the-money and the source-of-truth is clear. I downweight the market modestly because single-minute crypto threshold contracts retain more tail risk than a casual reading of 89% suggests.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why this persona was slightly below, but still broadly aligned with, the market.