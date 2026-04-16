---
type: source_note
case_key: case-20260414-fdb38a8b
dispatch_id: dispatch-case-20260414-fdb38a8b-20260414T180238Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-fdb38a8b | base-rate
question: Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules for bitcoin-above-on-april-17
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-fdb38a8b/researcher-analyses/2026-04-14/dispatch-case-20260414-fdb38a8b-20260414T180238Z/personas/base-rate.md]
tags: [polymarket, contract-rules, market-implied-probability, binance]
---

# Summary

This source establishes the exact market-implied probability being evaluated and the governing contract mechanics for resolution.

## Key facts extracted

- The assigned current market price for the 72,000 threshold is 0.815, implying roughly 81.5% probability for Yes.
- The market page showed the 72,000 line at roughly 81% at fetch time, consistent with the assignment context.
- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-17 has a final close strictly higher than 72,000.
- The source of truth is Binance BTC/USDT with 1m candles selected; not other exchanges or other trading pairs.
- The wording is strict: the close must be higher than 72,000, not equal to 72,000.
- Because the resolution is tied to a single minute candle at a specified ET time, there is narrow timing and source specificity risk.

## Evidence directly stated by source

- Contract text directly states the resolution condition and governing source.
- Outcome ladder on the market page provides the contemporaneous crowd-implied pricing.

## What is uncertain

- The public market page is not itself the settlement authority; it points to Binance as the authority.
- The web fetch view is a rendered page and may not expose every edge-case clarification beyond the main rules text.

## Why this source may matter

This source defines both the baseline to compare against and the precise mechanics that matter for any forecast. Because this is a narrow, date-specific crypto market, contract interpretation is materially important.

## Possible impact on the question

The market is already pricing a high probability of Yes, so any bearish view needs evidence strong enough to overcome both the current spot buffer above 72,000 and the short time horizon. The single-minute resolution format leaves room for intraday volatility risk even if the broader daily trend remains constructive.

## Reliability notes

Good for contract wording and market baseline, but settlement authority is external: Binance BTC/USDT 1-minute candle close at the specified time.