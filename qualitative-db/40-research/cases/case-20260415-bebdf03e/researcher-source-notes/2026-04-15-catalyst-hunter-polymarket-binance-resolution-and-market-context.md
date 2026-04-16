---
type: source_note
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 PM ET 1-minute candle close on 2026-04-21 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for Bitcoin above ___ on April 21
source_type: market rules / primary contract surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-bebdf03e/researcher-analyses/2026-04-15/dispatch-case-20260415-bebdf03e-20260415T221944Z/personas/catalyst-hunter.md]
tags: [polymarket, resolution-rules, binance, timing]
---

# Summary

This source provides the governing contract mechanics and current market baseline for the April 21 BTC threshold ladder. It is the primary source for how the market resolves and shows the current market-implied probability for the 72,000 threshold.

## Key facts extracted

- The April 21 threshold market resolves based on the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone.
- The winning condition for this specific threshold is that the final candle close must be higher than 72,000.
- The source of truth is explicitly Binance BTC/USDT, not other exchanges or other BTC pairs.
- The market page showed the 72,000 line trading around 81%-82% on 2026-04-15.
- The page displayed adjacent thresholds around the same timestamp: 70,000 about 91%-92%, 74,000 about 62%-63%, 76,000 about 41%-42%.

## Evidence directly stated by source

- Resolution source: Binance BTC/USDT chart with 1m candles.
- Resolution time: 12:00 PM ET on the specified date.
- Condition: final candle close higher than the named threshold.
- Current market pricing for the relevant threshold and nearby ladder levels.

## What is uncertain

- The Polymarket page does not itself prove where Binance spot will trade on April 21; it only defines the contract and reflects current trader expectations.
- The displayed market prices can move materially before resolution.

## Why this source may matter

This is the contract-defining source. It determines what counts, what does not count, the relevant timezone, the relevant venue, and the precise trigger condition.

## Possible impact on the question

This source makes the case primarily a short-horizon price-path and timing question rather than a broad thesis about Bitcoin in April. It also means exchange-specific and timestamp-specific operational details matter.

## Reliability notes

High reliability for contract interpretation and current market baseline. Not an independent source for terminal price truth.