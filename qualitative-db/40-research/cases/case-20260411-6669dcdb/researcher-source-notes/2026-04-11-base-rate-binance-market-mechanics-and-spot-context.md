---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-10
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-11
question: Will the price of Bitcoin be above $72,000 on April 11?
driver: operational-risk
date_created: 2026-04-10
source_name: Binance BTCUSDT APIs (exchangeInfo, ticker/price, 24hr ticker, 1h klines)
source_type: exchange / market data API
source_url: https://api.binance.com/api/v3/exchangeInfo?symbol=BTCUSDT
source_date: 2026-04-10
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/base-rate.md]
tags: [binance, btcusdt, resolution-mechanics, market-data]
---

# Summary

Binance directly confirms that the relevant instrument is spot `BTCUSDT`, that the exchange timezone is UTC, and that BTC/USDT was trading around 72.87k at research time, modestly above the 72k threshold. Recent hourly candles show BTC moving both above and below 72k over the last two days, which supports a high-but-not-near-certain base-rate view for a binary threshold 15.5 hours ahead.

## Key facts extracted

- `exchangeInfo` for `BTCUSDT` shows the spot symbol is active (`status: TRADING`) with base asset `BTC` and quote asset `USDT`.
- Binance `exchangeInfo` reports exchange timezone `UTC`.
- Binance spot ticker at research time showed `BTCUSDT` around `72872.81`.
- Binance 24h ticker showed open `71883.51`, high `73434.00`, low `71426.15`, and last `72872.80`.
- Recent 1h klines over the prior ~48 hours include multiple closes below 72k and multiple closes above 72k; the market is not pinned safely above the threshold.

## Evidence directly stated by source

- Binance is publishing the exact symbol the contract references: `BTCUSDT`.
- The spot market was live and liquid.
- The last traded price was above 72k at the time of the run.
- The prior 24h range crossed both sides of the threshold.

## What is uncertain

- The contract resolves on the 12:00 ET one-minute candle close, not on the current spot price or hourly closes.
- The exact noon-ET minute close cannot be known in advance.
- Exchange API data confirms the symbol and venue mechanics, but not Polymarket’s post-processing conventions if a display discrepancy appears.

## Why this source may matter

This is the governing venue and symbol for settlement. It directly addresses the case-specific checks about exact pair identification and timing mechanics, and it provides the most relevant current price context.

## Possible impact on the question

Because BTCUSDT is currently above 72k but has still been crossing the threshold within recent trading ranges, the direct market-data evidence supports a Yes lean while arguing against treating the market as near-certain.

## Reliability notes

High reliability for venue, symbol, and current-price context because this is the primary exchange source. Lower reliability for the final market outcome because the decisive one-minute close has not occurred yet and short-horizon crypto prices remain noisy.
