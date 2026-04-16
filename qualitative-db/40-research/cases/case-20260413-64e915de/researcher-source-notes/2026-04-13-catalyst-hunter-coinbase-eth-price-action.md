---
type: source_note
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: protocols
entity: ethereum
topic: near-term ETH price action versus $2,400 threshold
question: Will Ethereum reach $2,400 during April 13-19, 2026?
driver: liquidity
date_created: 2026-04-13
source_name: Coinbase Exchange ETH-USD ticker and candles API
source_type: exchange market data
source_url: https://api.exchange.coinbase.com/products/ETH-USD/ticker
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: [liquidity]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-64e915de/researcher-analyses/2026-04-13/dispatch-case-20260413-64e915de-20260413T234340Z/personas/catalyst-hunter.md]
tags: [source-note, crypto, ethereum, exchange-data, liquidity]
---

# Summary

Coinbase ETH-USD data shows ETH trading around $2,374 late on 2026-04-13 UTC after an intraday high of $2,395 on the daily candle, leaving the market only about 1.1% below the $2,400 threshold at assignment time. The recent daily series also shows a sharp rebound from sub-$2,100 levels earlier in April, so the question is less about whether ETH can trend higher over months and more about whether one additional burst of upside or exchange-specific wick can print during the Apr 13-19 resolution window.

## Key facts extracted

- Coinbase ticker at 2026-04-13T23:47:04Z showed ETH-USD price 2374.67 with ask 2374.59 and bid 2374.58.
- Daily Coinbase candle for 2026-04-13 so far showed open 2191.77, high 2395.00, low 2174.31, close/latest 2374.10, meaning ETH already came within $5 of the target on the first day of the window.
- Recent daily highs before assignment: Apr 12 high 2289.58, Apr 11 high 2330.56, Apr 10 high 2301.64, Apr 7 high 2272.86.
- Hourly candles on 2026-04-13 UTC showed a late-session acceleration from roughly 2233 at 19:00 UTC to 2375 at 23:00 UTC, indicating strong short-horizon momentum and the possibility of a wick extension.

## Evidence directly stated by source

- Spot exchange price and bid/ask at the time of query.
- Daily candle highs/lows/opens/closes for ETH-USD.
- Hourly candle sequence showing the strength and timing of the breakout.

## What is uncertain

- Coinbase is one exchange and may not be the settlement source for the Polymarket contract.
- API data does not itself explain what caused the move.
- The market could reverse before printing $2,400 on the governing resolution source even if Coinbase nearly touched or briefly exceeded it.

## Why this source may matter

This is the most direct evidence that the threshold is within immediate reach. For a date-bounded price-hit market, actual spot path and intraday highs matter more than longer-run valuation narratives.

## Possible impact on the question

This source materially raises the chance of a hit because ETH is already trading within a few tens of dollars of $2,400 and has demonstrated same-day ability to rally nearly to the threshold. It supports a view that near-term liquidity/momentum, rather than a specific scheduled protocol event, is the key catalyst path.

## Reliability notes

Coinbase API is primary market data for one major venue and highly reliable for its own prints. Reliability for contract resolution is medium-to-high but not complete until cross-checked against the market's stated source of truth.