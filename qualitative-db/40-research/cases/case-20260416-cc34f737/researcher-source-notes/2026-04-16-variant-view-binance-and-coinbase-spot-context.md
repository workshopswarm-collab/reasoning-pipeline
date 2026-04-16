---
type: source_note
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: spot-market-context
entity: ethereum
topic: ethereum-above-2300-on-april-17
question: Will the price of Ethereum be above $2,300 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance API spot and 24h data plus Coinbase spot cross-check
source_type: exchange API / spot market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, coinbase, spot-price, cross-check, 24h-range]
---

# Summary

Direct spot checks showed ETH/USDT on Binance around 2332.76 and ETH-USD on Coinbase around 2333.99 at about 12:29 ET on April 16. Binance 24-hour data showed a range from 2285.10 to 2385.61. The key takeaway is that ETH was only modestly above the 2,300 threshold with one day left, making a Yes outcome plausible but less robust than a 71% market price suggests.

## Key facts extracted

- Binance ETHUSDT spot price check returned about 2332.76.
- Coinbase ETH-USD spot check returned about 2333.99.
- Binance 24-hour ticker showed high 2385.61 and low 2285.10.
- Binance 1-minute recent candles showed ETH moving around the low-to-mid 2330s and low 2340s during the review window.

## Evidence directly stated by source

- Binance direct API output gave the current ETHUSDT price and 24h high/low.
- Coinbase direct API output provided a secondary spot cross-check at a similar level.

## What is uncertain

- Current spot is not tomorrow's noon ET close.
- A 24-hour range does not cleanly translate into a probability for a single minute close tomorrow.
- Exchange-specific basis could widen or narrow before resolution.

## Why this source may matter

This is the most direct non-rule evidence for whether the threshold is comfortably in range or only marginally in range. It also helps test whether the market may be overconfident because the line is only about 1.4% below spot, while ETH has already traded below it within the last 24 hours.

## Possible impact on the question

The data supports a mild Yes lean but also supports a credible variant view against an overly confident Yes consensus: ETH is not far above the line, and recent realized volatility is large enough that a sub-2300 noon print remains very live.

## Reliability notes

High recency and strong directness from exchange APIs. Binance is especially important because it is also the settlement venue. Coinbase adds a useful but not fully independent cross-check because both reflect the same broad ETH spot market.