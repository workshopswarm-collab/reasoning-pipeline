---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: spot-market
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 72000 on April 16, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API BTCUSDT ticker and 1m klines
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2cb747e6/researcher-analyses/2026-04-15/dispatch-case-20260415-2cb747e6-20260415T122916Z/personas/variant-view.md]
tags: [binance, btcusdt, spot, kline, resolution-source]
---

# Summary

Binance is the governing source of truth for this market. A spot API pull on 2026-04-15 around 08:31 ET showed BTCUSDT at 74204.32, already about 3.1% above the 72000 threshold, while recent one-minute klines were trading in the 74163-74213 range.

## Key facts extracted

- `ticker/price?symbol=BTCUSDT` returned `74204.32000000`.
- `klines?symbol=BTCUSDT&interval=1m&limit=5` showed the latest five one-minute candles clustered around 74177 to 74213.
- The instrument is `BTCUSDT` spot and is marked `TRADING` in Binance exchange metadata.
- Binance exchange metadata shows BTCUSDT uses a `PRICE_FILTER` tick size of `0.01000000`, which matters for precision around the threshold.

## Evidence directly stated by source

- Current Binance BTCUSDT spot price was above 72000 at the time checked.
- One-minute candle closes around the check time were comfortably above 72000.
- Binance spot BTCUSDT is an actively trading pair available for the contract's cited source.

## What is uncertain

- The market resolves on the April 16 noon ET one-minute candle close, not the April 15 morning spot print.
- One-minute resolution leaves room for intraday volatility, macro shocks, exchange-specific dislocations, or operational incidents before settlement.

## Why this source may matter

This is the contract-governing source family. It directly informs both the relevant instrument and the precise one-minute-close mechanics that determine settlement.

## Possible impact on the question

Because Binance spot BTCUSDT is already materially above 72000 the day before settlement, the threshold is not a knife-edge case. The remaining path to a "No" outcome likely requires a meaningful downside move, exchange-specific anomaly, or operational disruption before the exact noon ET close on April 16.

## Reliability notes

Primary and highly relevant because the market explicitly resolves from Binance BTCUSDT one-minute candle close data. Reliability risk remains nonzero because exchange APIs and chart views can differ in presentation timing, so final settlement should still anchor to the specified Binance candle close at resolution time.