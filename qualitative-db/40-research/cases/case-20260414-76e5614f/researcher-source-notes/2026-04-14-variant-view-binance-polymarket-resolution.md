---
type: source_note
case_key: case-20260414-76e5614f
dispatch_id: dispatch-case-20260414-76e5614f-20260414T182607Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page + Binance spot API
source_type: primary_market_rule_and_resolution_source
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-76e5614f/researcher-analyses/2026-04-14/dispatch-case-20260414-76e5614f-20260414T182607Z/personas/variant-view.md]
tags: [polymarket, binance, resolution-source, btc]
---

# Summary

The market resolves on a narrow and operationally specific condition: the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 17 must have a final close strictly greater than 72,000. This is not a generic BTC price market; exchange venue, pair, timestamp, and one-minute close all matter.

## Key facts extracted

- Polymarket's rule text says the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on April 17 has a final close price higher than 72,000.
- The source-of-truth venue is Binance BTC/USDT, not another exchange or index.
- Price precision is determined by the source.
- The live market snapshot on the event page showed the 72,000 line trading around 84 cents Yes / 19 cents No at fetch time.
- Binance spot API at fetch time showed BTCUSDT around 74,603.24, already materially above the strike with roughly three days remaining.

## Evidence directly stated by source

- Rule wording explicitly defines the contract as a single one-minute candle close at noon ET.
- The event page identifies Binance as the resolution source.
- Binance API provides a contemporaneous spot price snapshot for BTCUSDT.

## What is uncertain

- The decisive value is not today's spot snapshot but the exact noon ET April 17 one-minute close.
- Short-horizon crypto volatility could still move BTC below 72,000 by the relevant minute.
- There is some minor operational ambiguity around how Binance UI timestamps correspond to ET display versus backend candle timing, though Polymarket's rule text substantially reduces that ambiguity.

## Why this source may matter

This is the governing source of truth and directly defines the contract mechanics. Because the market is date-sensitive and multi-condition, operational details are first-order rather than incidental.

## Possible impact on the question

This source makes the variant angle clear: even with BTC currently above 72k, the real risk is not broad directional thesis alone but short-horizon path dependence into one exact minute on one venue. That operational narrowness supports some discount versus a naive "BTC is above 72k now, so Yes should be near certain" framing.

## Reliability notes

Polymarket is authoritative for contract wording; Binance is authoritative for the referenced market price series. Together they are high-value primary sources, though a final settlement check would still need the actual April 17 noon ET candle once available.
