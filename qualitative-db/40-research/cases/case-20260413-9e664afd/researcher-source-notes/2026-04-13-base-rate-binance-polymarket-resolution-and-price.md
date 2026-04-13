---
type: source_note
case_key: case-20260413-9e664afd
dispatch_id: dispatch-case-20260413-9e664afd-20260413T164930Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on April 14, 2026 close above 70000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket rules page plus Binance API spot/klines verification
source_type: primary_plus_contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [case-source, polymarket-rules, binance, btc]
---

# Summary

The market resolves from a very specific source of truth: the final close of the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 14, 2026. As of the research run on April 13, Binance spot/API data showed BTC/USDT trading around 72.3k, comfortably above the 70k threshold, while the Polymarket contract page listed the 70,000 line at about 93% Yes.

## Key facts extracted

- Polymarket rules specify that this market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 14 has a final close strictly higher than 70,000.
- The contract is exchange-specific and pair-specific: Binance BTC/USDT, not another venue or pair.
- Price precision is determined by the source, so the strict comparison is against Binance's displayed precision.
- Binance API verification during the run returned live BTCUSDT around 72,290 and recent 1-minute closes around 72.3k-72.4k.
- Recent Binance daily closes show BTC above 70k on each of the last 7 daily candles, and above 70k on 50% of the last 30 and about 51% of the last 90 daily candles.

## Evidence directly stated by source

From Polymarket market context/rules:
- Yes if the Binance 1 minute candle for BTC/USDT 12:00 in ET timezone on the specified date has a final Close price higher than the listed threshold.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- The contract is not about other exchanges or trading pairs.

From Binance API during the run:
- `ticker/price` returned BTCUSDT at 72,290.36.
- Recent 1-minute klines around the check time showed closes in the low 72.3k range.
- Recent daily kline analysis showed a 7-day streak of daily closes above 70k.

## What is uncertain

- The exact April 14 12:00 ET candle obviously had not happened yet at research time.
- Intraday volatility between now and settlement could still take BTC below 70k by the relevant minute.
- API data is a practical verification surface, but the contract names the Binance trading interface/candle display as the governing resolution source.

## Why this source may matter

This is the main direct evidence set for the case because it covers both contract mechanics and the current reference price relative to the threshold. It also clarifies that timing, venue, and the strict close condition all matter.

## Possible impact on the question

Because spot is already about 3% above the threshold with only about one day to go, the outside-view starting point leans Yes unless there is a plausible >3% downside move into the exact noon ET minute. The narrow exchange-specific resolution mechanism introduces some operational/contract risk, but not enough here to dominate the base-rate view.

## Reliability notes

- Polymarket rules page is the direct contract-context source and should govern interpretation unless the market is later amended.
- Binance API is not the literal named interface surface, but it is a credible direct exchange data surface and is suitable for verification of current spot/klines.
- Evidence independence is only medium because the contextual and direct price checks are both tied to Binance market data, but that is appropriate given the contract itself is exchange-specific.