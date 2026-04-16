---
type: source_note
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: spot-price-resolution
entity: ethereum
topic: case-20260416-243d5bed | catalyst-hunter
question: Will the price of Ethereum be above $2,300 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance ETH/USDT API and Polymarket market rules
source_type: exchange API + market rules
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=1000
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, resolution-source, eth-usdt, timing]
---

# Summary

This source note combines the governing Polymarket resolution text with direct Binance ETH/USDT spot data checked on 2026-04-16. It is the core provenance for a date-sensitive price-above market whose answer depends on a single 1-minute Binance close at noon ET on 2026-04-17.

## Key facts extracted

- Polymarket rules say the market resolves based on the Binance ETH/USDT 1-minute candle labeled 12:00 in ET timezone on Apr 17, 2026, using the final Close price.
- The threshold is strictly higher than 2300; equal to 2300 would not be enough for Yes.
- Direct Binance API checks on 2026-04-16 showed:
  - ticker price around 2340.24 USDT for ETHUSDT
  - recent 1-minute closes mostly above 2300
  - last 1000 1-minute closes had minimum close 2288.02, maximum close 2368.04, mean close 2344.21
  - about 98.0% of those 1000 minutes closed above 2300
  - over the most recent 180 minutes, about 88.9% of closes were above 2300
- Recent hourly candles showed a same-day drawdown from the mid-2350s into the high-2280s before rebounding back above 2330, which demonstrates that sub-2300 prints remain possible even with spot currently above the strike.

## Evidence directly stated by source

- Binance API returned live ETHUSDT ticker and recent candles directly from the named resolution venue.
- Polymarket rules explicitly name Binance ETH/USDT 1-minute close at noon ET as the resolution source.

## What is uncertain

- The relevant settling minute has not occurred yet.
- Overnight macro or crypto-specific headlines could still move ETH enough to push the noon ET close below 2300.
- A venue-specific operational issue or unusual wick at the exact resolving minute could matter more than broader spot averages.

## Why this source may matter

This is the direct contract-mechanics source. It identifies both the governing venue and the exact timing condition, while the Binance candles show current distance from strike and short-horizon fragility.

## Possible impact on the question

The evidence supports Yes as the base case because ETH is currently above 2300 on the exact named venue, but it also shows the core catalyst-hunter caveat: the market is exposed to path risk into one exact minute, not just to average daily ETH strength.

## Reliability notes

- Reliability is high for contract interpretation because Polymarket rules explicitly state the venue and timing.
- Reliability is high for current price context because Binance API is a direct exchange source.
- Independence is limited because both pieces relate to the same core mechanism rather than two separate causal channels, so an independent contextual cross-check remains useful.