---
type: source_note
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-close-market
entity: btc
topic: Direct Binance BTC/USDT checks for live price and intraday 1-minute candles
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot API
source_type: exchange primary data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1440
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/variant-view.md
tags: [binance, primary-source, btcusdt, 1m-candles, noon-check]
---

# Summary

Direct Binance API checks show BTC/USDT trading materially above the 72,000 threshold on Apr 15, but the contract is keyed to a specific future minute: **Apr 17 at 12:00 ET**. The most relevant direct context from Binance is that the Apr 15 **12:00 ET** 1-minute candle closed at **73,792.01**, and spot at roughly 15:10 ET on Apr 15 was about **74,646.66**.

## Key facts extracted

- Binance ticker price check returned **74,646.66** for BTCUSDT during this run.
- Binance 1-minute kline history for the last 1440 minutes includes a row corresponding to **2026-04-15 12:00 ET**.
- That Apr 15 12:00 ET candle had:
  - open: **73,844.07**
  - high: **73,844.07**
  - low: **73,762.89**
  - close: **73,792.01**
- Over the retrieved last 24 hours of 1-minute candles, the approximate intraday range was:
  - low: **73,514.00**
  - high: **74,699.99**
  - range: about **1.61%**
- Over the last 240 one-minute closes in the sample, mean absolute 1-minute return was about **0.0466%**.

## Evidence directly stated by source

Direct Binance outputs captured during the run:
- ticker endpoint: `{"symbol":"BTCUSDT","price":"74646.66000000"}`
- kline row for Apr 15 12:00 ET / 16:00 UTC:
  - `[1776268800000, '73844.07000000', '73844.07000000', '73762.89000000', '73792.01000000', ...]`

## What is uncertain

- These direct checks do **not** settle the Apr 17 market; they only confirm the governing source mechanics and current/nearby context.
- The 1440-minute history covers the last day, not the future resolution minute.
- Short-horizon realized volatility is only a rough context signal and not a full predictive model.

## Why this source may matter

This is the governing source family itself: Binance BTC/USDT 1-minute candles. It directly verifies what the resolution surface looks like in machine-readable form and confirms that the threshold is currently above water by roughly 2.2k to 2.6k depending on the comparison point.

## Possible impact on the question

The direct Binance data supports the market’s bullish direction because BTC is already comfortably above 72k. But it also supports the variant caution that the contract still depends on one exact minute two days later, so a temporary drawdown into Apr 17 noon ET would still flip the contract to No.

## Reliability notes

- High credibility because this is direct exchange data from Binance, the named governing source family.
- Strong recency.
- Independent from Polymarket’s own displayed probability, though still within the same general market ecosystem.
- Good for mechanism verification and current-state context, but not sufficient alone to infer a precise probability for a future timestamp.