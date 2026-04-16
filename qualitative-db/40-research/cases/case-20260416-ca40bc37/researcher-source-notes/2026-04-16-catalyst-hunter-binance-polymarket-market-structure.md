---
type: source_note
case_key: case-20260416-ca40bc37
dispatch_id: dispatch-case-20260416-ca40bc37-20260416T053546Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 72000 on 2026-04-20?
driver: liquidity
date_created: 2026-04-16
source_name: Binance BTCUSDT API + Polymarket market page
source_type: primary_market_and_resolution_reference
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [liquidity, macro]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, source-note, catalyst]
---

# Summary

This source package establishes the governing resolution mechanics and the immediate market state. The Polymarket page says the contract resolves from the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20, specifically the final close price. Binance spot API showed BTCUSDT at 75,117.76 on 2026-04-16 during this run, while Binance daily klines for the prior 10 sessions showed BTC already trading above 72k on most recent days with closes of 72,962.70, 73,043.16, 74,417.99, 74,131.55, 74,809.99, and 75,117.76 across the latest upswing.

## Key facts extracted

- Governing source of truth is Binance BTC/USDT, not other exchanges or BTC-USD composites.
- Resolution depends on one specific 1-minute candle close at 12:00 ET on April 20.
- Polymarket current price for 72k was about 0.845-0.86 during capture, implying roughly 84.5%-86% yes.
- Binance spot during this run was 75,117.76, about 4.3% above the 72,000 threshold.
- Recent Binance daily closes show BTC recovered from ~70.7k on April 11 to ~75.1k on April 16.

## Evidence directly stated by source

- Polymarket rule text directly states the exact resolution source and timing.
- Binance API directly states current BTCUSDT spot and recent daily OHLC data.

## What is uncertain

- The API spot price is not itself the settlement print; the market settles off the exact 12:00 ET 1-minute candle on April 20.
- Daily candles do not reveal whether an intraday macro shock could push BTC below 72k at the relevant minute.

## Why this source may matter

This is the core direct evidence set. It defines the contract and shows BTC currently has several thousand dollars of cushion over the strike with a positive recent path into the decision window.

## Possible impact on the question

This package supports a high yes probability but not certainty. The main remaining question is whether a catalyst in the next four days can erase a ~3.1k margin by the exact noon ET minute on April 20.

## Reliability notes

High reliability for contract interpretation and current exchange reference pricing. Independence is limited because both the market and resolution mechanics point back to Binance/Polymarket; additional contextual sources are still needed for catalyst risk.
