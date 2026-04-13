---
type: source_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-13
question: Will the price of Bitcoin be above $70,000 on April 13?
driver: reliability
date_created: 2026-04-13
source_name: Binance public API spot and recent 1-minute klines
source_type: exchange API
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/market-implied.md]
tags: [binance, api, spot, direct-source]
---

# Summary

A direct Binance API spot check returned BTCUSDT at 71,593.01 during this run. A second direct pull of recent 1-minute klines also showed multiple closes above 70,000 in the immediately available minute data. This does not directly settle the exact noon-ET candle, but it strongly supports the market's view that BTC was trading above the threshold around the relevant period.

## Key facts extracted

- Binance API ticker returned `{"symbol": "BTCUSDT", "price": "71593.01000000"}` during the run.
- Recent 1-minute kline data visible from Binance included closes such as 71,071.32, 71,061.61, 71,331.00, 71,616.45, and 71,700.16.
- The available in-session pull did not cleanly return the exact historical 12:00 ET candle via parameterized historical query, so this note remains a direct-but-incomplete verification of the source of truth.

## Evidence directly stated by source

- Current Binance BTCUSDT spot price: `71593.01000000`.
- Recent Binance 1-minute candles in the fetched API output were above 70,000.

## What is uncertain

- I did not obtain the exact 12:00 ET historical 1-minute close from the public API within this session.
- The direct kline sample available appeared to be recent rolling data rather than the exact target minute required for settlement.

## Why this source may matter

Binance is the governing source of truth for the contract. Even incomplete direct verification from Binance deserves more weight than third-party market commentary.

## Possible impact on the question

If Binance spot is currently around 71.6k and nearby 1-minute closes are above 70k, the market's prior around 71% is directionally reasonable and may even have been conservative if the fetched Polymarket ladder at 94% reflected later information.

## Reliability notes

High reliability as a direct exchange source, but only medium completeness for this exact contract because the precise noon-ET close was not directly captured in-session.