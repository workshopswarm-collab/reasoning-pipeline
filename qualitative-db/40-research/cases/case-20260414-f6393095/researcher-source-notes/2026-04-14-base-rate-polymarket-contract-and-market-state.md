---
type: source_note
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract text
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [polymarket, contract, resolution, market-implied-probability]
---

# Summary

Polymarket lists the Apr. 17 BTC threshold ladder and shows the $70,000 line trading around 93.9% Yes on 2026-04-14. The contract text says the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 17 has a final Close above 70,000; otherwise No.

## Key facts extracted

- Market title: Bitcoin above ___ on April 17?
- $70,000 line displayed at about 93.9% Yes.
- Resolution source is Binance BTC/USDT.
- Exact settlement condition is the 1-minute candle for 12:00 ET on the specified date.
- Precision is determined by the source’s displayed decimal precision.

## Evidence directly stated by source

- The page explicitly states the governing source of truth is Binance.
- The page explicitly states this is about BTC/USDT on Binance, not other exchanges or pairs.
- The page explicitly states the relevant observation is the final Close of the 12:00 ET one-minute candle.

## What is uncertain

- The public market page is a secondary presentation of the rules; the ultimate operational data source is Binance at the relevant minute.
- Market price can move materially before resolution.

## Why this source may matter

This source defines both the market-implied probability baseline and the exact contract mechanics. For a date-specific BTC threshold market, those mechanics matter because one minute at noon ET controls resolution rather than a daily close or cross-exchange average.

## Possible impact on the question

It sets a high market prior for Yes and narrows the operational question to one precise Binance minute rather than general BTC strength.

## Reliability notes

Useful and necessary for contract interpretation, but not fully independent from trading sentiment and not itself the final settlement datapoint. Best paired with direct Binance pricing/history verification.
