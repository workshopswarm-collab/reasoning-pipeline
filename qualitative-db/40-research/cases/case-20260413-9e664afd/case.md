---
type: research_case
case_key: case-20260413-9e664afd
case_id: 11e3012e-3168-423a-859b-3ee8eeaad746
market_id: 343b4125-9ce7-4238-81ad-f534fc4c6fae
platform: polymarket
external_market_id: 0xb4edd1ceca7ae170d1ed632677a8671797b3d47374d38ffac7d410cfb9e9f5c7
slug: bitcoin-above-70k-on-april-14
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $70,000 on April 14?

## Case identity
- case_key: `case-20260413-9e664afd`
- case_id: `11e3012e-3168-423a-859b-3ee8eeaad746`
- market_id: `343b4125-9ce7-4238-81ad-f534fc4c6fae`
- platform: `polymarket`
- external_market_id: `0xb4edd1ceca7ae170d1ed632677a8671797b3d47374d38ffac7d410cfb9e9f5c7`
- slug: `bitcoin-above-70k-on-april-14`

## Market context
- current_price: `0.845`
- closes_at: `2026-04-14T12:00:00-04:00`
- resolves_at: `2026-04-14T12:00:00-04:00`

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
