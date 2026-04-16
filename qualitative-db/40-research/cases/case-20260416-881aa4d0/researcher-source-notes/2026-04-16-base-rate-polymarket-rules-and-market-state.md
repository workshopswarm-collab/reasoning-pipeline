---
type: source_note
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 70000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and rules
source_type: market/rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
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
downstream_uses: [qualitative-db/40-research/cases/case-20260416-881aa4d0/researcher-analyses/2026-04-16/dispatch-case-20260416-881aa4d0-20260416T044756Z/personas/base-rate.md]
tags: [polymarket, rules, resolution, source-note]
---

# Summary

This source establishes the market-implied probability and the contract mechanics. It shows the April 17 $70,000 bracket trading around 99.0%, and states that settlement depends on the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 17, 2026, specifically the final Close price being higher than 70,000.

## Key facts extracted

- The market title is "Bitcoin above ___ on April 17?" with a specific $70,000 outcome.
- The displayed market-implied probability for "70,000" was about 99.0% at fetch time.
- The rules state the market resolves Yes if the Binance BTC/USDT 12:00 ET 1-minute candle on the specified date has a final Close price above 70,000.
- The rules state the source of truth is Binance BTC/USDT, not another exchange or pair.
- The rules state price precision is determined by the number of decimal places shown by the source.

## Evidence directly stated by source

Directly stated by the page/rules:
- source of truth is Binance
- relevant instrument is BTC/USDT
- relevant interval is 1 minute
- relevant timestamp is 12:00 ET on Apr. 17, 2026
- operative test is whether the final Close is higher than 70,000

## What is uncertain

- The web page is a secondary display of live odds, not the settlement source itself.
- The page does not itself provide the future April 17 noon ET candle; it only specifies how settlement will be determined.
- The page wording leaves a small operational question about how Binance's UI timestamp maps to ET, so direct Binance data verification still matters.

## Why this source may matter

It is the governing contract surface for what counts. For this case, contract mechanics and timing precision matter because the market is date-specific and based on a single exchange's single minute close.

## Possible impact on the question

This source frames the whole task: even if BTC is above 70,000 on other venues or at nearby times, the contract only resolves Yes if the Binance BTC/USDT 12:00 ET 1-minute candle on Apr. 17 closes above 70,000.

## Reliability notes

Useful and necessary for contract interpretation, but not sufficient alone for the probability view because it is not the authoritative future price record. It should be paired with direct Binance market data or Binance API verification.