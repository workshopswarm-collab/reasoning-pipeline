---
type: source_note
case_key: case-20260416-ca40bc37
dispatch_id: dispatch-case-20260416-ca40bc37-20260416T053546Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-ca40bc37 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and rules
source_type: market rules / market state
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, market-rules, resolution, bitcoin]
---

# Summary

Polymarket states this market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 20, using the final Close price, and the displayed market state shows the 72,000 line trading around 84-85% Yes at capture time.

## Key facts extracted

- The contract resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on the specified date has a final Close price higher than 72,000.
- The rules explicitly say the source is Binance BTC/USDT, not another exchange or pair.
- The rules explicitly say price precision is determined by the decimals in the source.
- The Polymarket event page showed the 72,000 line at roughly 84-85% Yes when captured.
- Other ladders on the same page imply a local probability curve around the threshold: 70,000 around 94% Yes, 74,000 around 65-66% Yes, 76,000 around 38-39% Yes.

## Evidence directly stated by source

- Governing source of truth: Binance BTC/USDT 1-minute candle close at 12:00 ET.
- Required material condition for Yes: the final close must be strictly higher than 72,000.
- Material exclusions: other exchanges and other trading pairs do not count.

## What is uncertain

- The Polymarket page is not the settlement source itself; it describes the intended source and rules.
- The page snapshot does not guarantee the live price path between now and April 20.
- The page wording references the Binance UI, but a reviewer may still want to cross-check Binance API behavior for minute-candle timing and availability.

## Why this source may matter

This is the contract-defining source for what counts, and it also provides the current market-implied baseline to compare against.

## Possible impact on the question

This source materially lowers ambiguity about resolution mechanics but also highlights a key risk-manager concern: this is a narrow, timing-specific, exchange-specific close-price contract, so even a generally bullish BTC view can fail if the exact noon ET minute closes below 72,000.

## Reliability notes

Useful and necessary for contract interpretation, but not independently authoritative on the actual eventual noon close. Best treated as the market-rules source plus market-pricing context, supplemented by Binance documentation/data for timing and source-of-truth interpretation.
