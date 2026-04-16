---
type: source_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: ethereum
topic: case-20260416-989964fe | risk-manager
question: Will the Binance ETH/USDT 1-minute candle for 12:00 PM ET on 2026-04-17 close above 2200?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules page and Binance public API context check
source_type: primary-market-rules plus contextual-exchange-data
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution-rules, ethusdt, 1m-candle]
---

# Summary

This source note captures the governing contract mechanics from Polymarket and a same-session contextual check of Binance public API pricing. The main relevance is not broad ETH thesis work; it is verifying exactly what must be true for resolution and whether the market's 95% pricing is directionally plausible against current exchange context.

## Key facts extracted

- Polymarket states the market resolves "Yes" if the Binance ETH/USDT 1 minute candle for 12:00 in the ET timezone on April 17 has a final close price higher than 2200.
- The market is specifically about Binance ETH/USDT, not other exchanges or other pairs.
- Price precision is determined by the source.
- A same-session Binance public API context check returned ETHUSDT spot around 2356.03 and a recent 1-minute kline close around 2356.03.
- A timezone conversion check confirms that 2026-04-17 12:00 PM ET corresponds to 2026-04-17 16:00:00 UTC.

## Evidence directly stated by source

- The governing source of truth is Binance ETH/USDT 1-minute candle data.
- The material conditions are conjunctive: correct venue (Binance), correct pair (ETH/USDT), correct interval (1m candle), correct date (April 17), correct time bucket (12:00 PM ET), and final close price strictly greater than 2200.

## What is uncertain

- The market page does not independently document whether Binance UI display and Binance API output could differ in edge-case formatting or rounding, though both are part of Binance data surfaces.
- Current spot is only contextual, not settlement evidence. ETH can move materially before noon ET on the resolution date.
- I was not able to fetch third-party contextual pages like CoinGecko/Coinbase due bot protection, so contextual independence is limited.

## Why this source may matter

This is the key source for contract interpretation. For a narrow date/time market, resolution mechanics matter as much as price direction. A trader can be directionally right on ETH but wrong on venue, pair, time bucket, or exact threshold logic.

## Possible impact on the question

The rules strongly support a high yes probability because current Binance ETH/USDT is already well above 2200, but they also create a hidden tail risk: the claim fails if any one of the specified conditions is not met in the required way, or if ETH drops more than roughly 6.6% by the exact noon ET candle close.

## Reliability notes

- Polymarket rules page is the authoritative contract source for what counts.
- Binance API data is a strong contextual source for current exchange price levels, but not itself the formal settlement snapshot for the future noon-ET candle.
- Evidence independence is only medium because both the current-price context and eventual settlement source depend on Binance market data.