---
type: research_case
case_key: case-20260413-395c5631
case_id: 566dcf26-4f27-48a7-9f69-30366853666e
market_id: 3fc6402b-4650-461d-9068-18ee4cd7525a
platform: polymarket
external_market_id: 0x7bdc81de7fa3bafa5ac9d027ff0a88d2b52e13a9b7b6872e2b49d4d281ae4f94
slug: bitcoin-above-72k-on-april-15
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $72,000 on April 15?

## Case identity
- case_key: `case-20260413-395c5631`
- case_id: `566dcf26-4f27-48a7-9f69-30366853666e`
- market_id: `3fc6402b-4650-461d-9068-18ee4cd7525a`
- platform: `polymarket`
- external_market_id: `0x7bdc81de7fa3bafa5ac9d027ff0a88d2b52e13a9b7b6872e2b49d4d281ae4f94`
- slug: `bitcoin-above-72k-on-april-15`

## Market context
- current_price: `0.725`
- closes_at: `2026-04-15T12:00:00-04:00`
- resolves_at: `2026-04-15T12:00:00-04:00`

## Description
This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".

The resolution source for this market is Binance, specifically the BTC/USDT "Close" prices currently available at https://www.binance.com/en/trade/BTC_USDT with "1m" and "Candles" selected on the top bar.

Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs.

Price precision is determined by the number of decimal places in the source.

## Case surfaces
- `researcher-swarm-current.md` = latest/current researcher swarm pointers
- `timeline.md` = programmatic lifecycle summary
- `researcher-source-notes/` = case-level source provenance across researcher analyses
- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only researcher analysis generations
