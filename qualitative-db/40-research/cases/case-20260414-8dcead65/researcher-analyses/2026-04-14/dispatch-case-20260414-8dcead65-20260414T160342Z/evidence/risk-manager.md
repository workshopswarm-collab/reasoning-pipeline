---
type: evidence_map
case_key: case-20260414-8dcead65
dispatch_id: dispatch-case-20260414-8dcead65-20260414T160342Z
research_run_id: c53cc882-6553-47d0-810b-205d680714ca
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-15
question: "Will the price of Bitcoin be above $70,000 on April 15?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-8dcead65/researcher-analyses/2026-04-14/dispatch-case-20260414-8dcead65-20260414T160342Z/personas/risk-manager.md"]
tags: ["evidence-netting", "timing-risk", "settlement"]
---

# Summary

Direct settlement mechanics and current spot levels support Yes strongly, but the remaining uncertainty is highly concentrated in one narrow future observation window.

## Question being evaluated

Will Binance BTC/USDT's 1-minute candle for April 15 at 12:00 ET close above 70,000?

## Current lean

Yes, with high but not absolute confidence.

## Prior / starting view

Starting view was that a market priced at 97.9% was probably directionally right but worth stress-testing because threshold/date-specific crypto contracts can hide timing and operational fragility.

## Evidence supporting the claim

- **Current Binance spot around 75.5k**
  - source: direct Binance ticker endpoint
  - causal relevance: gives a sizeable cushion above the 70k threshold
  - type: direct/contextual to final outcome
  - weight: high
- **Binance 24h low around 71.7k and high around 76.0k**
  - source: direct Binance 24h stats
  - causal relevance: recent realized range stayed above the threshold, suggesting a nontrivial buffer remains
  - type: direct/contextual
  - weight: medium-high
- **Direct verification of 12:00 ET -> 16:00 UTC candle mapping**
  - source: direct Binance kline pull for 2026-04-14 16:00 UTC returning the noon ET candle
  - causal relevance: reduces timezone/contract-mechanics ambiguity
  - type: direct for settlement interpretation
  - weight: high
- **Polymarket rules explicitly reference Binance BTC/USDT 1m candle close**
  - source: Polymarket market page
  - causal relevance: clarifies that only one price surface and one field matter
  - type: authoritative contract evidence
  - weight: high

## Evidence against the claim

- **The contract resolves on one future minute close, not current price**
  - source: Polymarket rules
  - causal relevance: path dependency is high; a late selloff could invalidate a currently comfortable buffer
  - type: direct rule risk
  - weight: high
- **Crypto can move >5-7% in less than a day on macro or market-structure shocks**
  - source: general asset-class behavior; partly visible in intraday realized ranges though not fully evidenced here
  - causal relevance: shows the threshold is not mathematically locked in
  - type: contextual
  - weight: medium
- **Single-venue dependence on Binance BTC/USDT**
  - source: contract wording
  - causal relevance: exchange-specific dislocation or operational issues could matter even if broader BTC markets stay firm
  - type: direct operational-risk consideration
  - weight: medium

## Ambiguous or mixed evidence

- Coingecko cross-check matched the broad spot level, which is useful sanity confirmation but not important to settlement because non-Binance venues do not count.

## Conflict between inputs

There is no major factual conflict. The main disagreement is weighting-based: whether the remaining 24-hour downside/timing risk deserves more discount than the market currently prices.

## Key assumptions

- No major downside shock pushes Binance BTC/USDT below 70k at the settlement minute.
- Binance remains a usable and coherent source-of-truth surface.
- ET/UTC mapping used in the market wording is interpreted straightforwardly as 12:00 ET = 16:00 UTC on April 15.

## Key uncertainties

- Final price path over the next ~24 hours.
- Exchange-specific operational noise or price dislocations.
- Whether volatility rises materially into settlement.

## Disconfirming signals to watch

- BTC falls toward 72k or below before settlement.
- Sudden Binance-specific divergence from other major BTC/USD or BTC/USDT venues.
- Confusion or inconsistency in how the relevant candle is displayed/finalized.

## What would increase confidence

- BTC remains comfortably above 73k-74k into the morning of April 15.
- No operational issues on Binance and continued cross-venue price coherence.
- Another direct check closer to settlement confirms a large remaining cushion.

## Net update logic

The direct source-of-truth and contract checks confirm that the market direction is likely right. The risk-manager discount comes from the fact that the event is not settled yet and depends on one narrow minute-close on one venue. That makes 97.9% feel slightly too confident even though Yes remains the clear base case.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review