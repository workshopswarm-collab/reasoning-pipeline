---
type: source_note
case_key: case-20260416-bbc8ed19
dispatch_id: dispatch-case-20260416-bbc8ed19-20260416T072336Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-bbc8ed19 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules page
source_type: market resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-bbc8ed19/researcher-analyses/2026-04-16/dispatch-case-20260416-bbc8ed19-20260416T072336Z/personas/risk-manager.md]
tags: [polymarket, market-rules, resolution, binance, timing]
---

# Summary

This source defines the contract mechanics for resolution and is the governing source for what counts.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 20 has a final Close price higher than 72,000.
- The resolution source is Binance BTC/USDT with 1m candles selected.
- The contract is about Binance BTC/USDT specifically, not other exchanges or other pairs.
- Price precision is determined by the number of decimals shown in the source.

## Evidence directly stated by source

The rules explicitly say the source of truth is Binance and the relevant datapoint is the final Close of the 12:00 ET one-minute candle on the specified date.

## What is uncertain

- The page itself does not spell out whether Binance’s chart display or API formatting is the practical fallback if the website UI is difficult to inspect at settlement time.
- The page does not discuss contingency handling if Binance has a temporary UI issue, though it does clearly name Binance as source of truth.

## Why this source may matter

This market is date-sensitive and mechanically narrow. The precise candle, timezone, pair, and close field all matter.

## Possible impact on the question

This sharply reduces interpretive ambiguity. The main remaining risk is not contract wording but price-path risk into a single one-minute settlement window.

## Reliability notes

High relevance and high authority for contract interpretation because it is the market’s own resolution rules page. Independence is low because it is the venue defining its own contract, but that is appropriate here.