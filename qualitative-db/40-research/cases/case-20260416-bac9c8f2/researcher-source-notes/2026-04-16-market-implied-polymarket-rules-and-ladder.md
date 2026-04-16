---
type: source_note
case_key: case-20260416-bac9c8f2
dispatch_id: dispatch-case-20260416-bac9c8f2-20260416T033803Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-bac9c8f2 | market-implied
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15T23:40:00-04:00
source_name: Polymarket event page and rule text
source_type: market_rule_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-bac9c8f2/researcher-analyses/2026-04-16/dispatch-case-20260416-bac9c8f2-20260416T033803Z/personas/market-implied.md]
tags: [polymarket, rules, threshold-market, settlement]
---

# Summary

The Polymarket event page states that this contract resolves Yes if the Binance BTC/USDT one-minute candle for 12:00 in ET on April 17 has a final close above 74,000. The page also showed the 74,000 line trading around 72%-73%, with neighboring ladder levels at 72,000 around 94% and 76,000 around 32%.

## Key facts extracted

- The governing source of truth is Binance BTC/USDT with `1m` candles selected.
- The relevant time is explicitly `12:00` in ET on April 17, 2026.
- The material condition is the final `Close` of that one-minute candle being strictly higher than 74,000.
- The fetched market page displayed the 74,000 contract around 72%-73% yes.
- Neighboring strikes were internally coherent: 72,000 much higher probability and 76,000 much lower probability.

## Evidence directly stated by source

- Exact resolution rule language.
- Exchange/pair specificity: Binance BTC/USDT, not another venue or pair.
- Timezone specificity: ET noon.
- Strict inequality: above 74,000, otherwise No.

## What is uncertain

- The scraped page is not an official rules API dump and may lag or render imperfectly.
- The page does not by itself prove that the visible market quote is fully up to date to the second.

## Why this source may matter

This is the clearest available statement of contract mechanics and the visible market-implied baseline. For a date-sensitive threshold contract, exact mechanics are central to correct analysis.

## Possible impact on the question

This source anchors both the market prior and the rule interpretation. The neighboring strike prices suggest the market is pricing a fairly standard BTC volatility distribution rather than a misread binary, which supports treating the 71% current price as broadly efficient.

## Reliability notes

- High importance because it defines the contract.
- Medium credibility rather than high because it is still a web page scrape, not a signed API or settlement record.
- Independence versus Binance is low on mechanics because Polymarket itself cites Binance as the source of truth; they are not independent evidentiary chains for the ultimate outcome.