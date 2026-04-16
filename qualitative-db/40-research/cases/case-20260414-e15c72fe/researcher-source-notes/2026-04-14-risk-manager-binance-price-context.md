---
type: source_note
case_key: case-20260414-e15c72fe
dispatch_id: dispatch-case-20260414-e15c72fe-20260414T193100Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-e15c72fe | risk-manager
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance API BTCUSDT daily and 1m klines
source_type: exchange market data / primary contextual
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=30
source_date: 2026-04-14
credibility: high
recency: high
stance: supports yes
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, price-context, primary-source]
---

# Summary

Direct Binance market-data pulls show BTC/USDT trading materially above 70,000 on 2026-04-14, around 74.3k at the time checked. Recent daily candles also show BTC closing above 70,000 for each of the last seven completed trading days, though daily intraday ranges remain large enough that a sub-70k noon print is still plausible if downside volatility returns.

## Key facts extracted

- Binance ticker price at check time: 74,258.35 BTC/USDT.
- Recent 1-minute candles around the check time were clustered near 74.24k-74.27k.
- Last seven completed daily closes from Binance were all above 70,000.
- Recent daily high-low ranges were roughly 1.75% to 6.13%.
- 2026-04-12 daily low was 70,505.88, showing price has recently approached but not breached 70,000.

## Evidence directly stated by source

- Direct Binance API responses for BTCUSDT ticker price and kline OHLC values.
- Daily candles:
  - 2026-04-08 close 71,069.93
  - 2026-04-09 close 71,787.97
  - 2026-04-10 close 72,962.70
  - 2026-04-11 close 73,043.16
  - 2026-04-12 close 70,740.98
  - 2026-04-13 close 74,417.99
  - 2026-04-14 latest fetched daily candle close field around 74,258 at retrieval time

## What is uncertain

- The market resolves on the 12:00 ET one-minute candle on 2026-04-20, not on current spot or daily close.
- The latest daily candle for 2026-04-14 was still in progress at retrieval time.
- Current price being well above 70k does not eliminate path risk over the next six days.

## Why this source may matter

This is the governing exchange and pair named in the contract. While the source does not settle the market yet, it is the most relevant direct contextual price source because resolution depends specifically on Binance BTC/USDT.

## Possible impact on the question

This source supports a high probability of Yes because spot is currently about 6% above the threshold and recent completed daily closes have all remained above 70k. It also highlights the main risk-manager caveat: recent realized ranges are large enough that a downside move to or below 70k by the noon ET minute on April 20 is still feasible.

## Reliability notes

- High credibility for exchange-native price data.
- Good directness for contract relevance because the contract explicitly names Binance BTC/USDT.
- Limited as a forecasting source: it gives current and historical prices, not causal drivers for the next six days.
