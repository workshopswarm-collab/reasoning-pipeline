---
type: source_note
case_key: case-20260415-75a50190
dispatch_id: dispatch-case-20260415-75a50190-20260415T205116Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: spot-price
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close be above 72000 on April 21, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot API and market rules
source_type: primary_market_data_and_resolution_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: base-rate
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, market-rules, spot-price, resolution]
---

# Summary

Binance is the governing source of truth for this contract, and direct Binance spot data already places BTC/USDT materially above 72,000 on 2026-04-15, giving the market a favorable starting point with six days remaining until resolution.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-21, using the final close for that minute.
- Binance spot ticker returned BTCUSDT price `74852.43` on 2026-04-15 during this research run.
- Binance 24h ticker returned last price about `74850.96`, 24h high `75281.00`, 24h low `73514.00`, and open `74181.39`.
- Binance recent daily klines show BTC/USDT daily closes around: 68,853.66; 71,924.22; 71,069.93; 71,787.97; 72,962.70; 73,043.16; then an intraperiod pullback to ~70,741 on the next listed day segment visible in the returned data.
- These recent observations imply BTC has already traded and closed above 72,000 on multiple nearby days, so the event does not require a fresh breakout from far below the strike.

## Evidence directly stated by source

- Binance ticker endpoints directly state the live BTCUSDT spot price and 24h range.
- Binance kline endpoint directly states recent daily open/high/low/close values.
- Polymarket rules directly state the governing settlement mechanism and exchange/pair/timeframe.

## What is uncertain

- This source does not settle the April 21 noon ET close yet; it only establishes current level and recent path.
- Daily closes are contextual rather than contract-identical because the market resolves on a one-minute noon ET candle, not a daily close.
- Intraday volatility over the next six days could still push BTC below 72,000 at the exact resolution minute.

## Why this source may matter

This is the most important source because it combines the contract’s governing exchange and pair with current market context. It anchors both contract interpretation and the outside-view question of how likely a six-day move below the strike is from the current level.

## Possible impact on the question

If BTC/USDT remains roughly in its recent range, the current cushion above 72,000 supports a high but not certain probability of Yes. The main residual risk is not contract ambiguity but ordinary crypto volatility at the exact resolution timestamp.

## Reliability notes

- High reliability for spot price and pair identification because Binance is the explicit source of truth in the contract.
- Medium reliability for translating current spot and recent daily closes into the exact April 21 noon ET one-minute close, because that requires a forecast over several days rather than direct settlement.
- Important operational caveat: the contract references the Binance web candle, so API values are highly relevant but still slightly indirect relative to the exact on-screen 1m candle specified in the rules.