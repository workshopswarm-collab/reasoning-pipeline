---
type: evidence_map
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
research_run_id: 9cf804b6-fb9e-4c64-aa0d-a5fbd9f57b79
analysis_date: 2026-04-11
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-11
question: "Will the price of Bitcoin be above $72,000 on April 11?"
driver: operational-risk
date_created: 2026-04-10
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/base-rate.md"]
tags: ["evidence-map", "bitcoin", "threshold"]
---

# Summary

The evidence nets to a Yes lean because BTCUSDT is currently above 72k and recent price behavior supports threshold persistence better than a pure coin flip. But the threshold is close enough to the active range that a high-70s/low-80s estimate is easier to defend than the much more aggressive live market price near 91%.

## Question being evaluated

Will the Binance BTCUSDT one-minute candle for 12:00 ET on April 11 close above 72,000?

## Current lean

Leaning Yes, but with meaningful fragility.

## Prior / starting view

Starting outside view: when a volatile asset has only a modest cushion above a nearby threshold with ~15.5 hours left, the answer should be favored but not treated as near-certain.

## Evidence supporting the claim

- Binance spot ticker showed BTCUSDT around 72,872.81 at research time.
  - Direct source note: `2026-04-11-base-rate-binance-market-mechanics-and-spot-context.md`
  - Direct evidence.
  - Weight: high.
- Binance 24h range was 71,426.15 to 73,434.00, with last price above the threshold.
  - Direct source note: same as above.
  - Matters because current threshold distance is positive and recent trading has supported recovery above 72k.
  - Weight: medium-high.
- Polymarket rules and market pricing confirm traders were heavily on the Yes side by research time.
  - Source note: `2026-04-11-base-rate-polymarket-rules-and-market-pricing.md`
  - Indirect/contextual for truth, but useful as a market baseline.
  - Weight: medium.

## Evidence against the claim

- The same Binance 24h range also traded materially below 72k, so a downside cross before noon ET is fully plausible.
  - Direct evidence from Binance.
  - Weight: high.
- Recent 48h hourly candles include multiple closes below 72k.
  - Direct evidence from Binance klines.
  - Weight: high.
- The contract resolves on a single one-minute close, not a broader daily average, which amplifies short-horizon noise.
  - Rule-based structural consideration.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- The live Polymarket price around 90.8% suggests strong confidence, but that may be partly narrative or momentum-driven rather than a disciplined base-rate estimate.
- Cross-venue reference prices such as CoinGecko broadly confirm spot level but do not settle the contract.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much confidence current spot-above-threshold should justify for a one-minute close roughly 15.5 hours later.

## Key assumptions

- Recent BTCUSDT trading regime persists into the resolution window.
- Noon ET corresponds to the 16:00 UTC minute on Binance.
- Settlement uses Binance spot BTCUSDT close as written, without hidden alternate pair logic.

## Key uncertainties

- Overnight and morning volatility before the decisive minute.
- Whether any venue-specific anomaly appears near settlement.
- How much the market’s recent upward repricing reflects genuine informational edge versus momentum.

## Disconfirming signals to watch

- BTCUSDT falling back below 72k and staying there through late morning ET.
- Increased realized volatility or abrupt macro shock.
- Any rule clarification that changes the operative candle interpretation.

## What would increase confidence

- BTCUSDT holding well above 72k into the European and US morning sessions.
- Additional Binance minute data near settlement showing support well above the threshold.
- Confirmation from another reliable rules mirror without any wording discrepancy.

## Net update logic

The outside view starts with: a modestly in-the-money threshold on a volatile asset is favorable but not overwhelmingly so. Current spot and recent recovery justify moving above a neutral prior, but the same recent range crossing below 72k keeps the estimate well below the most bullish market print.

## Suggested downstream use

Use as a synthesis input and retrospective benchmark for whether the swarm over- or underweighted short-horizon BTC threshold persistence relative to live market enthusiasm.
