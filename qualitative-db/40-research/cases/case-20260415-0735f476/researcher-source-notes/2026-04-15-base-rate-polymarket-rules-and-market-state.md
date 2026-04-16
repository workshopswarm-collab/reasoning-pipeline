---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-market
entity: btc
topic: polymarket contract mechanics and current market state for Bitcoin above $70,000 on April 20
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page for Bitcoin above ___ on April 20
source_type: primary market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/base-rate.md
tags: [source-note, polymarket, btc, contract-rules, market-state]
---

# Summary

This source note captures the governing contract language and the live market-implied baseline visible on the Polymarket event page.

## Key facts extracted

- The market resolves **Yes** only if the **Binance BTC/USDT 1-minute candle for 12:00 ET on April 20** has a final **Close** price **higher than 70,000**.
- The governing source is specifically the Binance BTC/USDT trading surface with **1m Candles** selected.
- The rule is a **close-above-at-a-specific-minute** condition, not an intraday high/touch condition and not a cross-exchange average.
- The Polymarket page showed the **70,000** bracket trading around **93-94% Yes** at fetch time.
- Nearby strikes on the same page imply a steep local probability curve: 68k ~97%, 72k ~83%, 74k ~65%.

## Evidence directly stated by source

- Exact source-of-truth wording names Binance BTC/USDT and the 12:00 ET 1-minute close.
- The page explicitly warns that the market is about Binance BTC/USDT, not other exchanges or trading pairs.
- Current event-page pricing places the 70k threshold in the low-90s probability range.

## What is uncertain

- The public page does not itself provide a locked historical proof for the eventual April 20 noon ET candle because the event is still unresolved.
- The page pricing is market sentiment, not proof of outcome.
- The page does not by itself quantify the probability distribution of BTC staying above or closing above 70k at the exact governing minute.

## Why this source may matter

This is the clearest primary source for settlement mechanics. Because the contract is narrow and date/time specific, correct interpretation of the governing source matters as much as directional BTC outlook.

## Possible impact on the question

This source sharply reduces resolution ambiguity. It supports a relatively high Yes prior because BTC is already comfortably above 70k, but it also prevents overconfidence based on weaker formulations such as “BTC traded above 70k recently” or “most exchanges are above 70k.”

## Reliability notes

High reliability for contract wording and visible market state. Lower reliability for estimating fair value by itself, since event-page price is endogenous market opinion rather than independent evidence.