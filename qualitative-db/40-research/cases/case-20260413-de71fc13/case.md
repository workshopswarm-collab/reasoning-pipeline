---
type: research_case
case_key: case-20260413-de71fc13
case_id: ab91a3ff-55fb-4b5e-a6c6-8be967ef2cea
market_id: 505a9a16-f0f2-4510-a416-df2a568b8c24
platform: polymarket
external_market_id: 0x06111b1cdb7ec493e413a5691c410ce3423c86929d0b168f6078e341adbb6a46
slug: bitcoin-above-68k-on-april-13
status: active
generated_by: orchestrator
---

# Will the price of Bitcoin be above $68,000 on April 13?

## Case identity
- case_key: `case-20260413-de71fc13`
- case_id: `ab91a3ff-55fb-4b5e-a6c6-8be967ef2cea`
- market_id: `505a9a16-f0f2-4510-a416-df2a568b8c24`
- platform: `polymarket`
- external_market_id: `0x06111b1cdb7ec493e413a5691c410ce3423c86929d0b168f6078e341adbb6a46`
- slug: `bitcoin-above-68k-on-april-13`

## Market context
- current_price: `0.929`
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
