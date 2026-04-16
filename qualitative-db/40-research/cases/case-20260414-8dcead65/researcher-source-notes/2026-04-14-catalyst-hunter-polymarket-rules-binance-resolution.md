---
type: source_note
case_key: case-20260414-8dcead65
dispatch_id: dispatch-case-20260414-8dcead65-20260414T160342Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the price of Bitcoin be above $70,000 on April 15?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules for bitcoin-above-on-april-15
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8dcead65/researcher-analyses/2026-04-14/dispatch-case-20260414-8dcead65-20260414T160342Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, resolution-rules, timing]
---

# Summary

This source establishes the governing contract mechanics and source of truth for the market.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1 minute candle labeled 12:00 in ET on April 15 has a final Close strictly above 70,000.
- The source of truth is Binance BTC/USDT with 1m candles selected.
- The market is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is whatever Binance displays in the source candle.

## Evidence directly stated by source

The rules state that resolution uses the Binance 1 minute candle for BTC/USDT at 12:00 ET on the specified date, and that the final Close must be higher than the threshold.

## What is uncertain

- The page does not itself provide the future settling candle.
- The page does not add fallback logic if Binance UI/API behavior changes; that leaves some operational dependence on Binance availability and final displayed candle data.

## Why this source may matter

This is the direct governing source for contract interpretation. For a narrow date/time market, the exact candle timing, exchange, pair, and strict-greater-than condition are all material.

## Possible impact on the question

It means the analysis should focus less on broad BTC direction and more on whether Binance BTC/USDT can remain above 70,000 specifically through the noon ET minute on April 15.

## Reliability notes

High relevance and high authority for market mechanics, but it is not an independent market-price source. It defines what counts rather than proving the future outcome.