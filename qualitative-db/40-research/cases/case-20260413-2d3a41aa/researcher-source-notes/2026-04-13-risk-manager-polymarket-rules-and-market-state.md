---
type: source_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-13
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-13 close above 70000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market page and rules
source_type: market-contract-page
source_url: https://polymarket.com/event/bitcoin-above-on-april-13
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/risk-manager.md]
tags: [polymarket, contract, resolution, bitcoin]
---

# Summary

This source provides the operative contract language and the contemporaneous market-implied probability for the 70,000 threshold.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-13 has a final Close price higher than 70,000.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- Precision is determined by Binance source decimals.
- The Polymarket page showed the 70,000 threshold trading around 94% Yes at fetch time.

## Evidence directly stated by source

- Resolution depends on one specific exchange, one specific pair, one specific candle interval, one specific minute, and the candle Close field.
- It is explicitly not about other exchanges or pairs.

## What is uncertain

- The fetched market page is not itself the authoritative settlement source; it describes the contract and displays a market snapshot.
- The page does not directly show the final noon ET Binance candle close for the resolving minute.

## Why this source may matter

It defines the exact condition that all must hold for Yes: Binance, BTC/USDT, 1-minute candle, the 12:00 ET minute on Apr 13, and a Close strictly greater than 70,000.

## Possible impact on the question

This sharply narrows the key risk from broad BTC direction to contract interpretation and exact timestamp risk. A broadly bullish BTC tape is insufficient if the specific noon ET 1-minute close dips below 70,000.

## Reliability notes

Useful and necessary for contract mechanics, but not sufficient alone for settlement because Polymarket is quoting Binance as the governing source of truth.