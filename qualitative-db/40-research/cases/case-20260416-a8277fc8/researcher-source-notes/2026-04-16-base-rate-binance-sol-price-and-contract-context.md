---
type: source_note
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: threshold-close-markets
entity: sol
topic: Binance SOL/USDT spot level versus April 19 noon ET close-above-80 contract
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close on April 19, 2026 be above 80?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API plus Polymarket contract page
source_type: exchange API and contract page
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, crypto, sol, binance, polymarket, close-market]
---

# Summary

This note captures the governing settlement mechanics from the Polymarket market page and a direct Binance spot/1-minute check relevant to the April 19 noon ET close-above-80 contract.

## Key facts extracted

- Polymarket rules state the market resolves Yes if the Binance SOL/USDT 1-minute candle for 12:00 ET on April 19 has a final close price higher than 80.
- The market is explicitly about Binance SOL/USDT, not other exchanges or pairs.
- A direct Binance API spot query returned `84.72000000` around research time.
- A direct Binance API 1-minute kline pull showed recent 1-minute closes clustered around `84.67` to `84.75`.
- Independent contextual spot checks from CoinGecko (`84.73`) and Coinbase (`84.705`) were closely aligned with Binance spot.

## Evidence directly stated by source

- Contract text: resolution source is Binance SOL/USDT with 1m candles, using the final close price for the 12:00 ET candle on the specified date.
- Binance ticker endpoint returned price `84.72000000`.
- Binance recent 1-minute klines showed contemporaneous closes above 80.

## What is uncertain

- The relevant settlement print is not the current price but the final close of the specific April 19 12:00 ET minute.
- Short-dated crypto moves can be large enough that being above 80 several days earlier does not guarantee remaining above 80 at settlement.
- The Polymarket web page is not itself the settlement source; it only describes the source.

## Why this source may matter

This source establishes both the exact mechanism to be forecast and the current cushion versus the threshold. For a short-dated close-above market, distance from threshold and precise source-of-truth wording are the main structural inputs.

## Possible impact on the question

With SOL trading about 5.9% above the threshold at research time, the outside-view prior for remaining above 80 by noon ET on April 19 is materially favorable, though not near certainty because this is a single-minute close condition rather than an anytime touch condition.

## Reliability notes

- Binance is the governing source of truth for settlement, so source-of-truth ambiguity is low once the rule text is established.
- Binance API output is direct and machine-readable, which is stronger than relying only on the exchange web UI.
- CoinGecko and Coinbase are useful independent contextual checks for current price level, but they do not govern settlement.