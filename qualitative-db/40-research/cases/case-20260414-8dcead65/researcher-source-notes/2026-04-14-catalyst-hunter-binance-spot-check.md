---
type: source_note
case_key: case-20260414-8dcead65
dispatch_id: dispatch-case-20260414-8dcead65-20260414T160342Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the price of Bitcoin be above $70,000 on April 15?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT spot price and recent 1m klines API spot check
source_type: exchange API / direct market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8dcead65/researcher-analyses/2026-04-14/dispatch-case-20260414-8dcead65-20260414T160342Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, spot, 1m-candle, verification]
---

# Summary

A direct API check on Binance showed BTC/USDT trading materially above the 70,000 threshold roughly 20 hours before the relevant noon ET settling minute.

## Key facts extracted

- Binance ticker returned BTCUSDT price 75521.40 at the time of check.
- Recent 1m klines showed closes around 75458.63 to 75521.41.
- The latest observed candle opens were around 16:06 to 16:08 UTC on April 14, which corresponds to 12:06 to 12:08 ET.
- BTC was therefore about 7.9% above the 70,000 threshold at the time of verification.

## Evidence directly stated by source

Direct Binance API outputs:
- ticker price: 75521.40000000
- recent 1m closes: 75483.30000000, 75521.40000000, 75521.41000000

## What is uncertain

- This does not settle the market because the contract resolves on the April 15 12:00 ET 1m candle, not the current price.
- Intraday volatility, macro headlines, exchange-specific dislocations, or a sharp overnight selloff could still move BTC below the threshold by settlement.

## Why this source may matter

It is the closest direct evidence to the future resolution surface because it comes from the same exchange and pair named in the rules.

## Possible impact on the question

The current buffer above 70,000 means a very large adverse move would be required before noon ET tomorrow for the market to resolve No, absent a Binance-specific pricing anomaly.

## Reliability notes

High-quality direct source for current state and highly aligned with settlement mechanics. Independence is limited because this is the same source family that ultimately governs settlement.