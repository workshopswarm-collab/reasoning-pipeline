---
type: research_case
case_key: case-20260413-2d3a41aa
case_id: fa000235-7c00-4625-acbe-8d681ac361f9
market_id: ed9459a3-1412-4874-91c9-1b2edcfcaef4
platform: polymarket
external_market_id: 0xbc820c185b6fe8a77c3ac68a54bdcd6ef28667b5f4ec5f09c0ea65002c6ee49e
slug: bitcoin-above-70k-on-april-13
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 13?

## Case identity
- case_key: `case-20260413-2d3a41aa`
- case_id: `fa000235-7c00-4625-acbe-8d681ac361f9`
- market_id: `ed9459a3-1412-4874-91c9-1b2edcfcaef4`
- platform: `polymarket`
- external_market_id: `0xbc820c185b6fe8a77c3ac68a54bdcd6ef28667b5f4ec5f09c0ea65002c6ee49e`
- slug: `bitcoin-above-70k-on-april-13`

## Market context
- current_price: `0.71`
- closes_at: `2026-04-13T12:00:00-04:00`
- resolves_at: `2026-04-13T12:00:00-04:00`

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
