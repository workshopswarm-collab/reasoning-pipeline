---
type: source_note
case_key: case-20260415-540d9abf
dispatch_id: dispatch-case-20260415-540d9abf-20260415T234706Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: solana
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle close on 2026-04-19 be above 80?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page plus Binance public price/klines API
source_type: primary_market_rules_and_exchange_data
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-540d9abf/researcher-analyses/2026-04-15/dispatch-case-20260415-540d9abf-20260415T234706Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, resolution, source-note, catalyst-hunter]
---

# Summary

This source note captures the governing contract mechanics from Polymarket and the direct exchange context from Binance public endpoints. Together they establish both the exact source of truth and the current distance of SOL/USDT above the $80 threshold several days before resolution.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance SOL/USDT 1 minute candle for 12:00 ET on April 19 has a final close above $80.
- The contract is specifically about Binance SOL/USDT, not other exchanges or other trading pairs.
- Price precision is determined by the number of decimal places in the source.
- Current Polymarket displayed market-implied probability for the $80 strike is about 90%.
- Binance public ticker showed SOLUSDT around 84.99 at the time of verification.
- Binance recent daily closes from April 11-15 were all above $80 except April 11 at 78.94, and several daily highs were in the mid-to-high 80s.
- Recent 1h and 4h Binance klines on April 15 showed SOL mostly trading in the 83-85.8 range.

## Evidence directly stated by source

From the Polymarket rules page:
- Yes if the Binance 1 minute candle for SOL/USDT at 12:00 ET on the specified date has a final close higher than the strike.
- Resolution source is Binance with 1m candles selected.
- Contract is Binance SOL/USDT specific.

From Binance public API outputs checked during this run:
- Ticker price: 84.99.
- Daily closes over the recent two weeks were generally above 80, indicating current spot is not hovering marginally above threshold but sitting several dollars above it.

## What is uncertain

- The contract resolves on a single exact one-minute close, so a sharp intraday crypto drawdown near April 19 noon ET could still flip the outcome.
- The visible Polymarket page reflects market pricing and rules, but not whether Binance may later revise candle presentation or have an outage; operational edge cases remain low-probability but real.
- This note does not establish any specific external macro or crypto-calendar catalyst for the next four days; it mainly establishes current buffer and mechanics.

## Why this source may matter

This is the central source pair for the case: Polymarket defines the rule and Binance defines the observed state that will matter for settlement. The market is narrow and timing-specific, so direct rule verification is essential.

## Possible impact on the question

The source strongly supports a high Yes probability because SOL is already materially above $80 with several days remaining, but it also makes clear that all conditions must hold simultaneously: Binance source, SOL/USDT pair, 1-minute candle, 12:00 ET timestamp, and close strictly above 80.

## Reliability notes

- Polymarket rules are the authoritative contract description for what counts.
- Binance is the named settlement source and therefore the governing market data source for the actual outcome.
- Evidence independence is moderate rather than high because the contract explicitly points to Binance, so the contextual and direct evidence are linked by design.