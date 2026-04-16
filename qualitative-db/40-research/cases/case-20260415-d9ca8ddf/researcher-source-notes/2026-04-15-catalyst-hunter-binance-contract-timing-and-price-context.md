---
type: source_note
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket contract page plus Binance API timing and price checks
source_type: contract rules plus exchange API context
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-d9ca8ddf/researcher-analyses/2026-04-15/dispatch-case-20260415-d9ca8ddf-20260415T195847Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, btcusdt, timing, catalyst]
---

# Summary

The case is mostly a timed spot-price question rather than a fundamental thesis question. The governing contract requires the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 17, 2026 to close above 72,000. Extra verification confirmed that 12:00 ET on that date maps to 16:00 UTC, and Binance spot context on April 15 showed BTC/USDT around 74.9k with a 24-hour range of roughly 73.5k to 75.3k, leaving a cushion of about 4% above the strike.

## Key facts extracted

- Polymarket rules specify the decisive observation: Binance BTC/USDT, 1-minute candle, 12:00 ET, final close price.
- The assignment current_price of 0.91 is consistent with the event page showing the 72,000 threshold around 93% Yes at fetch time.
- 2026-04-17 12:00 ET converts to 2026-04-17 16:00 UTC because New York is on daylight saving time.
- Binance API spot checks on 2026-04-15 showed BTCUSDT last price around 74,885-74,893, 5-minute average around 74,936, 24-hour high 75,281, and 24-hour low 73,514.
- The key near-term catalyst is simply whether macro / crypto risk sentiment remains stable over the next ~44 hours; no single scheduled protocol-specific catalyst was identified in the sourced materials.

## Evidence directly stated by source

- Polymarket contract text: the market resolves Yes only if the specified Binance 1-minute candle close is higher than 72,000.
- Binance market data endpoints document that `/api/v3/klines` provides 1-minute candle data and that startTime/endTime are interpreted in UTC.
- Binance ticker and avgPrice endpoints showed BTC trading comfortably above the threshold at verification time.

## What is uncertain

- There may still be unsourced macro or crypto-specific headlines between now and April 17 noon ET that move BTC sharply.
- Current spot context is not the resolving candle itself.
- The contract points to the Binance trading interface as the visible resolution surface, so API context is supportive rather than the literal settlement screen.

## Why this source may matter

This source bundle captures the whole mechanism that actually matters: timestamp mapping, source-of-truth venue, and current cushion versus the strike. For a short-dated BTC threshold market, these are the highest-information inputs.

## Possible impact on the question

If BTC merely stays in its recent range, Yes should resolve. The most plausible repricing catalyst before expiry is not a scheduled event but a sharp broad-market drawdown that compresses BTC by more than about 4% into the exact resolution minute.

## Reliability notes

High-quality for contract mechanics and price context because it combines the contract-defining page with Binance's own API documentation and live exchange data. Independence is only medium because all price-context checks still route back to Binance surfaces.