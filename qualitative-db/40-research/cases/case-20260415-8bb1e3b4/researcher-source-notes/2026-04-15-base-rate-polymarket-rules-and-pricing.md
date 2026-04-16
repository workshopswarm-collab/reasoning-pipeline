---
type: source_note
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close be above 70000 on 2026-04-20?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market page / contract specification
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract, rules, market-implied-probability]
---

# Summary

The Polymarket contract currently prices the 70,000 line at about 0.88 implied probability for Yes and explicitly defines the settlement condition as the Binance BTCUSDT 1-minute candle close at 12:00 ET on 2026-04-20.

## Key facts extracted

- The 70,000 contract was quoted at roughly `88¢` Yes on the fetched market page, matching the assignment `current_price: 0.88`.
- The title and rules are for whether Bitcoin is above a specified level on April 20.
- The rule text states the market resolves Yes if the Binance BTCUSDT `1 minute candle` for `12:00` in `ET timezone (noon)` on that date has a final `Close` price above the threshold.
- The rules also state the market is specifically about Binance BTCUSDT, not other exchanges or pairs.
- Price precision is determined by the source decimals.

## Evidence directly stated by source

- Market-implied baseline is about 88%.
- Settlement requires all of the following: correct date, Binance venue, BTCUSDT pair, 1-minute candle, noon ET timestamp, final close field, and close strictly greater than 70,000.

## What is uncertain

- The market page is not itself the final resolution source; it defines the rule but Binance provides the actual settling print.
- Page fetches can reflect UI snapshots rather than exchange audit logs.

## Why this source may matter

This source defines the contract mechanics and current crowd baseline. It is necessary for judging whether the market is over- or underpricing the event and for checking date/timing/source-of-truth ambiguity.

## Possible impact on the question

The market is already at an extreme probability, so the run needs extra verification. The exact noon-ET one-minute-close condition means even a generally bullish BTC regime can still miss on a localized dip.

## Reliability notes

- High credibility for contract wording and market price snapshot.
- Not independent from the market itself for probability assessment.
- Strong for resolution interpretation, weaker than Binance for the eventual truth value.