---
type: source_note
case_key: case-20260415-b4a49d1b
dispatch_id: dispatch-case-20260415-b4a49d1b-20260415T000939Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event rules page
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: base-rate
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-b4a49d1b/researcher-analyses/2026-04-15/dispatch-case-20260415-b4a49d1b-20260415T000939Z/personas/base-rate.md]
tags: [source-note, polymarket, rules, settlement, resolution]
---

# Summary

The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET (noon) on April 20 has a final Close price strictly higher than 70,000. It is specifically Binance BTC/USDT, not another exchange or pair.

## Key facts extracted

- Governing settlement source is Binance.
- Governing instrument is BTC/USDT.
- Governing timestamp is the 12:00 ET 1-minute candle on April 20.
- Governing field is the final Close price for that candle.
- Threshold condition is strictly higher than 70,000.
- Price precision is determined by the source.

## Evidence directly stated by source

- Full market context and rules specifying the resolution mechanics.
- Current Polymarket price around 86 cents Yes for the 70,000 threshold.

## What is uncertain

- The page is authoritative for market rules in practice, but operationally the exact resolving value still depends on Binance’s displayed candle at the relevant time.
- The fetched page did not itself provide a direct Binance candle archive for the future resolution minute.

## Why this source may matter

This source defines what has to be true for the contract to pay out. For a narrow timing market, contract mechanics materially matter: spot price on other venues, daily closes, and intraday highs are irrelevant if the named Binance minute close at noon ET is not above 70,000.

## Possible impact on the question

The note narrows the forecasting target to one exact minute close on one exchange, which slightly lowers confidence relative to a broader daily-close-style contract and makes short-horizon volatility around the fixing minute more important.

## Reliability notes

- High relevance for contract interpretation.
- Medium credibility as a settlement-rules surface rather than the settlement data itself.
- Independent of Binance market data for mechanics, but not independent for eventual settlement outcome since Binance still governs the final answer.