---
type: source_note
case_key: case-20260416-63fb3082
dispatch_id: dispatch-case-20260416-63fb3082-20260416T145628Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-63fb3082 | base-rate
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-21 close above 68000?
driver: reliability
date_created: 2026-04-16
source_name: Binance BTC/USDT API market data and market rules reference
source_type: exchange data / primary market source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, primary-source, resolution-source]
---

# Summary

Binance is the governing resolution source for this market, and current Binance data show BTC/USDT trading well above the 68,000 threshold with a substantial recent cushion.

## Key facts extracted

- Binance ticker price on retrieval was about 73,921.27 USDT for BTC/USDT.
- Binance 5-minute average price on retrieval was about 73,957.51.
- Recent 1-minute candles around retrieval time were clustered around 73.87k-74.01k.
- Recent daily Binance closes for 2026-04-07 through 2026-04-16 were all above 68,000 except none in that span were below 70,740 after April 7; the 2026-04-16 intraday low shown in the daily kline was about 73,309.85.
- From the recent 15 daily rows reviewed, only 2026-04-02 to 2026-04-04 were below 68,000 on close; from 2026-04-05 onward all reviewed daily closes were above 68,000.

## Evidence directly stated by source

- The Binance API directly reports BTC/USDT prices and historical klines for the exact trading pair named in the contract.
- The Polymarket rules page names Binance BTC/USDT 1-minute candle close at 12:00 ET on April 21 as the settlement condition.

## What is uncertain

- This source does not itself settle the future April 21 noon ET candle.
- API data retrieved now do not guarantee Binance front-end display conventions, though they are highly likely to map to the same underlying exchange data.
- A large BTC drawdown over the next five days could still move price below 68,000 despite the current cushion.

## Why this source may matter

This is the closest thing to a primary source because the contract explicitly resolves on Binance BTC/USDT 1-minute candle close, not on a general BTC/USD reference.

## Possible impact on the question

Because BTC/USDT is currently roughly 5,900 above the threshold, the market only fails if BTC drops materially before the April 21 noon ET settlement minute. That makes the key base-rate question a short-horizon drawdown probability rather than long-run Bitcoin direction.

## Reliability notes

- High relevance: exact exchange and pair named in contract.
- High recency: live and recent historical data.
- Main limitation is not source quality but future uncertainty over a five-day window.
