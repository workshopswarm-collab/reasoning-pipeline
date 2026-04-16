---
type: source_note
case_key: case-20260414-e15c72fe
dispatch_id: dispatch-case-20260414-e15c72fe-20260414T193100Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-20 above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance BTCUSDT API + Polymarket market rules page
source_type: primary_market_data_and_contract_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-20
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-e15c72fe/researcher-analyses/2026-04-14/dispatch-case-20260414-e15c72fe-20260414T193100Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, contract-rules, source-note, catalyst-hunter]
---

# Summary

This source note captures the governing resolution mechanics from the Polymarket market page and a direct Binance spot check showing BTC/USDT already trading materially above $70,000 on 2026-04-14.

## Key facts extracted

- The market resolves on the Binance BTC/USDT **1-minute candle at 12:00 ET on 2026-04-20**.
- The relevant field is the candle's final **Close** price, not intraday high/low and not another exchange.
- A direct Binance API spot check on 2026-04-14 returned BTCUSDT around **74,049.50**.
- Recent 1-minute Binance klines fetched during the same check were all in the **74.0k-74.3k** area, which confirms current trading is several thousand dollars above the 70k threshold.
- Polymarket listed the 70,000 line around **89%** at capture time, consistent with assignment context current_price 0.845 but somewhat higher on page snapshot.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From Binance API checks executed from workspace:
- ticker price endpoint returned `{"symbol":"BTCUSDT","price":"74049.50000000"}`
- recent 1m klines showed closes including `74239.97`, `74258.36`, `74217.11`, `74106.79`, `74049.50`

## What is uncertain

- The direct check is a point-in-time snapshot six days before resolution, so it does not settle the case.
- No single near-term scheduled catalyst guarantees BTC remains above 70k into April 20 noon ET.
- Exchange-specific idiosyncrasies remain relevant because the contract is Binance-only.

## Why this source may matter

This is the core source-of-truth pair for the case: Polymarket defines the exact settlement mechanic, and Binance is the authoritative pricing venue the contract points to.

## Possible impact on the question

Because BTC/USDT is already roughly 5.8% above the threshold, the market mostly hinges on whether a sizable drawdown occurs before the exact noon ET minute on April 20. That makes catalyst timing and downside shock risk the main remaining drivers rather than ordinary day-to-day noise.

## Reliability notes

- Polymarket rules page is authoritative for contract interpretation.
- Binance API is authoritative for live Binance price data, though not a direct future print for the resolution minute.
- Evidence independence is moderate: the two sources serve different purposes (rules vs live price) but both are directly tied to the same market structure.