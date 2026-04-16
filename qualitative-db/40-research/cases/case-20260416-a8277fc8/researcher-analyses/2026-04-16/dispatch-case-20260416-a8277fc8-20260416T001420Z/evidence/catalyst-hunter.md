---
type: evidence_map
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
research_run_id: bb273820-bcdd-4521-8c8d-c966f1df5f00
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: daily-threshold-close
entity: sol
topic: "Netting current cushion versus weekend timestamp risk for SOL > $80 on Apr 19 noon ET"
question: "Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above 80?"
driver: reliability
date_created: 2026-04-16
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["threshold proximity"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-source-notes/2026-04-16-catalyst-hunter-binance-polymarket-resolution-surface.md", "qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/assumptions/catalyst-hunter.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "sol", "threshold"]
---

# Summary

This evidence map nets a simple but timing-sensitive crypto threshold-close case: SOL is already above $80 by a nontrivial margin, but the contract resolves from one exact Binance one-minute close on Sunday noon ET rather than from a path-high or average level.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle at 12:00 ET on Apr 19, 2026 close above $80?

## Current lean

Lean Yes with high but not near-certain probability.

## Prior / starting view

Starting view: likely Yes because the market was already pricing ~88.5% and short-dated spot looked above threshold, but needed direct verification of exact contract mechanics before accepting the extreme baseline.

## Evidence supporting the claim

- Direct contract-mechanics verification from Polymarket rules.
  - Direct source.
  - Confirms the event is a close-above contract on Binance SOL/USDT at a single minute.
  - High weight because it defines what counts.
- Direct Binance API spot and recent 1-minute candle check showing SOL/USDT around 84.67-84.74.
  - Direct contextual source for current market state.
  - Matters because current cushion is about $4.67 above threshold.
  - High weight.
- CoinGecko contextual market data showing SOL around 84.73 with positive short-horizon performance.
  - Indirect/contextual.
  - Matters because it suggests the above-$80 regime is not a one-tick anomaly.
  - Medium weight.

## Evidence against the claim

- The market settles on one exact minute close, not on current spot, intraday high, or average price.
  - Direct contract-mechanics implication.
  - High weight because a short-lived dip at the wrong time is enough for No.
- Weekend altcoin volatility could easily produce several-percentage-point moves before Sunday noon ET.
  - Indirect/contextual.
  - Medium weight.
- SOL’s 30-day performance was negative on the CoinGecko readout.
  - Indirect/contextual.
  - Low-to-medium weight because it shows recent weakness is not absent.

## Ambiguous or mixed evidence

- Lack of a discrete bullish catalyst is mixed: it weakens the case for further upside, but this market does not require further upside if the current cushion broadly holds.
- Broader crypto sentiment could help or hurt; no specific near-term scheduled catalyst was identified that looked more material than ordinary market beta.

## Conflict between inputs

No major source conflict. The main tension is weighting-based: how much confidence to place on current cushion versus timestamp-specific downside risk.

## Key assumptions

- Current above-threshold cushion is large enough that ordinary weekend noise is more likely to leave SOL above $80 than below it.
- Binance settlement surface will not diverge meaningfully from broader spot references at the resolution minute.

## Key uncertainties

- Magnitude of weekend crypto volatility.
- Whether SOL underperforms broader crypto into Sunday.
- Whether any idiosyncratic Binance print issue matters at the resolution minute.

## Disconfirming signals to watch

- SOL spending sustained time below 82 before Sunday.
- Broad risk-off crypto move into the weekend.
- Binance SOL/USDT weakening relative to other spot references.

## What would increase confidence

- Another verification pass closer to Apr 19 still showing SOL safely above $80.
- Evidence of stable trading range above low-80s into the weekend.

## Net update logic

The decisive update was not a flashy catalyst but mechanism verification plus direct spot confirmation. Once the contract was confirmed as a Binance close-above-$80 market and spot was directly observed around 84.67, the case became mostly about whether a roughly 5.8% cushion survives until one timestamp. That supports a high Yes probability, but not certainty, because single-minute close risk remains real.

## Suggested downstream use

Use as forecast update and Orchestrator synthesis input, with emphasis on timestamp risk and governing-source specificity rather than broad Solana narrative.