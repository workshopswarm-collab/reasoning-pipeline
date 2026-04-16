---
type: source_note
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260413-64e915de | market-implied
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-13
source_name: Live ETH price checks (CoinGecko API, Binance API, Coinbase API)
source_type: market data / exchange APIs
source_url: https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=7&interval=hourly
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260413-64e915de/researcher-analyses/2026-04-13/dispatch-case-20260413-64e915de-20260413T234340Z/personas/market-implied.md
tags: [price-data, coingecko, binance, coinbase, verification]
---

# Summary

Independent live price checks show ETH trading just below $2,400 during this run, which strongly supports the market's direction but not necessarily the market's extreme confidence.

## Key facts extracted

- CoinGecko hourly market-chart API returned a latest ETH/USD point around 2374.37 and a 7-day maximum around 2374.37.
- The same 7-day dataset showed no hourly observation at or above 2400 during the fetched window.
- Binance spot API returned ETHUSDT around 2373.39.
- Coinbase spot API returned ETH-USD around 2374.745.

## Evidence directly stated by source

- Multiple live market data endpoints place ETH within roughly 1.0% of $2,400.
- As of the verification pass, ETH had not yet crossed $2,400 in the sampled recent hourly CoinGecko data.

## What is uncertain

- CoinGecko hourly candles can miss an intra-hour wick above $2,400.
- Exact Polymarket source-of-truth methodology for the weekly high is not visible in the extracted rules text here, so whether an exchange-specific wick or broader reference print governs resolution should still be checked from the official rules surface if later needed.
- Crypto trades continuously, so a small move could settle the question quickly after this note.

## Why this source may matter

This is the strongest contextual evidence for why the market is so confident: ETH is already trading within about $25-$27 of the threshold with nearly a full week remaining.

## Possible impact on the question

The data materially support a high probability of a $2,400 touch before April 19, but because price is still below the threshold, they do not justify certainty by themselves.

## Reliability notes

Good recency and decent independence across data providers. Independence is not perfect because all feeds reference the same global crypto market, but cross-checking Binance and Coinbase materially reduces single-source error risk.