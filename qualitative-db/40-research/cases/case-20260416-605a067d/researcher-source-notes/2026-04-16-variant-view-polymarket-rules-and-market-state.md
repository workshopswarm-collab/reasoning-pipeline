---
type: source_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: threshold-close-markets
entity: ethereum
topic: Polymarket ETH above 2200 on April 17 contract rules and quoted market state
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on April 17 close above 2200?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page for Ethereum above ___ on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/variant-view.md
tags: [source-note, polymarket, ethereum, binance, resolution-rules]
---

# Summary

The Polymarket market page provides the direct contract wording, identifies Binance ETH/USDT 1-minute candle close at 12:00 ET on April 17 as the governing source of truth, and showed the 2,200 line trading around 91.5% Yes at fetch time.

## Key facts extracted

- The market resolves Yes if the Binance ETH/USDT 1-minute candle for 12:00 in ET on April 17 has a final close price higher than 2,200.
- The market is explicitly about Binance ETH/USDT, not another venue or trading pair.
- The market page cited the Binance trading page with 1m candles as the resolution source.
- At fetch time, the 2,200 line was displayed around Buy Yes 91.5¢ / Buy No 9.9¢, implying roughly 91% market probability.
- Neighboring ladder outcomes showed a sharp drop from 2,100 (~99%) to 2,200 (~91%) to 2,300 (~57%), which is consistent with ETH trading in the low 2300s rather than far above 2400.

## Evidence directly stated by source

- Direct resolution language ties settlement to Binance ETH/USDT 1-minute close at 12:00 ET on the target date.
- Direct market-state quote on the page places the 2,200 threshold in low-90s implied probability territory.

## What is uncertain

- The public market page is not itself the final Binance candle proof; it only states the rules and current market pricing.
- The fetched market price can move after fetch time.
- The page does not itself display the final April 17 noon candle because the event had not resolved at research time.

## Why this source may matter

This is the governing contract source for what counts, when it counts, and which venue matters. It is necessary to avoid using the wrong exchange, wrong timestamp, or wrong interpretation of what “above 2200” means.

## Possible impact on the question

This source sharply narrows the mechanism: the claim is not about whether ETH trades above 2200 at any time, but whether the Binance ETH/USDT 12:00 ET 1-minute candle on April 17 closes above 2200. That makes time-specific reversal risk relevant even though spot ETH is already above the threshold.

## Reliability notes

High value for contract interpretation, medium-high reliability for quoted market state. Lower value for proving the outcome itself because it is not the authoritative final candle print.