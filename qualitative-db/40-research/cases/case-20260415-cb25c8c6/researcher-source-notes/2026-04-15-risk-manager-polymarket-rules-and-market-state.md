---
type: source_note
case_key: case-20260415-cb25c8c6
dispatch_id: dispatch-case-20260415-cb25c8c6-20260415T194743Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: btc
topic: case-20260415-cb25c8c6 | risk-manager
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-19 close above 68000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for "Bitcoin above ___ on April 19?"
source_type: market rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-15
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, rules, binance, btc]
---

# Summary

This source is the governing contract/rules surface for the market and also exposes the current market price. It is authoritative for market wording and useful for current implied probability, but not authoritative for the eventual BTC price outcome itself.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET (noon) on 2026-04-19 has a final close price strictly higher than 68,000.
- The resolution source is Binance BTC/USDT with 1m candles selected.
- The contract is specifically about Binance BTC/USDT, not other exchanges or other BTC pairs.
- The market page currently showed the 68,000 line trading around 98.6% Yes / 2.1% No when fetched.
- Precision is determined by the number of decimals in the Binance source.

## Evidence directly stated by source

- Exact wording of the market mechanics.
- Exact named source-of-truth venue: Binance.
- Explicit time reference: 12:00 in ET timezone on the date in the title.

## What is uncertain

- The fetched page is not itself the final settlement source; it quotes the rules and current prices, but actual resolution depends on the Binance candle at the specified time.
- The page does not independently verify timezone conversion details beyond saying ET.

## Why this source may matter

This is the key source for avoiding contract-interpretation mistakes. The main risk is not broad BTC direction but narrow settlement mechanics: exact venue, exact pair, exact one-minute candle, exact timestamp, and strict greater-than threshold.

## Possible impact on the question

It materially lowers ambiguity about what must happen for Yes: all of the following must hold simultaneously for a correct Yes call:
1. the relevant source must be Binance,
2. the pair must be BTC/USDT,
3. the relevant candle must be the 12:00 ET one-minute candle on 2026-04-19,
4. the final close must be strictly above 68,000.

## Reliability notes

Useful and necessary as the contract/governing rules surface, but not independent from the market itself. Should be paired with a direct Binance or Binance API verification source for outcome context and settlement-mechanics confidence.