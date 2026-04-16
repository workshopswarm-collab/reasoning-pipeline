---
type: source_note
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: case-20260414-91430615 | variant-view
question: Will the price of Bitcoin be above $70,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket rules page plus Binance BTCUSDT spot endpoints
source_type: primary market rules + primary exchange market data
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [bitcoin, btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-91430615/researcher-analyses/2026-04-14/dispatch-case-20260414-91430615-20260414T235247Z/personas/variant-view.md]
tags: [polymarket, binance, btc, resolution, source-note]
---

# Summary

This source note combines the governing contract wording from Polymarket with direct Binance BTC/USDT spot data needed to assess whether the market's 90% pricing for the $70,000 threshold looks overstretched or reasonable.

## Key facts extracted

- The market resolves from the Binance BTC/USDT **1 minute candle for 12:00 ET (noon) on April 19, 2026**, using the final **Close** price, not an intraday high/low and not another exchange or pair.
- The Polymarket page showed the `$70,000` line trading around **90% / 91c Yes** at capture time.
- Binance spot API showed BTCUSDT around **74,065.09** at capture time on 2026-04-14.
- Recent Binance daily closes from the last 7 sessions in the fetched series were approximately: **71,069.93, 71,787.97, 72,962.70, 73,043.16, 70,740.98, 74,417.99, 74,067.75**.
- In that 7-day sample BTC traded below 70,000 intraday on Binance **zero times**; the lowest low shown was **70,466.00** on one day and **70,505.88** on another.
- The market settles at **Sunday April 19 noon ET**, not daily close, so there is substantial remaining path dependence even if the spot level is currently well above 70k.

## Evidence directly stated by source

- Polymarket directly states the governing source of truth and the exact resolution condition.
- Binance directly states current spot price and recent OHLCV history for BTCUSDT.

## What is uncertain

- Binance daily candles are UTC-based and not the exact settlement minute; they are contextual, not settlement-direct.
- The fetched data does not by itself show how volatile BTC may be between now and Sunday noon ET.
- There remains exchange-specific operational or print-risk around the exact settlement minute, although no direct evidence of such disruption was found in this pass.

## Why this source may matter

This is the core source set for the case because it establishes both the contract mechanics and the current gap between spot price and the threshold. The key variant question is whether the market is underpricing weekend path dependence and one-minute-settlement fragility, or whether the current cushion above 70k is large enough that 90% is still justified.

## Possible impact on the question

The source set pushes toward a Yes lean because BTC is currently about 5.8% above the threshold and recent Binance trading has stayed above 70k. But it also supports a modest variant discount to the market because resolution depends on a **single minute close at a specific ET timestamp on Binance**, which is a narrower condition than a broad statement like "BTC will still be around 70k+ this week."

## Reliability notes

- Polymarket rules page is the authoritative contract wording for interpretation here.
- Binance spot endpoints are highly relevant because Binance is the named resolution source.
- The daily-kline context is strong but indirect for settlement because the market settles on one ET-minute, not a UTC daily close.