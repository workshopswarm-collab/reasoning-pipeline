---
type: source_note
case_key: case-20260415-2ce6159e
dispatch_id: dispatch-case-20260415-2ce6159e-20260415T142913Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: btc
topic: case-20260415-2ce6159e | risk-manager
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-16 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules for bitcoin-above-on-april-16
source_type: market rules / market state
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2ce6159e/researcher-analyses/2026-04-15/dispatch-case-20260415-2ce6159e-20260415T142913Z/personas/risk-manager.md]
tags: [polymarket, rules, market-implied-probability, source-of-truth]
---

# Summary

Polymarket shows the 72,000 strike at roughly 93% Yes and specifies a narrow resolution rule: the contract resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on 2026-04-16, using the final Close price, with Binance as the governing source of truth.

## Key facts extracted

- The 72,000 outcome was displayed at about 93% Yes on 2026-04-15.
- The market resolves using the Binance BTC/USDT pair only, not BTC/USD or other exchanges.
- The relevant datapoint is the 1-minute candle for 12:00 PM ET on the date in the title.
- The resolution condition is strict: the final candle Close must be higher than 72,000, not equal.
- Price precision is determined by Binance source precision.

## Evidence directly stated by source

- The page states the market will resolve Yes if the Binance 1-minute candle for BTC/USDT 12:00 in ET has a final Close price higher than the specified threshold.
- The page names Binance trade page candle data as the resolution source.
- The page displays current crowd pricing for the 72,000 strike near 93%.

## What is uncertain

- The fetched page is a rendered web surface rather than a signed rules archive, so UI display formatting could change.
- The page does not itself expose the future resolving candle; it only defines the rule and current market price.
- The exact ET-to-Binance candle mapping still needs verification because Binance APIs are UTC-based while the rule is ET-labeled.

## Why this source may matter

This is the governing contract/rules source for what counts. For a date-specific and narrow-resolution market, the biggest non-price risk is often misreading the exact source, pair, timestamp, or greater-than condition.

## Possible impact on the question

It materially reduces ambiguity about what must happen: BTC/USDT on Binance must remain above 72,000 specifically at the noon ET closing print on 2026-04-16. That makes timing and exchange-specific operational details part of the risk, even if spot BTC is already comfortably above the strike.

## Reliability notes

Useful as the direct market/rules source, but not fully independent because it is also the venue expressing the crowd probability. It is authoritative on contract wording, not on future price realization.