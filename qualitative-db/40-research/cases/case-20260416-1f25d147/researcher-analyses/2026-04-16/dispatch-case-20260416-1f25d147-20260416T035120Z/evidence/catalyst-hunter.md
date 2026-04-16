---
type: evidence_map
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
research_run_id: c45eaf43-60e6-45c8-86aa-1d4dd0a8c0e1
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: solana
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-analyses/2026-04-16/dispatch-case-20260416-1f25d147-20260416T035120Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "timing", "catalyst", "solana"]
---

# Summary

The evidence net is favorable to Yes because SOL is already trading above the strike and the contract window is near, but this is a timing-sensitive crypto price market where one adverse weekend move can still defeat an otherwise bullish setup.

## Question being evaluated

Will Binance SOL/USDT post a final close above 80 on the one-minute candle corresponding to 12:00 ET on April 19, 2026?

## Current lean

Lean Yes with high but not near-certain probability.

## Prior / starting view

Starting view was that a 92% market price looked plausibly high but required checking whether the contract mechanics or recent volatility made that overconfident.

## Evidence supporting the claim

- Binance daily market data shows SOL already above 80 on recent closes and trading around the mid-80s now.
  - Direct source.
  - Matters because the strike is in-the-money already.
  - Weight: high.
- Polymarket rules specify a single Binance SOL/USDT one-minute noon-ET close.
  - Direct contract source.
  - Matters because it confirms the key condition is narrow but straightforward.
  - Weight: high.
- Only a few days remain until resolution.
  - Indirect timing logic from the market calendar.
  - Matters because less time remains for drift below the strike, absent a shock.
  - Weight: medium.

## Evidence against the claim

- Recent Binance daily ranges show several-dollar moves remain normal for SOL.
  - Direct exchange context.
  - Matters because a moderate drawdown could still take price below 80 by the settlement minute.
  - Weight: high.
- The contract is not about daily close, weekend high, or average price; it is one exact minute.
  - Direct contract logic.
  - Matters because path dependence is high and gives no credit for earlier strength.
  - Weight: high.
- No clearly identified positive catalyst is required for Yes, but that also means the thesis is exposed mainly to surprise negative catalysts.
  - Interpretive.
  - Weight: medium.

## Ambiguous or mixed evidence

- The market's 92% pricing may simply reflect correct in-the-money positioning rather than complacency.
- Absence of a known scheduled catalyst cuts both ways: fewer upside repricing drivers, but also fewer obvious downside triggers.

## Conflict between inputs

There is little factual conflict. The main issue is weighting: whether current spot distance above the strike plus short time to expiry justifies a probability in the low 90s, or whether crypto weekend volatility should pull that down meaningfully.

## Key assumptions

- No major downside shock before resolution.
- Binance remains the operative and stable source surface.
- SOL does not mean-revert sharply below the low-80s area by noon ET April 19.

## Key uncertainties

- Weekend crypto volatility.
- Unscheduled Solana-specific or exchange-specific negative news.
- Exact cushion of spot above 80 closer to the resolution minute.

## Disconfirming signals to watch

- SOL losing 82 and then 80 ahead of the event.
- Broader crypto market risk-off acceleration.
- Binance trading irregularities or source-surface ambiguity.

## What would increase confidence

- Continued SOL trading above roughly 83-84 into April 18-19.
- Absence of major crypto risk-off headlines.
- Direct check of the relevant intraday Binance candles closer to settlement.

## Net update logic

The evidence moved the view toward agreeing with the market on direction because the strike is already crossed and the contract mechanics are clear. But the same mechanics keep confidence below near-certainty because the outcome is determined by a single narrow minute and recent volatility shows that a several-dollar drop remains realistic.

## Suggested downstream use

- Orchestrator synthesis input.
- Forecast update with explicit emphasis on late downside catalyst monitoring rather than further broad fundamental research.