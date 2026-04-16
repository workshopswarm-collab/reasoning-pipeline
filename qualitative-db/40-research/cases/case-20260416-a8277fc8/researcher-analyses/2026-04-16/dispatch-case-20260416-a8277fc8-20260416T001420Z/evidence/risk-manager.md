---
type: evidence_map
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
research_run_id: 384a5d37-1aab-4d46-9b7a-604a712b4e3c
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: short-dated-threshold
entity: sol
topic: solana-above-80-on-april-19
question: "Will Binance SOL/USDT close above 80 on the 12:00 ET one-minute candle on Apr. 19, 2026?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-source-notes/2026-04-16-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-source-notes/2026-04-16-risk-manager-binance-spot-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/risk-manager.md"]
tags: ["evidence-map", "threshold", "noon-close", "binance", "risk-manager"]
---

# Summary

The current lean is Yes, but the main risk-manager objection is that the market may be pricing current spot level as if it almost guarantees the exact settlement-minute close.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle stamped 12:00 ET on 2026-04-19 have a final close above 80?

## Current lean

Lean Yes, with caution against treating this as near-certain.

## Prior / starting view

Given a market-implied probability of 88.5%, the starting baseline was that traders see current spot and recent range as making a Yes outcome very likely.

## Evidence supporting the claim

- Binance current price around 84.67 on the governing exchange and pair.
  - Source: Binance API source note.
  - Why it matters: direct cushion above threshold.
  - Direct or indirect: direct contextual evidence.
  - Weight: high.
- Recent Binance 24h range of 82.65 to 85.83.
  - Source: Binance API source note.
  - Why it matters: recent realized trading remained entirely above 80.
  - Direct or indirect: direct contextual evidence.
  - Weight: medium-high.
- Multiple recent daily candles with lows and closes above 80.
  - Source: Binance API source note.
  - Why it matters: suggests threshold is not barely being held by a single transient spike.
  - Direct or indirect: direct contextual evidence.
  - Weight: medium.

## Evidence against the claim

- Settlement is on one exact 12:00 ET one-minute close, not on any trade before then.
  - Source: Polymarket rules note.
  - Why it matters causally: path dependence and timing precision create failure risk even when spot is currently above threshold.
  - Direct or indirect: direct evidence on mechanics.
  - Weight: high.
- The event has not yet occurred, so current spot cannot verify the qualifying candle.
  - Source: timing and rule structure.
  - Why it matters: prevents overclaiming and leaves room for weekend volatility.
  - Direct or indirect: direct timing constraint.
  - Weight: high.
- Crypto weekend downside of more than 5% over several days is plausible.
  - Source: general market behavior, supported indirectly by daily volatility in the fetched Binance ranges.
  - Why it matters: a move of that size would erase the cushion.
  - Direct or indirect: indirect contextual evidence.
  - Weight: medium.

## Ambiguous or mixed evidence

- Recent daily lows have stayed above 80, which is supportive, but the sampled period is short and may understate tail risk over the next three days.
- Using Binance as both context source and settlement source gives mechanism fit but low source independence.

## Conflict between inputs

There is no major factual conflict. The main disagreement is weighting-based: how much confidence should be assigned to a current ~5.8% cushion in a short-dated crypto market with an exact settlement minute.

## Key assumptions

- Current price regime remains broadly stable through Apr. 19 noon ET.
- No exchange-specific Binance distortion appears at the qualifying minute.
- Recent above-80 trading is informative for the qualifying candle rather than a temporary overshoot.

## Key uncertainties

- Weekend volatility and broad crypto market direction.
- Whether the cushion narrows materially before resolution.
- Whether Binance-specific microstructure deviates at the settlement minute.

## Disconfirming signals to watch

- SOL/USDT loses 82 and trends toward 80 before Apr. 19.
- Broader crypto market risk-off move with alt underperformance.
- Evidence of Binance-specific price weakness or outage risk near settlement.

## What would increase confidence

- Another verification pass closer to settlement showing SOL still comfortably above 80 on Binance.
- Broader market stability through the weekend.
- Evidence that similar recent noon ET minute closes have not been unusually weak versus surrounding spot.

## Net update logic

The evidence supports Yes because the governing exchange already trades meaningfully above 80, but the risk adjustment comes from exact-minute settlement mechanics and nontrivial residual time. That keeps the estimate below the market rather than flipping bearish.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with emphasis that the key risk is overconfidence, not a clean bearish thesis.