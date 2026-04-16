---
type: source_note
case_key: case-20260414-8dcead65
dispatch_id: dispatch-case-20260414-8dcead65-20260414T160342Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the price of Bitcoin be above $70,000 on April 15?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance BTCUSDT spot endpoints and Polymarket rules page
source_type: primary-plus-contract
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8dcead65/researcher-analyses/2026-04-14/dispatch-case-20260414-8dcead65-20260414T160342Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution-check, timing]
---

# Summary

This note captures the direct settlement mechanics and the main timing/rule risk for the April 15 BTC > 70k market.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle for **12:00 ET** on the date in the title.
- The relevant condition is the candle's final **Close** price, not the intraminute high, low, or another exchange price.
- Binance public spot endpoints were reachable at analysis time.
- Current Binance BTC/USDT spot price at analysis time was about **75,458-75,478**.
- Binance 24h stats showed a session high around **76,038** and low around **71,701**, indicating BTC was materially above 70k with about 24 hours left.
- A direct kline query for 2026-04-14 12:00 ET (16:00 UTC) returned a 1-minute candle close of **75,356.48**, confirming the ET-to-UTC mapping and that the API exposes the exact candle structure needed for settlement verification.

## Evidence directly stated by source

- Polymarket rules page: Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET has a final close above the threshold; otherwise No.
- Binance kline endpoint provides timestamped 1-minute OHLCV candles including the close field.
- Binance ticker endpoints provide current spot and 24h summary values consistent with BTC trading well above 70k.

## What is uncertain

- Final resolution depends only on the specific **April 15 12:00 ET** candle close, which had not occurred yet at analysis time.
- Binance web UI wording on the market page references the website chart, while direct API endpoints are easier to audit; there is small operational ambiguity if UI and API presentation diverge, though both should reflect the same underlying market data.
- A large price shock between analysis time and the settlement minute could still push BTC below 70k.

## Why this source may matter

This is the main source-of-truth pair for the market: Polymarket defines the contract logic and Binance supplies the underlying price series. The main remaining risk is not whether BTC is currently above 70k, but whether it can drop more than roughly 7% before the settlement minute or whether there is an operational interpretation issue around the exact candle/timezone mapping.

## Possible impact on the question

The direct evidence supports a strong Yes lean, but also shows the exact fragility: a single minute-close at a fixed future time decides the market. That means path risk, volatility, and timing interpretation matter more than broad bullish context.

## Reliability notes

- Polymarket is authoritative for contract wording.
- Binance is authoritative for the referenced price surface.
- Evidence independence is medium rather than high because the contract explicitly points to Binance, so the core verification sources are intentionally linked rather than independent.
- Coingecko provided a light contextual cross-check and matched the broad spot level, but it is not a settlement source.