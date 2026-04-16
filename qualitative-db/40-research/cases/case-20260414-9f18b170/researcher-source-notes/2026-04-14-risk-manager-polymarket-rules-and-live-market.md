---
type: source_note
case_key: case-20260414-9f18b170
dispatch_id: dispatch-case-20260414-9f18b170-20260414T142057Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-9f18b170 | risk-manager
question: Will Bitcoin reach $76,000 April 13-19?
driver: liquidity
date_created: 2026-04-14
source_name: Polymarket market page and rules for will-bitcoin-reach-76k-april-13-19
source_type: market_rules_and_live_market_data
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: medium-high
recency: live
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [liquidity]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-analyses/2026-04-14/dispatch-case-20260414-9f18b170-20260414T142057Z/personas/risk-manager.md]
tags: [polymarket, market-rules, resolution-source, live-odds]
---

# Summary

Polymarket’s own page establishes both the current market-implied probability for the $76k threshold and the governing resolution mechanics. The key rule is narrow and clean: this market resolves Yes if any Binance BTC/USDT 1-minute candle from 12:00 AM ET Apr 13 through 11:59 PM ET Apr 19 has a final High at or above $76,000.

## Key facts extracted

- The assigned market is `Will Bitcoin reach $76,000 April 13-19?`
- Live market price observed in page source was approximately 0.91-0.92 for Yes, consistent with assignment current_price 0.89 but slightly higher at fetch time.
- The rules explicitly say resolution is based on any Binance BTC/USDT 1-minute candle High during the specified ET date range.
- The rules explicitly exclude other exchanges, different trading pairs, and other spot references from settlement.
- Related ladder markets on the same page showed `↑ 74,000` and `↑ 72,000` already resolved Yes, confirming the weekly series is actively resolving by threshold crossings.

## Evidence directly stated by source

- “This market will immediately resolve to ‘Yes’ if any Binance 1-minute candle for BTC/USDT during the date range specified in the title ... has a final ‘High’ price equal to or greater than the price specified in the title.”
- “The resolution source for this market is Binance, specifically the BTC/USDT ‘High’ prices...”
- “Prices from other exchanges, different trading pairs, or spot markets will not be considered for the resolution of this market.”

## What is uncertain

- Polymarket page fetch does not by itself prove that Binance has already printed a qualifying 1-minute high for $76,000.
- The page is a live web surface, so the observed last trade / best bid / best ask may move quickly.

## Why this source may matter

This is the governing source-of-truth surface for contract interpretation. For a narrow threshold market, rule precision matters more than generic BTC directional analysis.

## Possible impact on the question

This source materially raises confidence that the correct framing is not “Will broad BTC spot trade above 76k somewhere?” but “Will Binance BTC/USDT print a qualifying 1-minute high during the ET window?” That makes exchange-specific path risk the main remaining failure mode.

## Reliability notes

Polymarket is authoritative for the contract wording and displayed odds, but not itself the underlying exchange data. Reliability for rules is high; reliability for settlement facts is incomplete without checking Binance or an independent live exchange reference.