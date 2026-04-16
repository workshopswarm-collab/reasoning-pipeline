---
type: source_note
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 74000?
driver: operational-risk
date_created: 2026-04-15T20:46:00-04:00
source_name: Binance API BTCUSDT ticker and 1m klines
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: live
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, live-price, catalyst-window]
---

# Summary

Binance primary market data shows BTC/USDT trading around 74.76k on the evening before resolution, above the 74k strike but not by a huge margin. The 24h range spans 73.5k to 75.4k, which means the strike is inside recent realized trading range rather than clearly out of reach.

## Key facts extracted

- Binance BTCUSDT last price observed: 74758.88.
- Binance 24h high: 75425.00.
- Binance 24h low: 73514.00.
- Binance 24h weighted average price: 74276.63.
- Binance 5-minute average price endpoint returned 74784.33, corroborating spot context.
- Recent 1-minute klines were accessible via Binance API, confirming operational access to the governing source family.

## Evidence directly stated by source

- The market is currently above 74000 on Binance spot.
- The market has also traded materially below 74000 during the same 24h window.
- Binance API endpoints are live and returning coherent current data.

## What is uncertain

- This does not settle the Apr 17 12:00 ET candle, only the current setup.
- Intraday volatility between now and tomorrow noon ET remains large enough to cross the threshold either way.

## Why this source may matter

This is the primary source family named by the contract. It establishes the most relevant near-term catalyst framing: the key issue is not whether BTC can ever touch 74k, but whether it can remain above 74k precisely into the noon ET resolution minute.

## Possible impact on the question

Because spot is already above the strike, the path to Yes does not require a fresh breakout. The dominant catalyst becomes hold/maintenance into the noon ET print, with overnight macro/risk sentiment and intraday volatility as the main repricing channels.

## Reliability notes

High reliability for current market state because this is the governing exchange/source family. Residual risk comes from exact contract interpretation and the fact that current spot is only contextual until the specified minute candle prints.
