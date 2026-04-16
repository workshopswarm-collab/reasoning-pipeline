---
type: evidence_map
case_key: case-20260414-9f18b170
dispatch_id: dispatch-case-20260414-9f18b170-20260414T142057Z
research_run_id: 48794af2-125e-4bc3-afd4-78f6aa7af611
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-bitcoin-reach-76-000-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
driver: liquidity
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["liquidity", "macro"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-analyses/2026-04-14/dispatch-case-20260414-9f18b170-20260414T142057Z/personas/risk-manager.md"]
tags: ["evidence-map", "threshold-market", "verification", "fragility"]
---

# Summary

Net evidence supports a high-probability Yes view, but the residual risk is concentrated in settlement mechanics and short-horizon path dependence rather than broad directional disagreement.

## Question being evaluated

Will Binance BTC/USDT print any 1-minute candle High at or above $76,000 between 12:00 AM ET on Apr 13 and 11:59 PM ET on Apr 19?

## Current lean

Yes is likely, but not literally near-certain.

## Prior / starting view

Starting from the market baseline near 89%, the key question was whether that extreme confidence was overstating a venue-specific threshold crossing risk.

## Evidence supporting the claim

- Polymarket rules make the threshold easy to satisfy if touched even briefly: any qualifying 1-minute High is enough. Direct; high weight.
- Live market data on the Polymarket page showed the $76k leg trading around 91-92%, indicating informed traders already priced the threshold as very likely. Contextual; medium weight.
- Coinbase and Kraken both showed BTC around 75.76k at research time, meaning only a small additional move or wick is required. Contextual but independent enough for verification; high weight.
- The same weekly ladder showed lower upside thresholds already resolved Yes, confirming realized upward travel during the relevant window. Direct within the series; medium weight.

## Evidence against the claim

- Settlement is Binance-specific; other venues trading near or slightly above 76k do not guarantee a Binance qualifying print. Direct contract risk; high weight.
- Kraken high and Coinbase spot at the time checked were still fractionally below 76k, so the threshold had not obviously been overrun across all venues yet. Contextual; medium weight.
- Short-dated crypto threshold markets can fail on timing even when the broader thesis is right, especially if the move stalls just below the trigger. Contextual; medium weight.

## Ambiguous or mixed evidence

- CoinGecko’s aggregated data was slightly lower than Coinbase/Kraken; that cuts both ways because it may reflect averaging rather than venue truth.
- Market price near 90% can be informative, but it can also overstate confidence when traders compress a small remaining path risk.

## Conflict between inputs

There was no major factual conflict. The main difference was between broad-market spot context and the narrower Binance-specific settlement requirement.

## Key assumptions

- Binance BTC/USDT tracks closely enough with other major spot venues that a small remaining distance is likely to be crossed at least once.
- There is enough time left in the weekly window for a brief qualifying wick even if sustained trade above 76k does not occur immediately.

## Key uncertainties

- Exact Binance 1-minute highs after the latest check were not directly pulled from Binance in this run.
- Exchange-specific basis and microstructure may still matter at the margin.

## Disconfirming signals to watch

- Binance continues to trade below 76k while other venues briefly exceed it.
- BTC loses momentum and falls back materially away from the threshold.
- New volatility shock drives downside before any qualifying Binance print.

## What would increase confidence

- A direct Binance BTC/USDT 1-minute high print at or above 76,000.
- Additional independent venue checks showing spot clearly above 76k rather than just near it.

## Net update logic

The key update was that this is not a large directional leap from current spot; it is a small remaining threshold crossing under rules that count even a brief wick. That keeps the probability high, but the risk-manager haircut remains warranted because settlement is venue-specific.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why this run stayed slightly below the market rather than matching its extreme confidence exactly.