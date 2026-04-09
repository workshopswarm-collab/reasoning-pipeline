---
type: source_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: prediction-market-rules
entity: ethereum
topic: case-20260409-21554cf3 | risk-manager
question: Will the price of Ethereum be above $2,100 on April 9?
driver: operational-risk
date_created: 2026-04-09T03:36:10-04:00
source_name: Polymarket event rules page
source_type: market rules / contextual source
source_url: https://polymarket.com/event/ethereum-above-on-april-9
source_date: 2026-04-09
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: risk-manager
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, source-of-truth, timezone]
---

# Summary

Polymarket's market page provides the operative contract wording: settlement depends on the Binance ETH/USDT 1-minute candle for 12:00 ET on April 9, with a Yes resolution only if the final close is higher than 2,100.

## Key facts extracted

- The market resolves Yes if the Binance 1-minute candle for ETH/USDT at 12:00 in the ET timezone has a final close above the threshold in the title.
- The resolution source is specified as Binance, specifically the ETH/USDT market with 1m candles selected.
- The market is explicitly about Binance ETH/USDT, not other exchanges or other trading pairs.
- Price precision is determined by the number of decimal places in the source.
- The displayed current market price for the 2,100 bracket was about 97% on the fetched page, somewhat above the assignment snapshot of 95.15%.

## Evidence directly stated by source

- The contract wording directly states what counts for resolution.
- The page directly identifies the venue, pair, interval, timezone, and comparison operator.

## What is uncertain

- The fetched page is a rendered web surface, not the eventual settlement memo itself.
- The page points users to the Binance trading interface, but does not explain whether any exchange outages or UI/API discrepancies would be handled specially.
- A fetched market price on the page may differ from the assignment snapshot due to movement or page caching.

## Why this source may matter

This is the key contextual source for interpreting the contract mechanics correctly and for avoiding false reliance on non-Binance spot prices or wrong timezone assumptions.

## Possible impact on the question

The rules make this a narrow timing-and-source problem rather than a general ETH sentiment question. That materially limits the thesis: being bullish ETH broadly is not enough; the position still depends on one exact Binance minute close at noon ET.

## Reliability notes

- Strong contextual reliability for contract interpretation.
- Not independent from the market itself, so it should be paired with a direct Binance check for evidence sufficiency.
- Main value is clarifying what counts, not proving the eventual outcome.