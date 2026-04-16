---
type: source_note
case_key: case-20260415-2cba3460
dispatch_id: dispatch-case-20260415-2cba3460-20260415T115730Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-pricing]
---

# Summary

This source establishes both the current market-implied probability and the exact contract mechanics. It is not the final settlement source itself, but it specifies that settlement depends on Binance BTC/USDT with 1m candles and the 12:00 ET candle on April 16.

## Key facts extracted

- The relevant threshold market is **72,000**.
- The displayed market-implied probability for "above 72,000" is about **89%**.
- The market resolves to Yes if the **Binance BTC/USDT 1 minute candle for 12:00 ET (noon)** on 2026-04-16 has a final **Close** price above 72,000.
- The source explicitly says the settlement source is Binance, not other exchanges or pairs.
- Price precision is determined by the number of decimal places in the source.

## Evidence directly stated by source

- The contract is tied to the **Binance BTC/USDT close price**, not spot aggregates.
- The relevant timestamp is **12:00 ET** on the date in the title.
- The page displayed the 72k line at roughly **89%** when checked.

## What is uncertain

- The market page itself is not the authoritative price feed; it only points to Binance as the authority.
- The fetched page is a rendered public page snapshot, so intraday price display could move after capture.

## Why this source may matter

The case is rule-sensitive and date-sensitive. This source defines what must happen for the contract to resolve Yes and provides the market-implied baseline against which the research estimate should be compared.

## Possible impact on the question

This source anchors the analysis around the correct reference pair, correct exchange, correct price field (Close), and correct time window. It also shows that the market is already pricing a high likelihood of Yes, so any disagreement needs stronger verification than usual.

## Reliability notes

Useful and necessary for contract interpretation, but secondary for the actual price outcome because the authoritative source-of-truth is Binance itself.