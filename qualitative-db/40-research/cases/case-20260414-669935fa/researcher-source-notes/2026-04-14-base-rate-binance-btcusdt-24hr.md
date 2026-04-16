---
type: source_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: will-bitcoin-reach-76000-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Binance BTCUSDT 24hr ticker API
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: very-high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/base-rate.md]
tags: [binance, exchange-data, btc-price]
---

# Summary

This source provides a direct, recent exchange-data verification pass on whether BTC traded at or above $76,000 in the most recent 24-hour window.

## Key facts extracted

- lastPrice: 74576.71
- highPrice: 76038.00
- lowPrice: 72053.78
- openPrice: 72510.14
- priceChangePercent: 2.850
- closeTime indicates the data is current to the fetch time on 2026-04-14.

## Evidence directly stated by source

- Binance reports BTCUSDT highPrice = 76038.00 over the last 24 hours.
- That directly exceeds the market threshold of $76,000.

## What is uncertain

- Binance is a strong real-time price source but not necessarily the official settlement reference for Polymarket.
- A 24-hour rolling high is not by itself a full contract transcript; settlement may depend on a specified benchmark/index in the Rules section.

## Why this source may matter

- It is direct evidence that at least one major exchange printed above the threshold during the relevant period.
- It serves as the required extra verification pass for an extreme-probability market.

## Possible impact on the question

- Strongly supports the view that the threshold has already been hit in the relevant weekly window, unless the contract uses a materially different source or benchmark that excluded that print.

## Reliability notes

- High-quality direct market data from a major exchange.
- Best used as direct contextual verification, not as a substitute for the contract's official settlement source.