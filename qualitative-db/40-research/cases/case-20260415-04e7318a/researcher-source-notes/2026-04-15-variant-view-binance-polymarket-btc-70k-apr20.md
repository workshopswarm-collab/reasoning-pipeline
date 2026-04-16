---
type: source_note
case_key: case-20260415-04e7318a
dispatch_id: dispatch-case-20260415-04e7318a-20260415T145259Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 PM ET one-minute candle close on 2026-04-20 be above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance API spot/1m candle surfaces
source_type: primary_and_resolution_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-04e7318a/researcher-analyses/2026-04-15/dispatch-case-20260415-04e7318a-20260415T145259Z/personas/variant-view.md]
tags: [bitcoin, polymarket, binance, resolution-source, timing]
---

# Summary

This source note captures the governing market mechanics from Polymarket and a direct live price check from Binance. Together they establish what the contract is actually asking and where BTC/USDT sits relative to the 70,000 threshold on 2026-04-15.

## Key facts extracted

- Polymarket states the market resolves using the Binance BTC/USDT **1 minute candle for 12:00 in ET timezone (noon)** on April 20, 2026.
- The contract resolves Yes only if that candle's final **Close** is **higher than 70,000**.
- The market is explicitly about **Binance BTC/USDT**, not other exchanges or pairs.
- At approximately 2026-04-15 14:54:58 UTC / 10:54:58 EDT, the live Binance API ticker returned **BTCUSDT = 74154.46**.
- The latest Binance 1m kline output around that time showed closes in the low **74.1k** range, comfortably above 70k.

## Evidence directly stated by source

From Polymarket rules page:
- Resolution source is Binance.
- Relevant measurement is the BTC/USDT 1m candle.
- Relevant observation time is 12:00 PM ET on the stated date.
- The threshold test is whether the final Close is higher than 70,000.

From Binance API outputs checked during this run:
- `ticker/price?symbol=BTCUSDT` returned `74154.46000000`.
- Recent 1m klines showed closes near 74129.72, 74102.41, and 74154.46.

## What is uncertain

- The contract references Binance's candle at **12:00 in ET timezone**, while Binance APIs normally timestamp candles in UTC. The mapping is likely straightforward because noon ET on 2026-04-20 corresponds to 16:00 UTC, but the exact UI display convention still matters operationally.
- A single noon minute close on April 20 can still fall below 70,000 even if spot is above 70,000 for most of the surrounding period.
- Binance-specific outages, candle revisions, or display quirks are low-probability but contract-relevant risks.

## Why this source may matter

This is the core direct evidence for both contract interpretation and the current cushion versus threshold. The market is date-specific, exchange-specific, and minute-specific, so the governing source matters more than generic BTC headlines.

## Possible impact on the question

The current spot level near 74.15k implies a buffer of roughly 4.15k, which supports a high Yes probability. The main variant-view implication is that the market may still be slightly overconfident because the contract depends on a single exchange-specific minute close rather than a broad daily price state.

## Reliability notes

- Polymarket rules page is the authoritative market-contract surface for what counts.
- Binance API is a direct exchange surface and highly relevant contextual evidence, though the final settlement is described via the Binance trading candle interface rather than the public REST endpoint.
- Evidence independence between Polymarket rules and Binance price data is medium: they serve different functions, but the contract itself depends on Binance.