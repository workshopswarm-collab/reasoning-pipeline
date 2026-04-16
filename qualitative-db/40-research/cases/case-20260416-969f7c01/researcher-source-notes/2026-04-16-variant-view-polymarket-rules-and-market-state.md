---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: prediction-markets
entity: ethereum
topic: case-20260416-969f7c01 | variant-view
question: Will the price of Ethereum be above $2,200 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for Ethereum above ___ on April 17
source_type: market rules / market state
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [variant-view finding, evidence map]
tags: [polymarket, rules, market-state, eth]
---

# Summary

This source establishes both the market-implied baseline and the contract mechanics. It shows the $2,200 strike trading around 95% Yes and states that resolution depends specifically on the Binance ETH/USDT 1-minute candle labeled 12:00 ET on April 17, using the final Close price and Binance price precision.

## Key facts extracted

- The relevant line is ETH above $2,200 on April 17.
- The observed market-implied probability on capture was about 95% Yes for the $2,200 line.
- The contract resolves Yes only if the Binance ETH/USDT 1-minute candle for 12:00 ET has a final Close strictly higher than 2200.
- The source of truth is Binance ETH/USDT, not other exchanges or ETH/USD pairs.
- Price precision is whatever Binance displays in the source candle data.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for ETH/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the ETH/USDT 'Close' prices currently available at https://www.binance.com/en/trade/ETH_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance ETH/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The market page itself does not provide a historical realized close for the resolution minute yet because the event has not occurred.
- The page does not quantify basis risk between current spot references and the exact future Binance resolution candle.

## Why this source may matter

This is the governing contract source. It defines the exact price series, timestamp convention, comparison operator, and market-implied benchmark that the finding must analyze.

## Possible impact on the question

It narrows the question from a generic ETH price call to a one-minute, exchange-specific, timezone-specific close test. That makes the main residual risk less about medium-term ETH direction and more about short-horizon execution noise, exchange-specific basis, and intraday volatility around the exact noon ET minute.

## Reliability notes

Primary for contract interpretation and market state, but not primary for the future realized settlement value itself until the actual candle exists.