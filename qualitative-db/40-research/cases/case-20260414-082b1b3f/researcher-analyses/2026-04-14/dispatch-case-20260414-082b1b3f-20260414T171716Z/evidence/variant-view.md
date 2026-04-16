---
type: evidence_map
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
research_run_id: 9f2a1a56-1503-4339-aa71-4b6f97e197de
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: altcoins
entity: sol
topic: solana-above-80-on-april-17
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close above $80 on April 17, 2026?"
driver: operational-risk
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/variant-view.md"]
tags: ["evidence-netting", "settlement-risk", "volatility"]
---

# Summary

Net evidence still leans Yes, but the strongest credible alternative to consensus is that the market is overconfident because a multi-day, single-minute settlement condition is being priced too much like a same-day spot observation.

## Question being evaluated

Whether Binance SOL/USDT will print a final 1-minute close above $80 at 12:00 ET on April 17, 2026.

## Current lean

Lean Yes, but less strongly than the market.

## Prior / starting view

Starting view from the market was very strong Yes because current price sat comfortably above $80 and the market implied ~88.5%.

## Evidence supporting the claim

- Current Binance spot/24h data showed SOL around 85.25 with intraday range 82.58-87.67.
  - direct source
  - matters because the threshold is still several dollars below spot
  - deserves high weight
- Recent daily closes recovered from early-April weakness and are now back in the low/mid-80s.
  - direct source
  - matters because it suggests current state favors remaining above 80 absent a fresh shock
  - deserves medium-high weight
- The threshold is only a binary settlement against one venue, so there is no need for broad cross-exchange confirmation if Binance itself remains above 80.
  - direct contract interpretation
  - deserves medium weight

## Evidence against the claim

- Binance daily candles show sub-$80 close on April 1 and sub-$80 intraday lows on April 2, April 6, and April 7.
  - direct source
  - matters because it proves the threshold is not a remote tail within the current regime
  - deserves high weight
- Time to settlement is about 2.5 days, which is long enough for a mid-single-digit altcoin move.
  - indirect but highly relevant contextual evidence
  - matters because the market may be pricing a time-specific event like a static spot condition
  - deserves medium-high weight
- Market is at an extreme probability despite the cushion only being around 6-7% above threshold.
  - interpretive evidence
  - matters because extreme pricing should require either a much larger cushion or stronger stabilizing evidence than was visible here
  - deserves medium weight

## Ambiguous or mixed evidence

- Recent recovery from low-80s to mid-80s can be read either as strengthening support above 80 or as evidence that a reversal back toward 80 remains plausible because the move was recent.
- No specific near-term catalyst was identified in this run; that slightly lowers confidence in a sharp downside variant, but also means the market may just be extrapolating quiet conditions.

## Conflict between inputs

There is little factual conflict. The disagreement is mainly weighting-based: how much confidence should traders assign to a spot price in the mid-80s remaining above 80 at one exact minute on April 17.

## Key assumptions

- Recent Binance volatility is more informative than broad Solana narrative priors for this short-dated market.
- The settlement UI candle should align closely enough with Binance API price series for practical analysis.

## Key uncertainties

- Whether broad crypto beta helps or hurts SOL over the next ~2.5 days.
- Whether the noon ET timing creates any idiosyncratic risk versus a daily close framework.
- Whether market participants have superior near-term catalyst information not captured here.

## Disconfirming signals to watch

- SOL sustaining a much larger cushion above 80 into April 16-17.
- Realized volatility compressing markedly while price holds in the upper-80s.
- Confirmation from later checks that Binance minute-level trading remains comfortably above 80 through settlement morning.

## What would increase confidence

- A direct Binance UI candle check closer to settlement.
- Another independent data surface showing similar recent realized volatility and no hidden contract-interpretation wrinkle.
- Continued price action establishing 80 as clearly distant support rather than nearby support.

## Net update logic

The evidence kept the direction as Yes but cut conviction relative to the market. What mattered most was not broad Solana sentiment but the mismatch between an extreme market probability and a still-modest distance above the threshold with multiple days remaining. The variant thesis is therefore a calibration challenge, not a bearish fundamental call.

## Suggested downstream use

orchestrator synthesis input