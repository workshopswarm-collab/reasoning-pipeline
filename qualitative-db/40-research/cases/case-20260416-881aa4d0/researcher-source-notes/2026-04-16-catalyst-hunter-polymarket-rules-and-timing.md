---
type: source_note
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-structure
entity: binance
topic: settlement-rules-and-time-mapping
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 70000?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market rules page
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [binance, btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-881aa4d0/researcher-analyses/2026-04-16/dispatch-case-20260416-881aa4d0-20260416T044756Z/personas/catalyst-hunter.md
tags: [source-note, polymarket, rules, settlement, timing]
---

# Summary

The Polymarket rules explicitly say the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close strictly higher than 70,000; otherwise No.

## Key facts extracted

- Resolution source is Binance BTC/USDT, not other exchanges or other BTC pairs.
- Relevant chart mode is Binance with `1m` candles selected.
- The governing datapoint is the candle labeled `12:00` in ET on the specified date.
- The condition is strictly `higher than` 70,000, not `at or above` 70,000.
- Price precision is determined by the number of decimals shown by the source.

## Evidence directly stated by source

- The rules identify the settlement source of truth directly.
- The rules specify the relevant timeframe and trading pair directly.
- The rules clarify that other exchanges do not count.

## What is uncertain

- The page does not itself explain Binance timestamp conventions in UTC terms.
- The page does not spell out rare exchange-interface edge cases such as post hoc candle revisions or display/API mismatch.

## Why this source may matter

This source governs contract interpretation. For a date-sensitive, narrow-resolution market, knowing the exact source-of-truth surface and all conditions that must hold is necessary before assigning probability.

## Possible impact on the question

The market does not ask whether Bitcoin trades above 70k generally on April 17. It asks whether one exact Binance one-minute close at noon ET is above 70k. That sharply narrows the catalyst set: broad bullish developments matter less than any event capable of knocking Binance BTC/USDT below 70k precisely into the settlement minute.

## Reliability notes

- High reliability for contract mechanics because this is the market’s own rules surface.
- Not independent of the market itself, so it must be paired with direct Binance verification for execution and price context.