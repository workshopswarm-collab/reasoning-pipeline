---
type: research_case
case_key: case-20260416-b80742d2
case_id: 93fd42ef-caf6-4c6a-a632-7e9a4f029c69
market_id: 471f03a4-fe72-4cb2-84b3-51ecddf2d352
platform: polymarket
external_market_id: 0x5dd98f44ae358d59b1b1a651036568b9693f0b5faa642e74c9c63f095cbebefd
slug: xrp-above-1pt3-on-april-19
status: active
generated_by: orchestrator
---

# Will the price of XRP be above $1.30 on April 19?

## Case identity
- case_key: `case-20260416-b80742d2`
- case_id: `93fd42ef-caf6-4c6a-a632-7e9a4f029c69`
- market_id: `471f03a4-fe72-4cb2-84b3-51ecddf2d352`
- platform: `polymarket`
- external_market_id: `0x5dd98f44ae358d59b1b1a651036568b9693f0b5faa642e74c9c63f095cbebefd`
- slug: `xrp-above-1pt3-on-april-19`

## Market context
- current_price: `0.95`
- closes_at: `2026-04-19T12:00:00-04:00`
- resolves_at: `2026-04-19T12:00:00-04:00`

## Description
This market will resolve to "Yes" if the Binance 1 minute candle for XRP/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title. Otherwise, this market will resolve to "No".

The resolution source for this market is Binance, specifically the XRP/USDT "Close" prices currently available at https://www.binance.com/en/trade/XRP_USDT with "1m" and "Candles" selected on the top bar.

Please note that this market is about the price according to Binance XRP/USDT, not according to other exchanges or trading pairs.

Price precision is determined by the number of decimal places in the source.

## Case surfaces
- `researcher-swarm-current.md` = latest/current researcher swarm pointers
- `timeline.md` = programmatic lifecycle summary
- `researcher-source-notes/` = case-level source provenance across researcher analyses
- `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = append-only researcher analysis generations
