---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle close above 80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API SOLUSDT spot price and recent daily candles
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-07c415fe/researcher-analyses/2026-04-16/dispatch-case-20260416-07c415fe-20260416T031541Z/personas/variant-view.md]
tags: [binance, source-note, spot-price, daily-candles]
---

# Summary

Binance API checks show SOL/USDT spot trading materially above the $80 threshold on 2026-04-16, with recent daily candles mostly in the low-to-mid 80s. This is not settlement data for April 19 noon ET, but it is the most relevant direct context because the contract resolves off Binance SOL/USDT specifically.

## Key facts extracted

- Binance ticker endpoint returned `SOLUSDT` price `85.29000000` when checked on 2026-04-16.
- Recent daily closes from Binance API over the prior week were approximately: 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, and 85.29 (current partial day).
- Recent daily highs/lows in the returned series stayed above and below $80, but closes were consistently above $80 in that sample.
- The assignment market settles on the Binance SOL/USDT one-minute candle at 12:00 ET on 2026-04-19, so Binance is the governing venue and pair.

## Evidence directly stated by source

- Exact current ticker value from Binance API.
- Exact recent OHLC daily candles from Binance API.

## What is uncertain

- The source does not tell us the April 19 12:00 ET one-minute close.
- A crypto asset can move materially in three days, and intraminute noon pricing could differ from broader daily trends.
- Public API access is a strong contextual proxy for the exchange source of truth, but the market text specifies Binance trading UI candles as the formal resolution surface.

## Why this source may matter

This is the closest direct pre-resolution evidence because the contract references Binance SOL/USDT specifically. If spot is already around 85 and recent closes are persistently above 80, the market needs a meaningful downward move before noon ET on April 19 to resolve No.

## Possible impact on the question

This source supports a high Yes probability, but not certainty. It suggests the market’s high implied probability is directionally reasonable, while leaving room for a variant view that 89-92% may still be somewhat overconfident because short-dated crypto downside and exact-timestamp settlement risk remain nontrivial.

## Reliability notes

- High credibility for venue-specific price context because Binance is the named resolution source.
- Best treated as direct contextual evidence rather than definitive settlement evidence, since the relevant one-minute candle has not occurred yet.
- Independence from Polymarket is high, though both depend on Binance as the venue of interest.
