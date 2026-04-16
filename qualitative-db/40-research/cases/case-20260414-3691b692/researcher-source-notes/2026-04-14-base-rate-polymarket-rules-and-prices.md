---
type: source_note
case_key: case-20260414-3691b692
dispatch_id: dispatch-case-20260414-3691b692-20260414T170231Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-16 above 72000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market_rules_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-14
credibility: medium
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3691b692/researcher-analyses/2026-04-14/dispatch-case-20260414-3691b692-20260414T170231Z/personas/base-rate.md]
tags: [polymarket, rules, resolution, market-implied-probability]
---

# Summary

The Polymarket event page specifies that the market resolves from the Binance BTC/USDT 1-minute candle at 12:00 PM ET on April 16, using the final Close value from the Binance trading interface with 1m candles selected. The page also showed the 72,000 bracket trading around 90%-91% Yes at time of review.

## Key facts extracted

- Market question is not about generic BTC spot price; it is specifically Binance BTC/USDT.
- Resolution timestamp is 12:00 PM ET on 2026-04-16.
- The relevant datapoint is the final Close of the 1-minute candle for that timestamp.
- The 72,000 line was priced at about 90%-91% Yes during review.
- The rule wording implies all of these conditions must hold for Yes: correct date, correct exchange, correct pair, correct 1-minute candle, and final close strictly higher than 72,000.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- Price precision is determined by Binance's displayed decimals.

## What is uncertain

- The public web page is not itself the final settlement source; it points to Binance as source of truth.
- The page does not itself provide the future April 16 noon close, only the rule and current market odds.

## Why this source may matter

It governs contract interpretation and provides the live market-implied baseline against which the research view is compared.

## Possible impact on the question

Because the contract is narrow and source-specific, a generally bullish BTC view is not enough; the relevant question is whether Binance BTC/USDT remains above 72,000 at one exact minute in ET. That makes timing risk and exchange-specific price risk material.

## Reliability notes

Useful as the governing contract/rules surface and for current odds, but not independent evidence about the future price path. Reliability for rules is high enough because it is the market issuer's page; reliability for forecasting is low because it mainly reflects the market itself.