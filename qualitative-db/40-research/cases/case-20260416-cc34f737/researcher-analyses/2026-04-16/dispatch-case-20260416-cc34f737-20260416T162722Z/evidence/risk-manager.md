---
type: evidence_map
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
research_run_id: 2ab956ac-aa55-4814-84b3-9c7d49c475b1
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-market-timing
entity: ethereum
topic: will-the-binance-eth-usdt-1-minute-candle-for-12-00-et-on-2026-04-17-close-above-2300
question: "Will the Binance ETH/USDT 1 minute candle for 12:00 ET on 2026-04-17 close above 2300?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-cc34f737/researcher-analyses/2026-04-16/dispatch-case-20260416-cc34f737-20260416T162722Z/personas/risk-manager.md"]
tags: ["evidence-map", "timing-risk", "contract-interpretation"]
---

# Summary

The evidence nets to a modest Yes lean, but with meaningful path-risk because settlement depends on one exact Binance one-minute candle close rather than broad daily price direction.

## Question being evaluated

Will Binance ETH/USDT close strictly above 2300 on the 12:00 ET one-minute candle on 2026-04-17?

## Current lean

Lean Yes, but with lower confidence than a simple current-price-above-threshold reading would imply.

## Prior / starting view

Starting baseline was the market-implied 71-72% Yes.

## Evidence supporting the claim

- Polymarket rules establish a clean operational test rather than a complex interpretive one. This reduces fundamental ambiguity. Direct; high weight.
- Binance spot data during analysis showed ETHUSDT around 2332, so the market is currently above threshold by about 32 dollars. Direct contextual evidence; high weight.
- CoinGecko cross-check showed ETH around 2335 at nearly the same time, which supports that Binance was not showing an obviously idiosyncratic outlier print. Contextual; medium weight.
- Less than one day remains. Because price is already above threshold, Yes only requires maintaining the cushion rather than achieving a fresh breakout. Interpretive; medium weight.

## Evidence against the claim

- Binance 24h low was about 2285, which is below threshold and demonstrates that a move through 2300 is fully plausible on this horizon. Direct contextual evidence; high weight.
- Settlement is based on the exact close of one one-minute candle at noon ET, not on average price, intraday high, or broader daily close. A brief downdraft at the wrong moment is enough to lose. Direct contract/timing evidence; high weight.
- The threshold is only about 1.4% below the observed Binance spot price during analysis, which is small relative to ordinary crypto intraday movement. Contextual; medium-high weight.

## Ambiguous or mixed evidence

- Current price being above 2300 is supportive, but the cushion is not large enough to remove short-horizon volatility risk.
- External ETH/USD references broadly align with Binance, but the contract resolves on Binance ETH/USDT specifically, so non-Binance references are only partial reassurance.

## Conflict between inputs

There is no major factual conflict. The main disagreement is weighting-based: whether the current cushion deserves more emphasis than the settlement-window fragility.

## Key assumptions

- Binance spot conditions remain representative enough that current above-threshold pricing has predictive value for the noon ET close.
- No exchange-specific operational anomaly materially distorts the governing candle.
- Overnight/intraday volatility does not erase the current cushion at the specific settlement minute.

## Key uncertainties

- Short-horizon ETH volatility into the U.S. morning on April 17.
- Whether 2300 acts as a magnet/support or gets retested and lost.
- Any Binance-specific microstructure or temporary divergence around the settlement minute.

## Disconfirming signals to watch

- ETHUSDT trading persistently below 2310 or repeatedly probing 2300 before noon ET.
- A sharp downward momentum move into late morning ET.
- Binance-specific weakness versus other ETH/USD reference feeds.

## What would increase confidence

- ETHUSDT holding comfortably above 2330 into the U.S. morning.
- A widening cushion above 2300 with reduced realized intraday volatility.
- Additional confirmation that Binance UI candles and public API values align cleanly for settlement purposes.

## Net update logic

I stayed near the market but marked confidence down slightly. The clean source of truth and current above-threshold price support Yes, but the narrow one-minute settlement condition and demonstrated recent range below 2300 mean the market may be embedding slightly too much confidence for such a short-horizon crypto threshold.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- decision-maker review