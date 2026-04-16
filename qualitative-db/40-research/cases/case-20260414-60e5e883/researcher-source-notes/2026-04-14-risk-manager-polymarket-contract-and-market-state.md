---
type: source_note
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-60e5e883 | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules for Bitcoin above $70,000 on April 17
source_type: market rules / market state
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-60e5e883/researcher-analyses/2026-04-14/dispatch-case-20260414-60e5e883-20260414T190542Z/personas/risk-manager.md]
tags: [polymarket, contract, market-implied-probability, resolution-rules]
---

# Summary

This source establishes the contract mechanics and the market-implied baseline. It is the governing statement for what the market is actually asking, but it is not itself independent evidence about where BTC will trade on April 17.

## Key facts extracted

- The current market price for the $70,000 line is about 93% Yes.
- The market resolves using the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, 2026.
- The specific resolution datapoint is the final Close of that 1-minute candle.
- The contract is Binance-specific, not a generalized BTC/USD spot market question.
- Price precision is determined by the source decimals.

## Evidence directly stated by source

- Yes resolves only if the Binance BTC/USDT 12:00 ET one-minute candle on April 17 has a final close above 70,000.
- Other exchanges or pairs do not govern resolution.

## What is uncertain

- The public market page does not itself show the future Binance candle; it only defines the rule and crowd pricing.
- The page does not independently validate whether 93% is calibrated.
- Exchange-specific operational quirks around candle display/finalization remain a live risk until resolution.

## Why this source may matter

This is the primary source for market wording and resolution interpretation. Because the contract is narrow and date-specific, exact timing and source-of-truth details materially matter.

## Possible impact on the question

It raises confidence that the right question is not simply "Will BTC still be above 70k generally?" but "Will Binance BTC/USDT close above 70k in the specific 12:00-12:01 ET minute on April 17?" That narrows the path to Yes and makes timing/venue risk the main residual downside.

## Reliability notes

Reliable for contract wording and market-implied probability, but not an independent source for fair value or eventual price realization. Evidence independence is low if used alone.