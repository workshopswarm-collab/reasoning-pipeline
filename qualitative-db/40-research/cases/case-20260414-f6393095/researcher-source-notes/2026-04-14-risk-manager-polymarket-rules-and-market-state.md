---
type: source_note
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity:
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 70000 on April 17, 2026?
driver: reliability
date_created: 2026-04-14
source_name: Polymarket event page and rules
source_type: market contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-implied-probability]
---

# Summary

This note captures the contract wording, governing source-of-truth mechanics, and current market price used as the baseline for comparison.

## Key facts extracted

- The event page listed the 70,000 strike outcome at about 93.9 cents Yes, implying roughly 93.9% market probability.
- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 17 has a final close strictly higher than 70,000.
- The contract is explicitly about Binance BTC/USDT, not other exchanges or other pairs.
- Price precision is determined by the source.

## Evidence directly stated by source

- The rules specify: `This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".`
- The page also specifies Binance BTC/USDT with 1m candles as the resolution source.
- The market board displayed the 70,000 line at `93%` / `Buy Yes 93.9¢`.

## What is uncertain

- The event page is a front-end surface and can lag or round values, so it is strong for contract wording and approximate market price but not a substitute for final exchange data.
- The page itself does not clarify every possible edge case around outages or later candle revisions, though it names the source of truth clearly.

## Why this source may matter

It defines the contract and the market-implied baseline probability that the research note must compare against.

## Possible impact on the question

The rule wording narrows the relevant question to one exact minute, one exact exchange, one exact pair, and a strict `>` threshold. That raises timing and operational-resolution risk relative to a looser "Bitcoin price on that day" interpretation.

## Reliability notes

High relevance because it is the contract page. Best used together with direct Binance price data and an extra contextual cross-check rather than alone.