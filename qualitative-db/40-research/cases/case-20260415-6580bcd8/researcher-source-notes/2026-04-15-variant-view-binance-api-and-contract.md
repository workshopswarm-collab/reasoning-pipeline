---
type: source_note
case_key: case-20260415-6580bcd8
dispatch_id: dispatch-case-20260415-6580bcd8-20260415T081158Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API klines documentation plus live BTCUSDT ticker/klines, and Polymarket market rules page
source_type: primary_and_resolution_context
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints ; https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6580bcd8/researcher-analyses/2026-04-15/dispatch-case-20260415-6580bcd8-20260415T081158Z/personas/variant-view.md]
tags: [source-note, binance, polymarket, resolution-mechanics, btc]
---

# Summary

This note captures the core direct evidence for the case: the market resolves off Binance BTC/USDT one-minute candle close data at 12:00 ET on 2026-04-17, and live Binance spot data on 2026-04-15 shows BTC/USDT already trading materially above 72,000.

## Key facts extracted

- Polymarket rules state the market resolves to Yes if the Binance BTC/USDT 12:00 ET one-minute candle on the specified date has a final Close price higher than 72,000.
- The contract is exchange-specific: Binance BTC/USDT, not a broader BTC index or other venue.
- Binance spot API documentation states `GET /api/v3/klines` returns kline/candlestick bars uniquely identified by open time, with a `1m` interval available.
- Live Binance API calls on 2026-04-15 returned BTCUSDT spot around 73.8k, already above the 72k threshold.
- Recent Binance daily candles show BTC closing above 72k on most recent days except a dip on 2026-04-12, indicating the threshold is currently near-but-below prevailing spot rather than far out of range.

## Evidence directly stated by source

- Binance docs directly specify the kline endpoint mechanics and that klines are identified by open time.
- Polymarket directly specifies the governing source of truth and exact condition required for Yes.
- Live Binance endpoint output directly showed `{"symbol":"BTCUSDT","price":"73830.09000000"}` during this run.
- Live 1-minute klines directly showed recent minute-level closes in the 73.7k-73.8k range during this run.

## What is uncertain

- The public web page wording says "12:00 in the ET timezone (noon)" but does not independently clarify whether the operationally decisive candle should be mapped as the candle opening at 12:00 ET or the one closing at 12:00 ET; the market text says "candle for BTC/USDT 12:00 ... final Close price," which practically points to the 12:00 ET one-minute bar as displayed by Binance.
- Live spot being above 72k now does not guarantee the 2026-04-17 noon ET minute closes above 72k.
- Binance-specific operational issues, wickiness, or a venue-local dislocation could matter because this is not an all-exchange benchmark contract.

## Why this source may matter

This is the main direct evidence set for both resolution mechanics and baseline price state. It establishes that the question is mostly about whether BTC loses enough ground over the next roughly two days, or suffers a Binance-specific divergence, to finish below 72k at the exact resolution minute.

## Possible impact on the question

The direct evidence pushes the baseline toward Yes because BTC is already comfortably above 72k and the market is resolved by the same venue whose live price is being checked. At the same time, the exchange-specific wording creates a modest variant-view angle: even if broad BTC remains healthy, the contract can still fail on a narrow timing or venue-specific print.

## Reliability notes

- High reliability for contract wording because Polymarket is the market operator.
- High reliability for current spot and minute bars because Binance is the named resolution source.
- Independence is only medium: both the current price and eventual settlement depend on the same venue, which is correct for this contract but reduces cross-source triangulation on venue-specific anomalies.
