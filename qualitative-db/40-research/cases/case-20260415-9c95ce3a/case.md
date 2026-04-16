---
type: research_case
case_key: case-20260415-9c95ce3a
case_id: 05e7de4e-003e-413f-b6d1-7b6457289985
market_id: 34b19a2f-03db-4e0f-ba94-a0ddb3b0670c
platform: polymarket
external_market_id: 0x278e937ecb8ff1da49c4e04aba52d1922b3e0a7a15d09e621bbf33154c230287
slug: bitcoin-above-72k-on-april-17
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $72,000 on April 17?

## Case identity
- case_key: `case-20260415-9c95ce3a`
- case_id: `05e7de4e-003e-413f-b6d1-7b6457289985`
- market_id: `34b19a2f-03db-4e0f-ba94-a0ddb3b0670c`
- platform: `polymarket`
- external_market_id: `0x278e937ecb8ff1da49c4e04aba52d1922b3e0a7a15d09e621bbf33154c230287`
- slug: `bitcoin-above-72k-on-april-17`

## Market context
- current_price: `0.82`
- closes_at: `2026-04-17T12:00:00-04:00`
- resolves_at: `2026-04-17T12:00:00-04:00`

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
