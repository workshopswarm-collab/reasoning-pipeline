---
type: research_case
case_key: case-20260415-5ecb60de
case_id: af3d9ace-bed1-4e1a-9fed-2a300456068e
market_id: 139f80d9-bf3b-4b6b-9dea-031313b6ae5b
platform: polymarket
external_market_id: 0x00b28e37776a7f2f56ceec3bc4cf4f49d832b1c9db1ddd1cb597fb4438918f95
slug: solana-above-80-on-april-19
status: active
generated_by: orchestrator
---

# Will the price of Solana be above $80 on April 19?

## Case identity
- case_key: `case-20260415-5ecb60de`
- case_id: `af3d9ace-bed1-4e1a-9fed-2a300456068e`
- market_id: `139f80d9-bf3b-4b6b-9dea-031313b6ae5b`
- platform: `polymarket`
- external_market_id: `0x00b28e37776a7f2f56ceec3bc4cf4f49d832b1c9db1ddd1cb597fb4438918f95`
- slug: `solana-above-80-on-april-19`

## Market context
- current_price: `0.9`
- closes_at: `2026-04-19T12:00:00-04:00`
- resolves_at: `2026-04-19T12:00:00-04:00`

## Description
This market will resolve to "Yes" if the Binance 1 minute candle for SOL/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".

The resolution source for this market is Binance, specifically the SOL/USDT "Close" prices currently available at https://www.binance.com/en/trade/SOL_USDT with "1m" and "Candles" selected on the top bar.

Please note that this market is about the price according to Binance SOL/USDT, not according to other exchanges or trading pairs.

Price precision is determined by the number of decimal places in the source.

## Case surfaces
- `researcher-swarm-current.md` = latest/current researcher swarm pointers
- `timeline.md` = programmatic lifecycle summary
- `researcher-source-notes/` = case-level source provenance across researcher analyses
- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only researcher analysis generations
