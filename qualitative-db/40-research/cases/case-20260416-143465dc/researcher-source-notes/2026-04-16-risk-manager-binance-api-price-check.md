---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: markets
entity: sol
topic: solana-touch-90-april-13-19
question: Will Solana reach $90 April 13-19?
date_created: 2026-04-16
source_name: Binance API daily kline and 24h ticker check
source_type: exchange_market_data
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=10
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: orchestrator
related_entities: [sol]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/risk-manager.md]
tags: [source-note, binance, api, market-data, verification]
---

# Summary

This source provides direct exchange data from Binance, the governing resolution venue. It supports both the current-state check and the additional verification pass.

## Key facts extracted

- Binance daily SOL/USDT candles for the relevant week show highs of:
  - Apr 13: **87.67**
  - Apr 14: **85.83**
  - Apr 15: **89.15**
- The Binance 24h ticker at fetch time showed:
  - last price **88.84**
  - 24h high **89.15**
  - 24h low **83.80**
- No checked Binance data point in this pass showed a price at or above **90.00**.

## Evidence directly stated by source

- Daily kline output includes date-bucket OHLC values directly from Binance's public API.
- The 24h ticker output includes a highPrice field of **89.15000000**.

## What is uncertain

- Daily candles cannot prove that an intraday 1-minute high never exceeded the daily high, but they do strongly constrain it because any 1-minute high above 90 would necessarily imply a daily high above 90.
- This check does not yet cover the remaining days through April 19, so it cannot settle the final market outcome.

## Why this source may matter

Because the contract explicitly names Binance SOL/USDT 1m highs as the source of truth, Binance API data is the most operationally relevant verification surface available in this run.

## Possible impact on the question

As of the verification pass on April 16, the market has **not** already effectively resolved Yes from the checked Binance highs. The remaining question is whether SOL can add roughly another 1%+ from an observed 89.15 high before the deadline.

## Reliability notes

High reliability. This is direct exchange data from the named source of truth. Independence versus the Polymarket contract text is medium rather than high because both concern the same venue, but one is rule text and the other is actual market data, so together they are sufficient and materially complementary.