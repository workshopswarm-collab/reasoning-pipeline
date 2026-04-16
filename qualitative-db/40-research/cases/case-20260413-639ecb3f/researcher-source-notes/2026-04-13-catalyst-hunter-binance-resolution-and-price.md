---
type: source_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: protocols
entity: ethereum
topic: April 13-19 ETH $2,400 touch threshold
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-13
source_name: Polymarket rules page and Binance ETHUSDT 24h ticker
source_type: primary_market_rules_plus_exchange_data
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19 | https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [catalyst-hunter.md, catalyst-hunter.sidecar.json]
tags: [polymarket, binance, resolution, eth, threshold-market]
---

# Summary

The governing source of truth is explicit: the Polymarket page states this outcome resolves Yes if any Binance 1-minute ETH/USDT candle between 12:00 AM ET Apr 13 and 11:59 PM ET Apr 19 has a final High at or above the threshold. Binance 24h ticker data on Apr 13 already shows ETHUSDT trading in the mid-2350s with a 24h high above 2363, leaving roughly a 1.5%-2.0% move to hit 2400.

## Key facts extracted

- Polymarket HTML embeds the rule that the market resolves Yes if any Binance 1-minute ETH/USDT candle in the stated window has a final High equal to or greater than the target price.
- The rule also says resolution depends solely on Binance ETH/USDT, not other exchanges or pairs.
- Binance 24h ticker on capture showed:
  - lastPrice: 2354.20
  - highPrice: 2363.94
  - lowPrice: 2175.68
  - priceChangePercent: 7.155
- This means ETH was already trading within about 36 dollars of 2400 at the time of review, after a strong day.

## Evidence directly stated by source

- Direct rule text from Polymarket page: market resolves Yes if any Binance 1-minute ETH/USDT candle during the named date range has a final High at or above the target.
- Direct exchange data from Binance ticker: spot ETHUSDT 24h high reached 2363.94 and last traded near 2354.

## What is uncertain

- The Binance 24h ticker is not itself the settlement surface; the settlement surface is Binance 1-minute candle highs during the exact Apr 13-19 ET window.
- Short-horizon crypto prices can reverse sharply after momentum bursts.
- A near-miss run to 2390s would still resolve No for the 2400 line.

## Why this source may matter

It directly defines what counts for settlement and shows the market is close enough that a modest additional impulse could resolve the contract quickly.

## Possible impact on the question

This source raises confidence that the path to Yes does not require a regime shift; it requires only a relatively small further move on the governing venue. It also narrows interpretive ambiguity because the source-of-truth is Binance 1-minute highs, not generalized ETH price headlines.

## Reliability notes

High reliability for contract mechanics because the rules come from the market page itself. High reliability for spot context because Binance is the named exchange in the rules. Lower reliability for forecasting beyond the immediate snapshot because exchange ticker data is only a moment-in-time context input.