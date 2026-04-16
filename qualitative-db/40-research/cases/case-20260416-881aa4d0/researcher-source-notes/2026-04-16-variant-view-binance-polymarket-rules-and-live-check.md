---
type: source_note
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules page + Binance BTCUSDT API live checks
source_type: primary-plus-direct
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-881aa4d0/researcher-analyses/2026-04-16/dispatch-case-20260416-881aa4d0-20260416T044756Z/personas/variant-view.md]
tags: [polymarket, binance, resolution, timing, live-price]
---

# Summary

This note captures the governing contract mechanics from the Polymarket market page and a direct live verification pass against Binance BTC/USDT. The direct check shows BTC/USDT materially above $70,000 at assignment time, which makes the remaining variant case mostly about contract mechanics, timing, or exchange-specific operational failure rather than broad price direction.

## Key facts extracted

- Polymarket rules state the market resolves to "Yes" if the Binance BTC/USDT 1 minute candle for **12:00 ET (noon)** on **April 17, 2026** has a final **Close** price above **70,000**.
- The rules explicitly say the source of truth is **Binance**, specifically the BTC/USDT pair with **1m** candles.
- The rules explicitly exclude other exchanges and other trading pairs.
- Binance direct API checks on 2026-04-16 around 00:49-00:50 EDT returned BTCUSDT spot prices around **74,858**, **74,923**, and recent 1m klines with closes around **74,924.99**.
- Binance exchange info returned BTCUSDT status as **TRADING**, which weakly reduces but does not eliminate exchange-availability concerns.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From Binance API live check:
- `ticker/price`: BTCUSDT around 74.9k.
- `klines?interval=1m&limit=1`: latest minute close around 74.9k.
- `exchangeInfo`: symbol status `TRADING`.

## What is uncertain

- The market resolves on the **April 17 12:00 ET** candle, not current spot, so a large intraday move lower before noon could still produce "No."
- The rules rely on the Binance surface "currently available" on the website; there is some operational ambiguity around final candle publication, revisions, or UI/API mismatch, though this is likely low.
- This source note does not itself establish macro or flow reasons for whether BTC could fall below 70k by tomorrow noon.

## Why this source may matter

This is the core source-of-truth package for the case: it defines what counts, when it counts, and confirms that current live price is comfortably above the threshold. That sharply narrows any serious variant thesis.

## Possible impact on the question

The direct evidence materially favors "Yes" because BTC/USDT is already about 7% above the threshold roughly 35 hours before settlement. The remaining plausible path to "No" is not a mild pricing miss but a meaningful downside move into the exact noon ET minute close, or a low-probability exchange-specific resolution issue.

## Reliability notes

- Polymarket rules page is the governing contract surface, so it is authoritative for mechanics.
- Binance API is a strong direct source for the referenced market, though the literal resolution page mentions the Binance web chart UI rather than the API. Still, the API is highly relevant as an extra verification pass.
- Evidence independence is moderate: both sources center on the same contract/source-of-truth chain rather than independent market forecasting evidence.