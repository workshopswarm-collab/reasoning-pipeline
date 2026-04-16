---
type: evidence_map
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
research_run_id: 21f0a156-5a26-4e98-87c3-0e4b3216cab5
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-74k-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: reliability
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "binance", "short-horizon"]
---

# Summary

The evidence nets to a modest Yes lean that is close to the market price. Current spot context supports the market, but the contract is narrow enough that ordinary overnight volatility remains the main counterweight.

## Question being evaluated

Will Binance BTC/USDT print a final close above 74,000 on the 12:00 ET one-minute candle on April 17, 2026?

## Current lean

Lean Yes, but not by a huge margin.

## Prior / starting view

Start from the market price of roughly 65% Yes as an information-rich prior.

## Evidence supporting the claim

- Polymarket ladder pricing and strike-specific quote: around 65% for 74,000, with nearby strikes priced coherently. Direct for market-implied baseline; medium weight.
- Binance ticker around 74,645 and recent 1-minute closes all above 74,000. Direct contextual evidence about the actual settlement venue/pair; high weight.
- Coinbase BTC-USD around 74,659 at nearly the same time. Indirect but independent contextual confirmation that Binance was not obviously idiosyncratic; medium weight.

## Evidence against the claim

- The contract resolves on one exact future minute, not on current spot. Direct contract-structure risk; high weight.
- BTC only sat modestly above the strike, so an ordinary sub-1% move could flip the outcome. Direct contextual downside; high weight.
- No strong catalyst evidence was identified that would lock price above the strike through noon ET. Indirect but relevant; medium weight.

## Ambiguous or mixed evidence

- Current price being above strike is supportive, but the margin is small enough that it also highlights fragility.
- Nearby market ladder coherence suggests market efficiency, but does not prove informational edge beyond simple spot anchoring.

## Conflict between inputs

There is little factual conflict. The main tension is weighting-based: how much persistence should be inferred from current price being only modestly above the strike.

## Key assumptions

- Current BTC strength contains enough persistence to matter for a next-day noon ET print.
- Binance will remain close to broader spot pricing and operationally normal.

## Key uncertainties

- Overnight and morning volatility before the exact resolving minute.
- Whether any macro or crypto-specific news shock hits before noon ET.

## Disconfirming signals to watch

- Sustained trading back below 74,000 on Binance before noon ET.
- Rising exchange divergence or unusual Binance-specific behavior.
- Sharp downside move in broader crypto risk sentiment.

## What would increase confidence

- Continued Binance trading above 74,000 into the late morning ET window on April 17.
- Evidence of stable or improving spot support above the strike rather than repeated rejection.

## Net update logic

The market prior survives scrutiny. Current venue-specific spot context supports a Yes lean, but the narrow one-minute resolution condition and limited cushion above the strike argue against overconfidence. That leaves a fair value near, but slightly below, the quoted 65%.

## Suggested downstream use

Use as orchestrator synthesis input and decision-maker review input. Main open question is not rule ambiguity but short-horizon volatility persistence.