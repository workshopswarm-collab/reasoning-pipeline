---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: ethereum
topic: case-20260416-969f7c01 | risk-manager
question: Will the Binance ETH/USDT 1-minute candle closing at 12:00 ET on 2026-04-17 close above 2200?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-969f7c01/researcher-analyses/2026-04-16/dispatch-case-20260416-969f7c01-20260416T013210Z/personas/risk-manager.md]
tags: [source-note, polymarket, contract, market-implied-probability]
---

# Summary

Polymarket’s market page defines the exact resolution mechanics and shows the current market-implied probability for the 2200 threshold leg. This is the governing contract wording for what counts, though Binance is the ultimate source of truth for settlement.

## Key facts extracted

- Market resolves "Yes" if the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 has a final close strictly higher than 2200.
- Otherwise it resolves "No".
- Resolution source is Binance ETH/USDT with 1m candles selected.
- Price precision is determined by Binance source precision.
- The visible market pricing for the 2200 leg was about 95% Yes / 6% No at fetch time, matching assignment current_price 0.945 approximately.

## Evidence directly stated by source

- The page explicitly states Binance ETH/USDT 1-minute candle at 12:00 ET is the settlement basis.
- The page explicitly states other exchanges or trading pairs do not count.
- The page explicitly states the contract requires the close to be higher than the threshold.

## What is uncertain

- The market page is not itself the final settlement database; Binance data is.
- The page does not independently explain whether exchange/API outages or temporary display issues could complicate retrieval, though the contract points to Binance as source.

## Why this source may matter

This source governs what must be true for the market to resolve Yes. It removes ambiguity about venue, pair, timestamp, and comparator.

## Possible impact on the question

The contract wording makes this a narrow, timing-sensitive, exchange-specific question rather than a broad "ETH trades above 2200 sometime that day" question. That raises operational and timestamp risk, but because spot ETH/USDT is already materially above 2200, the remaining risk is mostly path/timing risk rather than threshold distance.

## Reliability notes

Useful and necessary for contract interpretation, but not fully independent because it is the market operator’s own page. Settlement still depends on Binance as the ultimate external source.