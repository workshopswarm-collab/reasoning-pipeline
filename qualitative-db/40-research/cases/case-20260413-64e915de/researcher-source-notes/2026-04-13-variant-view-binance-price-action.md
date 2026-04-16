---
type: source_note
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260413-64e915de | variant-view
question: Will Ethereum reach $2,400 April 13-19?
driver: liquidity
date_created: 2026-04-13
source_name: Binance ETHUSDT API price action
source_type: exchange market data
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1d&limit=14
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [liquidity]
upstream_inputs: []
downstream_uses: []
tags: [crypto, ethereum, price-action, exchange-data, verification]
---

# Summary

Binance daily ETHUSDT candles show ETH accelerating into the April 13 window but still not yet touching $2,400 on the verified April 13 daily high available during this run.

## Key facts extracted

- Binance daily data for 2026-04-13 shows high = 2394.71, low = 2175.68, close-so-far / last daily close field = 2373.39 in the returned candle snapshot.
- The separate 24-hour ticker endpoint during this run showed lastPrice = 2373.25 and highPrice = 2394.71.
- ETH therefore came within roughly $5.29 of the threshold without crossing it in this verified pass.
- The last 24-hour move was strong (+8.415%), which supports the bullish consensus but also shows how much of the move may already have been consumed before the threshold printed.

## Evidence directly stated by source

- Daily candle highs/lows/close values from Binance REST API.
- 24-hour ticker values including last price, high, and percent change.

## What is uncertain

- Binance is not necessarily the market’s governing source of truth for Polymarket resolution.
- A later move during the April 13-19 window could still trade through $2,400 even if it had not yet done so at this snapshot.
- Exchange-specific highs can vary slightly across venues.

## Why this source may matter

This is the cleanest directly observed market-data source available in-run for checking whether ETH is already effectively at the threshold versus still needing another marginal push.

## Possible impact on the question

The source supports a high probability that $2,400 is reachable within the week because ETH is already within about 1.1% of the threshold. But it also supports the variant view that the market may be mildly overconfident: a near-miss is not the same as a print, and the remaining move still has to happen within the resolution window.

## Reliability notes

Binance API market data is high-credibility for real-time crypto price context, but it is contextual rather than necessarily the authoritative resolution source for this exact contract.