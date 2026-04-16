---
type: source_note
case_key: case-20260414-d5888900
dispatch_id: dispatch-case-20260414-d5888900-20260414T143228Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-14 close above 70000?
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, resolution-source, market-implied-probability]
---

# Summary

This source provides the contract wording, the governing resolution source, and the live market-implied probability for the 70,000 threshold contract.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-14 has a final close above 70,000.
- The governing source of truth is Binance BTC/USDT with 1m candles.
- The market page showed the 70,000 line trading effectively at 100% Yes; assignment context recorded current_price 0.9995.
- Precision is determined by the source itself.

## Evidence directly stated by source

- Exact contract mechanics: Binance, BTC/USDT, 1-minute candle, 12:00 ET, final close, strictly higher than 70,000.
- The market is exchange-specific and pair-specific, so other exchanges and BTC/USD references are only contextual.

## What is uncertain

- The market page is not itself the settlement print; it points to Binance as the settlement source.
- The page snapshot can lag or round displayed percentages.

## Why this source may matter

This is the primary contract interpretation source. It defines the exact time window and source of truth, which are the key non-price risks in a narrow-resolution market.

## Possible impact on the question

It sharply narrows the question: the relevant event is not simply whether Bitcoin trades above 70,000 somewhere on April 14, but whether Binance BTC/USDT closes the noon ET 1-minute candle above 70,000.

## Reliability notes

Useful as the authoritative contract/rules source, but not the final settlement datapoint itself. It should be paired with direct Binance pricing data.