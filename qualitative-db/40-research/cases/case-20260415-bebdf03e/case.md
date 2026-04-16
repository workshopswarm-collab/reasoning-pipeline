---
type: research_case
case_key: case-20260415-bebdf03e
case_id: 85c57a7f-0186-4d81-b95b-00812d026bc1
market_id: 6c5bfff7-39b3-49d4-bb33-c8b7881a4e51
platform: polymarket
external_market_id: 0x98836967b3291ac597477867ab3e5d141ec344cac432df45f0aea9539fb5c4f2
slug: bitcoin-above-72k-on-april-21
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $72,000 on April 21?

## Case identity
- case_key: `case-20260415-bebdf03e`
- case_id: `85c57a7f-0186-4d81-b95b-00812d026bc1`
- market_id: `6c5bfff7-39b3-49d4-bb33-c8b7881a4e51`
- platform: `polymarket`
- external_market_id: `0x98836967b3291ac597477867ab3e5d141ec344cac432df45f0aea9539fb5c4f2`
- slug: `bitcoin-above-72k-on-april-21`

## Market context
- current_price: `0.815`
- closes_at: `2026-04-21T12:00:00-04:00`
- resolves_at: `2026-04-21T12:00:00-04:00`

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
