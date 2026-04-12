---
type: research_case
case_key: case-20260409-da826a3f
case_id: 98dcb25a-8c4d-4128-b276-f61f27ce4973
market_id: 5df39648-01c8-4bd8-a740-53b89c46ec45
platform: polymarket
external_market_id: 0xd537f4bd3d09f79083ffdf2170686125a1501644970554b34916cb79d5d43ac0
slug: bitcoin-above-68k-on-april-10
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $68,000 on April 10?

## Case identity
- case_key: `case-20260409-da826a3f`
- case_id: `98dcb25a-8c4d-4128-b276-f61f27ce4973`
- market_id: `5df39648-01c8-4bd8-a740-53b89c46ec45`
- platform: `polymarket`
- external_market_id: `0xd537f4bd3d09f79083ffdf2170686125a1501644970554b34916cb79d5d43ac0`
- slug: `bitcoin-above-68k-on-april-10`

## Market context
- current_price: `0.959`
- closes_at: `2026-04-10T12:00:00-04:00`
- resolves_at: `2026-04-10T12:00:00-04:00`

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
