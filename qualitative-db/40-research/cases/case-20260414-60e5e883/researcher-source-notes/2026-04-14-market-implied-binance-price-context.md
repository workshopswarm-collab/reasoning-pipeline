---
type: source_note
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-60e5e883 | market-implied
question: Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 70000?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT spot ticker and recent klines
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [market-implied finding, evidence map]
tags: [binance, market-data, spot-price, recent-range]
---

# Summary

Binance is the contract's governing price source, and current Binance BTC/USDT data places BTC well above the 70k threshold with a recent trading range mostly in the 70k-76k area.

## Key facts extracted

- Binance ticker on 2026-04-14 showed **BTCUSDT = 74,293.57**.
- Recent daily closes from the fetched 10-day series were approximately: 69,034; 68,854; 71,924; 71,070; 71,788; 72,963; 73,043; 70,741; 74,418; and current around 74,294.
- The most recent ten-day low in the fetched daily data was about **66,612**, but that was several days earlier and price has since recovered.
- Recent daily highs in the fetched data reached up to about **76,038**.
- This means current price is about **$4.3k above** the resolution threshold, or roughly **6.1%** cushion over 70k.

## Evidence directly stated by source

- Exact Binance spot quote at time of fetch.
- Exact recent daily open/high/low/close values from Binance klines.

## What is uncertain

- These are current and recent data, not the actual 12:00 PM ET Apr 17 settlement candle.
- Short-horizon crypto volatility can still move BTC several percent in a few days.

## Why this source may matter

Because Binance is the stated resolution source, Binance spot and kline data are the highest-quality direct evidence for whether the market's 93% Yes probability is broadly sensible.

## Possible impact on the question

This source supports the market's bullish pricing: BTC is not hovering near 70k but trading materially above it, and the recent range suggests 70k is below the center of current price action. It does not eliminate timing risk or a sharp selloff scenario.

## Reliability notes

High relevance and high authority for this contract because the source is the same exchange named in the rules. The main limitation is horizon mismatch: current spot data must be projected three days forward to the specific noon ET close.
