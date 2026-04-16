---
type: evidence_map
case_key: case-20260415-9c95ce3a
dispatch_id: dispatch-case-20260415-9c95ce3a-20260415T173129Z
research_run_id: 62f03cc1-3fb8-4490-8a40-d18041bc0aa5
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the Binance BTC/USDT 12:00 PM ET 1-minute candle on 2026-04-17 close above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: base-rate
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-9c95ce3a/researcher-analyses/2026-04-15/dispatch-case-20260415-9c95ce3a-20260415T173129Z/personas/base-rate.md"]
tags: ["base-rate", "threshold", "binance", "timing"]
---

# Summary
Evidence favors Yes because spot is already above the threshold and recent realized trading range has often included >72k prints, but the contract is narrow enough that an 82% market price looks somewhat aggressive for a single future minute.

## Question being evaluated
Will the Binance BTC/USDT 1-minute candle labeled 12:00 PM ET on Apr. 17, 2026 have a close above 72,000?

## Current lean
Lean Yes, but not as strongly as the market.

## Prior / starting view
Starting outside-view prior: once a liquid asset is already several percent above a threshold with only ~2 days remaining, Yes should be favored, but single-minute threshold markets are usually less certain than spot-level intuition suggests.

## Evidence supporting the claim
- Current Binance BTC/USDT spot around 74.1k on Apr. 15.
  - direct/contextual: contextual, not settlement-direct
  - weight: high
  - why it matters: only a moderate downward move is needed to lose, but starting above threshold gives Yes a favorable base state.
- Recent daily highs exceeded 72k on 9 of the last 11 days in the Apr. 5-15 sample.
  - direct/contextual: contextual
  - weight: medium
  - why it matters: shows 72k is inside normal recent trading range, not an outlier barrier.
- Recent daily closes exceeded 72k on 5 of the last 11 days.
  - direct/contextual: contextual
  - weight: medium
  - why it matters: shows persistence above threshold is meaningful but not overwhelming.

## Evidence against the claim
- The contract settles on one exact future 1-minute close at 12:00 PM ET, not on any intraday touch, daily close, or other exchange print.
  - direct/contextual: direct contract interpretation
  - weight: high
  - why it matters: narrow timing makes failure easier than generic “BTC stays strong” intuition suggests.
- BTC has recently shown multi-thousand-dollar daily ranges.
  - direct/contextual: contextual
  - weight: medium-high
  - why it matters: a move from ~74.1k to below 72k by settlement minute is plausible within observed volatility.
- Polymarket Yes at ~82-83% implies only a small chance of a downside breach by settlement, which seems tighter than the recent realized distribution supports.
  - direct/contextual: market-context
  - weight: medium

## Ambiguous or mixed evidence
- Recent momentum is supportive, but short-horizon crypto can reverse quickly.
- Strong recent highs suggest upside cushion, but they also come with elevated volatility.

## Conflict between inputs
No major factual conflict. The main disagreement is weighting-based: whether being ~3% above threshold with two days left deserves an 80%+ probability or something closer to the low-70s.

## Key assumptions
- No major adverse macro/crypto shock before settlement.
- Binance settlement mechanics remain straightforward and available.
- Current price regime remains broadly stable.

## Key uncertainties
- Whether noon ET on Apr. 17 coincides with a volatile downswing.
- Whether spot drifts lower into settlement despite currently favorable levels.

## Disconfirming signals to watch
- BTC losing 73k and failing to reclaim it by Apr. 16.
- Risk-off macro/news shock.
- A clear weakening trend in Binance spot into US hours on settlement day.

## What would increase confidence
- Continued trading above 73.5k through Apr. 16 and into Apr. 17 morning.
- Lower intraday volatility and stable spot across major sessions.

## Net update logic
The outside view starts with Yes favored because BTC is already above the line, but the contract’s single-minute/noon-ET design and recent volatility pull the estimate down from the market’s 82% toward a more cautious low-70s number.

## Suggested downstream use
Use as an Orchestrator synthesis input emphasizing that this is a favorable-but-not-near-certain threshold setup, with contract interpretation and realized volatility doing most of the work.