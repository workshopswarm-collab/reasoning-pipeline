---
type: source_note
case_key: case-20260416-5baa54ee
dispatch_id: dispatch-case-20260416-5baa54ee-20260416T032738Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-5baa54ee | market-implied
question: Will the Binance BTC/USDT 12:00 PM ET one-minute candle on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-15T23:30:00-04:00
source_name: Binance BTCUSDT API and Polymarket market rules page
source_type: primary-plus-resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=3 ; https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: supports-yes
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-5baa54ee/researcher-analyses/2026-04-16/dispatch-case-20260416-5baa54ee-20260416T032738Z/personas/market-implied.md]
tags: [binance, polymarket, resolution-check, btc]
---

# Summary

This source check pairs the market's governing resolution language on Polymarket with direct Binance BTCUSDT API data. Together they show both what counts for settlement and where spot BTC/USDT was trading during the research run.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in ET on the date in the title, using the final candle close.
- The threshold is strictly higher than 70,000; equal to 70,000 would not resolve Yes.
- Binance spot API returned BTCUSDT at 75,029.99 during this check.
- The last three Binance 1-minute klines fetched were all above 75,000 on the close: 75,068.50, 75,032.91, and 75,029.99.
- The event resolves on 2026-04-20 at 12:00 PM ET, around four days after this run.

## Evidence directly stated by source

- Polymarket rules page directly states the settlement source and exact condition: Binance BTC/USDT, 1m candle, 12:00 ET, final close price higher than the listed threshold.
- Binance API directly reports the current spot price and recent 1-minute candle closes.

## What is uncertain

- This source set does not itself guarantee where BTC/USDT will trade at the exact settlement minute on 2026-04-20.
- The fetched klines are recent spot context, not the final resolving candle.
- Web-fetching the human Binance trade page failed, so the direct exchange verification here relies on Binance's public API rather than the web chart UI named in the market description.

## Why this source may matter

This is the key direct evidence pair for a date-specific crypto price threshold market: one source defines exactly what will count, and the other shows the instrument currently trading materially above the threshold.

## Possible impact on the question

This source set supports the market's high implied probability because the named settlement instrument is already roughly 7% above the 70,000 line with only a short time remaining. It also surfaces the main remaining risk: BTC can still fall below 70,000 by the exact noon ET candle on April 20, or a Binance-specific operational/data issue could matter at settlement.

## Reliability notes

- Binance API is highly relevant because it is the same exchange family referenced by the contract, though the rules name the chart UI as the practical resolution surface.
- Polymarket's rules page is the authoritative contract-language source for what must happen.
- Independence is only moderate because both sources are tightly coupled to the same settlement chain rather than providing cross-checking from unrelated venues.
- For this contract, that coupling is a feature more than a bug because settlement depends specifically on Binance, not broader market consensus.
