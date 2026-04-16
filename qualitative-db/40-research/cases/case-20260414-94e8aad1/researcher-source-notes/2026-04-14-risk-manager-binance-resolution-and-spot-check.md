---
type: source_note
case_key: case-20260414-94e8aad1
dispatch_id: dispatch-case-20260414-94e8aad1-20260414T175223Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-94e8aad1 | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 16?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance BTCUSDT market data and Polymarket rules
source_type: exchange API + market rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: risk-manager
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-94e8aad1/researcher-analyses/2026-04-14/dispatch-case-20260414-94e8aad1-20260414T175223Z/personas/risk-manager.md]
tags: [source-note, binance, polymarket, btc]
---

# Summary

This source note captures the governing source-of-truth and a direct spot check of current BTC/USDT pricing versus the $70,000 threshold. The market resolves on the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 16, using the final Close price, not any other exchange or generalized BTC/USD print.

## Key facts extracted

- Polymarket's rules state the contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final Close strictly greater than 70,000.
- The contract is specifically tied to Binance BTC/USDT, with 1m candles selected.
- A Binance API spot check on 2026-04-14 showed BTCUSDT at 74,664.77.
- A Binance 1-minute kline spot check showed recent closes in the 74,650-74,701 range.

## Evidence directly stated by source

- Direct from Polymarket rules: source of truth is Binance BTC/USDT 1-minute candle close at 12:00 ET on the target date.
- Direct from Binance API: current price materially exceeds the 70,000 threshold by roughly 6.6% or about $4.65k.

## What is uncertain

- The final resolution depends on a single future 1-minute close at a fixed timestamp, so path risk remains despite current price cushion.
- Binance's web UI phrasing references ET, while Binance API timestamps are UTC milliseconds, so practical resolution requires converting noon ET on April 16 to the corresponding minute in Binance data.
- A temporary exchange-specific dislocation on Binance at the target minute could matter even if broader BTC pricing stays above 70,000 elsewhere.

## Why this source may matter

This is the authoritative settlement source plus the most direct available evidence on where BTC/USDT currently trades relative to the threshold.

## Possible impact on the question

It supports a high Yes probability because spot is already well above 70,000 and the resolution source is explicit. It also highlights the main underpriced failure mode: because settlement hinges on one exchange and one minute close, a sharp selloff or Binance-specific anomaly at the exact minute could still flip the contract to No.

## Reliability notes

- Polymarket rules are the authoritative contract mechanics source.
- Binance API is the closest direct machine-readable proxy for the specified exchange source, though final operational resolution may still rely on Binance's displayed candle data rather than this note's ad hoc query.
- These two sources are not fully independent, but together they are the most relevant direct evidence for this contract.