---
type: research_case
case_key: case-20260415-868fc947
case_id: 48d7cfdb-757c-4f26-a2b7-3fe6872de771
market_id: 7da0bb87-594f-4bdb-a7ae-fddfc3f0f8bd
platform: polymarket
external_market_id: 0xee2d4eeeae30d06342d630e97c23ff423da2e542cbfb30a8ce252b9f47ccc9e3
slug: bitcoin-above-72k-on-april-16
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $72,000 on April 16?

## Case identity
- case_key: `case-20260415-868fc947`
- case_id: `48d7cfdb-757c-4f26-a2b7-3fe6872de771`
- market_id: `7da0bb87-594f-4bdb-a7ae-fddfc3f0f8bd`
- platform: `polymarket`
- external_market_id: `0xee2d4eeeae30d06342d630e97c23ff423da2e542cbfb30a8ce252b9f47ccc9e3`
- slug: `bitcoin-above-72k-on-april-16`

## Market context
- current_price: `0.875`
- closes_at: `2026-04-16T12:00:00-04:00`
- resolves_at: `2026-04-16T12:00:00-04:00`

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
