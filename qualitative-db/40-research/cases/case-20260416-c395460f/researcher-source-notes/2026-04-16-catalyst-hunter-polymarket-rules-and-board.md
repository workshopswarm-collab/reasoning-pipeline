---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market contract / venue page
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/catalyst-hunter.md]
tags: [source-note, polymarket, contract-rules, resolution-source]
---

# Summary

This source establishes the market-implied probability and the exact resolution mechanics. It is the governing contract surface for what counts, especially the timing, exchange, pair, and candle-close requirements.

## Key facts extracted

- The $80 outcome on the Apr. 19 market was trading around 89% Yes on the fetched page.
- Resolution is based on the Binance SOL/USDT 1-minute candle for 12:00 in ET timezone on Apr. 19, 2026.
- The required value is the final candle "Close" price, not intraminute high/low and not another exchange.
- Price precision is determined by the source display.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for SOL/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... SOL/USDT... '1m' and 'Candles' selected."
- The live board displayed the 80 strike at roughly 89% Yes / 13% No at fetch time.

## What is uncertain

- The fetch is a web-rendered market page, not a directly authenticated API pull.
- The page does not itself provide a historical intraday SOL chart that can be audited from the fetch output.

## Why this source may matter

This is the source of truth for contract interpretation. For a narrow date/time market, timing and source-of-truth mechanics are as important as directional price opinion.

## Possible impact on the question

It sharply narrows the question: to resolve Yes, SOL must still be above 80 specifically on Binance SOL/USDT at exactly the noon ET 1-minute candle close on Apr. 19. A temporary spike above 80 elsewhere, or before noon ET, would not be enough.

## Reliability notes

Reliable for market wording and current displayed odds, but not fully independent on price fundamentals. Best paired with an independent spot-price context source and, ideally, direct Binance verification closer to resolution.