---
type: source_note
case_key: case-20260415-e4a8d83c
dispatch_id: dispatch-case-20260415-e4a8d83c-20260415T230345Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the Binance BTC/USDT 12:00 PM ET 1-minute candle on 2026-04-17 close above 74000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / primary contract surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-e4a8d83c/researcher-analyses/2026-04-15/dispatch-case-20260415-e4a8d83c-20260415T230345Z/personas/catalyst-hunter.md]
tags: [market-rules, resolution-source, timing]
---

# Summary

This source defines the contract mechanics and the current market-implied baseline for the 74,000 line.

## Key facts extracted

- The market resolves from the Binance BTC/USDT **1-minute candle** for **12:00 PM ET** on **2026-04-17**.
- The relevant value is the candle's final **Close** price.
- "Yes" requires the close price to be **higher than 74,000**; equality does not qualify.
- The rules specify Binance BTC/USDT, not another exchange or pair.
- The Polymarket page showed the 74,000 contract trading around **72% Yes** at fetch time.

## Evidence directly stated by source

- Resolution source: Binance BTC/USDT chart with 1m candles selected.
- Timing condition: 12:00 in the ET timezone on the date in the title.
- Threshold condition: close price must be higher than the specified level.

## What is uncertain

- The page itself does not provide the future noon candle, only the rules and current implied pricing.
- The market page does not clarify whether daylight-saving changes could ever matter, so explicit ET interpretation remains part of timing verification.

## Why this source may matter

It is the governing source for how the contract settles, so it determines which catalysts actually matter: only developments that can affect Binance BTC/USDT into the noon ET close window on April 17 are decision-relevant.

## Possible impact on the question

Because the market is line-based and time-specific, the key catalyst is not a broad long-term Bitcoin thesis but whether BTC can remain above 74,000 precisely into the designated Binance minute close.

## Reliability notes

Primary contract surface and therefore authoritative for wording and settlement mechanics, but not itself an authoritative future price source.