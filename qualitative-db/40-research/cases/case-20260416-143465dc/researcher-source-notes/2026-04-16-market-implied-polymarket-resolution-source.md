---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: price-threshold-markets
entity: sol
topic: case-20260416-143465dc | market-implied
question: Will Solana reach $90 April 13-19?
date_created: 2026-04-16
source_name: Polymarket market page / contract wording
source_type: market-rule-page
source_url: https://polymarket.com/event/what-price-will-solana-hit-april-13-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [sol]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/market-implied.md]
tags: [polymarket, resolution-source, binance, touch-market]
---

# Summary

The Polymarket contract wording makes this a Binance-touch market, not a generic spot-price market. It resolves Yes if any Binance SOL/USDT 1-minute candle from 12:00 AM ET April 13 through 11:59 PM ET April 19 has a final High at or above 90.

## Key facts extracted

- The market resolves immediately to Yes if any Binance 1-minute candle for SOL/USDT in the date range has a final High greater than or equal to 90.
- The governing source of truth is Binance, specifically the SOL/USDT chart with 1m candles selected.
- Prices from other exchanges or other pairs do not count.

## Evidence directly stated by source

- "This market will immediately resolve to \"Yes\" if any Binance 1-minute candle for SOL/USDT during the date range specified in the title ... has a final \"High\" price equal to or greater than the price specified in the title."
- "The resolution source for this market is Binance, specifically the SOL/USDT \"High\" prices..."
- "Prices from other exchanges, different trading pairs, or spot markets will not be considered for the resolution of this market."

## What is uncertain

- The page excerpt itself does not provide a full historical table of qualifying highs, so a separate Binance verification pass is still required.
- Contract wording is clear, but practical verification depends on access to Binance candle data or chart rendering.

## Why this source may matter

This source defines what counts. For a narrow, date-specific touch market, this is the primary governing source and prevents using less relevant references such as Coinbase spot price or generic aggregate crypto prices.

## Possible impact on the question

Because only Binance SOL/USDT 1-minute highs count, a market participant could rationally price Yes above the current spot-vs-threshold gap if intraday wick behavior on Binance tends to overshoot visible spot references.

## Reliability notes

Primary contract source. High reliability for rules, low sufficiency for outcome by itself because it does not prove whether a qualifying 1-minute high has already occurred.