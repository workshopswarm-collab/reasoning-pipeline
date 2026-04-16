---
type: source_note
case_key: case-20260415-6580bcd8
dispatch_id: dispatch-case-20260415-6580bcd8-20260415T081158Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page for Bitcoin above ___ on April 17
source_type: market rules / resolution source summary
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6580bcd8/researcher-analyses/2026-04-15/dispatch-case-20260415-6580bcd8-20260415T081158Z/personas/base-rate.md]
tags: [polymarket, rules, resolution, binance, btc]
---

# Summary

This source establishes the contract mechanics: the market resolves from Binance BTC/USDT, specifically the 1-minute candle for 12:00 in ET on April 17, using the final Close price. The threshold test is strictly whether that final Close is higher than 72,000.

## Key facts extracted

- Resolution source is Binance BTC/USDT, not another exchange or pair.
- The relevant observation is the 1-minute candle labeled 12:00 in ET timezone on the specified date.
- The deciding field is the final candle Close.
- The threshold condition is strictly greater than 72,000.
- Price precision is determined by the decimal places shown by the source.

## Evidence directly stated by source

The rules page states that the market resolves to Yes if the Binance 1 minute candle for BTC/USDT 12:00 in ET timezone on the specified date has a final Close above the listed threshold, otherwise No.

## What is uncertain

- The public page names Binance web UI as the source surface but does not independently explain how Binance labels candle times across timezone display settings.
- The page itself does not provide a worked example for edge cases around exactly 72,000.00000000, though "higher than" implies equality resolves No.

## Why this source may matter

This is the governing contract surface. It determines what all other evidence must map onto.

## Possible impact on the question

It narrows the problem from a generic Bitcoin price forecast to a very specific exchange/pair/time-window settlement event. That lowers source ambiguity but increases importance of timing interpretation and Binance-specific operational details.

## Reliability notes

Useful and necessary as the governing rules source, but not fully sufficient alone because it is still a market-hosted restatement of the resolution method rather than the underlying Binance data surface itself.