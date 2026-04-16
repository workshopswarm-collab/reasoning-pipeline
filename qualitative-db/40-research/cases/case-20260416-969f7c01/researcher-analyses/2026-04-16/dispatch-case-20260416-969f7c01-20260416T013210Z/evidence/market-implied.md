---
type: evidence_map
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
research_run_id: 27948bd5-60af-48f1-a914-06657c345a9c
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-market-microstructure
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: "Will the price of Ethereum be above $2,200 on April 17?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
status: active
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["market-implied-finding", "later-synthesis"]
tags: ["evidence-map", "crypto", "contract-interpretation"]
---

# Summary

The evidence mostly supports the market's high-Yes stance. The only serious path to No is a relatively sharp downside move or exchange-specific settlement-minute issue before noon ET on Apr 17.

## Question being evaluated

Will Binance ETH/USDT's 12:00 ET 1-minute candle on Apr 17 have a final close above 2200?

## Current lean

Yes, with high but not near-certain probability.

## Prior / starting view

Start from the market prior of 94.5% because the market is liquid enough and the threshold is not close to spot.

## Evidence supporting the claim

- Binance direct price check around 2352.5-2352.6.
  - Direct.
  - Highest weight.
  - Matters because the contract settles on Binance ETH/USDT itself.
- Binance 24h low at 2308.5.
  - Direct/contextual hybrid.
  - High weight.
  - Matters because even recent downside stayed above the threshold.
- Polymarket strike ladder coherence: 2200 ~95%, 2300 ~71%, 2400 ~30%.
  - Direct for market view, indirect for truth.
  - Medium-high weight.
  - Matters because it suggests a sensible implied distribution rather than random overbidding.
- Secondary public price references also showing ETH in the low 2300s.
  - Contextual.
  - Low-medium weight.
  - Matters only as cross-check against a bad single print.

## Evidence against the claim

- Crypto can move >6% in less than a day, so the current cushion is meaningful but not decisive.
  - Indirect/contextual.
  - Highest disconfirming weight.
- The contract is venue-specific and minute-specific.
  - Direct contract-risk consideration.
  - Medium weight.
  - Even if broader ETH remains firm, a Binance-specific wick or noon-minute weakness could matter.

## Ambiguous or mixed evidence

- Secondary price pages were less directly extractable than desired, so their evidentiary value is limited.
- Public exchange UI wording references the website chart, while the research used Binance public API for verification; these should align in normal conditions but the UI is the literal stated source.

## Conflict between inputs

No material factual conflict. The main issue is weighting tail-risk versus present-state evidence.

## Key assumptions

- Current Binance price is a good anchor for tomorrow noon probability.
- Normal overnight volatility is more likely than an outsized downside shock.
- Binance API and UI are directionally consistent representations of the same market.

## Key uncertainties

- Overnight macro/crypto shock risk.
- Exact settlement-minute path dependence.
- Small residual ambiguity around UI-vs-API source representation, though both reference Binance ETH/USDT.

## Disconfirming signals to watch

- ETH losing the 2300 area overnight.
- Binance-specific negative spread to other spot references.
- Exchange operational anomalies near noon ET.

## What would increase confidence

- ETH remaining above roughly 2280-2300 into the morning of Apr 17.
- Another direct Binance check closer to settlement still comfortably above 2200.

## Net update logic

The market prior was already strong. Direct Binance evidence and the recent 24h range support that prior rather than undermine it. I downweighted pure price-page snippets and kept most weight on the contract-relevant venue plus the strike-ladder consistency check.

## Suggested downstream use

Use as a synthesis input supporting a high-Yes base case while preserving one clear caution: this is still a minute-specific, venue-specific crypto price event, so extreme confidence should be discounted modestly.