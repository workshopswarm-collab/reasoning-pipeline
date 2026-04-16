---
type: source_note
case_key: case-20260416-66f6f47e
dispatch_id: dispatch-case-20260416-66f6f47e-20260416T141457Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: threshold-close-markets
entity: btc
topic: Polymarket rule text for Bitcoin above 72000 on April 21
question: What exactly must happen for this market to resolve Yes?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page
source_type: primary
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
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
tags: [polymarket, rules, source-note, btc]
---

# Summary

This note preserves the exact contract mechanics from the market page so later reviewers can see what does and does not count.

## Key facts extracted

- The market resolves Yes if the **Binance 1 minute candle for BTC/USDT 12:00 in ET timezone on Apr 21** has a final **Close** price **higher than 72,000**.
- Otherwise it resolves No.
- The market is explicitly about **Binance BTC/USDT**, not other exchanges and not other trading pairs.
- Price precision is determined by the source.

## Evidence directly stated by source

Direct rule text from the page:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance..."

## What is uncertain

- The page snapshot is not itself a guarantee that rule wording can never be amended, though there is no sign here of ambiguity.
- The market page price for 72k was shown around 79-80%, but market prices can move after capture.

## Why this source may matter

It is the contract-definition source. The entire probability estimate depends on understanding that this is a **future single-minute close** question, not a "touch" market and not a broader weekly average or end-of-day close.

## Possible impact on the question

This wording makes timing risk and close-only risk the main downside. BTC can trade above 72k for days and still lose if the specific 12:00 ET 1-minute candle closes below 72k.

## Reliability notes

High reliability for contract mechanics. This is the primary source for what the market means.