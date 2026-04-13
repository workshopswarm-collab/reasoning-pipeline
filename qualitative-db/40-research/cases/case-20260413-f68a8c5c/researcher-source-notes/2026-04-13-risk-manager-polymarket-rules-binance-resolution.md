---
type: source_note
case_key: case-20260413-f68a8c5c
dispatch_id: dispatch-case-20260413-f68a8c5c-20260413T165914Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: exchanges
entity: btc
topic: case-20260413-f68a8c5c | risk-manager
question: Will the price of Bitcoin be above $68,000 on April 14?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket event rules page for Bitcoin above 68000 on April 14
source_type: market rules / resolution surface
source_url: https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-f68a8c5c/researcher-analyses/2026-04-13/dispatch-case-20260413-f68a8c5c-20260413T165914Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution, date-sensitive, source-of-truth]
---

# Summary

This source defines the market mechanics and is the governing contract surface for how the question resolves.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 14 has a final Close price strictly higher than 68000.
- The market resolves No otherwise.
- The resolution source is Binance, specifically BTC/USDT with 1m candles.
- The contract is explicitly about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the number of decimals shown on the source.

## Evidence directly stated by source

Direct rule text says the relevant observation is the Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date, and the winning condition is that the final Close is higher than the listed threshold.

## What is uncertain

- The public webpage itself does not independently confirm tomorrow's actual 12:00 ET close; it only defines how settlement will be determined.
- The rule wording points to the Binance trading interface rather than directly to a documented API endpoint, so there is mild operational ambiguity around which exact public surface later reviewers should archive.

## Why this source may matter

This is the contract-defining source. Any thesis about likely resolution must map back to this exact candle, exact venue, exact pair, exact timezone, and strict greater-than condition.

## Possible impact on the question

This source sharply narrows what counts. A high BTC/USD price elsewhere is irrelevant if Binance BTC/USDT 12:00 ET close is not above 68000. It also means timing risk matters more than broad daily direction because only one minute-close determines resolution.

## Reliability notes

High reliability for contract interpretation because it is the market operator's own rule surface. Lower reliability for archiving exact future settlement data because the page references the Binance UI rather than a machine-readable settlement memo.