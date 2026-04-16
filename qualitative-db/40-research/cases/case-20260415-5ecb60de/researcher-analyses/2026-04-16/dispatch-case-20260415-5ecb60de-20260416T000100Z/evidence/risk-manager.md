---
type: evidence_map
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
research_run_id: d25de3d1-4961-4365-b083-096ab0446405
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-price-resolution
entity: sol
topic: will-the-binance-sol-usdt-12-00-et-1-minute-candle-close-on-2026-04-19-be-above-80
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close on 2026-04-19 be above 80?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["crypto-weekend-volatility"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/risk-manager.md"]
tags: ["evidence-map", "risk-manager", "threshold-market"]
---

# Summary

The evidence still leans Yes because SOL is currently above the threshold and recent direct Binance price history has mostly stayed above 80, but the market looks somewhat overconfident because this contract resolves on one minute at one exact time and only needs a modest drawdown to fail.

## Question being evaluated

Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 have a final close above 80?

## Current lean

Lean Yes, but with more path-risk than a 90% market price implies.

## Prior / starting view

Starting view was that a 90% market price might be justified if SOL were far above 80 or if resolution were immediate; after checking the threshold distance and exact timing mechanics, the view shifted modestly toward underconfidence in the market.

## Evidence supporting the claim

- Current Binance spot price around 84.92. Direct. High weight.
  - Matters because the market only requires SOL to stay above 80 at one specific future minute.
- Recent Binance daily klines show lows around 81.27 and 83.30 over the past several days, with recent closes in the low-to-mid 80s. Direct. Medium-high weight.
  - Matters because recent realized range has mostly held above the strike.
- Polymarket rules name Binance SOL/USDT 1-minute close specifically, reducing source ambiguity. Direct for mechanics. Medium weight.
  - Matters because there is little room for cross-venue interpretation disputes.

## Evidence against the claim

- The strike is only about 5 dollars below current spot, so a roughly 6% adverse move can flip the outcome. Derived from direct price data. High weight.
  - Matters because crypto can move that much over a weekend without extraordinary news.
- This is a single-timestamp noon ET market, not an average-price or end-of-day market. Direct from rules. High weight.
  - Matters because narrow timing increases fragility and makes one transient selloff sufficient for No.
- Market-implied probability near 90% embeds high confidence despite limited cushion to the threshold. Interpretive. Medium weight.
  - Matters because confidence can be underpriced/overpriced separately from directional lean.

## Ambiguous or mixed evidence

- Binance API and Binance web-chart source classes should align, but the contract names the website candle display. Usually low issue, but still a mild operational ambiguity.
- Recent daily data are supportive, but daily candles can hide intraday or intraminute swings that matter for this contract.

## Conflict between inputs

No major factual conflict found. The main tension is weighting-based: recent price support argues Yes, while timing and volatility mechanics argue against near-certainty.

## Key assumptions

- Recent low-to-mid-80s trading regime persists through Sunday noon ET.
- No exchange-specific pricing anomaly on Binance at the relevant minute.
- Weekend volatility does not produce a brief but decisive sub-80 close.

## Key uncertainties

- Crypto-wide market direction between now and April 19.
- Whether SOL retains a comfortable cushion above 80 into the final 24 hours.
- Whether a brief noon ET dislocation occurs even if the broader day is strong.

## Disconfirming signals to watch

- SOL trading back into the low 82s or 81s before the weekend.
- Rising realized volatility or sharp downside in BTC/ETH.
- Any Binance-specific chart or operational irregularity.

## What would increase confidence

- Another verification pass closer to expiry showing SOL still several dollars above 80.
- Continued recent intraday lows above 80 on Binance.
- Stable broader crypto tape into the weekend.

## Net update logic

The direct evidence supports Yes, but the risk-manager adjustment is to haircut confidence because the contract resolves on one exact minute and because the current cushion is not large relative to normal crypto volatility.

## Suggested downstream use

Use as an orchestrator synthesis input and as a check against over-weighting the raw market price as if it represented a low-fragility event.