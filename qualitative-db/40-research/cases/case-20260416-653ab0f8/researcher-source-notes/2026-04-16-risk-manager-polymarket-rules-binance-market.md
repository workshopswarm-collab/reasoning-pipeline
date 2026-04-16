---
type: source_note
case_key: case-20260416-653ab0f8
dispatch_id: dispatch-case-20260416-653ab0f8-20260416T090226Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-653ab0f8 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 18?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and stated resolution rules for Bitcoin above $72,000 on April 18
source_type: market-rule-page
source_url: https://polymarket.com/event/bitcoin-above-on-april-18
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-653ab0f8/researcher-analyses/2026-04-16/dispatch-case-20260416-653ab0f8-20260416T090226Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution-rules, btc]
---

# Summary

This source establishes the governing contract mechanics and current market pricing context for the April 18 BTC > $72,000 question.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1 minute candle labeled 12:00 in ET on April 18 has a final close above 72,000.
- The source of truth is Binance BTC/USDT, not other exchanges or pairs.
- Price precision follows the decimals shown by the source.
- Current market pricing on the Polymarket page showed the 72,000 line around 88% at time of check.

## Evidence directly stated by source

- The rule text explicitly points to Binance and specifically to the 1 minute candle close for 12:00 ET.
- The page explicitly warns that other exchanges or trading pairs do not govern resolution.
- The market page lists the 72,000 threshold outcome near 88%.

## What is uncertain

- The page itself does not explain the ET-to-Binance timestamp mapping beyond naming 12:00 ET.
- The exact close that will matter is two days in the future, so current market pricing is only contextual and not dispositive.

## Why this source may matter

This is the primary governing source for what counts. The risk here is less about broad BTC direction than about narrow contract mechanics: exact venue, exact pair, exact one-minute close, exact ET timing.

## Possible impact on the question

This source makes clear that any bullish thesis still fails if Binance BTC/USDT prints 71,999.99 or lower on the relevant 12:00 ET one-minute close, even if most other venues trade above 72,000 around the same time.

## Reliability notes

High reliability for contract mechanics because it is the market's own stated rules. Lower reliability for forecasting direction because market price itself can be miscalibrated.