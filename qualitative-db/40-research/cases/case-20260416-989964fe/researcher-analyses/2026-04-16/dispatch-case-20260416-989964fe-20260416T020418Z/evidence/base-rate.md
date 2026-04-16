---
type: evidence_map
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
research_run_id: 5cae2cce-4164-48b7-94a8-799a5e7e95b2
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-market
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-200-on-april-17
question: "Will the price of Ethereum be above $2,200 on April 17?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/base-rate.md"]
tags: ["evidence-map", "base-rate", "crypto"]
---

# Summary

The net evidence supports Yes as the base-rate lean because current Binance ETH/USDT is already materially above 2200 and nearby realized closes are mostly above the threshold, but the extreme market price still deserves some discount for crypto volatility and minute-close settlement sensitivity.

## Question being evaluated

Will the Binance ETH/USDT 12:00 PM ET one-minute candle on April 17 close above 2200?

## Current lean

Lean Yes, high but not near-certain.

## Prior / starting view

Starting outside-view prior: when the underlying is already ~6-7% above the strike roughly a day before settlement, short-horizon continuation usually dominates unless there is a meaningful volatility shock.

## Evidence supporting the claim

- Binance API current price around 2355 on the named venue/pair. Direct contextual evidence. High weight.
- Recent one-minute klines clustered around the same level, suggesting the observed price was not a stale print. Direct contextual evidence. Medium weight.
- Nearby daily closes mostly above 2200 on the same exchange/pair. Indirect but relevant base-rate context. Medium weight.
- Polymarket ladder structure places 2200 at ~95% while 2300 is ~72%, implying the market also sees substantial buffer above the strike. Indirect contextual evidence. Low-to-medium weight.

## Evidence against the claim

- One nearby daily close around 2191.65 shows the threshold can be lost on normal crypto volatility. Indirect contextual evidence. Medium weight.
- Settlement is a single one-minute close at a precise time, so a transient dip at noon ET matters more than broader daily strength. Direct contract-interpretation risk. Medium weight.
- Binance-specific operational or pricing anomalies could matter because the contract names one exchange and pair. Direct operational-risk consideration. Low-to-medium weight.

## Ambiguous or mixed evidence

- Market price at 95% may be informative, but it can also overstate certainty in short-dated crypto threshold markets.
- Daily closes above 2200 are supportive but are not the same as noon ET minute closes.

## Conflict between inputs

No major factual conflict. The main disagreement is weighting-based: whether a ~6-7% spot buffer by itself justifies something as high as 95% for a volatile crypto asset.

## Key assumptions

- No major overnight or morning shock before settlement.
- Binance remains a reliable resolution venue with no unusual dislocation.
- Current price regime is a better guide than any single bearish headline.

## Key uncertainties

- Overnight crypto volatility.
- Venue-specific prints around the exact settlement minute.
- Any macro/crypto news before noon ET April 17.

## Disconfirming signals to watch

- ETHUSDT moving back near 2200 before the settlement window.
- Sudden broad crypto selloff.
- Exchange outage or obvious pricing anomaly on Binance.

## What would increase confidence

- A fresh Binance check on the morning of April 17 still showing ETH comfortably above 2200.
- Stable trading above ~2300 into the final hour.

## Net update logic

The base-rate started Yes because the asset is already well above the strike. Evidence did not overturn that. But because this is a single-minute close on a volatile asset, I downweight the market's near-certainty slightly rather than matching it exactly.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input; little additional research is needed unless price action materially changes before settlement.