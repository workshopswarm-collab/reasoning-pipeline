---
type: source_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: exchange-price
entity: btc
topic: case-20260414-669935fa | variant-view
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Binance BTCUSDT daily kline API
source_type: exchange API
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/variant-view.md]
tags: [source-note, binance, btc, exchange-data, verification]
---

# Summary

Binance daily BTCUSDT candles provide the key extra verification pass. The 2026-04-13 daily candle shows a high of $74,900, while the 2026-04-14 daily candle shows a high of $76,038, indicating that at least one major exchange printed above the $76,000 threshold during the relevant weekly window.

## Key facts extracted

- Binance 2026-04-13 daily candle high: $74,900.00.
- Binance 2026-04-14 daily candle high: $76,038.00.
- This means the $76,000 threshold was crossed on Binance by 2026-04-14.
- The market is for the April 13-19 weekly range, so an early-week threshold cross is highly material.

## Evidence directly stated by source

- API output explicitly includes OHLC values for each daily candle.
- The high field for the 2026-04-14 candle is 76038.00000000.

## What is uncertain

- Binance may or may not be the exact governing source for Polymarket resolution.
- The market title alone does not specify whether resolution uses any major exchange print, a named index, or a specific rules source.
- If Polymarket uses a different source with materially different weekly highs, that could matter, though for BTC at this scale major venue divergence is usually modest.

## Why this source may matter

This is the strongest direct verification found in the run because it shows an actual major-exchange print above the target level rather than only approaching it.

## Possible impact on the question

If Polymarket resolves on a standard high-price methodology using a major exchange or broad market composite, this source pushes the probability very near certainty. The remaining risk becomes almost entirely contract-source ambiguity rather than market-price uncertainty.

## Reliability notes

- High credibility as direct exchange market data.
- More direct than a news article or third-party commentary.
- Still not automatically the governing source of truth unless the contract rules explicitly point to Binance or a composite that necessarily includes comparable prints.