---
type: source_note
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Polymarket BTC > 72k on April 21 resolution mechanics
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules page for bitcoin-above-on-april-21
source_type: market rules / primary contract surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/risk-manager.md
tags: [polymarket, binance, resolution-source, source-note, btc]
---

# Summary

This source is the governing contract surface. It specifies that resolution depends on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21, 2026 and specifically the final **Close** price, not the daily high, not another exchange, and not another trading pair.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET (noon)** on April 21 has a final **Close** price higher than 72,000.
- The resolution source is Binance with BTC/USDT, using **1m** candles and the **Candles** view.
- The contract is explicitly about Binance BTC/USDT, not Coinbase, CoinDesk reference pricing, or any other exchange/pair.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

- Direct rule text says the market resolves to Yes if the Binance 1-minute candle for BTC/USDT 12:00 in ET timezone on the date in the title has a final Close price higher than the threshold.
- Direct rule text names Binance BTC/USDT as the resolution source and clarifies exchange/pair exclusivity.

## What is uncertain

- The source note does not itself provide the future April 21 12:00 ET closing print.
- The public web page is not an ideal archival proof surface for later auditing; later reviewers may want direct candle capture from Binance at resolution time.

## Why this source may matter

This is the primary source of truth for mechanism risk. The main risk in this market is not “will BTC trade above 72k at some point” but whether the exact Binance BTC/USDT **12:00 ET 1-minute close** on April 21 is above 72,000.

## Possible impact on the question

This source pushes analysis away from generic bullish BTC narratives and toward a narrow timing/venue/field check. Any thesis that relies on BTC merely touching 72k or closing above 72k on a different venue is insufficient.

## Reliability notes

High reliability for contract interpretation because it is the governing market rules page. Moderate archival reliability for later proof-capture because web rendering can change and does not itself preserve the final qualifying candle.