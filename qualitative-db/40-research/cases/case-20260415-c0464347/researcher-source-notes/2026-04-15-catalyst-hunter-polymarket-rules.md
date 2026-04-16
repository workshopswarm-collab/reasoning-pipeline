---
type: source_note
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event rules page
source_type: market_contract_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-c0464347/researcher-analyses/2026-04-15/dispatch-case-20260415-c0464347-20260415T011958Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, binance, timezone]
---

# Summary

The Polymarket contract page states that this market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 20 has a final close higher than 70,000. This sharply narrows the relevant question to one exchange, one pair, one minute, and one timezone-specific timestamp.

## Key facts extracted

- Governing source of truth is Binance BTC/USDT.
- The relevant interval is the 1-minute candle for 12:00 ET on April 20.
- The field that matters is the final `Close` price.
- Price must be strictly higher than 70,000, not equal.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Yes if the Binance 1 minute candle for BTC/USDT 12:00 ET on the specified date has final close above the threshold.
- Otherwise No.

## What is uncertain

- The page does not discuss edge handling for exchange outages beyond naming Binance as the source.
- It does not say whether users should map ET to EDT explicitly, but current calendar date is in daylight time.

## Why this source may matter

This is the contract definition. It determines what counts, what does not count, and which timing/cross-exchange arguments are irrelevant.

## Possible impact on the question

It makes catalyst analysis mostly about whether anything in the next five days is likely to push Binance BTC/USDT below 70k exactly at noon ET on April 20, not whether BTC sentiment is broadly constructive in some looser sense.

## Reliability notes

- High credibility as the contract page itself.
- Not independent of settlement because it is the market's own rule surface.
- Critical for avoiding false inference from other exchanges, daily closes, or intraday lows.