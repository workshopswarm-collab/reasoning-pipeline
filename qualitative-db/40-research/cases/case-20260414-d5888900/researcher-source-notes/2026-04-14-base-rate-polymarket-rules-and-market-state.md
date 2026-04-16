---
type: source_note
case_key: case-20260414-d5888900
dispatch_id: dispatch-case-20260414-d5888900-20260414T143228Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-d5888900 | base-rate
question: Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-14 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [base-rate.md]
tags: [source-note, polymarket, contract-rules, bitcoin]
---

# Summary

Polymarket's market page gives both the current market-implied baseline and the governing contract wording. For the assigned line, the page shows the 70,000 outcome trading at essentially 100% and states resolution depends specifically on the Binance BTC/USDT 1-minute candle at 12:00 ET on April 14, with the candle close required to be strictly higher than 70,000.

## Key facts extracted

- The event page lists the 70,000 threshold at 100%, consistent with the assignment field `current_price: 0.9995`.
- Resolution is based on the Binance BTC/USDT pair, not another exchange or another BTC pair.
- The market resolves "Yes" only if the Binance 1-minute candle for 12:00 in ET has a final close price higher than 70,000.
- The contract is a strict greater-than test, not greater-than-or-equal.
- Price precision is determined by the Binance source.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The public page does not itself provide the future 12:00 ET candle close at the time this note is written because the market had not yet reached the noon resolution time.
- The page does not independently verify Binance uptime or whether the Binance interface and API remain aligned at settlement.

## Why this source may matter

This is the governing resolution source for the contract and therefore the most important source for interpreting what conditions must hold for a Yes resolution.

## Possible impact on the question

This source makes clear that the relevant event is narrower than generic "Bitcoin above 70k today." The required conditions are: correct date, correct timezone, correct exchange, correct pair, correct 1-minute candle, and a strict close above 70,000.

## Reliability notes

Polymarket is authoritative for its own contract wording but not for the underlying BTC price. Reliability for contract interpretation is high; reliability for underlying asset state is only indirect.