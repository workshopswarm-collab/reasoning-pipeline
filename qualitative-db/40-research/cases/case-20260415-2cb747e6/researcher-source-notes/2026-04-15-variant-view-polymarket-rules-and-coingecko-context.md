---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 72000 on April 16, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market page rules plus CoinGecko spot check
source_type: market_rules_plus_secondary_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2cb747e6/researcher-analyses/2026-04-15/dispatch-case-20260415-2cb747e6-20260415T122916Z/personas/variant-view.md]
tags: [polymarket, rules, coingecko, verification]
---

# Summary

The Polymarket rules make this a narrow contract-interpretation problem: the only thing that matters is whether the Binance BTCUSDT one-minute candle labeled 12:00 in ET on April 16 closes above 72000. A separate CoinGecko spot pull showed bitcoin at 74203 USD around the same time as the Binance pull, serving as an independent contextual verification that BTC was trading well above the threshold.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance BTCUSDT one-minute candle for 12:00 ET on April 16 has a final close higher than 72000.
- The rules explicitly say Binance BTCUSDT, not other exchanges or pairs, governs.
- CoinGecko simple price endpoint returned bitcoin at 74203 USD on 2026-04-15.
- The displayed Polymarket market price for the 72000 threshold was about 90%, matching the assignment current_price of 0.895.

## Evidence directly stated by source

- Contract mechanics require all of the following for Yes: correct date, correct timezone framing, correct exchange, correct pair, correct candle, and a final close strictly greater than 72000.
- CoinGecko context independently supports the idea that spot bitcoin was trading above 72000 at the time checked.

## What is uncertain

- CoinGecko is contextual only; it does not settle the market.
- The Polymarket page is not itself the final exchange record and could differ from Binance charting if there is later data revision or interface nuance.

## Why this source may matter

This source note captures the main variant-view angle: the market looks directionally right, but it may still be slightly overconfident because the contract is much narrower than a generic "BTC is above 72k" statement. Timezone, exact minute, and exchange-specific close all matter.

## Possible impact on the question

The rules compress the uncertainty into a single minute on a single venue, which prevents treating broad market strength as identical to contract resolution certainty. That keeps some residual No probability alive even when spot levels are comfortably above 72000 a day early.

## Reliability notes

Polymarket rules are high relevance for contract interpretation but are not the final settlement datapoint by themselves. CoinGecko is useful as an independent contextual source but lower authority than Binance for settlement.