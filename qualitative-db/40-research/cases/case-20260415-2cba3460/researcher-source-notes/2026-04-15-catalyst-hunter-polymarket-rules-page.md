---
type: source_note
case_key: case-20260415-2cba3460
dispatch_id: dispatch-case-20260415-2cba3460-20260415T115730Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market rules / contract description
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2cba3460/researcher-analyses/2026-04-15/dispatch-case-20260415-2cba3460-20260415T115730Z/personas/catalyst-hunter.md]
tags: [polymarket, contract-rules, source-of-truth, timezone]
---

# Summary

The Polymarket rules page explicitly states that this market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 16 has a final close above 72,000. This makes the case primarily a timing-and-threshold question, not a broader directional call on Bitcoin over the whole day or across exchanges.

## Key facts extracted

- Resolution depends on the Binance BTC/USDT pair only.
- The relevant observation is the 1-minute candle labeled 12:00 in ET timezone (noon ET) on April 16, 2026.
- The field that matters is the candle's final Close price.
- The condition is strictly higher than 72,000.
- Price precision is determined by the source display/underlying source decimals.

## Evidence directly stated by source

- "Yes" requires the specified Binance candle close to be higher than the threshold.
- Other exchanges or trading pairs do not count.
- The market-implied probability shown on the event page for 72,000 was about 89% during this run.

## What is uncertain

- The public page text does not independently explain whether the website candle timestamp aligns exactly with ET labeling versus UTC under the hood; that needs cross-checking from Binance data handling.
- The rules page alone does not tell us future price path risk.

## Why this source may matter

This is the contract-governing source for what counts. It defines the exact conditions that all must hold for a Yes resolution.

## Possible impact on the question

It narrows the relevant catalyst set to events capable of moving Binance BTC/USDT below 72k at one specific minute tomorrow, rather than any broader narrative catalyst.

## Reliability notes

High reliability for contract mechanics because it is the market operator's own rule text. It is not independent evidence on future price direction, so it should be paired with Binance market data.