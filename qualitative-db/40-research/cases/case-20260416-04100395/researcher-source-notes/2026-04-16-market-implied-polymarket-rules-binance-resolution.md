---
type: source_note
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: prediction-markets
entity: ethereum
topic: case-20260416-04100395 | market-implied
question: Will the price of Ethereum be above $2,300 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules for ethereum-above-2300-on-april-17
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/market-implied.md]
tags: [polymarket, rules, binance, resolution]
---

# Summary

The market’s governing logic is narrow and mechanical: resolution depends on the Binance ETH/USDT 1-minute candle labeled 12:00 ET on April 17, 2026, and specifically whether that candle’s final Close is higher than 2300. This sharply limits what evidence matters and makes timing/source interpretation central.

## Key facts extracted

- The market resolves Yes if the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 has a final Close above 2300.
- The market resolves No otherwise.
- The resolution source is Binance, not another exchange or spot composite.
- The specified interface is Binance ETH/USDT with 1m candles selected.
- Price precision is determined by the number of decimals in the source.

## Evidence directly stated by source

- Polymarket explicitly states the market is about Binance ETH/USDT, not other exchanges or trading pairs.
- Polymarket explicitly states the relevant observation is the 12:00 ET candle and its final Close.
- The visible price on the market page for the 2300 threshold was around 64-65%, consistent with the assignment snapshot current_price of 0.725 being directionally Yes-favored but somewhat stale versus the fetched page.

## What is uncertain

- The public Polymarket page may lag the assignment snapshot or reflect intraday movement; it should not replace the assignment’s current_price for the formal market-implied baseline in this run.
- Binance’s website candle labeling conventions could create user confusion, but the plain-language rule still points to the 12:00 ET one-minute candle close.

## Why this source may matter

This is the governing source-of-truth for contract interpretation. For a date-sensitive, multi-condition market, correct resolution mechanics matter at least as much as directional price context.

## Possible impact on the question

Because the market is resolved by one specific minute close rather than a daily average or intraday high, the main analytical burden is whether ETH is likely to still be above 2300 exactly at noon ET tomorrow on Binance. Small intraday drift matters more than broad bullishness.

## Reliability notes

Primary source for contract interpretation. High reliability for resolution mechanics, but not sufficient alone for directional forecasting because it does not answer where ETH is likely to trade tomorrow.