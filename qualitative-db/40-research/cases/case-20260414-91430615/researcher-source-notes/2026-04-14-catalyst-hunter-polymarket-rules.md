---
type: source_note
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-91430615 | catalyst-hunter
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 70000?
date_created: 2026-04-14
source_name: Polymarket market rules page
source_type: market rules / contract definition
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-91430615/researcher-analyses/2026-04-14/dispatch-case-20260414-91430615-20260414T235247Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, btc, binance]
---

# Summary

The market resolves Yes only if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 19 has a final close strictly higher than 70000. This is a narrow, source-specific, timezone-specific contract.

## Key facts extracted

- Resolution uses Binance, not other exchanges or BTC/USD indexes.
- The relevant market is BTC/USDT.
- The relevant interval is the 1-minute candle.
- The relevant timestamp is 12:00 in ET timezone on April 19, 2026.
- The condition is strictly higher than 70000, not equal to 70000.
- Price precision is whatever Binance shows in the source.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The rules page does not explain fallback procedure if Binance UI/API is temporarily unavailable at resolution time.
- The page does not independently prove timezone conversion details beyond stating ET; external verification of the actual calendar/time mapping remains helpful.

## Why this source may matter

This is the contract-definition surface, so it governs what counts. It narrows the relevant evidence to Binance BTC/USDT and makes noon ET timing critical.

## Possible impact on the question

This source does not itself favor Yes or No, but it sharply reduces ambiguity. It means broad bitcoin bullishness matters only insofar as it is likely to still be reflected in that exact Binance minute candle on April 19.

## Reliability notes

- High importance because it defines the contract.
- Slightly lower than exchange data as a factual price source, but authoritative for resolution wording.
- Needs pairing with Binance data for actual market-state analysis.