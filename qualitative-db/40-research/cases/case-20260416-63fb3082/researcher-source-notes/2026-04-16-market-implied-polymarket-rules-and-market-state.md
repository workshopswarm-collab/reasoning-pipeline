---
type: source_note
case_key: case-20260416-63fb3082
dispatch_id: dispatch-case-20260416-63fb3082-20260416T145628Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-63fb3082 | market-implied
question: Will the price of Bitcoin be above $68,000 on April 21?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules for Bitcoin above 68,000 on April 21
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-63fb3082/researcher-analyses/2026-04-16/dispatch-case-20260416-63fb3082-20260416T145628Z/personas/market-implied.md
tags: [polymarket, contract-rules, market-implied, bitcoin]
---

# Summary

This source establishes both the live market-implied baseline and the contract mechanics. It shows the 68,000 line trading around 95% and states the exact resolution condition: the Binance BTC/USDT 1-minute candle at 12:00 ET on April 21 must have a final close above 68,000.

## Key facts extracted

- The assigned market line is 68,000 and the displayed probability is about 95% for Yes on 2026-04-16.
- The market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on April 21, 2026.
- The rule is based on the candle's final close, not intraminute highs, lows, or prices on other exchanges.
- Precision follows Binance source decimals.
- Related ladder prices on the same page imply a local distribution centered well above 68,000: 70,000 around 88%, 72,000 around 71%, 74,000 around 48%.

## Evidence directly stated by source

- The market page directly states the resolution source and the exact contract condition.
- The market page directly shows the current price for the 68,000 threshold and neighboring threshold markets.

## What is uncertain

- The web snapshot is not an official exchange API and could lag slightly from the live trading interface.
- The page does not explain why traders are pricing the threshold this way; it only reveals the crowd-implied distribution.

## Why this source may matter

It is the governing market-specific source for both the baseline probability and the resolution mechanics. For a narrow, date-specific contract, getting the exact candle, time zone, instrument, and close-price condition right matters more than generic Bitcoin price commentary.

## Possible impact on the question

This source strongly supports taking a high-Yes prior seriously. It also narrows the analysis to whether BTC/USDT on Binance is likely to remain above 68,000 specifically at 12:00 ET on April 21, rather than whether Bitcoin is generally bullish over the week.

## Reliability notes

Good for market-implied probability and contract wording, but not itself the external source of truth at settlement time. Settlement still depends on Binance’s displayed 1-minute BTC/USDT candle close.