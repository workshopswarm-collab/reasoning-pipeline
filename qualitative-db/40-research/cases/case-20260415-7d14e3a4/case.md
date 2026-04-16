---
type: research_case
case_key: case-20260415-7d14e3a4
case_id: fa83069e-7f0f-4e0e-9566-da60657a6614
market_id: b8af2a6b-b2cc-4f28-9c10-9cc5807007e1
platform: polymarket
external_market_id: 0x96dd7e4c2eb7fda6bc3b2a593ac07eb1b1cc99c51ea086bd923208ee49cd1f98
slug: bitcoin-above-72k-on-april-19
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $72,000 on April 19?

## Case identity
- case_key: `case-20260415-7d14e3a4`
- case_id: `fa83069e-7f0f-4e0e-9566-da60657a6614`
- market_id: `b8af2a6b-b2cc-4f28-9c10-9cc5807007e1`
- platform: `polymarket`
- external_market_id: `0x96dd7e4c2eb7fda6bc3b2a593ac07eb1b1cc99c51ea086bd923208ee49cd1f98`
- slug: `bitcoin-above-72k-on-april-19`

## Market context
- current_price: `0.865`
- closes_at: `2026-04-19T12:00:00-04:00`
- resolves_at: `2026-04-19T12:00:00-04:00`

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
