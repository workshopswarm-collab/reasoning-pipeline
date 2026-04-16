---
type: source_note
case_key: case-20260415-6c8d8ca4
dispatch_id: dispatch-case-20260415-6c8d8ca4-20260415T084705Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance public market data API (BTCUSDT ticker and klines)
source_type: exchange market data / primary
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6c8d8ca4/researcher-analyses/2026-04-15/dispatch-case-20260415-6c8d8ca4-20260415T084705Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, price-action, resolution-source, source-note]
---

# Summary

Binance public BTC/USDT data is the governing market data source for this contract and also provides the clearest direct evidence about current distance from the $72,000 threshold and near-term realized volatility.

## Key facts extracted

- Spot ticker during this run showed BTCUSDT at `74040.86`.
- That is about `2.83%` above the `72000` strike.
- Recent daily closes from Binance API:
  - 2026-04-10 close `73043.16`
  - 2026-04-11 close `70740.98`
  - 2026-04-12 close `74417.99`
  - 2026-04-13 close `74131.55`
  - partial 2026-04-14/15 session during run around `74040.86`
- Recent hourly action showed BTC trading mostly in the `73.5k-74.8k` area during the latest Asia/Europe/US crossover hours, with no immediate break back under `72k`.
- Recent one-minute candles around the observation time were clustered near `74040-74125`, indicating the market is not sitting near the threshold right now.

## Evidence directly stated by source

- Exact current BTC/USDT spot price on Binance.
- Exact historical daily/hourly/minute OHLC values from Binance.
- Direct observation that recent traded prices remain comfortably above the resolution threshold.

## What is uncertain

- The contract resolves on the 12:00 ET one-minute candle close on April 17, not on the current spot price.
- Binance API access here does not by itself say what macro or flow catalysts may move BTC between now and resolution.
- Short-term crypto volatility can still erase a 2-4% cushion within hours.

## Why this source may matter

This is both a primary evidentiary source and the governing settlement source family. Any thesis about the market must respect the exact Binance BTC/USDT price path and the noon ET timing window.

## Possible impact on the question

Because BTC is currently several percent above the strike and has recently traded in the mid-74k area, the market begins from a favorable state for “Yes.” The main remaining risk is a sharp downside catalyst or intraday drawdown before the specific noon ET close on April 17.

## Reliability notes

High reliability for direct price observation and contract mechanics because Binance BTC/USDT is the specified resolution source. Reliability is lower for forward-looking interpretation, which requires contextual sources beyond raw exchange data.
