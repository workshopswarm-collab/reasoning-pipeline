---
type: source_note
case_key: case-20260414-d5888900
dispatch_id: dispatch-case-20260414-d5888900-20260414T143228Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-d5888900 | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 14?
driver: reliability
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market rules / contract text
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-14
credibility: high
recency: same-day
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-d5888900/researcher-analyses/2026-04-14/dispatch-case-20260414-d5888900-20260414T143228Z/personas/risk-manager.md]
tags: [polymarket, contract, rules, resolution, timing]
---

# Summary

This source note captures the market's governing contract language and current market-implied baseline.

## Key facts extracted

- The market resolves "Yes" if the Binance 1-minute candle for BTC/USDT at 12:00 in ET on 2026-04-14 has a final close above 70,000.
- The market resolves from Binance BTC/USDT specifically, not from other exchanges or other trading pairs.
- Price precision is determined by the source's displayed decimals.
- The market page showed the 70,000 line trading at effectively 100% / current_price 0.9995 from assignment context.

## Evidence directly stated by source

- Contract condition is multi-part: correct date, correct timezone, correct exchange, correct pair, correct 1-minute candle, and correct field (close).
- The source of truth named in the rules is the Binance trading page candle view with 1m selected.

## What is uncertain

- The market page itself is not independent evidence about the actual noon close; it only defines how the answer will be judged.
- The page does not resolve edge cases beyond the stated source-of-truth language, such as temporary UI/API mismatch or exchange data revisions.

## Why this source may matter

This is the governing source for contract interpretation. For a narrow date-and-time market, rule fidelity is as important as directional BTC price evidence.

## Possible impact on the question

The rules make the thesis highly favorable to "Yes" if BTC remains anywhere near observed spot levels, but they also create a narrow operational failure mode: a wrong timezone mapping, wrong candle, wrong pair, or wrong source surface could produce an incorrect analysis even if the broad BTC narrative is right.

## Reliability notes

High reliability for contract interpretation because it is the market's own rule text. Not independent evidence about the underlying BTC price at noon.