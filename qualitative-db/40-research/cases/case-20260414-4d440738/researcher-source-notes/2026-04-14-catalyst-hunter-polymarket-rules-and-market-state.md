---
type: source_note
case_key: case-20260414-4d440738
dispatch_id: dispatch-case-20260414-4d440738-20260414T195302Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 68000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market contract / resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4d440738/researcher-analyses/2026-04-14/dispatch-case-20260414-4d440738-20260414T195302Z/personas/catalyst-hunter.md]
tags: [source-note, polymarket, resolution-rules, binance]
---

# Summary

This source defines the contract mechanics and gives the current market-implied baseline. It is the governing source for what counts at resolution.

## Key facts extracted

- The market resolves YES if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 20, 2026 has a final close above 68,000.
- The market resolves NO otherwise.
- The source of truth is Binance BTC/USDT with 1m candles selected; other exchanges and pairs do not count.
- Price precision is whatever Binance displays in the source candle.
- The Polymarket page currently showed the 68,000 line trading around 94% YES / 7% NO when checked on 2026-04-14.

## Evidence directly stated by source

- Contract wording explicitly ties resolution to a single timestamped Binance candle rather than a daily close or broad market average.
- The rules explicitly exclude other exchanges or pairs.

## What is uncertain

- The Polymarket page itself is not the settlement source for the actual price; it only defines the contract and current odds.
- The page does not itself provide the final April 20 candle, only the rule for where to look.

## Why this source may matter

For a date-sensitive and narrow-resolution contract, rule interpretation is decisive. The relevant event is not just whether BTC is generally above 68k in the coming week, but whether Binance BTC/USDT is above 68k at exactly noon ET on April 20.

## Possible impact on the question

This source makes timing the primary catalyst frame. Any event that can move BTC materially before or during the next six days matters, but all must cash out through one precise Binance minute candle.

## Reliability notes

High reliability for contract interpretation and current market state; not sufficient alone for directional price judgment because it is not an independent market-context source.