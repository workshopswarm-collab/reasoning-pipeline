---
type: source_note
case_key: case-20260415-58166133
dispatch_id: dispatch-case-20260415-58166133-20260415T083617Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-58166133 | catalyst-hunter
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket rules plus direct Binance API timing and price checks
source_type: primary-plus-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-58166133/researcher-analyses/2026-04-15/dispatch-case-20260415-58166133-20260415T083617Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, timing, catalyst, settlement]
---

# Summary

This note captures the governing market mechanics and the most relevant near-term timing context for the catalyst-hunter view. The contract resolves off one specific Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-16, so the key catalyst is simply whether anything before that timestamp forces BTC back below 72,000 on Binance.

## Key facts extracted

- Polymarket states that the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-16 has a final Close above 72,000.
- The relevant time converts to 2026-04-16 16:00:00 UTC.
- Direct Binance API spot check during research showed BTCUSDT around 74,096 to 74,119, roughly 2.9% above the 72,000 threshold.
- Direct Binance hourly-kline check over the prior 24 hours showed closes ranging from 73,730.43 to 75,525.94, with the latest sampled close at 74,094.83.
- In this setup, soft narrative catalysts matter less than any hard shock that could move BTC more than about 3% lower before the noon ET resolution candle.

## Evidence directly stated by source

From Polymarket:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- Binance BTC/USDT with 1m candles is the explicit resolution source.

From direct Binance API checks:
- BTCUSDT current price was approximately 74.1k during the research window.
- Recent hourly closes in the sampled 24-hour window all remained above 72,000.

## What is uncertain

- No specific scheduled macro or crypto-native catalyst was verified in this run that is likely to dominate the next ~31 hours.
- A sudden risk-off move, exchange-specific disruption, or macro headline could still move BTC more than 3% before the resolution minute.
- The Binance API is a close operational proxy for the named source-of-truth surface, but the contract text names the Binance UI candle display specifically.

## Why this source may matter

It identifies the real timing bottleneck for the trade: not "where BTC trades on average tomorrow," but where Binance BTC/USDT prints exactly at the noon ET one-minute close.

## Possible impact on the question

The key near-term catalyst is negative rather than positive: a shock large enough to drag BTC below 72,000 by the specific settlement minute. Absent such a shock, the current cushion leaves Yes favored.

## Reliability notes

- Contract mechanics: high reliability for interpretation because Polymarket states the rule directly.
- Price context: high reliability because Binance API is direct exchange data for the same pair.
- Evidence independence: medium, since both surfaces depend on Binance as the operative source.
