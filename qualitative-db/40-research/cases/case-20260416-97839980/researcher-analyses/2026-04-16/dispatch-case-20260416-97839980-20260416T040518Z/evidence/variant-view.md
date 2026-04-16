---
type: evidence_map
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
research_run_id: e70a0e85-1712-465f-b1f0-3d16b88cba71
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: trading
entity: sol
topic: solana-above-80-on-april-19
question: "Will the price of Solana be above $80 on April 19?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
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
tags: ["evidence-map", "sol", "variant-view"]
---

# Summary

The net evidence supports Yes, but the variant view is that 92% may be too confident for a three-day crypto threshold contract that settles on one exchange-specific 1-minute noon ET close.

## Question being evaluated

Will Binance SOL/USDT print a final 1-minute candle close above 80 at 12:00 ET on April 19, 2026?

## Current lean

Lean Yes, but with lower confidence than the market implies.

## Prior / starting view

Starting view was that 92% looked directionally sensible because spot was already above 85, but worth stress-testing because extreme short-dated crypto probabilities can underweight timing-specific downside.

## Evidence supporting the claim

- Binance spot snapshot around 85.39 on April 16.
  - Direct source note: `researcher-source-notes/2026-04-16-variant-view-binance-sol-price-and-rules.md`
  - Matters because the threshold is already in the money by about 5.39 points.
  - Direct evidence.
  - High weight.
- Recent Binance daily closes all above 80 in the fetched sample.
  - Same source note.
  - Matters because it shows recent persistence above threshold rather than a one-off spike.
  - Direct contextual evidence from the same settlement source.
  - Medium-high weight.
- CoinGecko cross-check around 85.29.
  - Source note: `researcher-source-notes/2026-04-16-variant-view-coingecko-context.md`
  - Matters because it independently validates broad spot context.
  - Indirect/contextual evidence.
  - Medium weight.

## Evidence against the claim

- The contract settles on one exact 1-minute close at noon ET, not on average weekend price or daily close.
  - Polymarket rules in the Binance/rules note.
  - Matters because timing compression increases tail-risk versus a looser threshold market.
  - Direct contract-interpretation evidence.
  - High weight.
- Recent Binance daily sample included lows below 80 and a close as low as 81.53.
  - Binance source note.
  - Matters because sub-80 is demonstrably within recent realized range.
  - Direct contextual evidence.
  - Medium-high weight.
- Crypto remains a high-beta asset class where a 6% move over ~3 days is plausible.
  - Inference from observed recent range and market structure.
  - Indirect evidence.
  - Medium weight.

## Ambiguous or mixed evidence

- Current price being materially above 80 helps Yes, but can also attract overconfidence if traders mentally substitute current spot for the exact future noon close.

## Conflict between inputs

No strong factual conflict. The main disagreement is weighting-based: whether the remaining downside path is small enough to justify 92%.

## Key assumptions

- Recent realized range is still informative for the next three days.
- No extraordinary bullish or bearish catalyst dominates before settlement.
- Binance remains usable and aligned with the contract source of truth.

## Key uncertainties

- Weekend crypto direction before April 19 noon ET.
- Whether SOL mean-reverts lower toward the low-80s.
- Whether noon ET microstructure differs from broader daily trend.

## Disconfirming signals to watch

- SOL breaks and holds below 82 before settlement.
- Broad crypto risk-off move into the weekend.
- Exchange-specific dislocation on Binance.

## What would increase confidence

- Another verification closer to settlement showing Binance SOL/USDT still safely above 80.
- Evidence of lower realized intraday volatility into April 19.

## Net update logic

The evidence kept the direction as Yes but lowered conviction versus the market because the contract is narrower than a casual reading suggests. What mattered most was the combination of current spot comfortably above 80 and the exact-noon-close resolution mechanic. The market seems right on direction but may be somewhat overconfident on magnitude.

## Suggested downstream use

- Forecast update.
- Orchestrator synthesis input.
- Light follow-up verification closer to settlement.