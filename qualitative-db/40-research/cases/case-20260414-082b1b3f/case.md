---
type: research_case
case_key: case-20260414-082b1b3f
case_id: 77483898-24dc-41d6-b931-1d2abc739273
market_id: 48dcd971-bfc6-4df3-9b7d-b6a0273a42fb
platform: polymarket
external_market_id: 0xdef8763a7c43c10dfd0b31e7de820a54c1327cdfb5d036094b9e2d5469dcf568
slug: solana-above-80-on-april-17
status: active
generated_by: orchestrator
---

# Will the price of Solana be above $80 on April 17?

## Case identity
- case_key: `case-20260414-082b1b3f`
- case_id: `77483898-24dc-41d6-b931-1d2abc739273`
- market_id: `48dcd971-bfc6-4df3-9b7d-b6a0273a42fb`
- platform: `polymarket`
- external_market_id: `0xdef8763a7c43c10dfd0b31e7de820a54c1327cdfb5d036094b9e2d5469dcf568`
- slug: `solana-above-80-on-april-17`

## Market context
- current_price: `0.885`
- closes_at: `2026-04-17T12:00:00-04:00`
- resolves_at: `2026-04-17T12:00:00-04:00`

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
