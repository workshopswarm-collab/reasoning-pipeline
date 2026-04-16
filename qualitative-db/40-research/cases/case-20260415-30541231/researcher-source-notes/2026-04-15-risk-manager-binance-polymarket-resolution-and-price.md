---
type: source_note
case_key: case-20260415-30541231
dispatch_id: dispatch-case-20260415-30541231-20260415T133406Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-30541231 | risk-manager
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API + Polymarket market rules page
source_type: mixed primary market data and contract rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=48 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-30541231/researcher-analyses/2026-04-15/dispatch-case-20260415-30541231-20260415T133406Z/personas/risk-manager.md]
tags: [source-note, binance, polymarket, resolution, btc]
---

# Summary

This note captures the governing contract mechanics from the Polymarket market page and a direct spot-price / recent-range verification from Binance APIs.

## Key facts extracted

- Polymarket rules state the market resolves Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on 2026-04-17 has a final Close strictly higher than 72,000.
- The rules explicitly say the source of truth is Binance BTC/USDT, not other exchanges or pairs.
- On 2026-04-15 around 09:35 ET, Binance ticker API showed BTCUSDT at 74,124.31.
- Binance 48-hour hourly-klines pull showed a latest close around 74,158.95, 48h high 76,038.00, and 48h low 71,375.24.
- The current spot is above the threshold, but the 48-hour low demonstrates that a move below 72,000 is not remote over the remaining window.

## Evidence directly stated by source

- Polymarket directly states the exact resolution mechanics and governing source.
- Binance APIs directly state current BTCUSDT spot and recent candles.

## What is uncertain

- The contract resolves off one exact 1-minute close at 12:00 ET on April 17, not the current spot or any intraday high/low before then.
- API access here verified Binance direct data surfaces, but not the exact future resolving candle because it has not occurred yet.
- The Polymarket page text appears duplicated in fetch output, but the contract language itself is clear and internally consistent.

## Why this source may matter

This is the most important source set because it both defines the contract and shows the current state relative to the threshold.

## Possible impact on the question

These sources support a base case leaning Yes because BTC is currently comfortably above 72,000, but they also surface the core risk-manager objection: this is a single-minute, exact-time settlement condition with about 50 hours remaining, so path and timing risk still matter.

## Reliability notes

- Binance API is a direct data surface for the referenced exchange and pair, so it is high-value direct evidence for current state.
- Polymarket event rules page is the direct contract description for this market and therefore authoritative for interpretation, subject only to any later exchange/data anomalies at settlement time.
- Evidence independence is moderate rather than high because both the contract and current-state evidence ultimately revolve around the same exchange surface.