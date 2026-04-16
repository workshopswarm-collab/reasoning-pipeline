---
type: source_note
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the price of Bitcoin be above $70,000 on April 14?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket rules page plus Binance BTCUSDT API verification
source_type: primary-and-contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ce42d6c/researcher-analyses/2026-04-14/dispatch-case-20260414-3ce42d6c-20260414T130958Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, resolution-source, timing-check]
---

# Summary

This source note captures the governing contract mechanics from Polymarket and a direct Binance API verification showing BTC/USDT trading materially above $70,000 on the morning of 2026-04-14, well before the relevant noon ET candle.

## Key facts extracted

- Polymarket states the market resolves to "Yes" if the Binance BTC/USDT 1-minute candle for **12:00 ET** on 2026-04-14 has a final **Close** price strictly higher than **70,000**.
- The source of truth is explicitly Binance BTC/USDT, not other exchanges or other pairs.
- A timezone check converts **2026-04-14 12:00 ET** to **2026-04-14 16:00 UTC**, which is the relevant minute in exchange/API time.
- Direct Binance API checks during research showed:
  - ticker price: **74,576.52**
  - recent 1m kline closes in the mid-74.5k range, all comfortably above 70k.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

Direct Binance API observations captured during this run:
- `https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT` returned `{"symbol":"BTCUSDT","price":"74576.52000000"}`.
- `https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=3` returned three most recent 1m candles with closes around **74,565.41**, **74,551.02**, and **74,576.52**.

## What is uncertain

- This note does not itself capture the final settled 12:00 ET candle close; it verifies the governing mechanism and that the market is deep in-the-money before the event minute.
- Intraminute exchange dislocations, symbol-specific outages, or an extreme crash before noon ET remain logically possible even if they appear low probability.

## Why this source may matter

The market is rule-sensitive and date-sensitive. The key task is not generic Bitcoin direction but verifying the exact settlement surface, timing, and whether the current state leaves any realistic room for a sub-70k close by the relevant minute.

## Possible impact on the question

These sources strongly support a high-probability "Yes" view because:
- the governing source of truth is clear,
- the relevant observation window is precisely defined,
- BTC/USDT is more than $4,500 above the threshold shortly before the noon ET observation minute.

## Reliability notes

- Polymarket rules page is the best direct contract-mechanics source available for what counts.
- Binance API is a strong direct contextual source for the relevant exchange and pair, though the final resolving surface is the Binance chart candle itself at the specified minute.
- Evidence independence is moderate: the two sources answer different questions (rules vs price state) and complement each other rather than duplicating the same claim.
