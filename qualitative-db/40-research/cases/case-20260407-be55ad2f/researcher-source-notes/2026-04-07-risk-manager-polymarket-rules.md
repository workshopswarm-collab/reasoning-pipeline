---
type: source_note
case_key: case-20260407-be55ad2f
dispatch_id: dispatch-case-20260407-be55ad2f-20260407T193635Z
analysis_date: 2026-04-07
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: btc
topic: case-20260407-be55ad2f | risk-manager
question: Will the Binance BTC/USDT 1 minute candle for 12:00 ET on 2026-04-08 close above 66000?
driver: operational-risk
date_created: 2026-04-07T19:39:30Z
source_name: Polymarket market rules page
source_type: primary-contract
source_url: https://polymarket.com/event/bitcoin-above-on-april-8
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-be55ad2f/researcher-analyses/2026-04-07/dispatch-case-20260407-be55ad2f-20260407T193635Z/personas/risk-manager.md]
tags: [polymarket, rules, resolution]
---

# Summary

Polymarket's rule text is explicit: the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 8 has a final close price higher than 66,000. The contract further states that price precision is determined by the number of decimal places in the source.

## Key facts extracted

- Resolution source is Binance, specifically BTC/USDT with `1m` and `Candles` selected.
- The relevant time is `12:00` in the ET timezone, not a generic global daily close.
- The deciding field is the final `Close` price of that 1-minute candle.
- The threshold test is strictly `higher than` 66,000.
- Price precision is whatever decimal precision appears in the source.
- The market page showed a current price around 93.2% Yes for the 66,000 line when fetched on 2026-04-07.

## Evidence directly stated by source

- The exact resolution mechanics are directly stated in the rules section.
- The current market-implied probability can be read directly from the market page.

## What is uncertain

- The fetched page is a rendered web surface, so live price quotes may move after fetch.
- The page does not itself explain whether Binance UI candles are internally rendered from UTC with a timezone transform, though it clearly says ET for this contract.

## Why this source may matter

This is the governing market contract text. It defines both the threshold and the required source-of-truth surface.

## Possible impact on the question

The contract wording sharply narrows what counts. General BTC spot consensus, other exchanges, and even other Binance views are secondary unless they bear on the specific BTC/USDT 1-minute Binance close at 12:00 ET.

## Reliability notes

High relevance and high credibility for contract mechanics because this is the market's own rule text. It is not independent from the market operator, but independence is less important here because these are the binding rules.