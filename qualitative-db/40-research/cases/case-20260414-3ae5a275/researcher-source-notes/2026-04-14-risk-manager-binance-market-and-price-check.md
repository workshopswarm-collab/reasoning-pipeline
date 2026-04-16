---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance API and market specification surfaces
source_type: primary + direct market source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/risk-manager.md]
tags: [binance, resolution-source, btcusdt, timing-check]
---

# Summary

This source note captures the direct resolution mechanics and current price context for the Apr. 20 noon ET BTC > 70,000 market.

## Key facts extracted

- The market page states the governing source of truth is Binance BTC/USDT with the `1m` candle view and specifically the 12:00 ET candle close on the named date.
- The market resolves Yes only if that final Binance BTC/USDT 1-minute candle close is strictly higher than 70,000.
- A Binance spot ticker check on 2026-04-14 showed BTCUSDT at `74306.57`.
- Binance daily kline data for the preceding sessions showed BTC trading above 70,000 on most recent daily closes and reaching recent highs materially above that threshold.
- The same Polymarket surface showed the 70,000 line trading around 85-86%, which is the market-implied baseline used for comparison.

## Evidence directly stated by source

- Polymarket rules directly specify Binance BTC/USDT, 1-minute candle, 12:00 ET, and candle `Close` price as the settlement mechanism.
- Binance ticker directly states the spot BTCUSDT price at the time of fetch.
- Binance daily klines directly state recent open/high/low/close values, including recent closes above 70,000.

## What is uncertain

- The ticker price is not the settlement print; the market resolves on one specific 1-minute close at noon ET on Apr. 20.
- Daily klines are contextual rather than dispositive for a single minute six days forward.
- Exchange-specific operational issues, short-lived volatility, or a sharp drawdown could still push the noon print below 70,000 even if spot remains near or above that level most of the week.

## Why this source may matter

This is the core primary evidence set because it addresses both the governing settlement source and the current level relative to the threshold.

## Possible impact on the question

The direct evidence supports a high baseline probability because BTCUSDT is already above 70,000 by a meaningful margin, but it also clarifies the main fragility: only one exchange-specific minute close at one exact ET timestamp matters.

## Reliability notes

- Binance API is highly relevant because Binance is the named source of truth.
- The market page is authoritative for contract wording but is still distinct from the final Binance candle used for settlement.
- These sources are strong for mechanics and current state, but not sufficient to eliminate path risk between now and Apr. 20 noon ET.