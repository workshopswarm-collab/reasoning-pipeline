---
type: source_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260414-4ed80a0a | risk-manager
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-14
source_name: Polymarket event page / market rules for ETH April 13-19 ladder
source_type: market rules / primary resolution source summary
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-14
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/risk-manager.md]
tags: [polymarket, resolution-rules, binance, eth]
---

# Summary

Primary contract-interpretation note for the assigned market. The key point is that the market resolves off Binance ETH/USDT 1-minute candle highs, not off spot price on another venue and not off a closing price.

## Key facts extracted

- The relevant submarket is `Will Ethereum reach $2,400 April 13-19?`
- Resolution is immediate `Yes` if **any Binance 1-minute ETH/USDT candle** during Apr 13 12:00 AM ET through Apr 19 11:59 PM ET has a final **High** `>= 2400`.
- Otherwise the market resolves `No`.
- Polymarket states the resolution source is Binance ETH/USDT with the chart set to `1m` candles.
- Polymarket explicitly says prices from other exchanges, different trading pairs, or other spot references do **not** count.
- Current displayed outcome price for the $2,400 market was `1.0` Yes / `0.0` No when checked in page data on 2026-04-14.

## Evidence directly stated by source

- The event page embeds structured market data showing the exact threshold wording and outcome prices.
- The $2,400 line is one of a 14-market ladder, making contract wording and the governing venue especially important because adjacent lines are being priced simultaneously.

## What is uncertain

- The public page is a rendered market surface, not Binance itself; final settlement still depends on Binance market data availability/consistency.
- The page does not itself prove that a qualifying 1-minute high has already occurred; it only shows the rule and current market pricing.

## Why this source may matter

This is the governing source-of-truth description for contract interpretation. It determines what evidence counts and rules out weak shortcuts like using CoinGecko or a different exchange to settle the question.

## Possible impact on the question

This source sharply lowers source-of-truth ambiguity once paired with direct Binance price data. It also makes the market highly sensitive to intraperiod wick behavior: one qualifying 1-minute high is enough.

## Reliability notes

High reliability for contract wording because it is the market host’s own rule text. Moderate reliability for inference about whether the event already happened, since that still requires checking Binance data directly.