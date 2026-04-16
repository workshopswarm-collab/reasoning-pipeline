---
type: evidence_map
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
research_run_id: 2b563fa8-d430-4236-92b5-644c8c8bbed0
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68k-on-april-20
question: "Will the price of Bitcoin be above $68,000 on April 20?"
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
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-79281f9a/researcher-analyses/2026-04-15/dispatch-case-20260415-79281f9a-20260415T202526Z/personas/risk-manager.md"]
tags: ["stress-test", "scenario-analysis", "settlement-risk"]
---

# Summary
The evidence still leans Yes, but the main stress-test point is that a 97% market price embeds very high confidence for a short-dated crypto level market with exact-minute and single-venue settlement mechanics.

## Question being evaluated
Will Binance BTC/USDT print a final 1-minute candle close above 68,000 at 12:00 ET on 2026-04-20?

## Current lean
Lean Yes, but with lower confidence than the market price implies.

## Prior / starting view
Starting view was that a market at 97% is probably directionally correct given BTC's distance above strike, but worth stress-testing because exact-minute crypto contracts can still fail through volatility or settlement-mechanics edge cases.

## Evidence supporting the claim
- Binance direct spot context around 74.85k.
  - Source: 2026-04-15-risk-manager-binance-market-context.md
  - Why it matters causally: the governing venue is materially above strike.
  - Direct.
  - Weight: high.
- Binance recent 1-minute klines around 74.61k-74.68k.
  - Source: same note.
  - Why it matters causally: direct evidence from the exact candle family used for settlement.
  - Direct.
  - Weight: high.
- CoinGecko spot cross-check around 74.75k.
  - Source: 2026-04-15-risk-manager-cross-venue-context.md
  - Why it matters causally: reduces concern about one-off venue distortion at review time.
  - Indirect/contextual.
  - Weight: medium.

## Evidence against the claim
- The contract resolves on one exact minute on one venue, so path and timing risk remain real even with a large current cushion.
  - Source: Polymarket rules plus Binance single-minute contract structure.
  - Why it matters causally: large intraday crypto moves can invalidate a currently safe-looking level.
  - Direct on rules, indirect on volatility risk.
  - Weight: high.
- Market is already at an extreme 97.15% implied probability.
  - Source: assignment context current_price.
  - Why it matters causally: leaves little room for hidden uncertainty and raises verification burden.
  - Direct.
  - Weight: medium-high.
- Venue-specific or UI/API interpretation edge cases could matter if Binance experiences anomalies near settlement.
  - Source: rules naming Binance candle display and ET minute.
  - Why it matters causally: this is a single-source settlement market.
  - Direct.
  - Weight: medium.

## Ambiguous or mixed evidence
- Cross-venue agreement is supportive, but crypto markets are highly correlated, so it is not a strongly independent mechanism check.

## Conflict between inputs
No major factual conflict found. The main disagreement is weighting-based: how much to discount a 97% price for residual volatility and operational edge risk.

## Key assumptions
- Binance BTC/USDT remains near broader BTC spot pricing.
- No large downside shock pushes BTC below 68k by the resolution minute.
- Noon ET maps cleanly to the relevant Binance 1-minute candle without settlement ambiguity.

## Key uncertainties
- Short-horizon BTC volatility over the next four-plus days.
- Whether any Binance-specific operational issue appears close to settlement.

## Disconfirming signals to watch
- BTC losing the 70k area or accelerating toward 68k before April 20.
- Binance-specific price dislocation or trading interruption.
- Clarification showing a different candle mapping than assumed.

## What would increase confidence
- Continued BTC stability above low-70k into April 19-20.
- Another clean Binance check closer to the settlement date showing ample cushion.
- No exchange-status or data-quality concerns from Binance.

## Net update logic
The direct exchange evidence is strong enough to keep a Yes lean, but the risk-manager adjustment is to trim confidence below market because a 97% price understates the residual risk of a short-dated crypto move and single-minute single-venue settlement.

## Suggested downstream use
Use as orchestrator synthesis input and as a prompt to explicitly separate directional agreement from confidence disagreement.