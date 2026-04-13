---
type: source_note
case_key: case-20260413-9e664afd
dispatch_id: dispatch-case-20260413-9e664afd-20260413T164930Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-14 close above 70000?
driver: reliability
date_created: 2026-04-13
agent: Orchestrator
source_name: Polymarket market page and rules text
source_type: market contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9e664afd/researcher-analyses/2026-04-13/dispatch-case-20260413-9e664afd-20260413T164930Z/personas/variant-view.md]
tags: [polymarket, rules, resolution, btcusdt]
---

# Summary

The Polymarket rules make this a narrow contract-interpretation case rather than a broad Bitcoin thesis case. Resolution depends only on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 14 and whether its final close is strictly greater than 70,000.

## Key facts extracted

- Resolution condition is whether the Binance 1-minute candle for BTC/USDT at `12:00` in ET has a final close above `70,000`.
- Resolution source is Binance, specifically the BTC/USDT close prices visible on the Binance trading page with `1m` and `Candles` selected.
- The rules explicitly exclude other exchanges and other trading pairs.
- Price precision is determined by the number of decimals in the Binance source.
- The market page at fetch time showed the 70,000 line trading around `93%` Yes, above the assignment snapshot of `84.5%`.

## Evidence directly stated by source

Direct rules text from the market page states:
- `This market will resolve to "Yes" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final "Close" price higher than the price specified in the title.`
- `The resolution source for this market is Binance, specifically the BTC/USDT "Close" prices currently available at https://www.binance.com/en/trade/BTC_USDT with "1m" and "Candles" selected on the top bar.`

## What is uncertain

- The wording `12:00 in the ET timezone` still requires a timezone mapping step because Binance exchange data is natively organized in UTC.
- The rules point to the Binance web chart rather than the raw API, so there is mild UI-versus-API source-of-truth ambiguity if Binance later revised or displayed data differently.
- The market page is not itself evidence that the final noon candle will stay above 70,000; it only defines the contract and shows current crowd pricing.

## Why this source may matter

This is the governing contract surface. It defines the exact pair, time, comparison operator, and settlement source, which all matter more here than generic BTC directional commentary.

## Possible impact on the question

This source narrows the real live uncertainty to one thing: whether Binance BTC/USDT remains above 70,000 into the exact noon-ET minute close on April 14.

## Reliability notes

Very high relevance because it defines the contract. It is not independent from the market itself, so it should be paired with direct Binance data and an explicit timing check before finalizing.
