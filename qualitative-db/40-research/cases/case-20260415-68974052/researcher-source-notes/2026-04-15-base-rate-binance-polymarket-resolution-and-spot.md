---
type: source_note
case_key: case-20260415-68974052
dispatch_id: dispatch-case-20260415-68974052-20260415T183011Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-68974052 | base-rate
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules + Binance spot API and kline docs
source_type: market rules + exchange API documentation + live exchange data
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-68974052/researcher-analyses/2026-04-15/dispatch-case-20260415-68974052-20260415T183011Z/personas/base-rate.md]
tags: [polymarket, binance, resolution, btc, spot-price]
---

# Summary

This source set establishes the contract mechanics and current reference context for the April 17 BTC > 72,000 market. It shows the governing source of truth is Binance BTC/USDT 1-minute candle data at 12:00 ET on Apr. 17, and that current BTCUSDT spot is already above the threshold by roughly 3.1% as of Apr. 15.

## Key facts extracted

- Polymarket rules say the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 17 has a final Close strictly higher than 72,000.
- The market is specifically tied to Binance BTC/USDT, not other exchanges or pairs.
- Binance API documentation says klines are uniquely identified by open time and support 1-minute intervals; response includes open time, close time, and close price.
- Binance live ticker fetched on 2026-04-15 showed BTCUSDT at 74,233.75.
- Recent 1-minute klines fetched on 2026-04-15 also showed closes near 74.2k, consistent with the live ticker.
- Noon ET on Apr. 17 corresponds to 16:00 UTC.

## Evidence directly stated by source

- Direct contract wording from Polymarket:
  - Yes resolves if the Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date has a final Close above the threshold.
  - Resolution source is Binance BTC/USDT with 1m candles.
- Direct Binance documentation:
  - `GET /api/v3/klines` returns kline/candlestick bars for a symbol.
  - Klines are uniquely identified by open time.
  - The response includes close price.
- Direct Binance live data:
  - `ticker/price?symbol=BTCUSDT` returned 74233.75000000 on 2026-04-15.

## What is uncertain

- This does not by itself prove where BTCUSDT will be at 12:00 ET on Apr. 17.
- Polymarket’s rule text references the Binance trading UI rather than the API explicitly, so there is small operational ambiguity if UI and API display ever differ transiently.
- Without broader historical-volatility data in this note, the exact probability of a drop below 72k by settlement remains inferential rather than mechanically derived.

## Why this source may matter

This is the governing source-of-truth set for the contract plus the most important current-state check. For a short-horizon BTC threshold market, contract interpretation and current distance from strike are the most material first-order inputs.

## Possible impact on the question

Because BTCUSDT is currently above 72k by about 2,233.75, the market needs a meaningful downward move by Friday noon ET to resolve No. That supports a high-but-not-certain Yes probability, subject to BTC’s short-horizon volatility and exchange-specific execution/operational edge cases.

## Reliability notes

- Polymarket rule text is the authoritative contract source for how the market should be judged.
- Binance exchange docs are high-credibility for interpreting API candle fields and timestamp behavior.
- Binance live ticker and recent klines are direct but time-sensitive snapshots; they are reliable for current-state context, not for future settlement.
- Evidence independence is medium: the spot snapshot and recent klines both come from Binance, while the rule text comes from Polymarket but points back to Binance as settlement source.