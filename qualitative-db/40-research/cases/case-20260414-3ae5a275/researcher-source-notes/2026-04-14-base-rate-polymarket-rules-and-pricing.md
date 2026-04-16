---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-20 above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
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
downstream_uses: [base-rate-finding]
tags: [polymarket, contract-rules, market-implied-probability, binance]
---

# Summary

This source establishes the market-implied probability and the exact resolution mechanics. It shows the April 20 $70,000 line trading around 86-87% Yes and states that settlement depends specifically on the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone, using the final Close price.

## Key facts extracted

- The relevant line is **Bitcoin above 70,000 on April 20**.
- The market was trading around **86-87% Yes** at collection time.
- Resolution is based on the **Binance BTC/USDT** market, not other exchanges or pairs.
- The decisive observation is the **1-minute candle labeled 12:00 in ET (noon)** on the resolution date.
- The market resolves Yes only if the final **Close** price is **strictly higher** than 70,000.
- Price precision follows Binance source precision.

## Evidence directly stated by source

- Rules text explicitly names Binance as the governing source of truth.
- Rules text explicitly defines the timing window and the required field: the 1-minute candle's final Close.
- The page displays the contemporaneous market-implied probability for the $70,000 threshold.

## What is uncertain

- The public market page is not itself the final settlement source; it quotes the rules but does not independently verify what Binance will show on April 20.
- The phrase "12:00 in the ET timezone" should be interpreted as noon ET on April 20, but the exact candle mapping should still be independently checked against Binance time handling.

## Why this source may matter

This is the primary contract-definition source. Without it, analysis could drift into the wrong exchange, wrong pair, wrong timestamp, or wrong condition.

## Possible impact on the question

The rules matter a lot because the contract is narrow and date-sensitive. A bullish 6-day directional view for BTC is not identical to the probability that the exact Binance BTC/USDT noon-ET 1-minute close on April 20 is above 70,000.

## Reliability notes

Useful and necessary for contract interpretation, but not independently authoritative on future price. Reliability is medium rather than high because Polymarket is describing the settlement rule, not reporting the future resolving datapoint itself.