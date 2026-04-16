---
type: research_case
case_key: case-20260414-91430615
case_id: 85e993e8-f355-4efa-99a8-4db53cfd4da9
market_id: 00b2316a-1303-48a8-bfec-d7743c2a4264
platform: polymarket
external_market_id: 0x181bd38eac20ef70a12daab11f081f999991b044ad46c3d4ee468d97aee461a5
slug: bitcoin-above-70k-on-april-19
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 19?

## Case identity
- case_key: `case-20260414-91430615`
- case_id: `85e993e8-f355-4efa-99a8-4db53cfd4da9`
- market_id: `00b2316a-1303-48a8-bfec-d7743c2a4264`
- platform: `polymarket`
- external_market_id: `0x181bd38eac20ef70a12daab11f081f999991b044ad46c3d4ee468d97aee461a5`
- slug: `bitcoin-above-70k-on-april-19`

## Market context
- current_price: `0.9`
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
