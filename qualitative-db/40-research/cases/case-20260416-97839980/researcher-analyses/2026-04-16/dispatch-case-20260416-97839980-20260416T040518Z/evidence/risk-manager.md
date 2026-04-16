---
type: evidence_map
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
research_run_id: 3a7e2827-18f7-4f75-9a5f-9b536335e7b1
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-price-resolution
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?"
driver: operational-risk
date_created: 2026-04-16
agent: risk-manager
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/risk-manager.md"]
tags: ["evidence-map", "risk-manager", "timing-risk"]
---

# Summary

The evidence leans Yes because Binance spot is already above the strike with several days left and recent trading has mostly held above 80. The main reason not to match the market's 92% confidence is narrow-resolution timing risk: this contract resolves on one exact Binance minute close, so a weekend risk-off move or last-mile dip could still break the thesis.

## Question being evaluated

Will the Binance SOL/USDT 12:00 ET 1-minute candle on April 19, 2026 close strictly above 80?

## Current lean

Lean Yes, but with lower confidence than the market price implies.

## Prior / starting view

Starting view was that 92% looked high for a crypto market with multiple days left unless SOL was already materially above 80 on Binance and recent path data showed stable acceptance.

## Evidence supporting the claim

- Binance spot ticker showed SOL/USDT at 85.39 on 2026-04-16.
  - Direct source: Binance API source note.
  - Causal relevance: gives immediate cushion of about $5.39 above strike on the settlement venue.
  - Direct vs indirect: direct contextual evidence.
  - Weight: high.

- Recent Binance daily and hourly candles remained mostly above 80 after the rebound.
  - Direct source: Binance API source note.
  - Causal relevance: suggests the market is not relying on a one-off wick above strike.
  - Direct vs indirect: direct contextual evidence.
  - Weight: high.

- Contract only requires a close above 80, not a move to new highs.
  - Direct source: Polymarket rules source note.
  - Causal relevance: lowers hurdle because present spot already satisfies the directional requirement if maintained.
  - Direct vs indirect: direct contract interpretation.
  - Weight: medium.

## Evidence against the claim

- Resolution depends on one exact Binance 1-minute close at 12:00 ET on April 19.
  - Source: Polymarket rules source note.
  - Why it matters: narrow timestamp markets can fail despite a generally correct directional call.
  - Direct vs indirect: direct contract evidence.
  - Weight: high.

- Crypto can move more than $5 over a three-day window, especially through weekend or macro risk-off conditions.
  - Source: inference from recent hourly/daily volatility in Binance candles.
  - Why it matters: current buffer is meaningful but not enormous.
  - Direct vs indirect: contextual risk inference.
  - Weight: medium-high.

- Tick size is 0.01 and the rule is strictly above 80.
  - Source: Binance exchange info plus Polymarket rules.
  - Why it matters: 80.00 resolves No; there is no benefit of the doubt around equality.
  - Direct vs indirect: direct operational detail.
  - Weight: medium.

## Ambiguous or mixed evidence

- The market at 92% may reflect correct recognition that SOL is already comfortably above strike, but it may also underprice tail/timing risk because the setup feels nearly settled when it is not.

## Conflict between inputs

No major factual conflict. The main tension is weighting-based: current spot state argues for Yes, while the contract's narrow settlement mechanics argue against extreme confidence.

## Key assumptions

- SOL remains above 80 on Binance into settlement.
- Binance spot remains the relevant, functioning settlement venue without anomalous venue-specific distortion.

## Key uncertainties

- Weekend crypto sentiment between now and April 19 noon ET.
- Whether Binance-specific price action diverges from broader spot venues near settlement.
- Whether a last-hour selloff compresses the cushion enough to make the noon minute close fragile.

## Disconfirming signals to watch

- Hourly closes back under 83 and especially under 80 on Binance spot.
- Sharp market-wide crypto drawdown.
- Evidence of exchange-specific pricing anomaly on Binance SOL/USDT.

## What would increase confidence

- Continued Binance spot trading above 84-85 into April 18-19.
- Reduced realized volatility and sustained hourly closes above strike.
- Cross-venue confirmation that Binance spot is not weak relative to peers.

## Net update logic

The key update versus a generic crypto prior is that the contract settles on Binance spot and SOL is already above the strike by a visible margin there. That moves the base case to Yes. The main downweight versus the market is that this is still a narrow one-minute timestamp market, so path risk and strict-close mechanics keep the probability below the market's near-certainty posture.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why the run agrees with the market direction but discounts market confidence due to timing fragility.