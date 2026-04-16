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
source_name: Binance ETHUSDT kline data with CoinGecko contextual cross-check
source_type: exchange market data + contextual aggregator
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=200
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/market-implied.md]
tags: [binance, ethusdt, klines, coingecko, verification]
---

# Summary

This note records the verification pass on market data after checking the Polymarket rules.

## Key facts extracted

- Binance 1h kline data for ETHUSDT shows a **high of 2415.50** at the candle opened **2026-04-14T14:00:00Z**.
- That timestamp is within the Polymarket contract window for April 13-19.
- A 1h candle high above 2400 does not by itself prove the exact 1m candle high, but it strongly implies at least one 1m candle inside that hour also traded at or above 2400 because hourly highs are aggregated from intrahour trades.
- CoinGecko 7-day hourly context showed ETH recently peaking at about **2392.12** on its own aggregated series, below Binance's venue-specific print and below the threshold.

## Evidence directly stated by source

- Binance API output included a row with high `2415.50000000` at `2026-04-14T14:00:00Z`.
- CoinGecko market chart context showed a 7-day max around `2392.1227513286062` and last around `2330.077874540196` at fetch time.

## What is uncertain

- The Binance check performed here used 1h candles, not the exact 1m candles named by the contract.
- However, since the contract asks whether **any** 1m candle high reached or exceeded 2400, an hourly high above 2400 is strong practical evidence that the minute-level condition was met.
- CoinGecko is not the settlement source and may smooth or aggregate across venues, so its lower contextual high should not override Binance.

## Why this source may matter

This is the key verification artifact that tests whether the market's extreme price is justified by venue-specific data rather than generic ETH price context.

## Possible impact on the question

Very high impact. If Binance printed above 2400 inside the relevant date range, the threshold market's Yes side is effectively already satisfied, making a very high market-implied probability rational.

## Reliability notes

- Binance is the named settlement source, so exchange data tied to Binance deserves primary weight.
- This note uses 1h klines for speed and auditability, which is slightly less exact than direct 1m candle extraction but directionally very strong because the threshold was exceeded by a meaningful margin.
- CoinGecko serves only as an independent contextual check and highlights that multi-venue contextual data may understate or differ from the governing venue-specific print.