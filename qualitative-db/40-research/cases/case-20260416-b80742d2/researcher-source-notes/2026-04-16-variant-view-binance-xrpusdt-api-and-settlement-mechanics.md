---
type: source_note
case_key: case-20260416-b80742d2
dispatch_id: dispatch-case-20260416-b80742d2-20260416T014833Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-structure-and-resolution
entity: xrp
topic: XRP/USDT April 19 noon ET settlement mechanics and current price
question: Will the Binance XRP/USDT 1 minute candle for 12:00 ET on April 19, 2026 close above 1.30?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API and Binance XRP/USDT trading surface
source_type: exchange API / direct market data
source_url: https://api.binance.com/api/v3/klines?symbol=XRPUSDT&interval=1m&limit=5
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [xrp]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-b80742d2/researcher-analyses/2026-04-16/dispatch-case-20260416-b80742d2-20260416T014833Z/personas/variant-view.md
tags: [binance, settlement-mechanics, xrp, direct-source]
---

# Summary

This source note captures the direct Binance surfaces most relevant to the contract: current XRP/USDT spot price, 1-minute kline structure, and the practical time conversion for the April 19 noon ET settlement candle.

## Key facts extracted

- Binance spot API returned current XRP/USDT price at approximately `1.40180000` during this run.
- Binance 1-minute kline API for XRPUSDT returned recent candles with close prices around `1.3998` to `1.4018`, confirming the pair is actively trading around 1.40.
- Binance exchange info for XRPUSDT shows the market is `TRADING` and includes a `PRICE_FILTER` tick size of `0.00010000`, which implies 4-decimal price precision on the exchange API surface.
- The market rule says the relevant candle is the Binance `1m` candle for `12:00` in ET on April 19. In April, ET is EDT (UTC-4), so the corresponding UTC open time is `2026-04-19 16:00:00 UTC`.
- Querying the future settlement-candle timestamp now correctly returns no data, which is consistent with normal API behavior and confirms the timestamp mapping logic rather than introducing ambiguity.

## Evidence directly stated by source

- Direct API endpoint output from `ticker/price` showed XRPUSDT at `1.40180000`.
- Direct API endpoint output from `klines` showed recent minute bars with close values above 1.30.
- Direct API endpoint output from `exchangeInfo` showed XRPUSDT status `TRADING` and tick size `0.00010000`.

## What is uncertain

- The current price is not the settlement price; XRP can move materially before April 19 noon ET.
- The Polymarket rules reference the Binance web trading interface with `1m` and `Candles` selected. The API appears consistent with that surface, but the exact displayed close on the web UI at resolution time is still the formal source named in the rule text.
- Binance does not guarantee that current price regime persists over the next ~3 days.

## Why this source may matter

This is the closest available direct source to the contract’s governing source of truth. It verifies that the contract is keyed to a specific exchange, pair, interval, and timestamp rather than general XRP spot performance across venues.

## Possible impact on the question

Because XRP/USDT on Binance is already trading around 1.40, the market only needs XRP to avoid a decline of roughly 7% by the resolution minute. That supports a high Yes probability, but not certainty, because crypto can move sharply over a multi-day window.

## Reliability notes

- High credibility for direct exchange market state and minute-candle structure.
- Independence is limited because this is the same family of source the contract resolves on; it is authoritative for settlement mechanics but not independent confirmation of broader market regime.
- Strongest use is direct resolution interpretation and current-price baseline, not long-horizon forecasting by itself.
