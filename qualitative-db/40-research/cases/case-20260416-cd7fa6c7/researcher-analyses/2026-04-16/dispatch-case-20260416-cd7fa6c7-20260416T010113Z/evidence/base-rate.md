---
type: evidence_map
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
research_run_id: 1bc1a04f-2233-431e-a262-b328f3d70546
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-1-minute-candle-on-april-17-2026-close-above-74000
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 17, 2026 close above 74000?"
driver: reliability
date_created: 2026-04-16
agent: base-rate
status: draft
confidence: medium
conflict_status: low
action_relevance: medium
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/base-rate.md"]
tags: ["evidence-map", "threshold-market", "binance"]
---

# Summary

Net lean is modestly Yes because current Binance BTC/USDT spot is above the strike, but confidence stays moderate because recent realized movement already crossed below 74,000 and the contract settles on one exact 1-minute close.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 17, 2026 close above 74,000?

## Current lean

Modest Yes lean.

## Prior / starting view

Starting outside-view prior was near 50/50 with a slight tilt from current spot-versus-strike once current Binance pricing was checked.

## Evidence supporting the claim

- **Current Binance spot above threshold**
  - source: Binance ticker / source note
  - causal relevance: current level versus strike is the dominant short-horizon threshold input
  - direct vs indirect: indirect for settlement, but highly relevant contextual evidence
  - weight: high

- **Recent daily closes clustered around/above 74k**
  - source: Binance daily klines / source note
  - causal relevance: suggests the market regime is near the line rather than far below it
  - direct vs indirect: indirect
  - weight: medium

- **No identified special exclusion beyond exact venue/pair/time/candle-close mechanics**
  - source: Polymarket rules / source note
  - causal relevance: removes some contract-interpretation uncertainty
  - direct vs indirect: direct for settlement mechanics
  - weight: medium

## Evidence against the claim

- **Recent 24h low below threshold at 73,514**
  - source: Binance 24h stats / source note
  - causal relevance: shows an ordinary adverse move is enough to lose the contract
  - direct vs indirect: indirect
  - weight: high

- **One-minute settlement noise**
  - source: contract rules / source note
  - causal relevance: exact-minute close is noisier than daily close and easier to miss even in a broadly supportive trend
  - direct vs indirect: direct on contract structure
  - weight: high

## Ambiguous or mixed evidence

- CoinGecko corroborates the broad price regime but adds little incremental edge because settlement is Binance-specific.
- Recent trend is mildly favorable, but not so strong that it overwhelms short-horizon volatility.

## Conflict between inputs

No major factual conflict. The main issue is weighting: current level says slight Yes, recent realized volatility says avoid overconfidence.

## Key assumptions

- Current price regime remains informative through settlement.
- No large overnight catalyst or Binance-specific dislocation emerges.

## Key uncertainties

- Overnight/morning volatility before noon ET Apr 17.
- Exact ET-to-Binance-candle operational mapping in the final settlement view, though the rules are fairly clear.

## Disconfirming signals to watch

- Sustained trading below 74,000 before the settlement window.
- Broad crypto risk-off move.
- Binance-specific pricing weakness relative to other venues.

## What would increase confidence

- BTC holding clearly above 75,000 into late morning ET Apr 17.
- Continued narrow realized volatility with price consistently above 74,000.

## Net update logic

The evidence moved the prior from near-neutral to modest Yes because current spot is above the strike on the relevant venue. But the update stayed small because recent realized range already crossed below 74,000, meaning this is a threshold living inside normal noise rather than a comfortably cleared line.

## Suggested downstream use

Use as an orchestrator synthesis input: small positive weight for Yes, but not as a high-confidence anchor.