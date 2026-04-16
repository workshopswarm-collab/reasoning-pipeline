---
type: source_note
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-structure
entity: ethereum
topic: binance-ethusdt-resolution-source
question: Will the Binance ETH/USDT 1-minute candle at 12:00 ET on 2026-04-17 close above 2300?
driver: reliability
date_created: 2026-04-16
source_name: Binance spot API (ETHUSDT ticker and 1m klines)
source_type: exchange market data / resolution source proxy
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=60
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/catalyst-hunter.md]
tags: [binance, resolution-source, market-data, eth]
---

# Summary

Binance is the governing source of truth for this market, and the public spot API is a usable proxy for checking current ETH/USDT 1-minute candles and current spot price before final settlement.

## Key facts extracted

- The assignment states the market resolves from Binance ETH/USDT with the 1m candle at 12:00 ET on 2026-04-17.
- Binance API returned current ETHUSDT ticker price of 2339.97 at research time.
- Recent 1m klines showed ETH trading consistently above 2300 during the checked window.
- A larger intraday pull from Binance klines showed 1000 recent 1m closes with 980 closes above 2300, last close 2339.08, minimum close 2288.02, and maximum close 2368.04 during the retrieved sample.

## Evidence directly stated by source

- Binance ticker endpoint returned `{"symbol":"ETHUSDT","price":"2339.97000000"}`.
- Binance kline endpoint returned recent 1-minute OHLCV candles for ETHUSDT, including multiple consecutive closes between roughly 2333 and 2342 during the observed period.

## What is uncertain

- The API snapshots do not settle the contract because the relevant candle is specifically the 12:00 ET candle on 2026-04-17.
- The retrieved 1000-minute sample is less than a full 24 hours, so it is supportive context rather than a complete path analysis.

## Why this source may matter

This is the most important source because the contract explicitly resolves against Binance ETH/USDT 1-minute candle close data. It also shows that, at research time, ETH is already meaningfully above the 2300 threshold.

## Possible impact on the question

The source pushes the probability toward Yes because current ETH/USDT is ~40 points above the strike and recent minute-level trading has spent most observed time above 2300. It does not remove overnight/event risk.

## Reliability notes

High reliability for contract interpretation and live pricing because Binance is the named settlement source. The public API is a strong practical proxy for the exchange UI, though final settlement should still be treated as the Binance 1m candle visible at the actual resolution time.