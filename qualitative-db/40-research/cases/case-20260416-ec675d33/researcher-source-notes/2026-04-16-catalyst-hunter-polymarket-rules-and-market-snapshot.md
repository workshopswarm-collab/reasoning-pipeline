---
type: source_note
case_key: case-20260416-ec675d33
dispatch_id: dispatch-case-20260416-ec675d33-20260416T073538Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-20 above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules for "Bitcoin above ___ on April 20?"
source_type: market rules / venue page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-ec675d33/researcher-analyses/2026-04-16/dispatch-case-20260416-ec675d33-20260416T073538Z/personas/catalyst-hunter.md]
tags: [polymarket, contract-mechanics, source-note, btc]
---

# Summary

This source establishes the contract mechanics, current market-implied probability, and the governing resolution source for the case.

## Key facts extracted

- The specific leg under review is the 72,000 outcome for April 20, 2026.
- The market page showed the 72,000 contract trading around 85¢ / 84% at fetch time.
- The market resolves "Yes" if the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on the named date has a final close above 72,000.
- The source of truth is Binance BTC/USDT with 1m candles selected.
- The rules explicitly say the market is about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Resolution depends on one exact observation: the final close price of the Binance BTC/USDT 1-minute candle associated with 12:00 PM ET on 2026-04-20.
- The market is not asking about intraday highs, daily close, other exchanges, or index averages.
- Current crowd pricing on the page implies a high-probability but not near-certain view for the 72k threshold.

## What is uncertain

- The page itself does not spell out whether Binance internally timestamps the 1-minute candle in UTC while the contract references ET; that requires interpretive checking against Binance API behavior.
- The page is a live venue surface, so the quoted 84-85% price can move after fetch time.

## Why this source may matter

This is the governing contract/rules surface. For a narrow-resolution, date-specific crypto price market, contract interpretation matters almost as much as directional BTC analysis.

## Possible impact on the question

The rules narrow the real question to: will Binance BTC/USDT still be above 72,000 at exactly the noon ET minute-close on April 20. That reduces the importance of broad sentiment alone and increases the importance of timing/path risk into a single observation window.

## Reliability notes

Polymarket is authoritative for the market wording and the displayed market-implied probability, but not for the settlement datapoint itself. Reliability is therefore high for contract mechanics and medium for everything else.