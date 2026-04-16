---
type: source_note
case_key: case-20260415-10579f0a
dispatch_id: dispatch-case-20260415-10579f0a-20260415T184424Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-17 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / market pricing surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, pricing, resolution]
---

# Summary

The Polymarket market page provides the contract mechanics and live market pricing for the April 17 Bitcoin threshold ladder. For the 70,000 threshold, the page showed roughly 97.1% Yes at fetch time, consistent with the assignment's `current_price` of 0.965.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET (noon)** on **2026-04-17** has a final **Close** price strictly higher than 70,000.
- The page explicitly states the source is Binance BTC/USDT with `1m` and `Candles` selected.
- The page also states price precision is determined by the source.
- The same ladder page showed adjacent thresholds around the market state: 72,000 roughly 86% and 74,000 roughly 56%, which contextualizes where the market currently places spot relative to the distribution.

## Evidence directly stated by source

- Resolution depends on a specific Binance BTC/USDT 1-minute close, not other exchanges and not a daily close.
- The operative timestamp is noon in ET, which on the stated date is EDT and therefore maps to 16:00 UTC.
- 70,000 was trading near 97% Yes at the time captured.

## What is uncertain

- The webpage is a secondary display surface for live market prices and rules; the actual settling value still depends on the Binance candle that will exist on April 17.
- The page does not itself provide the future candle, only the settlement criteria.

## Why this source may matter

This is the governing contract/rules surface for the market. It defines the exact timestamp, exchange, pair, and price field that matter.

## Possible impact on the question

This source sharply narrows what can change the result: only a fast downside move that leaves the Binance BTC/USDT 12:00 ET one-minute candle close at or below 70,000 can flip the market to No.

## Reliability notes

Good for contract interpretation and live crowd pricing, but not itself authoritative for the final outcome beyond exposing the market's own stated rule set. The authoritative source-of-truth for settlement is the Binance BTC/USDT 1-minute candle referenced in the rules.