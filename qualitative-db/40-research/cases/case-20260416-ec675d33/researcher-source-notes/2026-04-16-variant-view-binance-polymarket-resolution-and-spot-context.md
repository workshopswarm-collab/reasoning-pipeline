---
type: source_note
case_key: case-20260416-ec675d33
dispatch_id: dispatch-case-20260416-ec675d33-20260416T073538Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance BTCUSDT API plus Polymarket rules page
source_type: primary-plus-resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-ec675d33/researcher-analyses/2026-04-16/dispatch-case-20260416-ec675d33-20260416T073538Z/personas/variant-view.md]
tags: [source-note, binance, polymarket, btc, resolution]
---

# Summary

This source note captures the governing settlement mechanics from Polymarket and a direct Binance price snapshot/history check relevant to whether the market may be slightly underpricing short-horizon downside variance.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 20, 2026, using the final candle close, and the threshold is strictly higher than 72,000.
- Resolution is specifically Binance BTC/USDT, not other exchanges or pairs.
- On 2026-04-16 during this run, Binance spot API returned BTCUSDT around 74,875.88.
- Recent Binance daily candles show BTC already trading above 72,000 on multiple recent days, but with daily intraday lows ranging well below 72,000 earlier in the sample and one recent close near 70,740.98 before rebounding.
- The assignment timestamp confirms resolution time is Monday 2026-04-20 12:00 EDT.

## Evidence directly stated by source

From the Polymarket rules page:
- Yes resolves if the Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date has a final close above the threshold.
- Otherwise No.
- Price precision follows the source.

From Binance direct endpoints observed in-run:
- ticker price: 74,875.88
- last 10 daily candles included highs up to 76,038 and recent closes at 71,924.22, 71,069.93, 71,787.97, 72,962.70, 73,043.16, 70,740.98, 74,417.99, 74,131.55, 74,809.99, 74,873.96.

## What is uncertain

- This snapshot does not itself settle the April 20 noon ET candle.
- Short-horizon BTC volatility over four days can still produce a sub-72k noon print even if spot is currently ~74.9k.
- Binance UI/candle labeling conventions could matter in an edge case, though the rules are fairly explicit.

## Why this source may matter

This is the strongest direct source set for the contract because it combines the settlement mechanics with the actual source-of-truth venue. It also shows why a high Yes probability is plausible while still leaving room for a meaningful No path through ordinary crypto volatility.

## Possible impact on the question

The direct data supports a Yes-lean because BTC is currently meaningfully above the threshold. The same data also supports a variant caution: the market is not settled by current spot, but by one specific minute close four days later, so short-horizon downside volatility remains the main underweighted way the market can still fail.

## Reliability notes

- Binance API is effectively the direct venue/source family referenced by the contract, so it is high-value for settlement interpretation and current-price context.
- Polymarket page is authoritative for the market wording but not for the future outcome itself.
- Evidence independence is only medium because both sources are tied to the same contract/source-of-truth ecosystem rather than independent macro analysis.
