---
type: source_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: prediction-markets
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market rule page
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, contract]
---

# Summary

The Polymarket market page provides both the current market-implied probability for the $80 threshold and the governing resolution language. It is the key contract-interpretation source for this case but not the final numerical source of truth itself.

## Key facts extracted

- The listed market price for "80" was about 92-93% at fetch time.
- The market resolves Yes if the Binance SOL/USDT 1-minute candle labeled 12:00 in ET on April 19 has a final close strictly higher than 80.
- The resolution source is Binance SOL/USDT with 1m candles selected.
- Price precision is determined by the decimal places shown by the Binance source.

## Evidence directly stated by source

- Resolution depends on Binance SOL/USDT, not other exchanges or pairs.
- The relevant timestamp is 12:00 ET on the specified date.
- The operative field is the candle close, not intraminute high.
- The condition is strictly greater than $80, not greater than or equal to $80.

## What is uncertain

- The market page is not itself the final settlement print; Binance is.
- The public market page can show slightly stale odds or rounded prices.
- The fetched page does not independently verify Binance uptime or any edge-case handling if Binance display/API behavior changes.

## Why this source may matter

This source defines the contract mechanics and therefore determines which catalysts matter. For this case, broad SOL sentiment matters only insofar as it affects the Binance SOL/USDT 12:00 ET one-minute close on April 19.

## Possible impact on the question

Because the contract is a narrow time-window market, the main practical question is whether SOL is likely to remain above $80 into that exact minute rather than merely trade above $80 at some point before then.

## Reliability notes

Good for contract wording and current market baseline. Not sufficient alone for terminal truth because Binance is the governing settlement source.