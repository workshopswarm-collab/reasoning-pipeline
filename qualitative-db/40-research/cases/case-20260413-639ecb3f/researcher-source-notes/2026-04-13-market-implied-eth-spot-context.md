---
type: source_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260413-639ecb3f | market-implied
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-13
source_name: Binance / Kraken / CryptoCompare ETH spot snapshots
source_type: exchange and market-data API snapshots
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-639ecb3f/researcher-analyses/2026-04-13/dispatch-case-20260413-639ecb3f-20260413T225424Z/personas/market-implied.md]
tags: [binance, kraken, cryptocompare, spot-price, eth]
---

# Summary

Independent spot snapshots show ETH trading around $2,356-$2,365 at research time, leaving the contract target roughly 1.5%-1.9% above spot. Kraken's 24h high print at $2,364.74 also indicates the market was already close to the threshold.

## Key facts extracted

- Binance ETHUSDT spot snapshot returned $2,362.46.
- Kraken XETHZUSD last trade returned about $2,364.74, with 24h high also $2,364.74 and open around $2,191.74.
- CryptoCompare returned ETH at $2,356.33.
- Across these sources, ETH is consistently in the mid-$2,300s.

## Evidence directly stated by source

- Current trade/quote levels were all below $2,400 at snapshot time.
- The gap from spot to target is around $35-$45, or under 2%.
- Recent intraday range already spans well over $100 on Kraken, implying meaningful short-horizon volatility.

## What is uncertain

- These are point-in-time snapshots rather than a full realized-volatility study.
- Kraken and CryptoCompare do not settle the contract; Binance does.
- A snapshot near $2,360 does not guarantee a wick to $2,400, especially if risk sentiment reverses quickly.

## Why this source may matter

The contract is a hit-level market over the rest of the week, so current distance-to-barrier matters a lot. When the barrier is less than 2% away, a high market-implied probability can be mechanically justified even without a strong directional thesis beyond ordinary crypto volatility.

## Possible impact on the question

This contextual evidence supports the market's 76% Yes pricing as broadly plausible. It suggests traders are not asking for a major regime shift, only a modest continuation or brief upside wick sometime during the remaining window.

## Reliability notes

These are timely and useful contextual data points. They are reasonably independent across venues, though all are ultimately observing the same global ETH market. They improve confidence in distance-to-target but are not a full volatility model.