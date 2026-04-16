---
type: source_note
case_key: case-20260415-cd803ba3
dispatch_id: dispatch-case-20260415-cd803ba3-20260415T203927Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-cd803ba3 | market-implied
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page for bitcoin-above-on-april-17
source_type: market page / primary contract surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-cd803ba3/researcher-analyses/2026-04-15/dispatch-case-20260415-cd803ba3-20260415T203927Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-price, binance-resolution]
---

# Summary

Polymarket currently prices the $74,000 line around 63-70% depending on scrape point; the assignment context gives `current_price: 0.7`, while the fetched event page showed the 74,000 row at 63%. The page also states the governing resolution rule: the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, specifically the final candle "Close" price, and "higher than" $74,000 is required.

## Key facts extracted

- Market question is whether BTC/USDT on Binance closes above 74,000 on the 12:00 ET one-minute candle on 2026-04-17.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- Contract requires the final close to be strictly higher than 74,000; equality would resolve No.
- Assignment metadata states current price `0.7`.
- Web fetch of the event page showed the 74,000 contract at 63% at fetch time, indicating some scrape timing / page-state mismatch but same directional baseline: market modestly favors Yes.

## Evidence directly stated by source

- The source explicitly names Binance BTC/USDT as source of truth.
- The source explicitly names the relevant reporting window: the 12:00 ET one-minute candle on April 17.
- The source explicitly says the price threshold must be exceeded, not merely touched.

## What is uncertain

- The fetched web page may lag the exact live assignment price, since it showed 63% while assignment context states 70%.
- The page itself does not supply Binance candle data ahead of resolution, so it cannot answer the market directly yet.

## Why this source may matter

This is the primary contract/rules surface and therefore the governing source for what counts, when it counts, and what exact market probability is being compared against.

## Possible impact on the question

This source sets the correct interpretation: the question is not general BTC spot direction, but whether the Binance BTC/USDT close for one precise minute at noon ET tomorrow is strictly above 74,000. That narrows the problem to short-horizon price level probability and timing sensitivity.

## Reliability notes

High reliability for contract interpretation and market-implied baseline. Lower reliability for exact live displayed odds because scrape timing or dynamic-page state can differ from assignment metadata.