---
type: source_note
case_key: case-20260414-4e668883
dispatch_id: dispatch-case-20260414-4e668883-20260414T133938Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260414-4e668883 | base-rate
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-14
source_name: Polymarket market page rule text + Binance ETH/USDT market data
source_type: primary_market_rules_and_exchange_data
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [polymarket, binance, resolution-rules, ethereum, price-threshold]
---

# Summary

This source bundle establishes the governing source of truth and the direct threshold evidence for the market. The Polymarket page text states that the market resolves based on whether any Binance 1-minute ETH/USDT candle during the title’s ET date range has a final High at or above the threshold. Binance data fetched during this run shows ETH still below $2,400.

## Key facts extracted

- Polymarket rule text states: the market resolves Yes if any Binance 1-minute candle for ETH/USDT during Apr 13 12:00 AM ET through Apr 19 11:59 PM ET has a final High equal to or greater than $2,400.
- The same rule text identifies Binance ETH/USDT 1-minute High prices as the resolution source.
- Binance daily candles in the recent run-up show highs progressing to 2394.71 and 2396.03, but not 2400.
- Binance 1-hour candles since Apr 13 00:00 UTC in this run showed a maximum High of 2396.03.
- Latest fetched Binance 1-minute candles also showed a maximum High of 2396.03 over the accessible recent window.

## Evidence directly stated by source

- Direct rule text from the Polymarket page: this market resolves based on Binance 1-minute ETH/USDT High prices during the specified ET window.
- Direct exchange data from Binance: observed candle highs remain below the required threshold at the time of checking.

## What is uncertain

- This source does not say what ETH will do for the remainder of Apr 14-19; it only anchors the current state and settlement mechanics.
- The fetched 1-minute window is recent only, so the wider date-range check is supported mainly by 1-hour and daily Binance candles for earlier periods in the week.

## Why this source may matter

This is the closest thing to an authoritative source pair for this market: Polymarket defines the rule and Binance defines the settlement datapoint.

## Possible impact on the question

It strongly supports a high probability that the threshold is plausible but not yet achieved. It also confirms the contract is narrow and mechanical: the only thing that matters is whether Binance prints a 1-minute High >= 2400 in the specified window.

## Reliability notes

Reliability is high for settlement interpretation because the rule text is from the market page itself and the price source is the named exchange. Remaining uncertainty is about future price path, not about what counts for resolution.
