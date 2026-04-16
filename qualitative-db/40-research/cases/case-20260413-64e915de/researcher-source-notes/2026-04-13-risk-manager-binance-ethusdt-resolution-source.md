---
type: source_note
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260413-64e915de | risk-manager
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-13
source_name: Binance ETH/USDT market data and Polymarket rule text
source_type: exchange-data-plus-market-rules
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT
source_date: 2026-04-13
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
downstream_uses:
  - qualitative-db/40-research/cases/case-20260413-64e915de/researcher-analyses/2026-04-13/dispatch-case-20260413-64e915de-20260413T234340Z/personas/risk-manager.md
tags: [source-note, binance, polymarket-rules, resolution-source]
---

# Summary
This note captures the governing resolution mechanics and current exchange context for the ETH $2,400 weekly touch market.

## Key facts extracted
- Polymarket page HTML exposes the rule text: the market resolves Yes if any Binance 1-minute ETH/USDT candle during Apr 13 12:00 AM ET through Apr 19 11:59 PM ET has a final High at or above the threshold named in the contract.
- The rule text also says the source of truth is Binance ETH/USDT 1-minute candles; other exchanges and pairs do not count.
- Binance 24h ticker on 2026-04-13 showed lastPrice 2373.05, highPrice 2394.71, lowPrice 2175.68, and +8.291% over 24h.
- Daily Binance kline for 2026-04-13 showed intraday high 2394.71, leaving ETH only about $5.29 below the 2400 threshold on day one of the window.

## Evidence directly stated by source
- Rule text on the market page explicitly defines both the trigger condition and the authoritative source.
- Binance API directly reports spot ETH/USDT prices and recent highs used as context for path risk.

## What is uncertain
- The public 24h ticker and daily candles do not themselves prove whether a 1-minute candle reached 2400 after the snapshot; they only show the latest available context.
- The market could still fail if ETH remains just below 2400 on Binance for the full remaining window.

## Why this source may matter
This is the primary settlement frame. Because the contract is a date-bounded touch market with a single exchange source of truth, resolution mechanics matter almost as much as directional ETH view.

## Possible impact on the question
The source materially supports a high Yes probability because ETH is already trading within a few dollars of the trigger and the contract only needs one qualifying 1-minute high over nearly a full week.

## Reliability notes
- High reliability for settlement logic because the rule text is embedded on the market page.
- High reliability for current exchange context because Binance is the named resolution venue.
- Limitation: snapshot data is contextual, not a full forward path forecast.
