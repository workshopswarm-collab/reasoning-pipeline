---
type: source_note
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: threshold-close-markets
entity: btc
topic: Binance BTC/USDT 1-minute close-above threshold resolution surface for April 20 noon ET market
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT 1m klines API plus Polymarket market page / contract description
source_type: mixed_primary_and_contextual
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/variant-view.md
tags: [binance, polymarket, source-of-truth, btcusdt, one-minute-close]
---

# Summary

This source note captures the governing resolution mechanics and a direct spot check of the relevant source surface. The market resolves on the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 20, based on the final Close price, not on a touch/high at any point and not on another exchange.

## Key facts extracted

- The assignment includes the market description specifying: resolve Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on April 20 has a final Close price above $70,000; otherwise No.
- The assignment further specifies the intended source surface is Binance BTC/USDT with 1m candles selected.
- Direct Binance API spot check on 2026-04-15 returned recent BTCUSDT 1-minute klines with close prices in the high $73.9k to low $74.0k range.
- Direct Binance ticker spot check on 2026-04-15 returned BTCUSDT price 73994.60000000.
- Therefore, as of the research date BTC is materially above the threshold, but the contract is not yet settled because the relevant observation window is specifically the April 20 12:00 ET minute close.

## Evidence directly stated by source

- Binance kline API directly reports 1-minute OHLCV candles for BTCUSDT.
- Binance ticker API directly reports BTCUSDT last price.
- The contract description directly states the settlement mechanism and source-of-truth requirements.

## What is uncertain

- The exact April 20 noon ET candle has not occurred yet.
- The precise mapping between Binance UI candle labeling and ET noon requires using the specified 12:00 ET minute on the date of resolution; this is operationally straightforward but still date/time sensitive.
- A live Binance UI check closer to resolution could still be useful to avoid any misunderstanding about candle labeling or daylight-savings handling, though the assignment already specifies ET.

## Why this source may matter

This is the direct governing-source surface. It matters more than generic BTC spot articles or cross-exchange prices because the contract is explicitly tied to Binance BTC/USDT 1-minute final close at a specific time.

## Possible impact on the question

The direct source supports a high current probability for Yes because BTC is already comfortably above $70k several days before the observation time. But it also limits overconfidence: the market is still exposed to a downside move before or at the exact April 20 noon ET minute close.

## Reliability notes

- Binance API output is direct and machine-readable, which makes it strong for verifying the relevant instrument and recent price level.
- Polymarket webpage fetch was usable mainly for contextual confirmation that the event exists; the assignment-provided contract description was the cleaner rules source in this run.
- Evidence independence is only medium because both the contract wording and Binance surface are tightly coupled to the same settlement mechanism rather than independent market analysis.