---
type: source_note
case_key: case-20260413-63496469
dispatch_id: dispatch-case-20260413-63496469-20260413T173535Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: prediction-market-contract
entity: btc
topic: case-20260413-63496469 | risk-manager
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-14 close above 66000?
driver: reliability
date_created: 2026-04-13
source_name: Polymarket market rules page
source_type: contract_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-63496469/researcher-analyses/2026-04-13/dispatch-case-20260413-63496469-20260413T173535Z/personas/risk-manager.md]
tags: [polymarket, contract, resolution, source-of-truth]
---

# Summary

Polymarket rules specify that this market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 14, using the final close price, with Yes requiring a close strictly higher than 66000.

## Key facts extracted

- Resolution source is Binance BTC/USDT.
- Relevant observation is the 1-minute candle for `12:00` in the ET timezone on the date in the title.
- The decisive field is the candle's final `Close` price.
- The condition is `higher than` the threshold, not greater-than-or-equal.
- Price precision follows the source's displayed decimal places.

## Evidence directly stated by source

- The rules directly define what all material conditions are for Yes: correct venue, correct pair, correct minute, correct timezone, and close price strictly above 66000.

## What is uncertain

- Web fetch provided page text rather than a structured API or screenshot of the live UI, so downstream reviewers may still want a final-time manual confirmation of the exact settlement candle display if there is any dispute.
- The page does not itself provide the future settlement value.

## Why this source may matter

This is the contract-mechanics source. It governs which exchange, pair, minute, timezone, and comparison operator matter.

## Possible impact on the question

It narrows the true risk surface: non-Binance prices, intraminute spikes, and closes exactly at 66000 would not resolve Yes.

## Reliability notes

High value for contract interpretation because it is the market's own rules page. Independence is limited because it is the market operator describing its own contract, so it should be paired with a direct Binance source for the price surface.