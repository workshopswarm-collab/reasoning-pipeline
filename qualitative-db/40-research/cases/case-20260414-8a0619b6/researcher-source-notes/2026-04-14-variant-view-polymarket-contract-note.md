---
type: source_note
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-8a0619b6 | variant-view
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-18 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket contract page for Bitcoin above 70000 on April 18
source_type: primary_market_source
source_url: https://polymarket.com/event/bitcoin-above-on-april-18
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/variant-view.md]
tags: [polymarket, resolution-criteria, timing-risk]
---

# Summary

This note records the market-implied baseline and the exact resolution wording for the specific Polymarket contract.

## Key facts extracted

- The relevant line is 70,000 and the market price shown during this run was about 90%, implying roughly 0.89 to 0.90 market-implied probability for Yes.
- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 18 has a final close strictly higher than 70,000.
- The market is not about any other exchange, any BTC/USD composite, an intraday high, or being above 70k at any point before noon.
- Price precision is determined by the number of decimal places in the source.

## Evidence directly stated by source

- The contract page directly states the settlement source is Binance BTC/USDT with 1m candles selected.
- The contract page directly states the relevant timestamp is 12:00 ET on the specified date.
- The contract page directly states the condition is higher than 70,000, not greater than or equal to 70,000.

## What is uncertain

- The fetched page is a web rendering, not a signed rule export, so UI extraction noise is possible.
- The page does not independently explain how daylight-saving alignment is handled beyond saying ET, though on April 18 ET means EDT.

## Why this source may matter

This is the governing market source for what counts. It sharply narrows the question from “will BTC stay above 70k generally” to “will one specific Binance minute close exceed 70k at noon ET on April 18.”

## Possible impact on the question

The market’s 89-90% Yes pricing looks directionally justified by current spot, but the contract wording creates a narrower failure path than casual traders may internalize. A brief selloff or exchange-specific print at the wrong minute is enough for No.

## Reliability notes

- High reliability for contract wording and market-implied baseline.
- Not independent from market consensus because it is the market itself.
- Useful mainly for rules interpretation, not for forecasting the underlying BTC path.