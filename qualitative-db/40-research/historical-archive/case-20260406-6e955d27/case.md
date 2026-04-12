---
type: research_case
case_key: case-20260406-6e955d27
case_id: 6b5183c4-58e3-48dc-98bc-8edc6e7dce0d
market_id: a38c7b49-5885-4c48-b1e9-2dd137cd38ab
platform: polymarket
external_market_id: 0x1d46d3d1f080e4ac1441cebe8965d796189224f0f91eae8a481b6322180ec0ad
slug: bitcoin-above-66k-on-april-6
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $66,000 on April 6?

## Case identity
- case_key: `case-20260406-6e955d27`
- case_id: `6b5183c4-58e3-48dc-98bc-8edc6e7dce0d`
- market_id: `a38c7b49-5885-4c48-b1e9-2dd137cd38ab`
- platform: `polymarket`
- external_market_id: `0x1d46d3d1f080e4ac1441cebe8965d796189224f0f91eae8a481b6322180ec0ad`
- slug: `bitcoin-above-66k-on-april-6`

## Market context
- current_price: `0.825`
- closes_at: `2026-04-06T12:00:00-04:00`
- resolves_at: `2026-04-06T12:00:00-04:00`

## Description
This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".

The resolution source for this market is Binance, specifically the BTC/USDT "Close" prices currently available at https://www.binance.com/en/trade/BTC_USDT with "1m" and "Candles" selected on the top bar.

Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs.

Price precision is determined by the number of decimal places in the source.

## Case surfaces
- `researcher-swarm-current.md` = latest/current researcher swarm pointers
- `timeline.md` = programmatic lifecycle summary
- `researcher-source-notes/` = case-level source provenance across analyses
- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only analysis generations
