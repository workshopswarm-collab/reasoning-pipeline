---
type: source_note
case_key: case-20260406-6e955d27
dispatch_id: dispatch-case-20260406-6e955d27-20260408T153555Z
analysis_date: 2026-04-08
persona: risk-manager
domain: crypto
subdomain: prediction-market-resolution
entity: btc
topic: case-20260406-6e955d27 | risk-manager
question: Will the Binance BTC/USDT 1-minute candle for 2026-04-06 12:00 ET close above 66000?
driver: reliability
date_created: 2026-04-08
source_name: Polymarket market description as supplied in runtime assignment
source_type: market_rule_text
source_url: https://polymarket.com/event/bitcoin-above-on-april-6
source_date: 2026-04-08
credibility: medium-high
recency: current-contract-context
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [market-rules, resolution-criteria, candle-logic, contextual-evidence]
---

# Summary

This source note captures the contract mechanics quoted in the runtime assignment for how the market resolves.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for `12:00` in ET on the specified date has a final close above the listed threshold.
- The source of truth is Binance BTC/USDT with `1m` and `Candles` selected.
- The market explicitly says this is about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the number of decimal places in the source.

## Evidence directly stated by source

The assignment reproduces the market description and identifies both the timing rule and the governing resolution surface.

## What is uncertain

- The quoted text references the Binance website interface rather than the Binance REST API.
- The phrase `12:00 in the ET timezone (noon)` must be mapped to the 16:00 UTC kline for that calendar date.

## Why this source may matter

It defines the contract mechanics and therefore determines which candle matters and what data source counts.

## Possible impact on the question

This source narrows the analysis to a mechanical resolution check: identify the correct ET-noon BTCUSDT 1-minute candle on Binance and compare its final close to 66000.

## Reliability notes

- High relevance because it states the contract mechanics.
- Moderate independence because it comes through the runtime assignment rather than a separately fetched archived rules page.
- Main residual risk is source-surface specificity (UI candle vs API candle) rather than wording ambiguity.
