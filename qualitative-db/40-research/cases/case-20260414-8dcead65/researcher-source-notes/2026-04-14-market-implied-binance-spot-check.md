---
type: source_note
case_key: case-20260414-8dcead65
dispatch_id: dispatch-case-20260414-8dcead65-20260414T160342Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the price of Bitcoin be above $70,000 on April 15?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance BTCUSDT API spot check and 1m klines
source_type: exchange_api
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=20
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, 1m-candle, direct-source]
---

# Summary

Direct check of Binance public API surfaces relevant to the market's source of truth. The latest BTC/USDT spot price at check time was 75483.31000000 and recent 1-minute candles were all comfortably above 70,000.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price 75483.31000000.
- Binance server time endpoint returned 2026-04-14T16:06:56.008000+00:00.
- Recent 1-minute klines show closes in the roughly 75.4k range, including final observed closes: 75439.68000000, 75468.62000000, 75469.03000000, 75458.63000000, 75483.31000000.
- Resolution mechanics in the Polymarket rules point to Binance BTC/USDT 1-minute candle close at 12:00 ET on 2026-04-15.

## Evidence directly stated by source

- Direct exchange-reported BTCUSDT spot price is above the 70,000 strike by more than 5,400 at check time.
- Direct exchange-reported 1-minute close data are far above the threshold.

## What is uncertain

- The contract resolves on the specific 12:00 ET candle on 2026-04-15, not on the current spot price.
- A large downside move before the deadline remains possible in principle.
- Public API access today does not itself guarantee Binance UI availability or unchanged market rules tomorrow.

## Why this source may matter

This is the governing underlying exchange surface named in the contract. It directly measures whether BTC/USDT is currently trading near or far from the 70,000 threshold and helps assess whether the market-implied 97.9% probability is directionally reasonable.

## Possible impact on the question

Because BTC is currently trading around 75.4k on Binance, the market only fails if BTC falls more than 7% before the noon ET resolution candle tomorrow. That makes a high Yes probability plausible absent new shock information or source-of-truth disruptions.

## Reliability notes

Binance is the stated resolution source, so for this contract it is authoritative for the underlying print. The main residual reliability issue is operational rather than informational: exact settlement depends on the final Binance 1-minute candle at the specified time window and timezone.
