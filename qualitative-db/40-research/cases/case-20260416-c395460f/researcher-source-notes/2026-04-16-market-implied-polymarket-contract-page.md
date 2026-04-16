---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: prediction-markets
entity: sol
topic: case-20260416-c395460f | market-implied
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close be above 80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page
source_type: market_contract_page
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium_high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract, resolution, threshold-market, market-implied]
---

# Summary

The Polymarket event page provided the live market-implied probability and the exact settlement wording, including the noon-ET timing and Binance 1-minute close requirement.

## Key facts extracted

- The listed probability for the 80 threshold was about 89% on the fetched page, consistent with the assignment context current_price 0.89.
- The market covers April 19, 2026 at 12:00 PM ET.
- Resolution depends on the Binance SOL/USDT 1-minute candle for 12:00 ET, specifically the final close of that minute.
- The threshold is strict: the close must be higher than 80, not equal to 80.
- Price precision follows the source's decimal precision.

## Evidence directly stated by source

- Market-implied probability around 89% for above 80.
- Exact contract wording and governing source-of-truth instructions.

## What is uncertain

- The fetched public page is not the final settlement record; it is a live market surface.
- The page does not itself prove future price direction.

## Why this source may matter

This source is necessary to avoid contract-interpretation mistakes. A short-dated threshold market can be misread if one ignores the exact timestamp, exchange, pair, or strict comparison operator.

## Possible impact on the question

It raises confidence that the central issue is short-horizon price path risk around a well-defined noon-ET candle, not broad ambiguity about what counts.

## Reliability notes

Strong for market-implied probability and wording; lower than Binance itself for underlying spot data because Polymarket is quoting a derivative market, not the settlement price directly.