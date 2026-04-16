---
type: source_note
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-f29db686 | market-implied
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance BTCUSDT ticker and 1m klines API
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: live
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/market-implied.md]
tags: [binance, btcusdt, primary-source, resolution-context]
---

# Summary

Binance live market data shows BTC/USDT already trading above the contract threshold, which is the strongest direct support for the market's >50% yes pricing. At capture time, the Binance ticker showed 74,792.45 and recent one-minute klines around the same area.

## Key facts extracted

- Binance BTCUSDT ticker returned `74,792.45000000`.
- Recent 1-minute klines included closes of `74,819.80`, `74,774.37`, `74,828.33`, `74,834.00`, and `74,792.45`.
- These observations put spot roughly 0.8% to 1.1% above the 74,000 threshold at time checked.
- Because the contract resolves on the Binance 12:00 ET one-minute candle close on Apr. 17, current Binance spot is directly relevant but not dispositive.

## Evidence directly stated by source

- Current Binance BTCUSDT spot was above 74,000 at capture time.
- Very recent 1-minute candle closes were also above 74,000.

## What is uncertain

- The source does not tell us where BTC/USDT will print at exactly 12:00 ET on Apr. 17.
- The public API is not literally the UI candle view named in the rule, though it is the same exchange/instrument family and should closely track the governing source.
- Short-horizon crypto volatility could still take price below 74,000 by the resolution minute.

## Why this source may matter

This is the most relevant direct evidence because the contract settles on Binance BTC/USDT, not on a broad crypto index or another exchange. If current Binance price were still below 74,000, a yes price above 60% would look hard to defend. Instead, current exchange data broadly supports the market's baseline.

## Possible impact on the question

Supports a modest yes lean because the market only needs BTCUSDT to remain above 74,000 at one specific minute tomorrow, and current exchange data starts from above-threshold territory.

## Reliability notes

- High relevance because instrument/exchange match the contract.
- Residual operational caveat: the rule points to the Binance UI candle view rather than the public API endpoint, so a final resolution check should still be treated as UI-governed if any discrepancy appears.
