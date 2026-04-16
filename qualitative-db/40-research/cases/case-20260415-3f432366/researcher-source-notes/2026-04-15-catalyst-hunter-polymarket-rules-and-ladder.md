---
type: source_note
case_key: case-20260415-3f432366
dispatch_id: dispatch-case-20260415-3f432366-20260415T074424Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: prediction-markets
entity:
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket event page and market rules
source_type: market rules / market pricing
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3f432366/researcher-analyses/2026-04-15/dispatch-case-20260415-3f432366-20260415T074424Z/personas/catalyst-hunter.md]
tags: [polymarket, contract-rules, resolution, implied-probability]
---

# Summary

The Polymarket page provides the contract wording, the current implied probability, and the precise settlement mechanic: the Binance BTC/USDT 1-minute candle at 12:00 ET on Apr 17 must have a final close strictly above 72,000.

## Key facts extracted

- Current market-implied probability for the 72,000 line is roughly `75%` to `76%` on the event page.
- The contract resolves from the Binance BTC/USDT 1-minute candle for `12:00` in ET timezone on Apr 17.
- The operative field is the final candle `Close` price, not any intraminute high, daily close, or price from another exchange.
- The rule requires price to be **higher than** 72,000, not equal to 72,000.

## Evidence directly stated by source

- Event page listed the `72,000` outcome at about `75%`/`76%`.
- Rules text states the market resolves Yes if the Binance 1-minute candle for BTC/USDT 12:00 in ET timezone has a final Close price higher than the specified threshold.
- Rules text states the source is Binance with `1m` and `Candles` selected.
- Rules text states price precision is determined by the source and that other exchanges or trading pairs do not count.

## What is uncertain

- The event page is a secondary display of market odds and may shift quickly.
- The public page does not itself provide a historical audit trail for the exact settlement candle yet, since settlement is in the future.

## Why this source may matter

This is the authoritative contract-definition source. It determines which price counts, what timestamp matters, and the strict inequality needed for Yes.

## Possible impact on the question

The resolution mechanics make timing unusually important. A generally bullish BTC view is not enough; all material analysis must reduce to whether Binance BTCUSDT is likely to print a final 12:00 ET one-minute close above 72,000 on Apr 17.

## Reliability notes

- High reliability for contract interpretation and market-implied baseline.
- Not independent from the market price itself, so it should be paired with exchange data and a contextual market source.