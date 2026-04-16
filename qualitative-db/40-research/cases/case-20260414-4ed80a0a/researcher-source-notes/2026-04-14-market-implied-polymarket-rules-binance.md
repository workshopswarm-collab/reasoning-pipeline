---
type: source_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260414-4ed80a0a | market-implied
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-14
source_name: Polymarket market page rules text
source_type: market rules / primary contract source
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/market-implied.md]
tags: [polymarket, rules, binance, source-of-truth, threshold-market]
---

# Summary

This source note captures the governing contract language visible on the Polymarket event page for the April 13-19 ETH hit-price market.

## Key facts extracted

- The market resolves Yes if **any Binance 1-minute candle for ETH/USDT** during the title date range has a final **High** price equal to or greater than the threshold in the title.
- The specified date window is from **12:00 AM ET on the first date to 11:59 PM ET on the last date**.
- The market page says the **resolution source is Binance**, specifically ETH/USDT high prices on the Binance chart with **1m candles** selected.
- The page explicitly says prices from **other exchanges, different trading pairs, or spot markets will not be considered**.

## Evidence directly stated by source

Visible rule text on the page states, in substance:
- "This market will immediately resolve to Yes if any Binance 1-minute candle for ETH/USDT during the date range specified in the title ... has a final High price equal to or greater than the price specified in the title."
- "The resolution source for this market is Binance... with the chart settings on 1m candles selected."

## What is uncertain

- The page text visible through fetch/extraction does not itself provide the minute-by-minute historical candles; it only defines the governing source and rule.
- Because the page is rendered client-side, extraction can be noisy, so direct exchange-data verification is still useful.

## Why this source may matter

This is the main source-of-truth note for what counts. It prevents over-weighting prices from other vendors or using daily/high-level aggregators incorrectly.

## Possible impact on the question

High impact. For this threshold market, the key question is not ETH closing level or multi-exchange average; it is whether Binance ETH/USDT printed any qualifying intraperiod high during the named window.

## Reliability notes

Primary contract source for resolution mechanics. Strong for rules, but not sufficient alone to verify the historical qualifying print; exchange data still needs checking.