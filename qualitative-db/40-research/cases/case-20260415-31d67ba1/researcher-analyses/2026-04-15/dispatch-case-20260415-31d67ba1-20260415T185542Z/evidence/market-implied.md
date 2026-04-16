---
type: evidence_map
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
research_run_id: e84a2f7d-e7f1-4cf0-9531-091866beda54
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-17
question: "Will the price of Bitcoin be above $70,000 on April 17?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-31d67ba1/researcher-analyses/2026-04-15/dispatch-case-20260415-31d67ba1-20260415T185542Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "settlement"]
---

# Summary

The current market price near 97% looks mostly justified by a large current spot cushion versus the threshold, but not fully risk-free because the contract settles on one exact Binance minute close.

## Question being evaluated

Whether the Binance BTC/USDT 12:00 ET 1-minute candle on Apr 17 will close strictly above 70,000.

## Current lean

Lean Yes, high probability.

## Prior / starting view

Starting from the market prior, the main task was to test whether ~97% was a reasonable summary of current information or too aggressive for a short-horizon BTC threshold market.

## Evidence supporting the claim

- Binance current ticker around 74,374.14.
  - Direct evidence.
  - High weight because Binance BTC/USDT is the named settlement venue and pair.
- Recent Binance 1-minute closes around 74.35k-74.37k.
  - Direct evidence for current microstructure near the relevant market.
  - Medium weight.
- Polymarket ladder coherence: 72k at ~87%, 74k at ~58%, 76k at ~21%.
  - Indirect evidence that the market is pricing a plausible short-horizon BTC distribution centered in the mid-74k area rather than randomly overpricing the 70k rung.
  - Medium weight.

## Evidence against the claim

- BTC can move several percent in under two days.
  - Indirect but important.
  - High weight because only one exact settlement minute matters.
- Contract uses exact Binance 12:00 ET 1-minute close, not average trading level.
  - Direct contract-mechanics risk.
  - High weight relative to ordinary “BTC is above 70k now” reasoning.
- Binance-specific print risk or exchange-specific divergence.
  - Indirect but contract-relevant.
  - Low-to-medium weight.

## Ambiguous or mixed evidence

- Cross-venue confirmation from CoinGecko roughly matches Binance spot, which supports the general level but does not settle the exact contract because only Binance counts.

## Conflict between inputs

No major factual conflict found. The tension is mostly weighting-based: how much short-horizon BTC volatility should discount the very large current cushion above 70k?

## Key assumptions

- Spot remains comfortably above 70k through settlement.
- No Binance-specific anomaly dominates the exact settlement minute.

## Key uncertainties

- Short-horizon BTC volatility over the next ~41 hours.
- Whether a sharp downside move clusters near noon ET on Apr 17.

## Disconfirming signals to watch

- BTC/USDT falling rapidly toward 71k or below before settlement.
- Exchange-specific instability on Binance.

## What would increase confidence

- Binance BTC/USDT still trading above ~73k on Apr 16 evening or Apr 17 morning.
- Continued cross-venue consistency without exchange-specific stress.

## Net update logic

The evidence mostly validated the market rather than overturning it. Current direct settlement-venue pricing provides the main support for a strong Yes lean, while exact-minute settlement mechanics are the main reason not to treat 97% as certainty.

## Suggested downstream use

Use as an input to orchestrator synthesis and to keep other researchers from overstating contrarian downside without stronger evidence.