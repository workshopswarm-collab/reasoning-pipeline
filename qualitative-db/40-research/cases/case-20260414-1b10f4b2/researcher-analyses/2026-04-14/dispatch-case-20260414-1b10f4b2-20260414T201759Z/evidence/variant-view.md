---
type: evidence_map
case_key: case-20260414-1b10f4b2
dispatch_id: dispatch-case-20260414-1b10f4b2-20260414T201759Z
research_run_id: 6d1b180e-86d9-42ca-810c-0a177f79f8da
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68k-on-april-20
question: "Will the price of Bitcoin be above $68,000 on April 20?"
driver: liquidity
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["liquidity", "sentiment", "operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["variant-view.md"]
tags: ["evidence-map", "threshold-market", "binance"]
---

# Summary

The net evidence supports Yes, but the variant view is that market confidence is a bit too high because this is a narrow minute-specific Binance settlement rather than a generic "BTC stays strong" question.

## Question being evaluated

Will Binance BTC/USDT print a final 12:00 ET one-minute candle close above 68000 on April 20, 2026?

## Current lean

Yes, with probability below market confidence.

## Prior / starting view

Starting view was that a 94% market price likely reflected a simple large cushion over threshold, but that narrow contract mechanics might justify a modest discount.

## Evidence supporting the claim

- Binance spot around 74.3k on 2026-04-14.
  - source: Binance API source note
  - causal relevance: gives a sizeable cushion above 68k
  - direct vs indirect: direct contextual evidence from settlement venue
  - weight: high
- Recent Binance daily closes mostly above 70k and all closes after April 4 above 68k.
  - source: Binance API source note
  - causal relevance: suggests threshold has not been marginal recently
  - direct vs indirect: direct contextual evidence from settlement venue
  - weight: medium-high
- Market only requires price to remain above 68k at one specific minute, not to hold a higher daily close.
  - source: Polymarket rules source note
  - causal relevance: current cushion means many paths still resolve Yes
  - direct vs indirect: direct contract interpretation
  - weight: medium

## Evidence against the claim

- The contract is narrow: exact Binance pair, exact noon ET minute, strict greater-than test.
  - source: Polymarket rules source note
  - causal relevance: increases tail-risk relative to a broad daily-close intuition
  - direct vs indirect: direct contract interpretation
  - weight: high
- BTC routinely experiences multi-thousand-dollar swings over a few days.
  - source: Binance daily ranges source note
  - causal relevance: an 8-9% drawdown over six days is not impossible in crypto
  - direct vs indirect: contextual but venue-direct
  - weight: medium
- Exchange-specific operational or wick risk can matter more than consensus narrative appreciates.
  - source: contract mechanics plus venue specificity
  - causal relevance: this is the main variant path to No without requiring a broad bear thesis
  - direct vs indirect: interpretive but grounded in contract structure
  - weight: medium

## Ambiguous or mixed evidence

- The same wide BTC volatility cuts both ways: it makes sub-68k plausible, but the current cushion also means ordinary noise still leaves Yes likely.

## Conflict between inputs

- No major factual conflict between sources.
- Main disagreement is weighting-based: whether the large current cushion deserves near-certainty or merely high confidence.

## Key assumptions

- Current price cushion remains broadly intact through April 20.
- Binance venue behavior remains normal near settlement.
- No macro or crypto-specific shock produces a sharp downside move before noon ET on April 20.

## Key uncertainties

- Short-horizon BTC volatility over six days.
- Exact settlement-minute behavior on Binance.
- Whether market participants are underpricing exchange-specific and minute-specific tail risk.

## Disconfirming signals to watch

- BTC/USDT losing 70k convincingly before April 20.
- Elevated downside volatility or disorderly wicks on Binance.
- Binance trading or data issues near settlement.

## What would increase confidence

- BTC/USDT remaining above 72k-73k into April 19-20.
- Stable Binance trading conditions with no venue anomalies.
- Continued distance between spot and 68k threshold.

## Net update logic

The direct venue data supports Yes clearly. The variant adjustment comes from contract interpretation and tail-risk framing: the market appears directionally right, but 94% may be a little rich for a six-day crypto threshold market tied to one exact Binance minute.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- source collection gap