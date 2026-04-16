---
type: source_note
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-18
question: Will the price of Bitcoin be above $70,000 on April 18?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules for Bitcoin above ___ on April 18
source_type: market_contract
source_url: https://polymarket.com/event/bitcoin-above-on-april-18
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/risk-manager.md]
tags: [source-note, polymarket, market-rules, resolution]
---

# Summary

This source note captures the contract mechanics and visible market pricing for the April 18 BTC-above ladder market, with emphasis on what must be true for the $70,000 line to resolve Yes.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone on April 18 has a final Close price strictly higher than 70,000.
- The specified governing source of truth is Binance BTC/USDT with 1m candles selected.
- The market is specifically about Binance BTC/USDT, not other exchanges or other pairs.
- Price precision is determined by the number of decimal places in the Binance source.
- Visible market pricing on fetch showed the 70,000 contract around 90% Yes.

## Evidence directly stated by source

- Contract wording is explicit that all of the following matter: exchange = Binance, pair = BTC/USDT, timeframe = 1 minute candle, timestamp = 12:00 ET on April 18, metric = final Close, threshold test = higher than 70,000.
- The page presents the April 18 ladder and shows the 70,000 rung around 90% Yes at capture time.

## What is uncertain

- The public page fetch is not a direct API export, so displayed market price should be treated as a snapshot rather than a full audited tick history.
- The page text does not independently verify how Binance labels the 12:00 ET candle internally relative to UTC, though the contract wording itself is clear enough to identify the relevant noon ET minute.

## Why this source may matter

This is the governing contract and market-implied baseline. It defines the exact resolution mechanics and shows the crowd's current confidence level.

## Possible impact on the question

This source makes clear that broad claims like “BTC is above 70k this week” are insufficient. The thesis only pays if Binance BTC/USDT remains above 70,000 specifically at the April 18 noon ET 1-minute close.

## Reliability notes

Good for contract interpretation and baseline market pricing, but not sufficient alone for the actual probability estimate because it is also the object being analyzed. Independent price context is still needed.