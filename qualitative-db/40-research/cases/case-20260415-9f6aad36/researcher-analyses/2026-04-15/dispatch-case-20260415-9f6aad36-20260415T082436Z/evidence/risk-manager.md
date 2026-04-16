---
type: evidence_map
case_key: case-20260415-9f6aad36
dispatch_id: dispatch-case-20260415-9f6aad36-20260415T082436Z
research_run_id: 4632dceb-1076-4409-8cc2-52bedc2e938d
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-pm-et-1-minute-candle-on-2026-04-16-close-above-72-000
question: "Will the Binance BTC/USDT 12:00 PM ET 1-minute candle on 2026-04-16 close above 72,000?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["intraday-volatility"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-9f6aad36/researcher-analyses/2026-04-15/dispatch-case-20260415-9f6aad36-20260415T082436Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "polymarket", "binance", "timing-risk"]
---

# Summary

Net view: Yes remains likelier than No because current Binance price is comfortably above 72,000, but the market's 83.5% pricing looks a bit too confident for a one-minute, one-exchange, next-day settlement condition.

## Question being evaluated

Will Binance BTC/USDT's 12:00 PM ET 1-minute candle on April 16, 2026 have a final close above 72,000?

## Current lean

Lean Yes, but with meaningful respect for timing/path fragility.

## Prior / starting view

Starting baseline was the market-implied 83.5% Yes probability from current_price 0.835.

## Evidence supporting the claim

- **Direct exchange price context**: Binance ticker price during the run was 73,970.88, around 2.7% above the threshold. Weight: high.
- **Direct recent 1-minute Binance candles**: recent closes were also around 73.9k, confirming that the exchange-specific settlement venue is currently above the strike, not just a cross-exchange average. Weight: high.
- **Short remaining horizon**: only about one day remains to resolution, reducing the cumulative opportunity set for thesis-breaking shocks relative to a longer-dated market. Weight: medium.

## Evidence against the claim

- **Timing specificity**: the contract resolves on one specific minute, not on daily average, daily close, or broad exchange consensus. A brief but badly timed drawdown is enough to lose. Weight: high.
- **Single-venue reliance**: Binance BTC/USDT specifically governs. Exchange-specific irregularity or chart/candle interpretation issues are not the base case, but they are more relevant here than in a generic BTC-above-X market. Weight: medium.
- **Compressed buffer**: a roughly 2.7% cushion is meaningful but not huge for BTC over a one-day horizon. Weight: medium.

## Ambiguous or mixed evidence

- Polymarket market pricing itself is informative but not independent evidence.
- Current spot being above threshold is clearly supportive, but it does not guarantee the exact future one-minute close.

## Conflict between inputs

No major factual conflict. The main issue is weighting: how much discount should be applied for one-minute settlement risk despite supportive current price context.

## Key assumptions

- BTC can hold above 72,000 through the exact settlement minute.
- Binance candle mechanics remain accessible and ordinary.
- No fast downside shock arrives before noon ET.

## Key uncertainties

- Intraday BTC volatility into the settlement window.
- Whether the market is slightly underpricing path risk because current spot is already above the threshold.
- Low-probability but nonzero exchange-specific operational oddities.

## Disconfirming signals to watch

- BTC loses the low-73k area and trades persistently near or below 72,000.
- Broader crypto risk-off move accelerates before noon ET.
- Any Binance chart/candle-access anomaly close to settlement.

## What would increase confidence

- BTC still holding materially above 72,000 closer to the settlement window.
- Continued ordinary Binance exchange operation with stable chart/candle access.

## Net update logic

The direct evidence is strong enough to keep a Yes lean, but the contract's narrow timing mechanics prevent me from simply matching the market's confidence. The main adjustment is not a directional bearish thesis; it is a confidence haircut for one-minute settlement fragility.

## Suggested downstream use

Use as orchestrator synthesis input and as a risk-control note against over-trusting a high-probability market on a narrow one-minute settlement condition.