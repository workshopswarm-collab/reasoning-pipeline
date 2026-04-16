---
type: source_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: tokens
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Binance BTCUSDT 1-minute klines API threshold verification
source_type: primary_market_data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [binance, price-data, threshold-check, verification]
---

# Summary

This note records the direct additional verification pass against Binance 1-minute market data, which is the contract’s governing factual source. The fetched window contained at least one qualifying BTC/USDT 1-minute candle with a High above $76,000.

## Key facts extracted

- Binance 1-minute klines endpoint returned 1000 recent rows for `BTCUSDT`.
- The maximum observed `High` in the retrieved sample was **76038.0**.
- The row with that maximum high had open time **1776177120000 ms**, which converts to **2026-04-14 14:32:00 UTC**.
- That timestamp is **2026-04-14 10:32:00 ET**, which is inside the contract window running from Apr 13 00:00 ET through Apr 19 23:59 ET.

## Evidence directly stated by source

- The sampled Binance data directly shows a 1-minute candle high above the contract threshold.
- The qualifying print occurred inside the relevant weekly window.

## What is uncertain

- This verification used Binance’s public API rather than the exact web chart UI named in the rules, so there is still a small implementation-layer mismatch risk.
- The fetched sample covered recent minutes only, but that is sufficient here because it directly captured a qualifying in-window print.
- I did not independently archive the full raw payload outside this note.

## Why this source may matter

This is the most decision-relevant factual check for the contract because the rules name Binance BTC/USDT 1-minute highs as the settlement basis.

## Possible impact on the question

If the API sample matches the underlying Binance 1-minute highs used by the market rules, the contract’s terminal condition has already been satisfied and path risk for the rest of the week is no longer material.

## Reliability notes

High factual value because it is direct venue data from the named exchange and timeframe. Residual risk is mostly implementation consistency between Binance API data and the exact chart/high values the market operator uses for settlement.