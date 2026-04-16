---
type: source_note
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance BTC/USDT current spot and recent daily/4h context
question: How much cushion does BTC currently have versus 72,000 and what recent volatility context matters for a noon ET close on April 21?
driver: reliability
date_created: 2026-04-16
source_name: Binance public API ticker and kline endpoints
source_type: exchange market data / contextual source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/risk-manager.md
tags: [binance, btc, spot, klines, source-note]
---

# Summary

Binance public API data on April 16 showed BTC/USDT around 73,997.41, about 2.8% above the 72,000 threshold, while recent daily and 4-hour candles showed BTC has been trading in a broad enough range that a sub-72k noon close on April 21 is still plausible even though current spot favors Yes.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price: **73,997.41** on 2026-04-16.
- Recent daily candles from Binance public API:
  - Apr 11 close: **70,740.98**
  - Apr 12 close: **74,417.99**
  - Apr 13 high: **76,038.00**, close **74,131.55**
  - Apr 14 close: **74,809.99**
  - Apr 15 intraday / latest sampled candle showed low **73,309.85** and close field in returned sample **74,025.10**
- Recent 4-hour candles showed intraday swings from around **75,267.85** high down to **73,309.85** low in the sampled sequence.

## Evidence directly stated by source

- Direct Binance API responses supplied current BTCUSDT spot and recent kline OHLC values.
- The data show BTC is currently above the target threshold but with enough realized volatility that a single noon close several days later is path-dependent.

## What is uncertain

- Spot price now is not the settlement print; the contract resolves on the April 21 12:00 ET 1-minute close.
- The sampled daily candle set does not by itself prove where BTC will be at the resolution minute.
- Need care converting Binance API timestamps to ET when comparing sampled candles to the contract window.

## Why this source may matter

This is the strongest contextual source because the contract explicitly settles on Binance BTC/USDT. It gives direct evidence on current distance from threshold and recent volatility on the same venue/pair that governs resolution.

## Possible impact on the question

Current Binance pricing supports a Yes lean because BTC is already nearly 2,000 points above the line. But the same Binance context also highlights risk-manager caution: this is a **single-minute close** market with five calendar days left, so current cushion is real but not decisive.

## Reliability notes

High source quality for contemporaneous venue-matched pricing because the contract itself names Binance BTC/USDT. Independence versus the primary contract source is only medium because both depend on Binance surfaces, but they answer different questions: rules vs current state.