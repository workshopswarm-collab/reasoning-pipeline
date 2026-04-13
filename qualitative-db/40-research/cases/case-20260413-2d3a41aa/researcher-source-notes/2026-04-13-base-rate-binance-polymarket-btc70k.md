---
type: source_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-13
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-13 close above 70000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance BTCUSDT ticker + Polymarket rules page
source_type: primary market source plus contract surface
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, btc, resolution-source, timing]
---

# Summary

This source bundle establishes the contract mechanics and the live Binance price context shortly before resolution. The key outside-view fact is that BTC was already materially above the 70,000 threshold with about two hours and ten minutes remaining before the relevant 12:00 ET candle.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT **1 minute candle for 12:00 ET** on April 13, using the final **Close** price.
- The market threshold is strictly **higher than 70,000**.
- At approximately 09:50 ET on 2026-04-13, Binance spot ticker showed BTC/USDT around **71,601.08**.
- Binance 24h stats at that time showed:
  - open: **71,000.65**
  - high: **71,700.82**
  - low: **70,505.88**
  - last: **71,590.52**
- Coinbase spot at roughly the same time showed BTC around **71,433.47**, which is directionally consistent with Binance and reduces concern that Binance alone was showing an anomalous print.

## Evidence directly stated by source

- Polymarket directly states Binance BTC/USDT with 1m candles is the governing source of truth.
- Binance directly states live BTC/USDT ticker and 24h range values.
- Coinbase directly states current BTC/USD spot price.

## What is uncertain

- Live ticker prices are not the settlement candle itself; the relevant value is the 12:00 ET Binance 1-minute candle close, still in the future at research time.
- The exact short-horizon intraday distribution over the next ~130 minutes is not directly provided here.
- A sharp selloff could still push BTC below 70,000 by the settlement minute.

## Why this source may matter

It verifies both the contract mechanics and the most important current-state fact: BTC is already comfortably above the strike and the prior 24h low remained above 70,000. For a short-horizon threshold market, that materially raises the base-rate probability that the noon candle also finishes above 70,000 unless there is a notable downside move before noon.

## Possible impact on the question

This source pushes toward Yes. It does not settle the question yet, but it supports a high probability because all material conditions required for Yes appear straightforward except one: BTC must remain above 70,000 on the exact noon ET Binance 1-minute close.

## Reliability notes

- Binance is the authoritative resolution source named by the contract, so source-of-truth ambiguity is low.
- Polymarket rules page is the contract surface, but it is not itself the price source.
- Coinbase is only contextual verification, not settlement-relevant.
- Independence is moderate rather than high because both Binance and Coinbase reflect the same underlying global BTC market, but they are operationally separate surfaces.