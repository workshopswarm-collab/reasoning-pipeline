---
type: research_case
case_key: case-20260409-a6f5ffd8
case_id: bac7b54a-d0f7-4bd0-acc9-99754b87e093
market_id: 0bdf6579-0b96-43d3-95ea-eb32e0aeffe9
platform: polymarket
external_market_id: 0xb7e39472bbbd16b27344f130f97cd00aafe31143d437c914bd79bed10cee7408
slug: bitcoin-above-70k-on-april-9
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 9?

## Case identity
- case_key: `case-20260409-a6f5ffd8`
- case_id: `bac7b54a-d0f7-4bd0-acc9-99754b87e093`
- market_id: `0bdf6579-0b96-43d3-95ea-eb32e0aeffe9`
- platform: `polymarket`
- external_market_id: `0xb7e39472bbbd16b27344f130f97cd00aafe31143d437c914bd79bed10cee7408`
- slug: `bitcoin-above-70k-on-april-9`

## Market context
- current_price: `0.785`
- closes_at: `2026-04-09T12:00:00-04:00`
- resolves_at: `2026-04-09T12:00:00-04:00`

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
