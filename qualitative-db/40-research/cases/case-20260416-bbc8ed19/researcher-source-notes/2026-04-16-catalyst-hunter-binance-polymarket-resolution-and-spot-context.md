---
type: source_note
case_key: case-20260416-bbc8ed19
dispatch_id: dispatch-case-20260416-bbc8ed19-20260416T072336Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance BTCUSDT market data and Polymarket contract rules
source_type: primary-plus-resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-bbc8ed19/researcher-analyses/2026-04-16/dispatch-case-20260416-bbc8ed19-20260416T072336Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, btcusdt, resolution-source, timing]
---

# Summary

The core direct surfaces for this case are Polymarket's market rules and Binance BTC/USDT spot data. Polymarket states the contract resolves using the Binance BTC/USDT 1-minute candle with timestamp 12:00 ET on April 20, 2026, specifically the final Close price from that candle. Binance spot data on April 16 shows BTC/USDT already trading around 74.9k, i.e. materially above the 72k strike with four calendar days remaining.

## Key facts extracted

- Polymarket market rules say the contract resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026 has a final Close price above 72,000.
- The contract is not based on other exchanges or other pairs; Binance BTC/USDT is the governing source of truth.
- Price precision is whatever Binance displays in the source.
- Binance ticker on 2026-04-16 showed BTCUSDT near 74,884.77 to 74,888.68 during checks.
- Recent Binance daily candles showed BTC trading above 72k for most of the preceding several sessions, with closes around 72.96k, 73.04k, 74.42k, 74.13k, 74.81k, and 74.88k across the last week, after a brief dip as low as ~70.5k intraday on April 11-12.

## Evidence directly stated by source

- Direct rule text from Polymarket: resolution is based on the Binance 1-minute BTC/USDT candle at 12:00 ET on the date in the title, using the candle's final Close.
- Direct market data from Binance: BTC/USDT spot price was approximately 74.9k at time of review.
- Direct market data from Binance daily candles: BTC has recently traded several thousand dollars above the strike, though it has also shown multi-thousand-dollar swings over a few days.

## What is uncertain

- Binance public API checks do not themselves prove where BTC will print at exactly 12:00 ET on April 20.
- The Polymarket page did not fully clarify whether the 12:00 ET candle refers to the minute beginning at 12:00:00 ET or the candle labeled 12:00 after timezone conversion from Binance's native timestamps, though in practice the operative surface is the Binance chart itself with 1m candles selected.
- No separate macro calendar source was pulled in this run; near-term catalysts are inferred from generic weekend-to-Monday crypto flow and volatility behavior rather than a single dated scheduled event.

## Why this source may matter

This is the central source set because it gives both the settlement mechanics and the current distance from strike. For a narrow date-and-time crypto price market, contract interpretation and the exact governing venue matter as much as broader BTC direction.

## Possible impact on the question

The direct source set supports a base view that Yes is favored because BTC is already about 4% above the strike with only four days left. At the same time, the recent intraday range confirms that a move back below 72k by the exact noon-ET print is still plausible enough that 100% certainty would be unjustified.

## Reliability notes

- Polymarket rules are the best available contract-definition source.
- Binance is the stated resolution source and therefore authoritative for settlement, but exchange-specific prints and exact candle labeling introduce some operational interpretation risk.
- Evidence independence is only medium here because the contextual price evidence and settlement source are tightly linked to the same venue.