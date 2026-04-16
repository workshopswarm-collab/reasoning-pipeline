---
type: research_case
case_key: case-20260416-881aa4d0
case_id: e971a505-c1fd-48f4-a808-e9671cb9f951
market_id: 02f818d5-3451-482c-ba4b-0a663270e680
platform: polymarket
external_market_id: 0x80281108ecd458d73c9e0eafe0946a91645d98771f1326e565657b6f8dcc00e6
slug: bitcoin-above-70k-on-april-17
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 17?

## Case identity
- case_key: `case-20260416-881aa4d0`
- case_id: `e971a505-c1fd-48f4-a808-e9671cb9f951`
- market_id: `02f818d5-3451-482c-ba4b-0a663270e680`
- platform: `polymarket`
- external_market_id: `0x80281108ecd458d73c9e0eafe0946a91645d98771f1326e565657b6f8dcc00e6`
- slug: `bitcoin-above-70k-on-april-17`

## Market context
- current_price: `0.9905`
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
