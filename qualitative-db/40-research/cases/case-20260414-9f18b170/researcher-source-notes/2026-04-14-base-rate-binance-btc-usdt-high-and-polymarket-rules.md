---
type: source_note
case_key: case-20260414-9f18b170
dispatch_id: dispatch-case-20260414-9f18b170-20260414T142057Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-9f18b170 | base-rate
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Polymarket rules page and Binance BTC/USDT ticker
source_type: primary_market_rules_plus_exchange_data
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, resolution-source, btc]
---

# Summary

This source combination establishes the contract mechanics and the most relevant live verification point. Polymarket's embedded rules state that each threshold resolves from the Binance BTC/USDT 1-minute candle high during the ET date window in the title. A direct Binance 24-hour ticker check on 2026-04-14 showed BTC/USDT already trading above $75k, with a reported 24-hour high around $75,715, which leaves the $76k threshold close but not yet crossed at the time checked.

## Key facts extracted

- Polymarket rules state an outcome resolves Yes if the Binance BTC/USDT 1-minute candle high during Apr 13 12:00 AM ET through Apr 19 11:59 PM ET is at or above the threshold.
- Polymarket rules explicitly say the resolution source is Binance BTC/USDT and that other exchanges or trading pairs do not count.
- Direct Binance API check on 2026-04-14 returned last price about $75,683 and 24-hour high about $75,716.
- A separate Kraken ticker check at roughly the same time showed spot around $75,750, which is directionally consistent with BTC being very near the threshold.

## Evidence directly stated by source

- The governing source of truth is Binance BTC/USDT high prices on 1-minute candles for the specified ET window.
- The threshold has not been directly shown as hit in the checks captured here; Binance 24-hour high remained below $76,000 at the sampled time.

## What is uncertain

- The Binance 24-hour ticker is not itself the formal settlement artifact because the contract specifies the chart high on 1-minute candles over the entire date window.
- Intraday volatility later in the week could still push a 1-minute candle above $76,000 even if it had not happened at the time of this note.
- I did not capture a full 1-minute time series for the entire window, only a contemporaneous spot/high check.

## Why this source may matter

It defines the only source that matters for resolution and gives a live reality check on distance-to-threshold. For a near-threshold weekly high market, this is more decision-relevant than broader narrative coverage.

## Possible impact on the question

The rules make this mostly a question of whether BTC can trade about 0.4-0.5% above sampled spot during the remaining window. That pushes the base-rate view toward a high probability, though not certainty, because a one-minute wick on Binance is plausible within several days when BTC is already trading in the mid-$75k area.

## Reliability notes

- Polymarket rules are the primary authoritative contract source, though the web fetch/readability extraction was messy and required direct HTML grep for the relevant rule text.
- Binance API data is highly relevant contextual evidence because the contract explicitly points to Binance BTC/USDT.
- Independence is medium: both pieces are tightly linked to the same market/exchange mechanism, so they are excellent for resolution mechanics but weaker for broader outside-view context.