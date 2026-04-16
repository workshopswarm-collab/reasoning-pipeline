---
type: source_note
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: prediction-markets
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 74000?
driver: reliability
date_created: 2026-04-15T20:46:00-04:00
source_name: Polymarket contract page and rules text
source_type: market rules / settlement description
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, noon-et]
---

# Summary

Polymarket's rules specify a narrow settlement mechanism: the relevant observation is the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone on Apr 17, and the decisive field is the final Close price for that minute.

## Key facts extracted

- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 17 has a final Close price higher than 74000.
- Otherwise the market resolves No.
- The source of truth is Binance, not other exchanges or other BTC pairs.
- Price precision is governed by the decimal precision available from the source.
- On the page snapshot, the 74000 line was trading around 66-67%, matching the assignment current_price near 0.605 directionally.

## Evidence directly stated by source

- Exact source of truth: Binance.
- Exact timing: 12:00 ET.
- Exact condition: final Close of the 1-minute candle must be strictly greater than 74000.

## What is uncertain

- The public page text does not itself display the eventual settlement candle; it only defines the contract.
- Web rendering duplicates some text, so operationally the contract language matters more than page formatting.

## Why this source may matter

This is the governing contract language. It converts a generic BTC direction view into a highly time-specific catalyst problem: the relevant question is whether BTC remains above the threshold at one exact minute close, not whether it trades above it at other times.

## Possible impact on the question

This narrows the catalyst calendar. The main catalyst is price behavior into late morning ET on Apr 17, with anything before then relevant only insofar as it shifts the probability of being above 74k exactly at that timestamp.

## Reliability notes

High reliability for settlement mechanics because this is the market's own stated rules. Some operational ambiguity always remains unless one can inspect the exact Binance UI candle at settlement, but source-of-truth ambiguity is still low because the contract language is explicit.
