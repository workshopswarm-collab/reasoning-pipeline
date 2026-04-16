---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules for Bitcoin above ___ on April 16
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-implied, binance]
---

# Summary

This source provides both the live market-implied probability for the $72,000 threshold and the governing contract mechanics. It is the authoritative source for what the market is pricing and a direct source for the resolution conditions, but not for the underlying Binance settlement price itself.

## Key facts extracted

- The relevant threshold market is `72,000` and the page showed roughly `90%` for "Yes" at fetch time, consistent with the assignment's `current_price: 0.895`.
- The contract resolves based on the Binance BTC/USDT **1 minute candle for 12:00 in ET timezone (noon)** on April 16, 2026.
- The contract requires the final **Close** price of that candle to be **higher than** $72,000, not equal to it.
- The resolution source is Binance BTC/USDT with `1m` candles selected.
- The contract is specifically about **Binance BTC/USDT**, not other exchanges or other trading pairs.
- Price precision is determined by the number of decimals shown by the source.

## Evidence directly stated by source

- Current crowd pricing around 90% for the 72k threshold.
- Exact wording of the settlement rule and source-of-truth exchange/pair.
- Clear multi-condition structure: correct date, correct timezone, correct exchange, correct pair, correct candle interval, correct field (`Close`), and strict `>` comparison.

## What is uncertain

- The page itself is not the final settlement print; it only states where settlement will come from.
- The fetched web representation is not a structured API response, so the displayed market price should be treated as a close contextual reference rather than a machine-verified market history series.

## Why this source may matter

This is the governing source for contract interpretation. For a date-sensitive, rule-sensitive market, misunderstanding even one condition (for example UTC vs ET or spot price vs candle close) could flip the answer.

## Possible impact on the question

It anchors the analysis around whether BTC/USDT on Binance is likely to remain above 72k specifically at **2026-04-16 12:00 ET / 16:00 UTC**. It also explains why cross-exchange prices are contextual rather than dispositive.

## Reliability notes

High relevance and reasonably reliable for contract terms because it is the host market itself. Independence is low for the market-implied probability because it is the same venue being analyzed. It must be paired with at least one external price/context source.