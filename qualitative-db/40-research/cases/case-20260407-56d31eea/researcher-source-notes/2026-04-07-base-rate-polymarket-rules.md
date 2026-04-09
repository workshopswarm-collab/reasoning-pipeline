---
type: source_note
case_key: case-20260407-56d31eea
dispatch_id: dispatch-case-20260407-56d31eea-20260407T023203Z
analysis_date: 2026-04-07
persona: base-rate
domain: crypto
subdomain: market-structure
entity: binance
topic: case-20260407-56d31eea | base-rate
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-07 close above 66000?
driver: operational-risk
date_created: 2026-04-06
source_name: Polymarket market rules page for bitcoin-above-on-april-7
source_type: market rules / contract surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-7
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [bitcoin, binance]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-56d31eea/researcher-analyses/2026-04-07/dispatch-case-20260407-56d31eea-20260407T023203Z/personas/base-rate.md]
tags: [polymarket, resolution-rules, source-of-truth]
---

# Summary

Polymarket's own rules page makes this a narrow, operationally clean settlement question. The market resolves from a single source: the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on the stated date, using the final Close price. No cross-exchange consensus is required.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-07 has a final Close price above 66,000.
- The specified resolution surface is Binance BTC/USDT with 1m candles selected.
- The rules explicitly say this is Binance BTC/USDT only, not other exchanges or trading pairs.
- Price precision is determined by the source display / source precision.

## Evidence directly stated by source

- The source-of-truth exchange is Binance.
- The metric is the final Close price of a 1-minute candle.
- The relevant time bucket is 12:00 in ET.
- The market does not depend on broader reporting, consensus pricing, or interpretive news coverage.

## What is uncertain

- The rules page does not itself explain Binance API mechanics or how Binance labels / indexes the 12:00 ET candle in programmatic endpoints.
- The rules page does not show the future value; it only defines the governing resolution logic.

## Why this source may matter

This is the contract-defining source for the case. It determines what counts, what does not count, and why external price references are only contextual unless they match Binance BTC/USDT.

## Possible impact on the question

Because the market is governed by a single exchange and a precise minute-close definition, the research burden shifts away from broad narrative research and toward verifying (1) what exact candle will count and (2) whether current Binance BTC/USDT trading is meaningfully above the 66,000 threshold with enough margin to make a reversal by noon ET unlikely.

## Reliability notes

High reliability for contract interpretation because it is the platform's own rules page. Lower value for price forecasting by itself because it does not provide historical or live evidence beyond the rules text.
