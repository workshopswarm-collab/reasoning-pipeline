---
type: source_note
case_key: case-20260416-33b4e3b5
dispatch_id: dispatch-case-20260416-33b4e3b5-20260416T021538Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: spot-price-markets
entity: sol
topic: case-20260416-33b4e3b5 | catalyst-hunter
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-15T22:00:00-04:00
source_name: Binance API and Polymarket market page check
source_type: primary-plus-contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-33b4e3b5/researcher-analyses/2026-04-16/dispatch-case-20260416-33b4e3b5-20260416T021538Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, catalyst-calendar, resolution-mechanics]
---

# Summary

Direct checks on Binance public market-data endpoints and the Polymarket event page show SOL/USDT trading around $84.75-$84.82 on Apr. 15 evening ET, while the Polymarket Apr. 19 "$80" line is pricing roughly 89%-90% Yes. This supports a base case that SOL is currently above the threshold with modest cushion, but leaves several days for volatility before the contract’s specific noon ET 1-minute close.

## Key facts extracted

- Binance `/api/v3/ticker/price?symbol=SOLUSDT` returned `{"symbol":"SOLUSDT","price":"84.75000000"}`.
- Binance `/api/v3/klines?symbol=SOLUSDT&interval=1m&limit=10` returned recent 1-minute candles clustered around $84.75-$84.97.
- Binance `/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=10` showed daily closes around: Apr 12 $81.53, Apr 13 $86.51, Apr 14 $83.72, Apr 15 $84.90.
- Binance `/api/v3/klines?symbol=SOLUSDT&interval=1h&limit=72` implied a 72h close range of about $81.73 to $87.29.
- Binance `/api/v3/time` and `/api/v3/exchangeInfo?symbol=SOLUSDT` confirmed active trading surface and UTC server-time reference.
- Polymarket page for `solana-above-on-april-19` displayed the market rule: resolve from Binance SOL/USDT 1-minute candle close at 12:00 ET on Apr. 19, with the "$80" line around 89% Yes / 13% No on page fetch.

## Evidence directly stated by source

- Binance directly states the current quoted SOL/USDT price and recent kline closes.
- Polymarket directly states the contract mechanics and governing settlement source.

## What is uncertain

- The Polymarket page is a web-rendered contextual surface, not a structured API pull here, so quoted odds should be treated as approximate but directionally reliable for this run.
- Current spot price does not settle the contract; the relevant print is the Binance 1-minute close at 12:00 ET on Apr. 19.
- No discrete scheduled protocol catalyst was verified in this note; market outcome remains mostly exposed to broad crypto price action and any exchange-specific shock into the deadline.

## Why this source may matter

This is the core source bundle for a narrow, date-specific crypto threshold market. Binance is the governing resolution source, and Polymarket’s own rule text defines which Binance print matters.

## Possible impact on the question

These checks support a bullish base case for "above $80" because spot is already more than $4 above the strike and recent realized range has mostly remained above the threshold. But because resolution depends on a single noon ET minute close several days ahead, the remaining risk is not contract ambiguity; it is a sharp enough price drawdown before the deadline.

## Reliability notes

- Binance public API is the most authoritative source available in this run for current and recent price behavior.
- Polymarket page text is authoritative for displayed market rules but less robust than direct API extraction for odds snapshots.
- Independence is moderate: the rule source and resolution source are distinct, but both are still part of the market plumbing rather than fully independent market analysis.