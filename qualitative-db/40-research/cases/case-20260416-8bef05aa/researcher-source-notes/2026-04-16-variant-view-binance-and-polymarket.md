---
type: source_note
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-daily-close
entity: btc
topic: Binance BTC/USDT current level and Polymarket contract mechanics
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-21 be above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance BTCUSDT API and Polymarket market page
source_type: primary_market_and_governing_source_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-21
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
downstream_uses: [qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/variant-view.md]
tags: [source-note, binance, polymarket, resolution-mechanics, btc]
---

# Summary

This source bundle establishes the governing market mechanics and the current BTC/USDT reference level. It matters because the market is a date-specific noon close-above contract, not a touch/high contract.

## Key facts extracted

- Polymarket states the market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21 has a final Close price above 72,000.
- The listed resolution source is Binance BTC/USDT with 1m candles.
- Binance spot API on 2026-04-16 returned BTCUSDT around 73,982.
- Recent Binance daily candles show BTC/USDT has traded both below and above 72,000 during the prior 10 days.
- Recent daily highs include 74,900 on Apr 13, 76,038 on Apr 14, and 75,425 on Apr 15, while lows include 70,505.88 on Apr 12.

## Evidence directly stated by source

- The contract uses Binance BTC/USDT, 1-minute candle, noon ET, final Close price.
- Current public market pricing on Polymarket for the 72,000 line was about 71%.
- Binance directly reported current spot near 73,982 at collection time.

## What is uncertain

- The source note does not itself prove where BTC will be at noon ET on April 21.
- The fetched Polymarket page is a rendered market page rather than an API export, so exact displayed prices may move quickly.
- Binance current and recent prices are direct but only contextual for the future resolution timestamp.

## Why this source may matter

It directly answers the source-of-truth and timing mechanics, which are central because a close-above contract can fail even if BTC trades above 72,000 at many other times.

## Possible impact on the question

This source pushes against any lazy bullish interpretation based only on BTC already being above 72,000 now. It supports a more cautious reading: the relevant event is being above 72,000 at one specific noon ET close five days later.

## Reliability notes

- Binance is the governing source named by the contract, so source-of-truth ambiguity is low once the contract is read carefully.
- Polymarket is primary for contract wording and current market odds, but not for future price realization.
- Independence is only moderate within this note because both facts are part of the same market-mechanics bundle; additional contextual price sources are still useful.
