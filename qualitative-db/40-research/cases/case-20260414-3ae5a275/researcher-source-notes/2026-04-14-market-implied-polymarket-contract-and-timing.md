---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and assignment contract text
source_type: market contract / primary resolution description
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/market-implied.md]
tags: [polymarket, contract, resolution, timing]
---

# Summary

The market resolves based on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 20, with a final close strictly higher than 70,000 required for Yes. This makes the case narrow, timestamp-sensitive, exchange-specific, and sensitive to precise source-of-truth interpretation.

## Key facts extracted

- Title and assignment state the threshold market is: above $70,000 on April 20.
- Resolution source is Binance BTC/USDT, not another exchange or pair.
- The decisive datapoint is the Binance 1-minute candle for BTC/USDT at 12:00 ET (noon) on the specified date.
- The contract resolves Yes only if the final Close price for that minute candle is higher than 70,000.
- Price precision follows the source.
- The Polymarket page metadata showed the event resolves at 2026-04-20T16:00:00.000Z, consistent with 12:00 ET.

## Evidence directly stated by source

- Resolution source: Binance.
- Instrument: BTC/USDT.
- Time bucket: 1-minute candle labeled 12:00 ET.
- Comparator: final close price strictly greater than 70,000.

## What is uncertain

- Binance web UI is JS-gated from this environment, so the exact visual candle labeling convention on the website could not be directly inspected here.
- The assignment text is still sufficiently explicit about the operative candle and source.

## Why this source may matter

This source governs what counts. A general statement like “BTC traded above 70k that day” is insufficient; what matters is the exact Binance BTC/USDT 1-minute close at noon ET.

## Possible impact on the question

The narrow wording lowers ambiguity about the outcome variable but increases timing/exchange risk. Any estimate should focus on the chance BTC remains above 70k at that exact minute on Binance, not just at daily close or on other venues.

## Reliability notes

High reliability for contract interpretation because this is the governing market description and primary resolution framing. Residual ambiguity is low-to-medium only because the JS-gated Binance UI could not be visually confirmed in-session.