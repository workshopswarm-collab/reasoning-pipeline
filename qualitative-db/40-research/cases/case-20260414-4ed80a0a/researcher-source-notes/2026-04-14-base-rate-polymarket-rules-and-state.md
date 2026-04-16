---
type: source_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: eth-price-threshold
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-14
source_name: Polymarket market metadata / CLOB API
source_type: market rules and state
source_url: https://clob.polymarket.com/markets/0x9a91f5fa90b334c224cb4e638248acc8907b44fa8ed56361b24573cd20491763
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/base-rate.md]
tags: [polymarket, rules, source-of-truth, binance, resolution]
---

# Summary

Polymarket's machine-readable market metadata explicitly states that this contract resolves Yes if any Binance ETH/USDT 1-minute candle during Apr 13-19 ET has a final High at or above $2,400. The same metadata also showed the market already resolved Yes and closed on Apr 14.

## Key facts extracted

- Question: "Will Ethereum reach $2,400 April 13-19?"
- Resolution condition: any Binance ETH/USDT 1-minute candle High during the title date range reaches or exceeds $2,400.
- Time window: from 12:00 AM ET on Apr 13 through 11:59 PM ET on Apr 19.
- Resolution source: Binance ETH/USDT 1-minute chart/candle High values.
- Market state on fetch: token prices Yes=1, No=0; closed=true; umaResolutionStatus=resolved / automaticallyResolved=true in returned metadata.

## Evidence directly stated by source

- The description directly names Binance ETH/USDT 1-minute candle High as the governing source of truth.
- The returned market object directly shows the market as resolved/closed with the Yes side effectively at 1.

## What is uncertain

- The API response excerpt does not itself print the exact candle timestamp that first crossed $2,400.
- It shows the resolved state, but a later audit still benefits from checking an independent Binance price endpoint for consistency with a >=$2,400 high.

## Why this source may matter

This is the closest thing to an authoritative contract/rules source available in machine-readable form. For a rule-sensitive threshold market, the exact source-of-truth definition is more important than generic ETH spot pricing.

## Possible impact on the question

This sharply reduces interpretive ambiguity: the core question is not "did ETH trade above $2,400 anywhere" but specifically whether Binance ETH/USDT printed a qualifying 1-minute candle High in the stated ET window. The metadata also strongly indicates the answer is already Yes.

## Reliability notes

High reliability for contract wording and current market state because this is Polymarket infrastructure data rather than a third-party summary. Independence is limited because it is the market operator's own data, so an extra verification pass against Binance price data is still appropriate.