---
type: source_note
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT daily kline API check
source_type: exchange market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=20
source_date: 2026-04-14
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
downstream_uses: [base-rate-finding]
tags: [binance, btcusdt, price-history, verification]
---

# Summary

Direct Binance daily kline data shows BTC/USDT has closed above $70,000 on every day from Apr. 7 through Apr. 14, 2026, with recent closes mostly in the low-to-mid $70,000s and Apr. 14 trading reaching as high as 76,038 intraday.

## Key facts extracted

- Apr. 7 close: 71,924.22
- Apr. 8 close: 71,069.93
- Apr. 9 close: 71,787.97
- Apr. 10 close: 72,962.70
- Apr. 11 close: 73,043.16
- Apr. 12 close: 70,740.98
- Apr. 13 close: 74,417.99
- Apr. 14 close (latest available daily candle output at query time): about 74,084
- Recent daily lows since Apr. 7 include one touch near 70,466 on Apr. 9 and 70,506 on Apr. 12, still above 70,000.

## Evidence directly stated by source

- Binance data directly reports daily open, high, low, and close values for BTC/USDT.
- The recent trading regime has been consistently above the target threshold.

## What is uncertain

- Daily candles are not the same as the exact 12:00 ET one-minute close that resolves the market.
- Crypto volatility can produce a sub-$70,000 intraminute print even if recent daily closes are much higher, though current margin above threshold is substantial.

## Why this source may matter

This is the most relevant direct contextual source because the contract settles on Binance BTC/USDT itself. Even though interval mismatch remains, the same venue/pair evidence strongly informs the base-rate probability that noon ET on Apr. 17 will still be above 70,000.

## Possible impact on the question

Sustained trading several thousand dollars above the threshold materially supports a high Yes probability unless a sharp drawdown occurs in the next ~2.5 days.

## Reliability notes

High-quality direct venue data. Main limitation is interval mismatch versus the exact one-minute settlement candle.
